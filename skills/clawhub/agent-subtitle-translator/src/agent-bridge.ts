import { DEFAULT_HOST, DEFAULT_PORT, type CreateTaskRequest } from "./common.js";
import { startServer } from "./server.js";

type Flags = Record<string, string | boolean>;

function parseFlags(args: string[]): Flags {
  const flags: Flags = {};
  for (let index = 0; index < args.length; index += 1) {
    const token = args[index];
    if (!token?.startsWith("--")) {
      continue;
    }
    const key = token.slice(2);
    const value = args[index + 1];
    if (value && !value.startsWith("--")) {
      flags[key] = value;
      index += 1;
    } else {
      flags[key] = true;
    }
  }
  return flags;
}

function flag(flags: Flags, name: string, required = false): string | undefined {
  const value = flags[name];
  if (typeof value === "string" && value.trim()) {
    return value;
  }
  if (required) {
    throw new Error(`缺少参数 --${name}`);
  }
  return undefined;
}

function numberFlag(flags: Flags, name: string): number | undefined {
  const value = flag(flags, name);
  if (value === undefined) return undefined;
  const parsed = Number(value);
  if (!Number.isInteger(parsed)) throw new Error(`参数 --${name} 必须是整数`);
  return parsed;
}

function baseUrl(flags: Flags): string {
  return (flag(flags, "url") ?? process.env.SUBTITLE_VISUALIZER_URL ?? `http://${DEFAULT_HOST}:${DEFAULT_PORT}`).replace(/\/$/, "");
}

async function request(url: string, init?: RequestInit): Promise<unknown> {
  const response = await fetch(url, {
    ...init,
    headers: { "Content-Type": "application/json", ...(init?.headers ?? {}) },
  });
  const payload = (await response.json()) as { error?: string };
  if (!response.ok) {
    throw new Error(payload.error ?? `请求失败：${response.status}`);
  }
  return payload;
}

function jsonBody(value: unknown): RequestInit {
  return { method: "POST", body: JSON.stringify(value) };
}

function usage(): void {
  console.log(`字幕翻译可视化 Agent 桥接命令

服务：
  start [--open] [--port 4317] [--data-dir PATH]

任务：
  create --input FILE --target-language zh-Hans [--source-language en] [--batch-size 32]
  status
  note --task TASK_ID --message "说明"

Agent 身份：
  identify --agent "Agent 名称" --model "模型名称" [--model-version "版本"] [--model-series "系列"] [--reasoning-strength "推理强度"]

批次：
  batch-start --task TASK_ID --batch 1
  submit-response --task TASK_ID --batch 1 --response FILE [--allow-style-fallback]
  retry-batch --task TASK_ID --batch 1
  compose --task TASK_ID [--output FILE] [--overwrite]

服务默认只监听本机 127.0.0.1，不会替 Agent 调用翻译模型。`);
}

async function main(): Promise<void> {
  const [command, ...rest] = process.argv.slice(2);
  if (!command || command === "--help" || command === "help") {
    usage();
    return;
  }
  const flags = parseFlags(rest);
  if (command === "start") {
    const result = await startServer({
      open: flags.open === true,
      host: flag(flags, "host"),
      port: numberFlag(flags, "port"),
      dataDir: flag(flags, "data-dir"),
    });
    console.log(`字幕翻译可视化服务已启动：${result.url}`);
    await new Promise<void>(() => undefined);
    return;
  }

  const url = baseUrl(flags);
  if (command === "create") {
    const requestBody: CreateTaskRequest = {
      filePath: flag(flags, "input", true),
      targetLanguage: flag(flags, "target-language", true) as string,
    };
    const sourceLanguage = flag(flags, "source-language");
    const batchSize = numberFlag(flags, "batch-size");
    if (sourceLanguage) requestBody.sourceLanguage = sourceLanguage;
    if (batchSize !== undefined) requestBody.batchSize = batchSize;
    console.log(JSON.stringify(await request(`${url}/api/tasks`, jsonBody(requestBody)), null, 2));
    return;
  }
  if (command === "status") {
    console.log(JSON.stringify(await request(`${url}/api/tasks`), null, 2));
    return;
  }

  if (command === "identify") {
    console.log(JSON.stringify(await request(url + "/api/agent", jsonBody({
      agent: flag(flags, "agent", true),
      model: flag(flags, "model", true),
      modelVersion: flag(flags, "model-version"),
      modelSeries: flag(flags, "model-series"),
      reasoningStrength: flag(flags, "reasoning-strength"),
    })), null, 2));
    return;
  }

  const taskId = flag(flags, "task", true) as string;
  if (command === "note") {
    console.log(JSON.stringify(await request(`${url}/api/tasks/${encodeURIComponent(taskId)}/events`, jsonBody({ message: flag(flags, "message", true) })), null, 2));
    return;
  }
  if (command === "compose") {
    console.log(JSON.stringify(await request(`${url}/api/tasks/${encodeURIComponent(taskId)}/compose`, jsonBody({
      outputPath: flag(flags, "output"),
      overwrite: flags.overwrite === true,
    })), null, 2));
    return;
  }
  const batch = numberFlag(flags, "batch");
  if (batch === undefined) throw new Error("缺少参数 --batch");
  if (command === "batch-start") {
    console.log(JSON.stringify(await request(`${url}/api/tasks/${encodeURIComponent(taskId)}/batches/${batch}/start`, jsonBody({})), null, 2));
    return;
  }
  if (command === "retry-batch") {
    console.log(JSON.stringify(await request(`${url}/api/tasks/${encodeURIComponent(taskId)}/batches/${batch}/retry`, jsonBody({})), null, 2));
    return;
  }
  if (command === "submit-response") {
    console.log(JSON.stringify(await request(`${url}/api/tasks/${encodeURIComponent(taskId)}/batches/${batch}/response`, jsonBody({
      responsePath: flag(flags, "response", true),
      allowStyleFallback: flags["allow-style-fallback"] === true,
    })), null, 2));
    return;
  }
  throw new Error(`未知命令：${command}`);
}

main().catch((error: unknown) => {
  console.error(JSON.stringify({ status: "error", error: error instanceof Error ? error.message : String(error) }));
  process.exitCode = 1;
});
