import type { AgentProfile, BatchSnapshot, EntrySnapshot, TaskEvent, TaskSnapshot, TaskStatus, TaskSummary } from "../src/common.js";
import { applyNativeIcons, hydrateIcons, iconMarkup, setIcon, setupIconSystem } from "./icons.js";

const statusMeta: Record<TaskStatus, { label: string; tone: "neutral" | "active" | "success" | "danger" }> = {
  queued: { label: "排队中", tone: "neutral" },
  preparing: { label: "读取字幕", tone: "active" },
  awaiting_translation: { label: "等待 Agent", tone: "neutral" },
  translating: { label: "翻译中", tone: "active" },
  validating: { label: "校验中", tone: "active" },
  retrying: { label: "需要重试", tone: "danger" },
  ready_to_compose: { label: "准备生成", tone: "neutral" },
  composing: { label: "生成文件", tone: "active" },
  completed: { label: "已完成", tone: "success" },
  failed: { label: "处理失败", tone: "danger" },
  cancelled: { label: "已取消", tone: "neutral" },
  paused: { label: "已暂停", tone: "neutral" },
};

const batchMeta: Record<BatchSnapshot["status"], string> = {
  pending: "待开始",
  translating: "翻译中",
  validating: "校验中",
  validated: "已完成",
  retrying: "重试中",
  failed: "需重试",
};

interface ApiPayload<T> {
  task?: T;
  tasks?: T[];
  error?: string;
}

interface AppState {
  tasks: TaskSummary[];
  agentProfile?: AgentProfile;
  selectedId?: string;
  selected?: TaskSnapshot;
  eventSource?: EventSource;
  subtitleView: "stacked" | "columns";
}

const state: AppState = { tasks: [], subtitleView: "stacked" };

type ConnectionStatus = "checking" | "online" | "offline";

function element<T extends HTMLElement>(id: string): T {
  const node = document.getElementById(id);
  if (!node) throw new Error(`页面缺少元素 #${id}`);
  return node as T;
}

function setText(node: HTMLElement, value: string): void {
  if (node.textContent !== value) node.textContent = value;
}

function setWidth(node: HTMLElement, value: string): void {
  if (node.style.width !== value) node.style.width = value;
}

function applyChildOrder(container: HTMLElement, nodes: HTMLElement[]): void {
  let cursor = container.firstElementChild;
  nodes.forEach((node) => {
    if (node !== cursor) container.insertBefore(node, cursor);
    cursor = node.nextElementSibling;
  });
}

function formatDuration(durationMs: number | undefined): string {
  if (durationMs === undefined || !Number.isFinite(durationMs)) return "—";
  const totalSeconds = Math.max(0, Math.round(durationMs / 1000));
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  if (minutes >= 60) return `${Math.floor(minutes / 60)}小时 ${String(minutes % 60).padStart(2, "0")}分`;
  return `${String(minutes).padStart(2, "0")}分 ${String(seconds).padStart(2, "0")}秒`;
}

function formatEventTime(value: string): string {
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "刚刚" : date.toLocaleTimeString("zh-CN", { hour: "2-digit", minute: "2-digit", second: "2-digit" });
}

function formatSubtitleTime(entry: EntrySnapshot): string {
  if (entry.startMs === undefined || entry.endMs === undefined) return "无时间轴";
  const seconds = (value: number) => {
    const total = Math.floor(value / 1000);
    return `${String(Math.floor(total / 3600)).padStart(2, "0")}:${String(Math.floor((total % 3600) / 60)).padStart(2, "0")}:${String(total % 60).padStart(2, "0")}`;
  };
  return `${seconds(entry.startMs)} — ${seconds(entry.endMs)}`;
}

function setConnectionStatus(status: ConnectionStatus): void {
  const dot = element<HTMLElement>("live-dot");
  const labels: Record<ConnectionStatus, string> = {
    checking: "正在检查本地服务连接",
    online: "本地服务已连接",
    offline: "本地服务连接失败",
  };
  const label = labels[status];
  dot.dataset.status = status;
  dot.setAttribute("aria-label", label);
  dot.title = label;
}

async function api<T>(path: string, init?: RequestInit): Promise<T> {
  try {
    const response = await fetch(path, {
      ...init,
      headers: { "Content-Type": "application/json", ...(init?.headers ?? {}) },
    });
    const payload = (await response.json()) as ApiPayload<T>;
    if (!response.ok) throw new Error(payload.error ?? `请求失败：${response.status}`);
    setConnectionStatus("online");
    return payload as T;
  } catch (error) {
    setConnectionStatus("offline");
    throw error;
  }
}

function statusLabel(status: TaskStatus): string {
  return statusMeta[status]?.label ?? status;
}

function statusTone(status: TaskStatus): string {
  return statusMeta[status]?.tone ?? "neutral";
}

const languageLabels: Record<string, string> = {
  "zh-Hans": "简体中文",
  "zh-CN": "简体中文",
  "zh-Hant": "繁体中文",
  "zh-TW": "繁体中文",
  en: "英语",
  "en-US": "英语",
  ja: "日语",
  ko: "韩语",
  fr: "法语",
  de: "德语",
  es: "西班牙语",
};

type DetailNoticeTone = "neutral" | "warning" | "danger";
type EventTone = "neutral" | "active" | "success" | "warning" | "danger";

const eventTitles: Record<TaskEvent["type"], string> = {
  "task.created": "任务已建立",
  "task.preparing": "正在准备字幕",
  "task.ready": "字幕准备完成",
  "task.failed": "任务处理失败",
  "task.cancelled": "任务已取消",
  "batch.started": "开始翻译",
  "batch.validating": "正在校验",
  "batch.validated": "校验完成",
  "batch.retrying": "准备重试",
  "batch.failed": "校验未通过",
  "task.composing": "正在生成字幕文件",
  "task.completed": "字幕文件已生成",
  "agent.note": "Agent 备注",
};

function languageLabel(value: string): string {
  return languageLabels[value] ?? value;
}

function taskProgress(completedEntries: number, totalEntries: number, status?: TaskStatus): number {
  if (totalEntries > 0) return Math.min(100, Math.round((completedEntries / totalEntries) * 100));
  return status === "completed" ? 100 : 0;
}

function detailNotice(task: TaskSnapshot): { tone: DetailNoticeTone; text: string } | undefined {
  if (task.error) return { tone: "danger", text: task.error };
  if (task.status === "retrying") return { tone: "danger", text: "校验未通过，系统正在重新尝试。" };
  if (task.status === "failed") return { tone: "danger", text: "任务处理失败，请查看过程记录。" };
  if (task.status === "paused") return { tone: "neutral", text: "任务已暂停，可从过程记录了解原因。" };
  if (task.warningCount > 0) return { tone: "warning", text: `发现 ${task.warningCount} 个降级结果，请在字幕明细中留意。` };
  return undefined;
}

function createTaskCard(index: number): HTMLButtonElement {
  const card = document.createElement("button");
  card.className = "task-card";
  card.type = "button";
  card.style.animationDelay = `${Math.min(index * 45, 360)}ms`;
  card.innerHTML = `<span class="task-status-mark" data-task-status></span>
    <span class="task-card-copy"><strong class="task-card-name" data-task-name></strong></span>
    <span class="task-card-time" data-task-time></span>
    <span class="task-card-meta" data-task-meta></span>
    <span class="task-card-progress" aria-hidden="true"><span data-task-progress-fill></span></span>`;
  return card;
}

function taskModelParts(task: TaskSummary): string[] {
  const hasTaskModel = Boolean(task.model && task.model !== "等待模型自报");
  const model = hasTaskModel ? task.model : state.agentProfile?.model;
  if (!model || model === "等待模型自报") return [];

  const version = hasTaskModel ? task.modelVersion : state.agentProfile?.modelVersion;
  const series = hasTaskModel ? task.modelSeries : state.agentProfile?.modelSeries;
  const reasoning = hasTaskModel ? task.reasoningStrength : state.agentProfile?.reasoningStrength;
  const parts = [model];
  if (version && !model.toLocaleLowerCase().includes(version.toLocaleLowerCase())) parts.push(version);
  if (series) parts.push(series);
  if (reasoning) parts.push(`推理 · ${reasoning}`);
  return parts;
}

function taskModelLabel(task: TaskSummary): string {
  const parts = taskModelParts(task);
  if (parts.length === 0) return "待上报";
  const model = parts[0] as string;
  const hasTaskModel = Boolean(task.model && task.model !== "等待模型自报");
  const version = hasTaskModel ? task.modelVersion : state.agentProfile?.modelVersion;
  if (version && !model.toLocaleLowerCase().includes(version.toLocaleLowerCase())) return `${model}-${version}`;
  return model;
}

function taskAgentLabel(task: TaskSummary): string {
  const value = task.agent ?? state.agentProfile?.agent;
  return value && value !== "等待 Agent 自报" ? value : "Agent";
}

function updateTaskCard(card: HTMLButtonElement, task: TaskSummary): void {
  const selected = task.id === state.selectedId;
  card.dataset.taskId = task.id;
  card.dataset.status = task.status;
  card.classList.toggle("is-selected", selected);
  const progress = taskProgress(task.completedEntries, task.totalEntries, task.status);
  const statusMark = card.querySelector<HTMLElement>("[data-task-status]");
  const name = card.querySelector<HTMLElement>("[data-task-name]");
  const meta = card.querySelector<HTMLElement>("[data-task-meta]");
  const progressFill = card.querySelector<HTMLElement>("[data-task-progress-fill]");
  const duration = card.querySelector<HTMLElement>("[data-task-time]");
  if (statusMark) statusMark.dataset.status = task.status;
  if (name) setText(name, task.fileName);
  if (meta) {
    const metaText = `${languageLabel(task.targetLanguage)} · ${statusLabel(task.status)} · ${progress}% · ${taskAgentLabel(task)}`;
    setText(meta, metaText);
    meta.title = metaText;
  }
  if (progressFill) setWidth(progressFill, `${progress}%`);
  if (duration) setText(duration, formatDuration(task.durationMs));
}

function renderTaskList(): void {
  const list = element<HTMLDivElement>("task-list");
  setText(element<HTMLElement>("task-count"), String(state.tasks.length));
  if (state.tasks.length === 0) {
    if (!list.querySelector(".task-card-empty")) {
      list.innerHTML = `<div class="task-card-empty">还没有 Agent 提交的翻译任务。<br />请在 Agent 中发起字幕翻译。</div>`;
    }
    return;
  }
  list.querySelector(".task-card-empty")?.remove();
  const existing = new Map<string, HTMLButtonElement>();
  list.querySelectorAll<HTMLButtonElement>(".task-card[data-task-id]").forEach((card) => {
    if (card.dataset.taskId) existing.set(card.dataset.taskId, card);
  });
  const ordered: HTMLButtonElement[] = [];
  state.tasks.forEach((task, index) => {
    const card = existing.get(task.id) ?? createTaskCard(index);
    updateTaskCard(card, task);
    ordered.push(card);
    existing.delete(task.id);
  });
  applyChildOrder(list, ordered);
  existing.forEach((card) => card.remove());
}

function renderDetail(): void {
  const task = state.selected;
  const empty = element<HTMLElement>("empty-state");
  const detail = element<HTMLElement>("task-detail");
  if (!task) {
    empty.hidden = false;
    detail.hidden = true;
    return;
  }
  empty.hidden = true;
  detail.hidden = false;
  const meta = statusMeta[task.status] ?? statusMeta.queued;
  const statusDot = element<HTMLElement>("detail-status-dot");
  statusDot.dataset.status = task.status;
  setText(element<HTMLElement>("detail-status-label"), meta.label);
  setText(element<HTMLElement>("detail-language"), languageLabel(task.targetLanguage));
  setText(element<HTMLElement>("detail-format"), (task.outputFormat ?? task.inputFormat ?? "字幕").toUpperCase());
  setText(element<HTMLElement>("detail-file-name"), task.fileName);
  const notice = detailNotice(task);
  const noticeNode = element<HTMLElement>("detail-notice");
  noticeNode.hidden = !notice;
  if (notice) {
    noticeNode.dataset.tone = notice.tone;
    setText(element<HTMLElement>("detail-notice-text"), notice.text);
  } else {
    noticeNode.removeAttribute("data-tone");
    setText(element<HTMLElement>("detail-notice-text"), "");
  }
  setText(element<HTMLElement>("detail-entry-count"), `${task.completedEntries} / ${task.totalEntries}`);
  setText(element<HTMLElement>("detail-batch-count"), `${task.completedBatches} / ${task.batchCount}`);
  setText(element<HTMLElement>("detail-duration"), formatDuration(task.durationMs));
  const agentNode = element<HTMLElement>("detail-agent");
  const agentDetails = taskAgentLabel(task);
  setText(agentNode, agentDetails);
  agentNode.title = agentDetails;
  const modelDetails = taskModelLabel(task);
  const modelNode = element<HTMLElement>("detail-model");
  setText(modelNode, modelDetails);
  modelNode.title = modelDetails;
  element<HTMLElement>("detail-stat-model").title = `${agentDetails} · ${modelDetails}`;
  setText(element<HTMLElement>("batch-meta"), `${task.completedBatches} / ${task.batchCount} 批${task.warningCount > 0 ? ` · ${task.warningCount} 个提示` : ""}`);
  const downloadOutput = element<HTMLAnchorElement>("download-output");
  const detailActions = element<HTMLElement>("detail-actions");
  const hasDownload = task.status === "completed";
  downloadOutput.hidden = !hasDownload;
  detailActions.hidden = !hasDownload;
  downloadOutput.href = `/api/tasks/${encodeURIComponent(task.id)}/output`;
  renderFlow(task);
  renderSubtitles(task.entries);
}

function createBatchFlow(index: number): HTMLDetailsElement {
  const row = document.createElement("details");
  row.className = "flow-batch";
  row.style.animationDelay = `${Math.min(index * 55, 400)}ms`;
  row.innerHTML = `<summary class="flow-batch-summary">
      <span class="flow-batch-number" data-batch-number></span>
      <span class="flow-batch-copy"><span class="flow-batch-title"><strong data-batch-summary></strong><span class="flow-batch-count" data-batch-count></span></span><span class="flow-batch-summary-line" data-batch-summary-detail></span><span class="flow-batch-progress" aria-hidden="true"><span data-batch-progress-fill></span></span></span>
      <span class="flow-batch-state" data-batch-state></span>
      <span class="flow-batch-toggle" aria-hidden="true">${iconMarkup("chevron.down")}</span>
    </summary>
    <div class="flow-event-list flow-batch-events" data-flow-events></div>`;
  applyNativeIcons(row);
  return row;
}

function updateBatchFlow(row: HTMLDetailsElement, batch: BatchSnapshot, events: TaskEvent[]): void {
  const progress = batch.entryCount > 0 ? Math.round((batch.completedEntryCount / batch.entryCount) * 100) : 0;
  const summaryParts = [`${batch.completedEntryCount} / ${batch.entryCount} 条字幕`];
  if (batch.styleFallbackIds.length > 0) summaryParts.push(`${batch.styleFallbackIds.length} 条兼容样式`);
  if (batch.durationMs !== undefined) summaryParts.push(formatDuration(batch.durationMs));
  row.dataset.batchId = String(batch.batch);
  row.dataset.status = batch.status;
  if (!row.dataset.initialized) {
    row.open = ["translating", "validating", "retrying", "failed"].includes(batch.status) || events.length > 0 && batch.status !== "validated";
    row.dataset.initialized = "true";
  }
  const number = row.querySelector<HTMLElement>("[data-batch-number]");
  const countNode = row.querySelector<HTMLElement>("[data-batch-count]");
  const summaryNode = row.querySelector<HTMLElement>("[data-batch-summary]");
  const summaryDetailNode = row.querySelector<HTMLElement>("[data-batch-summary-detail]");
  const progressFill = row.querySelector<HTMLElement>("[data-batch-progress-fill]");
  const stateNode = row.querySelector<HTMLElement>("[data-batch-state]");
  if (number) setText(number, `B${String(batch.batch).padStart(2, "0")}`);
  if (countNode) setText(countNode, `${progress}%`);
  if (summaryNode) setText(summaryNode, summaryParts[0] ?? "");
  if (summaryDetailNode) setText(summaryDetailNode, summaryParts.slice(1).join(" · "));
  if (progressFill) setWidth(progressFill, `${progress}%`);
  if (stateNode) {
    stateNode.dataset.status = batch.status;
    setText(stateNode, batchMeta[batch.status]);
  }
  const eventList = row.querySelector<HTMLElement>("[data-flow-events]");
  if (eventList) renderFlowEvents(eventList, events, "批次过程会显示在这里。");
}

function eventTone(event: TaskEvent): EventTone {
  if (event.type === "batch.retrying") return "warning";
  if (event.type.endsWith("failed")) return "danger";
  if (["task.ready", "batch.validated", "task.completed"].includes(event.type)) return "success";
  if (["task.cancelled", "agent.note"].includes(event.type)) return "neutral";
  return "active";
}

function eventDetail(event: TaskEvent): string {
  const details: string[] = [];
  const entryCount = event.meta?.entryCount;
  if (event.type === "batch.validated" && typeof entryCount === "number") {
    details.push(`${entryCount} 条字幕`);
  } else if (event.type === "task.completed" && typeof entryCount === "number") {
    details.push(`${entryCount} 条字幕已合成`);
  } else {
    details.push(event.message);
  }
  if (["batch.validated", "task.completed"].includes(event.type) && event.durationMs !== undefined) {
    details.push(`用时 ${formatDuration(event.durationMs)}`);
  }
  const retryCount = event.meta?.retryCount;
  if (event.type === "batch.retrying" && typeof retryCount === "number") details.push(`第 ${retryCount} 次尝试`);
  const styleFallbackCount = event.meta?.styleFallbackCount;
  if (event.type === "batch.validated" && typeof styleFallbackCount === "number" && styleFallbackCount > 0) {
    details.push(`${styleFallbackCount} 条字幕采用兼容样式`);
  }
  const karaokeCount = event.meta?.karaokeCount;
  if (event.type === "batch.validated" && typeof karaokeCount === "number" && karaokeCount > 0) {
    details.push(`${karaokeCount} 条特效字幕保留原格式`);
  }
  const outputFormat = event.meta?.outputFormat;
  if (event.type === "task.completed" && typeof outputFormat === "string" && outputFormat) details.push(`输出格式 ${outputFormat.toUpperCase()}`);
  return details.filter(Boolean).join(" · ");
}

function createFlowEvent(index: number): HTMLDivElement {
  const row = document.createElement("div");
  row.className = "flow-event-row";
  row.style.animationDelay = `${Math.min(index * 35, 320)}ms`;
  row.innerHTML = `<span class="flow-event-marker" data-event-marker></span>
    <div class="flow-event-copy"><div class="flow-event-title"><strong data-event-title></strong></div><small data-event-detail></small></div>
    <time class="flow-event-time" data-event-time></time>`;
  return row;
}

function updateFlowEvent(row: HTMLDivElement, event: TaskEvent): void {
  row.dataset.eventId = String(event.id);
  const marker = row.querySelector<HTMLElement>("[data-event-marker]");
  const title = row.querySelector<HTMLElement>("[data-event-title]");
  const detail = row.querySelector<HTMLElement>("[data-event-detail]");
  const time = row.querySelector<HTMLElement>("[data-event-time]");
  if (marker) marker.dataset.tone = eventTone(event);
  if (title) setText(title, eventTitles[event.type]);
  if (detail) setText(detail, eventDetail(event));
  if (time) setText(time, formatEventTime(event.at));
}

function renderFlowEvents(list: HTMLElement, events: TaskEvent[], emptyMessage: string): void {
  if (events.length === 0) {
    if (!list.querySelector(".flow-empty")) list.innerHTML = `<div class="flow-empty">${emptyMessage}</div>`;
    return;
  }
  list.querySelector(".flow-empty")?.remove();
  const existing = new Map<string, HTMLDivElement>();
  list.querySelectorAll<HTMLDivElement>(".flow-event-row[data-event-id]").forEach((row) => {
    if (row.dataset.eventId) existing.set(row.dataset.eventId, row);
  });
  const ordered: HTMLDivElement[] = [];
  [...events].reverse().forEach((event, index) => {
    const row = existing.get(String(event.id)) ?? createFlowEvent(index);
    updateFlowEvent(row, event);
    ordered.push(row);
    existing.delete(String(event.id));
  });
  applyChildOrder(list, ordered);
  existing.forEach((row) => row.remove());
}

function createFlowBatch(index: number): HTMLDetailsElement {
  const row = createBatchFlow(index);
  return row;
}

function renderFlow(task: TaskSnapshot): void {
  const flowList = element<HTMLDivElement>("flow-list");
  const stage = element<HTMLElement>("flow-stage");
  const taskEvents = task.events.filter((event) => event.batch === undefined);
  const hasStage = taskEvents.length > 0;
  stage.hidden = !hasStage;
  flowList.dataset.hasStage = String(hasStage);
  setText(element<HTMLElement>("flow-stage-meta"), `${taskEvents.length} 条记录`);
  renderFlowEvents(element<HTMLElement>("flow-task-events"), taskEvents, "任务阶段记录会显示在这里。");

  const list = element<HTMLDivElement>("flow-batches");
  if (task.batches.length === 0) {
    if (!list.querySelector(".flow-empty")) list.innerHTML = `<div class="flow-empty">字幕准备完成后，批次会出现在这里。</div>`;
    return;
  }
  list.querySelector(".flow-empty")?.remove();
  const existing = new Map<string, HTMLDetailsElement>();
  list.querySelectorAll<HTMLDetailsElement>(".flow-batch[data-batch-id]").forEach((row) => {
    if (row.dataset.batchId) existing.set(row.dataset.batchId, row);
  });
  const ordered: HTMLDetailsElement[] = [];
  task.batches.forEach((batch, index) => {
    const row = existing.get(String(batch.batch)) ?? createFlowBatch(index);
    updateBatchFlow(row, batch, task.events.filter((event) => event.batch === batch.batch));
    ordered.push(row);
    existing.delete(String(batch.batch));
  });
  applyChildOrder(list, ordered);
  existing.forEach((row) => row.remove());
}

function createSubtitleRow(index: number): HTMLDivElement {
  const row = document.createElement("div");
  row.className = "subtitle-row";
  row.dataset.view = state.subtitleView;
  row.style.animationDelay = `${Math.min(index * 30, 300)}ms`;
  if (state.subtitleView === "columns") {
    row.innerHTML = `<span class="subtitle-id" data-subtitle-id></span>
      <time class="subtitle-time" data-subtitle-time></time>
      <div class="subtitle-field"><span class="subtitle-label">原字幕</span><strong data-subtitle-source></strong></div>
      <div class="subtitle-field translation-field"><span class="subtitle-label">翻译后</span><strong data-subtitle-translation></strong><span class="entry-badge" data-entry-badge hidden></span></div>`;
  } else {
    row.innerHTML = `<span class="subtitle-id" data-subtitle-id></span>
      <div class="subtitle-copy"><div class="subtitle-field"><span class="subtitle-label">原字幕</span><strong data-subtitle-source></strong></div><div class="subtitle-field translation-field"><span class="subtitle-label">翻译后</span><strong data-subtitle-translation></strong><span class="entry-badge" data-entry-badge hidden></span></div></div>
      <time class="subtitle-time" data-subtitle-time></time>`;
  }
  return row;
}

function updateSubtitleRow(row: HTMLDivElement, entry: EntrySnapshot): void {
  const translated = Boolean(entry.translatedText);
  const translationText = entry.translatedText ?? (entry.status === "pending" ? "等待 Agent 翻译" : "正在处理");
  const badgeText = entry.degradation === "karaoke" ? "卡拉 OK 已降级" : entry.styleFallback ? "样式已降级" : "";
  row.dataset.entryId = entry.id;
  const id = row.querySelector<HTMLElement>("[data-subtitle-id]");
  const source = row.querySelector<HTMLElement>("[data-subtitle-source]");
  const translation = row.querySelector<HTMLElement>("[data-subtitle-translation]");
  const time = row.querySelector<HTMLElement>("[data-subtitle-time]");
  const badge = row.querySelector<HTMLElement>("[data-entry-badge]");
  if (id) setText(id, entry.id);
  if (source) setText(source, entry.sourceText);
  if (translation) {
    translation.classList.toggle("translation", translated);
    translation.classList.toggle("is-pending", !translated);
    setText(translation, translationText);
  }
  if (time) setText(time, formatSubtitleTime(entry));
  if (badge) {
    badge.hidden = !badgeText;
    badge.classList.toggle("danger", entry.styleFallback === true);
    setText(badge, badgeText);
  }
}

function renderSubtitles(entries: EntrySnapshot[]): void {
  const list = element<HTMLDivElement>("subtitle-list");
  const viewChanged = list.dataset.view !== state.subtitleView;
  if (viewChanged) {
    list.dataset.view = state.subtitleView;
    list.innerHTML = "";
  }
  if (entries.length === 0) {
    if (!list.querySelector(".list-empty")) list.innerHTML = `<div class="list-empty">字幕条目准备后会在这里显示。</div>`;
    return;
  }
  list.querySelector(".list-empty")?.remove();
  const existing = new Map<string, HTMLDivElement>();
  list.querySelectorAll<HTMLDivElement>(".subtitle-row[data-entry-id]").forEach((row) => {
    if (row.dataset.entryId) existing.set(row.dataset.entryId, row);
  });
  const ordered: HTMLDivElement[] = [];
  entries.forEach((entry, index) => {
    const row = existing.get(entry.id) ?? createSubtitleRow(index);
    updateSubtitleRow(row, entry);
    ordered.push(row);
    existing.delete(entry.id);
  });
  applyChildOrder(list, ordered);
  existing.forEach((row) => row.remove());
}

let detailRefreshTimer: number | undefined;
function scheduleDetailRefresh(): void {
  if (detailRefreshTimer !== undefined) window.clearTimeout(detailRefreshTimer);
  detailRefreshTimer = window.setTimeout(() => {
    detailRefreshTimer = undefined;
    if (state.selectedId) void loadTask(state.selectedId, false);
  }, 100);
}

async function loadTask(id: string, connect = true): Promise<void> {
  try {
    const payload = await api<{ task: TaskSnapshot }>(`/api/tasks/${encodeURIComponent(id)}`);
    state.selectedId = id;
    state.selected = payload.task;
    renderTaskList();
    renderDetail();
    if (connect) connectEvents(id);
  } catch (error) {
    showHint(error instanceof Error ? error.message : String(error), true);
  }
}

function connectEvents(id: string): void {
  state.eventSource?.close();
  const stream = new EventSource(`/api/tasks/${encodeURIComponent(id)}/events`);
  stream.addEventListener("open", () => setConnectionStatus("online"));
  stream.addEventListener("snapshot", (event) => {
    const snapshot = JSON.parse((event as MessageEvent<string>).data) as TaskSnapshot;
    if (snapshot.id !== state.selectedId) return;
    state.selected = snapshot;
    renderDetail();
    renderTaskList();
  });
  stream.addEventListener("progress", () => scheduleDetailRefresh());
  stream.onerror = () => {
    setConnectionStatus("offline");
    element<HTMLElement>("visualizer-hint").textContent = "本地服务连接短暂中断，正在尝试重新连接……";
  };
  state.eventSource = stream;
}

async function refreshTasks(): Promise<void> {
  try {
    const payload = await api<{ tasks: TaskSummary[] }>("/api/tasks");
    state.tasks = payload.tasks;
    renderTaskList();
    if (state.selectedId && state.tasks.some((task) => task.id === state.selectedId)) {
      scheduleDetailRefresh();
    } else if (state.tasks[0]) {
      await loadTask(state.tasks[0].id);
    } else {
      renderDetail();
    }
  } catch (error) {
    showHint(error instanceof Error ? error.message : String(error), true);
  }
}

function showHint(message: string, isError = false): void {
  const hint = element<HTMLElement>("visualizer-hint");
  hint.textContent = message;
  hint.style.color = isError ? "var(--danger)" : "var(--ink-faint)";
}

function renderAgentProfile(profile: AgentProfile): void {
  const agentName = profile.agent === "等待 Agent 自报" ? "Agent" : profile.agent;
  setText(element<HTMLElement>("agent-session-agent"), agentName);
  renderTaskList();
  if (state.selected) renderDetail();
}

async function refreshAgentProfile(): Promise<void> {
  try {
    const payload = await api<{ agent: AgentProfile }>("/api/agent");
    state.agentProfile = payload.agent;
    renderAgentProfile(payload.agent);
  } catch (error) {
    showHint(error instanceof Error ? error.message : String(error), true);
  }
}

function renderProgramVersion(version: string): void {
  setText(element<HTMLElement>("program-version"), "v" + version);
}

async function refreshProgramVersion(): Promise<void> {
  try {
    const payload = await api<{ version: string }>("/api/health");
    renderProgramVersion(payload.version);
  } catch (error) {
    showHint(error instanceof Error ? error.message : String(error), true);
  }
}

function setupTheme(): void {
  const root = document.documentElement;
  const stored = window.localStorage.getItem("subtitle-visualizer-theme");
  if (stored === "dark" || stored === "light") root.dataset.theme = stored;
  const button = element<HTMLButtonElement>("theme-toggle");
  const updateThemeControl = (theme: "light" | "dark"): void => {
    const nextTheme = theme === "dark" ? "浅色" : "深色";
    const label = `切换到${nextTheme}主题`;
    button.setAttribute("aria-label", label);
    button.title = label;
    setIcon(element<HTMLElement>("theme-toggle-icon"), theme === "dark" ? "sun.max.fill" : "moon.fill");
  };
  updateThemeControl(root.dataset.theme === "dark" ? "dark" : "light");
  button.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    window.localStorage.setItem("subtitle-visualizer-theme", next);
    document.querySelector('meta[name="theme-color"]')?.setAttribute("content", next === "dark" ? "#1d2421" : "#f4f0e8");
    updateThemeControl(next);
  });
}

function setSubtitleView(view: "stacked" | "columns"): void {
  state.subtitleView = view;
  window.localStorage.setItem("subtitle-visualizer-subtitle-view", view);
  document.querySelectorAll<HTMLButtonElement>("[data-view-mode]").forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.viewMode === view));
  });
  if (state.selected) renderSubtitles(state.selected.entries);
}

function setupSubtitleView(): void {
  const stored = window.localStorage.getItem("subtitle-visualizer-subtitle-view");
  if (stored === "stacked" || stored === "columns") state.subtitleView = stored;
  document.querySelectorAll<HTMLButtonElement>("[data-view-mode]").forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.viewMode === state.subtitleView));
    button.addEventListener("click", () => {
      const view = button.dataset.viewMode;
      if (view === "stacked" || view === "columns") setSubtitleView(view);
    });
  });
}

function setMobileMenu(open: boolean): void {
  const shell = element<HTMLElement>("app-shell");
  const toggle = element<HTMLButtonElement>("mobile-menu-toggle");
  const backdrop = element<HTMLButtonElement>("mobile-menu-backdrop");
  const label = open ? "关闭翻译任务菜单" : "打开翻译任务菜单";
  shell.classList.toggle("mobile-menu-open", open);
  toggle.setAttribute("aria-expanded", String(open));
  toggle.setAttribute("aria-label", label);
  toggle.title = label;
  setText(element<HTMLElement>("mobile-menu-glyph"), open ? "×" : "☰");
  setText(element<HTMLElement>("mobile-menu-label"), open ? "关闭" : "菜单");
  backdrop.hidden = !open;
}

function setupMobileMenu(): void {
  const shell = element<HTMLElement>("app-shell");
  const toggle = element<HTMLButtonElement>("mobile-menu-toggle");
  const backdrop = element<HTMLButtonElement>("mobile-menu-backdrop");
  setMobileMenu(false);
  toggle.addEventListener("click", () => setMobileMenu(!shell.classList.contains("mobile-menu-open")));
  backdrop.addEventListener("click", () => setMobileMenu(false));
  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setMobileMenu(false);
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth > 760) setMobileMenu(false);
  });
}

function setupInteractions(): void {
  element<HTMLDivElement>("task-list").addEventListener("click", (event) => {
    const target = (event.target as HTMLElement).closest<HTMLElement>("[data-task-id]");
    if (target?.dataset.taskId) {
      setMobileMenu(false);
      void loadTask(target.dataset.taskId);
    }
  });
}

hydrateIcons();
setupIconSystem();
setupTheme();
setupSubtitleView();
setupMobileMenu();
setupInteractions();
void refreshAgentProfile();
void refreshProgramVersion();
void refreshTasks();
window.setInterval(() => {
  void refreshAgentProfile();
  void refreshProgramVersion();
  void refreshTasks();
}, 5000);
