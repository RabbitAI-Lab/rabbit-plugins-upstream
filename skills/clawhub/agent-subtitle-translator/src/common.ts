export const DEFAULT_HOST = "127.0.0.1";
export const DEFAULT_PORT = 4317;
export const MAX_BATCH_SIZE = 32;

export type TaskStatus =
  | "queued"
  | "preparing"
  | "awaiting_translation"
  | "translating"
  | "validating"
  | "retrying"
  | "ready_to_compose"
  | "composing"
  | "completed"
  | "failed"
  | "cancelled"
  | "paused";

export type BatchStatus =
  | "pending"
  | "translating"
  | "validating"
  | "validated"
  | "retrying"
  | "failed";

export type EntryStatus = "pending" | "translating" | "validated" | "fallback" | "failed";

export type TaskEventType =
  | "task.created"
  | "task.preparing"
  | "task.ready"
  | "task.failed"
  | "task.cancelled"
  | "batch.started"
  | "batch.validating"
  | "batch.validated"
  | "batch.retrying"
  | "batch.failed"
  | "task.composing"
  | "task.completed"
  | "agent.note";

export interface TaskEvent {
  id: number;
  taskId: string;
  type: TaskEventType;
  at: string;
  message: string;
  status?: TaskStatus;
  batch?: number;
  durationMs?: number;
  meta?: Record<string, string | number | boolean | null>;
}

export interface BatchSnapshot {
  batch: number;
  ids: string[];
  status: BatchStatus;
  retryCount: number;
  entryCount: number;
  completedEntryCount: number;
  startedAt?: string;
  finishedAt?: string;
  durationMs?: number;
  error?: string;
  styleFallbackIds: string[];
}

export interface EntrySnapshot {
  id: string;
  order: number;
  startMs?: number;
  endMs?: number;
  sourceText: string;
  translatedText?: string;
  status: EntryStatus;
  kind: "srt" | "ass";
  degradation?: "karaoke";
  styleFallback?: boolean;
}

export interface TaskSummary {
  id: string;
  fileName: string;
  agent?: string;
  model?: string;
  modelVersion?: string;
  modelSeries?: string;
  reasoningStrength?: string;
  inputFormat?: string;
  outputFormat?: string;
  targetLanguage: string;
  sourceLanguage?: string;
  status: TaskStatus;
  createdAt: string;
  updatedAt: string;
  startedAt?: string;
  finishedAt?: string;
  durationMs?: number;
  totalEntries: number;
  completedEntries: number;
  batchCount: number;
  completedBatches: number;
  warningCount: number;
  error?: string;
  outputFileName?: string;
}

export interface TaskSnapshot extends TaskSummary {
  batches: BatchSnapshot[];
  entries: EntrySnapshot[];
  events: TaskEvent[];
}

export interface AgentProfile {
  agent: string;
  model: string;
  modelVersion?: string;
  modelSeries?: string;
  reasoningStrength?: string;
  reportedAt?: string;
}

export interface CreateTaskRequest {
  filePath?: string;
  fileName?: string;
  contentBase64?: string;
  targetLanguage: string;
  sourceLanguage?: string;
  batchSize?: number;
}

export interface CreateTaskResponse {
  task: TaskSnapshot;
}

export interface ApiError {
  status: "error";
  error: string;
}

export function isTaskStatus(value: string): value is TaskStatus {
  return [
    "queued",
    "preparing",
    "awaiting_translation",
    "translating",
    "validating",
    "retrying",
    "ready_to_compose",
    "composing",
    "completed",
    "failed",
    "cancelled",
    "paused",
  ].includes(value);
}

export function formatDuration(durationMs: number | undefined): string {
  if (durationMs === undefined || !Number.isFinite(durationMs)) {
    return "—";
  }
  const totalSeconds = Math.max(0, Math.round(durationMs / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) {
    return `${hours}小时 ${String(minutes).padStart(2, "0")}分`;
  }
  return `${String(minutes).padStart(2, "0")}分 ${String(seconds).padStart(2, "0")}秒`;
}

export function formatTimestamp(ms: number | undefined): string {
  if (ms === undefined || !Number.isFinite(ms)) {
    return "—";
  }
  const totalSeconds = Math.max(0, Math.floor(ms / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}
