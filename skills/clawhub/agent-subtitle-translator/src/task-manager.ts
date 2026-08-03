import { randomBytes } from "node:crypto";
import { mkdir, readdir, readFile, stat, writeFile } from "node:fs/promises";
import path from "node:path";

import {
  type AgentProfile,
  type BatchSnapshot,
  type CreateTaskRequest,
  type EntrySnapshot,
  type TaskEvent,
  type TaskEventType,
  type TaskSnapshot,
  type TaskStatus,
  type TaskSummary,
  MAX_BATCH_SIZE,
} from "./common.js";
import { SubtitleCli, type SubtitleCommandResult } from "./python-cli.js";

interface InternalTask extends TaskSummary {
  inputPath: string;
  workDir: string;
  manifestPath: string;
  outputPath?: string;
  reportPath?: string;
  batchSize: number;
  batches: BatchSnapshot[];
  entries: EntrySnapshot[];
  events: TaskEvent[];
  nextEventId: number;
}

const DEFAULT_AGENT_NAME = "等待 Agent 自报";
const DEFAULT_MODEL_NAME = "等待模型自报";
const FROZEN_TASK_STATUSES = new Set<TaskStatus>(["completed", "failed", "cancelled", "paused"]);

export interface TaskManagerOptions {
  skillRoot: string;
  dataDir: string;
  pythonCommand?: string;
}

type TaskListener = (event: TaskEvent) => void;

function now(): string {
  return new Date().toISOString();
}

function durationBetween(startAt: string | undefined, endAt: string): number | undefined {
  if (!startAt) {
    return undefined;
  }
  const startMs = Date.parse(startAt);
  const endMs = Date.parse(endAt);
  if (!Number.isFinite(startMs) || !Number.isFinite(endMs)) {
    return undefined;
  }
  return Math.max(0, endMs - startMs);
}

function asRecord(value: unknown): Record<string, unknown> {
  return value && typeof value === "object" ? (value as Record<string, unknown>) : {};
}

function asString(value: unknown, fallback = ""): string {
  return typeof value === "string" ? value : fallback;
}

function asNumber(value: unknown, fallback = 0): number {
  return typeof value === "number" && Number.isFinite(value) ? value : fallback;
}

function asStringArray(value: unknown): string[] {
  return Array.isArray(value) ? value.filter((item): item is string => typeof item === "string") : [];
}

function taskId(): string {
  return `task-${Date.now().toString(36)}-${randomBytes(3).toString("hex")}`;
}

function safeFileName(value: string): string {
  const base = path.basename(value).replace(/[^\p{L}\p{N}._-]+/gu, "-");
  return base || "subtitle.srt";
}

function inputExtension(fileName: string): string {
  const extension = path.extname(fileName).toLowerCase();
  if (![".srt", ".vtt", ".ass"].includes(extension)) {
    throw new Error("支持的字幕格式为 SRT、VTT 和 ASS");
  }
  return extension;
}

function defaultBatch(batch: number, ids: string[]): BatchSnapshot {
  return {
    batch,
    ids,
    status: "pending",
    retryCount: 0,
    entryCount: ids.length,
    completedEntryCount: 0,
    styleFallbackIds: [],
  };
}

function parseResultReport(result: SubtitleCommandResult): Record<string, unknown> {
  return result.report;
}

export class TaskManager {
  private readonly skillRoot: string;
  private readonly dataDir: string;
  private readonly cli: SubtitleCli;
  private readonly tasks = new Map<string, InternalTask>();
  private readonly listeners = new Map<string, Set<TaskListener>>();
  private skillVersion = "未发布";
  private agentProfile: AgentProfile = {
    agent: DEFAULT_AGENT_NAME,
    model: DEFAULT_MODEL_NAME,
  };

  constructor(options: TaskManagerOptions) {
    this.skillRoot = path.resolve(options.skillRoot);
    this.dataDir = path.resolve(options.dataDir);
    this.cli = new SubtitleCli(options);
  }

  async init(): Promise<void> {
    await mkdir(this.dataDir, { recursive: true });
    this.skillVersion = await this.readSkillVersion();
    try {
      const rawProfile = asRecord(JSON.parse(await readFile(path.join(this.dataDir, "agent-profile.json"), "utf8")));
      this.agentProfile.agent = asString(rawProfile.agent, DEFAULT_AGENT_NAME);
      this.agentProfile.model = asString(rawProfile.model, DEFAULT_MODEL_NAME);
      const modelVersion = asString(rawProfile.modelVersion);
      const modelSeries = asString(rawProfile.modelSeries);
      const reasoningStrength = asString(rawProfile.reasoningStrength);
      if (modelVersion) this.agentProfile.modelVersion = modelVersion;
      if (modelSeries) this.agentProfile.modelSeries = modelSeries;
      if (reasoningStrength) this.agentProfile.reasoningStrength = reasoningStrength;
      const reportedAt = asString(rawProfile.reportedAt);
      if (reportedAt) this.agentProfile.reportedAt = reportedAt;
    } catch {
      // The first Agent session will create the profile through the bridge.
    }
    const names = await readdir(this.dataDir, { withFileTypes: true });
    for (const name of names) {
      if (!name.isDirectory()) {
        continue;
      }
      const statePath = path.join(this.dataDir, name.name, "task.json");
      try {
        const raw = await readFile(statePath, "utf8");
        const parsed = JSON.parse(raw) as InternalTask;
        if (!parsed.id || !Array.isArray(parsed.events)) {
          continue;
        }
        if (["preparing", "translating", "validating", "composing"].includes(parsed.status)) {
          if (parsed.startedAt) {
            parsed.durationMs = Math.max(0, Date.now() - new Date(parsed.startedAt).getTime());
          }
          parsed.status = "paused";
          parsed.error = "本地服务曾重启，任务已暂停；可从最近的批次继续。";
          parsed.updatedAt = now();
          await writeFile(statePath, `${JSON.stringify(parsed, null, 2)}\n`, "utf8");
        }
        this.tasks.set(parsed.id, parsed);
      } catch {
        // Ignore incomplete task directories; a later run can still create new work.
      }
    }
  }

  async createTask(request: CreateTaskRequest): Promise<TaskSnapshot> {
    const fileName = safeFileName(request.fileName ?? request.filePath ?? "subtitle.srt");
    const extension = inputExtension(fileName);
    const batchSize = request.batchSize ?? MAX_BATCH_SIZE;
    if (!Number.isInteger(batchSize) || batchSize < 1 || batchSize > MAX_BATCH_SIZE) {
      throw new Error(`批次大小必须在 1 到 ${MAX_BATCH_SIZE} 之间`);
    }
    if (!request.targetLanguage?.trim()) {
      throw new Error("必须提供目标语言");
    }
    if (!request.filePath && !request.contentBase64) {
      throw new Error("请选择一个字幕文件");
    }

    const id = taskId();
    const taskDir = path.join(this.dataDir, id);
    const workDir = path.join(taskDir, "work");
    await mkdir(taskDir, { recursive: true });

    let inputPath: string;
    if (request.contentBase64) {
      const inputDir = path.join(taskDir, "input");
      await mkdir(inputDir, { recursive: true });
      inputPath = path.join(inputDir, fileName);
      const content = Buffer.from(request.contentBase64, "base64");
      if (content.length === 0) {
        throw new Error("字幕文件内容为空");
      }
      await writeFile(inputPath, content);
    } else {
      inputPath = path.resolve(request.filePath as string);
      const inputStat = await stat(inputPath);
      if (!inputStat.isFile()) {
        throw new Error("字幕输入路径不是文件");
      }
      inputExtension(inputPath);
    }

    const createdAt = now();
    const task: InternalTask = {
      id,
      fileName,
      agent: this.agentProfile.agent,
      model: this.agentProfile.model,
      modelVersion: this.agentProfile.modelVersion,
      modelSeries: this.agentProfile.modelSeries,
      reasoningStrength: this.agentProfile.reasoningStrength,
      inputFormat: extension.slice(1),
      targetLanguage: request.targetLanguage.trim(),
      status: "queued",
      createdAt,
      updatedAt: createdAt,
      totalEntries: 0,
      completedEntries: 0,
      batchCount: 0,
      completedBatches: 0,
      warningCount: 0,
      inputPath,
      workDir,
      manifestPath: path.join(workDir, "manifest.json"),
      batchSize,
      batches: [],
      entries: [],
      events: [],
      nextEventId: 1,
    };
    if (request.sourceLanguage?.trim()) {
      task.sourceLanguage = request.sourceLanguage.trim();
    }
    this.tasks.set(id, task);
    await this.appendEvent(task, "task.created", "任务已建立，正在准备字幕文件。", "queued");
    void this.prepare(task);
    return this.snapshot(task);
  }

  listTasks(): TaskSummary[] {
    return [...this.tasks.values()]
      .sort((left, right) => right.createdAt.localeCompare(left.createdAt))
      .map((task) => this.summary(task));
  }

  getTask(id: string): TaskSnapshot {
    const task = this.requireTask(id);
    return this.snapshot(task);
  }

  getAgentProfile(): AgentProfile {
    return { ...this.agentProfile };
  }

  getSkillVersion(): string {
    return this.skillVersion;
  }

  async reportAgent(
    agent: string,
    model: string,
    modelVersion?: string,
    modelSeries?: string,
    reasoningStrength?: string,
  ): Promise<AgentProfile> {
    const agentName = agent.trim();
    const modelName = model.trim();
    if (!agentName) throw new Error("必须提供 Agent 名称");
    if (!modelName) throw new Error("必须提供模型名称");
    const nextProfile: AgentProfile = {
      agent: agentName,
      model: modelName,
      reportedAt: now(),
    };
    const versionName = modelVersion?.trim();
    const seriesName = modelSeries?.trim();
    const reasoningName = reasoningStrength?.trim();
    if (versionName) nextProfile.modelVersion = versionName;
    if (seriesName) nextProfile.modelSeries = seriesName;
    if (reasoningName) nextProfile.reasoningStrength = reasoningName;
    this.agentProfile = nextProfile;
    await writeFile(
      path.join(this.dataDir, "agent-profile.json"),
      JSON.stringify(this.agentProfile, null, 2) + "\n",
      "utf8",
    );
    return this.getAgentProfile();
  }

  getOutputPath(id: string): string {
    const task = this.requireTask(id);
    if (!task.outputPath) {
      throw new Error("任务还没有生成输出文件");
    }
    return task.outputPath;
  }

  subscribe(id: string, listener: TaskListener): () => void {
    const task = this.requireTask(id);
    if (!this.listeners.has(task.id)) {
      this.listeners.set(task.id, new Set());
    }
    const listeners = this.listeners.get(task.id) as Set<TaskListener>;
    listeners.add(listener);
    return () => listeners.delete(listener);
  }

  async startBatch(id: string, batchNumber: number): Promise<TaskSnapshot> {
    const task = this.requireTask(id);
    const batch = this.requireBatch(task, batchNumber);
    if (task.status === "cancelled") {
      throw new Error("任务已取消");
    }
    const startedAt = now();
    batch.status = "translating";
    batch.startedAt = startedAt;
    delete batch.finishedAt;
    delete batch.durationMs;
    delete batch.error;
    task.status = "translating";
    if (!task.startedAt) {
      task.startedAt = startedAt;
    }
    await this.appendEvent(
      task,
      "batch.started",
      `第 ${batchNumber} 批开始翻译，共 ${batch.entryCount} 条字幕。`,
      "translating",
      batchNumber,
    );
    return this.snapshot(task);
  }

  async retryBatch(id: string, batchNumber: number): Promise<TaskSnapshot> {
    const task = this.requireTask(id);
    const batch = this.requireBatch(task, batchNumber);
    batch.retryCount += 1;
    batch.status = "retrying";
    delete batch.error;
    task.status = "retrying";
    await this.appendEvent(
      task,
      "batch.retrying",
      `第 ${batchNumber} 批准备第 ${batch.retryCount} 次重试。`,
      "retrying",
      batchNumber,
      { retryCount: batch.retryCount },
    );
    return this.snapshot(task);
  }

  async submitResponse(
    id: string,
    batchNumber: number,
    responsePath: string,
    allowStyleFallback: boolean,
  ): Promise<TaskSnapshot> {
    const task = this.requireTask(id);
    const batch = this.requireBatch(task, batchNumber);
    const startedAt = batch.startedAt ?? now();
    batch.status = "validating";
    task.status = "validating";
    await this.appendEvent(
      task,
      "batch.validating",
      `正在校验第 ${batchNumber} 批的翻译结果。`,
      "validating",
      batchNumber,
    );

    try {
      const result = await this.cli.validateResponse(
        task.manifestPath,
        batchNumber,
        path.resolve(responsePath),
        allowStyleFallback,
      );
      const report = parseResultReport(result);
      const validatedPath = path.join(task.workDir, "validated", `batch-${String(batchNumber).padStart(4, "0")}.json`);
      const validated = asRecord(JSON.parse(await readFile(validatedPath, "utf8")));
      const rows = Array.isArray(validated.translations) ? validated.translations.map(asRecord) : [];
      const rowById = new Map(rows.map((row) => [asString(row.id), row]));
      const fallbackIds = asStringArray(validated.style_fallback_ids);
      for (const entryId of batch.ids) {
        const entry = task.entries.find((item) => item.id === entryId);
        const row = rowById.get(entryId);
        if (!entry || !row) {
          throw new Error(`第 ${batchNumber} 批缺少字幕 ${entryId} 的校验结果`);
        }
        const translatedText = asString(row.text);
        if (!translatedText.trim()) {
          throw new Error(`字幕 ${entryId} 的译文为空`);
        }
        entry.translatedText = translatedText;
        entry.styleFallback = row.style_fallback === true;
        entry.status = entry.styleFallback ? "fallback" : "validated";
      }
      batch.status = "validated";
      batch.finishedAt = now();
      batch.durationMs = Math.max(0, new Date(batch.finishedAt).getTime() - new Date(startedAt).getTime());
      batch.completedEntryCount = batch.entryCount;
      batch.styleFallbackIds = fallbackIds;
      delete batch.error;
      task.completedBatches = task.batches.filter((item) => item.status === "validated").length;
      task.completedEntries = task.batches.reduce((sum, item) => sum + item.completedEntryCount, 0);
      task.warningCount = task.entries.filter((entry) => entry.degradation === "karaoke" || entry.styleFallback).length;
      const allValidated = task.batches.every((item) => item.status === "validated");
      task.status = allValidated ? "ready_to_compose" : "awaiting_translation";
      delete task.error;
      await this.appendEvent(
        task,
        "batch.validated",
        `第 ${batchNumber} 批校验通过，耗时 ${Math.round((batch.durationMs ?? 0) / 1000)} 秒。`,
        task.status,
        batchNumber,
        {
          entryCount: batch.entryCount,
          styleFallbackCount: fallbackIds.length,
          karaokeCount: task.entries.filter((entry) => entry.degradation === "karaoke").length,
          reportStatus: asString(report.status),
        },
        batch.durationMs,
      );
      return this.snapshot(task);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      batch.status = "failed";
      batch.error = message;
      batch.finishedAt = now();
      batch.durationMs = Math.max(0, new Date(batch.finishedAt).getTime() - new Date(startedAt).getTime());
      task.status = "retrying";
      task.error = message;
      await this.appendEvent(task, "batch.failed", `第 ${batchNumber} 批校验失败：${message}`, "retrying", batchNumber);
      throw error;
    }
  }

  async compose(id: string, outputPath?: string, overwrite = false): Promise<TaskSnapshot> {
    const task = this.requireTask(id);
    if (task.batches.some((batch) => batch.status !== "validated")) {
      throw new Error("仍有批次没有完成校验");
    }
    task.status = "composing";
    await this.appendEvent(task, "task.composing", "所有批次已校验，正在生成字幕文件。", "composing");
    try {
      const result = await this.cli.compose(
        task.manifestPath,
        outputPath ? path.resolve(outputPath) : undefined,
        overwrite,
      );
      const report = parseResultReport(result);
      const output = asString(report.output);
      if (!output) {
        throw new Error("合成完成，但没有找到输出文件路径");
      }
      task.outputPath = output;
      task.reportPath = `${output}.report.json`;
      task.status = "completed";
      this.freezeDuration(task);
      task.error = undefined;
      await this.appendEvent(
        task,
        "task.completed",
        `字幕文件已生成，总耗时 ${Math.round((task.durationMs ?? 0) / 1000)} 秒。`,
        "completed",
        undefined,
        { outputFormat: asString(report.output_format), entryCount: asNumber(report.entry_count) },
        task.durationMs,
      );
      return this.snapshot(task);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      task.status = "failed";
      this.freezeDuration(task);
      task.error = message;
      await this.appendEvent(task, "task.failed", `生成字幕文件失败：${message}`, "failed");
      throw error;
    }
  }

  async addNote(id: string, message: string): Promise<TaskSnapshot> {
    const task = this.requireTask(id);
    if (!message.trim()) {
      throw new Error("事件说明不能为空");
    }
    await this.appendEvent(task, "agent.note", message.trim(), task.status);
    return this.snapshot(task);
  }

  async cancel(id: string): Promise<TaskSnapshot> {
    const task = this.requireTask(id);
    task.status = "cancelled";
    this.freezeDuration(task);
    task.error = undefined;
    await this.appendEvent(task, "task.cancelled", "任务已取消。", "cancelled");
    return this.snapshot(task);
  }

  private async prepare(task: InternalTask): Promise<void> {
    const startedAt = now();
    task.status = "preparing";
    task.startedAt = task.startedAt ?? startedAt;
    await this.appendEvent(task, "task.preparing", "正在读取字幕、检查时间轴并准备翻译批次。", "preparing");
    try {
      await this.cli.prepare(task.inputPath, task.targetLanguage, task.sourceLanguage, task.batchSize, task.workDir);
      const manifest = asRecord(await this.cli.readManifest(task.manifestPath));
      const rawEntries = Array.isArray(manifest.entries) ? manifest.entries.map(asRecord) : [];
      task.inputFormat = asString(manifest.input_format, task.inputFormat);
      task.outputFormat = asString(manifest.output_format);
      task.targetLanguage = asString(manifest.target_language, task.targetLanguage);
      task.sourceLanguage = asString(manifest.source_language, task.sourceLanguage);
      task.entries = rawEntries.map((raw, index) => {
        const entry: EntrySnapshot = {
          id: asString(raw.id, String(index + 1).padStart(6, "0")),
          order: asNumber(raw.order, index + 1),
          sourceText: asString(raw.source_text),
          status: "pending",
          kind: raw.kind === "ass" ? "ass" : "srt",
        };
        if (typeof raw.start_ms === "number") {
          entry.startMs = raw.start_ms;
        }
        if (typeof raw.end_ms === "number") {
          entry.endMs = raw.end_ms;
        }
        if (raw.degradation === "karaoke") {
          entry.degradation = "karaoke";
        }
        return entry;
      });
      const rawBatches = Array.isArray(manifest.batches) ? manifest.batches.map(asRecord) : [];
      task.batches = rawBatches.map((raw) => defaultBatch(asNumber(raw.batch), asStringArray(raw.ids)));
      task.totalEntries = task.entries.length;
      task.batchCount = task.batches.length;
      task.completedEntries = 0;
      task.completedBatches = 0;
      task.warningCount = task.entries.filter((entry) => entry.degradation === "karaoke").length;
      task.status = task.batches.length === 0 ? "ready_to_compose" : "awaiting_translation";
      task.error = undefined;
      await this.appendEvent(
        task,
        "task.ready",
        task.batches.length === 0
          ? "字幕已准备完成，可以直接生成输出文件。"
          : `字幕已准备完成，共 ${task.entries.length} 条，分为 ${task.batches.length} 批。`,
        task.status,
        undefined,
        { entryCount: task.entries.length, batchCount: task.batches.length, warningCount: task.warningCount },
      );
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      task.status = "failed";
      this.freezeDuration(task);
      task.error = message;
      await this.appendEvent(task, "task.failed", `字幕准备失败：${message}`, "failed");
    }
  }

  private requireTask(id: string): InternalTask {
    const task = this.tasks.get(id);
    if (!task) {
      throw new Error(`找不到任务：${id}`);
    }
    return task;
  }

  private async readSkillVersion(): Promise<string> {
    try {
      const packageJson = asRecord(JSON.parse(await readFile(path.join(this.skillRoot, "package.json"), "utf8")));
      return asString(packageJson.version, "未发布");
    } catch {
      return "未发布";
    }
  }

  private requireBatch(task: InternalTask, batchNumber: number): BatchSnapshot {
    const batch = task.batches.find((item) => item.batch === batchNumber);
    if (!batch) {
      throw new Error(`找不到第 ${batchNumber} 批`);
    }
    return batch;
  }

  private summary(task: InternalTask): TaskSummary {
    const summary: TaskSummary = {
      id: task.id,
      fileName: task.fileName,
      targetLanguage: task.targetLanguage,
      status: task.status,
      createdAt: task.createdAt,
      updatedAt: task.updatedAt,
      totalEntries: task.totalEntries,
      completedEntries: task.completedEntries,
      batchCount: task.batchCount,
      completedBatches: task.completedBatches,
      warningCount: task.warningCount,
    };
    if (task.agent) summary.agent = task.agent;
    if (task.model) summary.model = task.model;
    if (task.modelVersion) summary.modelVersion = task.modelVersion;
    if (task.modelSeries) summary.modelSeries = task.modelSeries;
    if (task.reasoningStrength) summary.reasoningStrength = task.reasoningStrength;
    if (task.inputFormat) summary.inputFormat = task.inputFormat;
    if (task.outputFormat) summary.outputFormat = task.outputFormat;
    if (task.sourceLanguage) summary.sourceLanguage = task.sourceLanguage;
    if (task.startedAt) summary.startedAt = task.startedAt;
    if (task.finishedAt) summary.finishedAt = task.finishedAt;
    const duration = this.duration(task);
    if (duration !== undefined) summary.durationMs = duration;
    if (task.error) summary.error = task.error;
    if (task.outputPath) summary.outputFileName = path.basename(task.outputPath);
    return summary;
  }

  private duration(task: InternalTask): number | undefined {
    if (task.durationMs !== undefined && Number.isFinite(task.durationMs)) {
      return Math.max(0, task.durationMs);
    }
    if (!task.startedAt) {
      return undefined;
    }
    const endAt = task.finishedAt ?? (FROZEN_TASK_STATUSES.has(task.status) ? task.updatedAt : now());
    return durationBetween(task.startedAt, endAt);
  }

  private freezeDuration(task: InternalTask, finishedAt = now()): void {
    task.finishedAt = finishedAt;
    const duration = durationBetween(task.startedAt, finishedAt);
    if (duration !== undefined) {
      task.durationMs = duration;
    }
  }

  private snapshot(task: InternalTask): TaskSnapshot {
    const summary = this.summary(task);
    return {
      ...summary,
      batches: task.batches.map((batch) => ({ ...batch, ids: [...batch.ids], styleFallbackIds: [...batch.styleFallbackIds] })),
      entries: task.entries.map((entry) => ({ ...entry })),
      events: task.events.map((event) => ({ ...event, meta: event.meta ? { ...event.meta } : undefined })),
    };
  }

  private async appendEvent(
    task: InternalTask,
    type: TaskEventType,
    message: string,
    status: TaskStatus,
    batch?: number,
    meta?: Record<string, string | number | boolean | null>,
    durationMs?: number,
  ): Promise<void> {
    task.status = status;
    task.updatedAt = now();
    const event: TaskEvent = {
      id: task.nextEventId,
      taskId: task.id,
      type,
      at: task.updatedAt,
      message,
      status,
    };
    if (batch !== undefined) event.batch = batch;
    if (durationMs !== undefined) event.durationMs = durationMs;
    if (meta !== undefined) event.meta = meta;
    task.nextEventId += 1;
    task.events.push(event);
    if (task.events.length > 2000) {
      task.events.splice(0, task.events.length - 2000);
    }
    await this.persist(task);
    for (const listener of this.listeners.get(task.id) ?? []) {
      listener(event);
    }
  }

  private async persist(task: InternalTask): Promise<void> {
    await writeFile(path.join(this.dataDir, task.id, "task.json"), `${JSON.stringify(task, null, 2)}\n`, "utf8");
  }
}
