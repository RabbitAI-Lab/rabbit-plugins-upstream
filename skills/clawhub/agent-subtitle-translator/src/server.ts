import { createReadStream, existsSync } from "node:fs";
import { mkdir, readFile, stat } from "node:fs/promises";
import { homedir } from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";
import { createServer, type IncomingMessage, type Server, type ServerResponse } from "node:http";
import { fileURLToPath } from "node:url";

import { DEFAULT_HOST, DEFAULT_PORT, type ApiError, type CreateTaskRequest, type TaskEvent } from "./common.js";
import { TaskManager } from "./task-manager.js";

const MAX_BODY_BYTES = 30 * 1024 * 1024;

interface ServerOptions {
  rootDir: string;
  host: string;
  port: number;
  dataDir: string;
  open: boolean;
}

function defaultRootDir(): string {
  const moduleDir = path.dirname(fileURLToPath(import.meta.url));
  const candidates = [
    path.resolve(moduleDir, "../.."),
    path.resolve(moduleDir, ".."),
    process.cwd(),
  ];
  return candidates.find((candidate) => existsSync(path.join(candidate, "web", "index.html"))) ?? process.cwd();
}

function json(res: ServerResponse, value: unknown, status = 200): void {
  const body = JSON.stringify(value);
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": Buffer.byteLength(body),
    "Cache-Control": "no-store",
  });
  res.end(body);
}

function errorJson(res: ServerResponse, message: string, status = 400): void {
  const payload: ApiError = { status: "error", error: message };
  json(res, payload, status);
}

function text(res: ServerResponse, value: string, contentType: string, status = 200): void {
  res.writeHead(status, {
    "Content-Type": contentType,
    "Content-Length": Buffer.byteLength(value),
  });
  res.end(value);
}

async function body(req: IncomingMessage): Promise<unknown> {
  const chunks: Buffer[] = [];
  let size = 0;
  for await (const chunk of req) {
    const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
    size += buffer.length;
    if (size > MAX_BODY_BYTES) {
      throw new Error("请求内容过大");
    }
    chunks.push(buffer);
  }
  const raw = Buffer.concat(chunks).toString("utf8");
  if (!raw.trim()) {
    return {};
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    throw new Error("请求 JSON 格式无效");
  }
}

function record(value: unknown): Record<string, unknown> {
  return value && typeof value === "object" ? (value as Record<string, unknown>) : {};
}

function stringValue(value: unknown): string | undefined {
  return typeof value === "string" && value.trim() ? value.trim() : undefined;
}

function numberValue(value: unknown): number | undefined {
  return typeof value === "number" && Number.isFinite(value) ? value : undefined;
}

async function staticFile(res: ServerResponse, filePath: string, contentType: string): Promise<void> {
  try {
    const contents = await readFile(filePath);
    res.writeHead(200, {
      "Content-Type": contentType,
      "Content-Length": contents.byteLength,
      "Cache-Control": "no-cache",
    });
    res.end(contents);
  } catch {
    errorJson(res, "Web 端尚未构建，请先运行 npm run build", 404);
  }
}

function writeSse(res: ServerResponse, eventName: string, value: unknown): void {
  if (res.writableEnded) {
    return;
  }
  res.write(`event: ${eventName}\ndata: ${JSON.stringify(value)}\n\n`);
}

function openBrowser(url: string): void {
  const platform = process.platform;
  const command = platform === "darwin" ? "open" : platform === "win32" ? "cmd" : "xdg-open";
  const args = platform === "win32" ? ["/c", "start", "", url] : [url];
  const child = spawn(command, args, { detached: true, stdio: "ignore" });
  child.unref();
}

async function route(
  req: IncomingMessage,
  res: ServerResponse,
  manager: TaskManager,
  rootDir: string,
): Promise<void> {
  const requestUrl = new URL(req.url ?? "/", "http://127.0.0.1");
  const pathname = requestUrl.pathname;
  const method = req.method ?? "GET";

  if (method === "GET" && pathname === "/api/health") {
    json(res, {
      status: "ok",
      service: "subtitle-visualizer",
      version: manager.getSkillVersion(),
      now: new Date().toISOString(),
      taskCount: manager.listTasks().length,
    });
    return;
  }

  if (method === "GET" && pathname === "/api/tasks") {
    json(res, { tasks: manager.listTasks() });
    return;
  }

  if (pathname === "/api/agent") {
    if (method === "GET") {
      json(res, { agent: manager.getAgentProfile() });
      return;
    }
    if (method === "POST") {
      const request = record(await body(req));
      json(res, {
        agent: await manager.reportAgent(
          stringValue(request.agent) ?? "",
          stringValue(request.model) ?? "",
          stringValue(request.modelVersion),
          stringValue(request.modelSeries),
          stringValue(request.reasoningStrength),
        ),
      });
      return;
    }
  }

  if (method === "GET" && pathname === "/") {
    await staticFile(res, path.join(rootDir, "web", "index.html"), "text/html; charset=utf-8");
    return;
  }
  if (method === "GET" && pathname === "/styles.css") {
    await staticFile(res, path.join(rootDir, "web", "styles.css"), "text/css; charset=utf-8");
    return;
  }
  if (method === "GET" && pathname === "/app.js") {
    await staticFile(res, path.join(rootDir, "dist", "web", "app.js"), "text/javascript; charset=utf-8");
    return;
  }
  if (method === "GET" && pathname === "/icons.js") {
    await staticFile(res, path.join(rootDir, "dist", "web", "icons.js"), "text/javascript; charset=utf-8");
    return;
  }
  if (method === "GET" && pathname === "/assets/icon-small.png") {
    await staticFile(res, path.join(rootDir, "assets", "icon-small.png"), "image/png");
    return;
  }
  if (method === "GET" && pathname === "/assets/icon-large.png") {
    await staticFile(res, path.join(rootDir, "assets", "icon-large.png"), "image/png");
    return;
  }
  if (method === "GET" && pathname === "/favicon.ico") {
    await staticFile(res, path.join(rootDir, "assets", "icon-small.png"), "image/png");
    return;
  }

  if (method === "POST" && pathname === "/api/tasks") {
    const request = record(await body(req)) as unknown as CreateTaskRequest;
    const task = await manager.createTask(request);
    json(res, { task }, 202);
    return;
  }

  const taskMatch = pathname.match(/^\/api\/tasks\/([^/]+)(?:\/(.*))?$/);
  if (!taskMatch) {
    errorJson(res, "接口不存在", 404);
    return;
  }
  const taskId = decodeURIComponent(taskMatch[1] as string);
  const action = taskMatch[2] ?? "";

  if (method === "GET" && action === "events") {
    const snapshot = manager.getTask(taskId);
    res.writeHead(200, {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
      "X-Accel-Buffering": "no",
    });
    writeSse(res, "snapshot", snapshot);
    const unsubscribe = manager.subscribe(taskId, (event: TaskEvent) => writeSse(res, "progress", event));
    req.on("close", unsubscribe);
    return;
  }

  if (method === "GET" && action === "output") {
    const outputPath = manager.getOutputPath(taskId);
    const outputStat = await stat(outputPath);
    res.writeHead(200, {
      "Content-Type": "application/octet-stream",
      "Content-Length": outputStat.size,
      "Content-Disposition": `attachment; filename*=UTF-8''${encodeURIComponent(path.basename(outputPath))}`,
    });
    createReadStream(outputPath).pipe(res);
    return;
  }

  if (method === "GET" && action === "") {
    json(res, { task: manager.getTask(taskId) });
    return;
  }

  if (method !== "POST") {
    errorJson(res, "只支持 GET 和 POST", 405);
    return;
  }

  const request = record(await body(req));
  if (action === "cancel") {
    json(res, { task: await manager.cancel(taskId) });
    return;
  }
  if (action === "compose") {
    json(res, { task: await manager.compose(taskId, stringValue(request.outputPath), request.overwrite === true) });
    return;
  }
  if (action === "events") {
    json(res, { task: await manager.addNote(taskId, stringValue(request.message) ?? "") });
    return;
  }

  const batchMatch = action.match(/^batches\/(\d+)\/(start|retry|response)$/);
  if (!batchMatch) {
    errorJson(res, "任务操作不存在", 404);
    return;
  }
  const batch = Number(batchMatch[1]);
  const operation = batchMatch[2];
  if (operation === "start") {
    json(res, { task: await manager.startBatch(taskId, batch) });
    return;
  }
  if (operation === "retry") {
    json(res, { task: await manager.retryBatch(taskId, batch) });
    return;
  }
  const responsePath = stringValue(request.responsePath);
  if (!responsePath) {
    errorJson(res, "缺少 responsePath");
    return;
  }
  json(
    res,
    {
      task: await manager.submitResponse(
        taskId,
        batch,
        responsePath,
        request.allowStyleFallback === true,
      ),
    },
  );
}

export async function startServer(options: Partial<ServerOptions> = {}): Promise<{ server: Server; manager: TaskManager; url: string }> {
  const rootDir = path.resolve(options.rootDir ?? defaultRootDir());
  const host = options.host ?? process.env.SUBTITLE_VISUALIZER_HOST ?? DEFAULT_HOST;
  const port = options.port ?? Number(process.env.SUBTITLE_VISUALIZER_PORT ?? DEFAULT_PORT);
  const dataDir = path.resolve(
    options.dataDir ?? process.env.SUBTITLE_VISUALIZER_DATA ?? path.join(homedir(), ".agent-subtitle-translator", "visualizer"),
  );
  await mkdir(dataDir, { recursive: true });
  const manager = new TaskManager({ skillRoot: rootDir, dataDir });
  await manager.init();
  const server = createServer((req, res) => {
    void route(req, res, manager, rootDir).catch((error: unknown) => {
      const message = error instanceof Error ? error.message : String(error);
      if (!res.headersSent) {
        errorJson(res, message, message.includes("找不到") ? 404 : 422);
      } else {
        res.end();
      }
    });
  });
  await new Promise<void>((resolve, reject) => {
    server.once("error", reject);
    server.listen(port, host, () => {
      server.off("error", reject);
      resolve();
    });
  });
  const address = server.address();
  const actualPort = typeof address === "object" && address ? address.port : port;
  const url = `http://${host}:${actualPort}`;
  if (options.open) {
    openBrowser(url);
  }
  return { server, manager, url };
}

function cliOptions(argv: string[]): Partial<ServerOptions> {
  const options: Partial<ServerOptions> = { open: argv.includes("--open") };
  for (let index = 0; index < argv.length; index += 1) {
    const flag = argv[index];
    const value = argv[index + 1];
    if (flag === "--host" && value) {
      options.host = value;
      index += 1;
    } else if (flag === "--port" && value) {
      options.port = Number(value);
      index += 1;
    } else if (flag === "--data-dir" && value) {
      options.dataDir = value;
      index += 1;
    }
  }
  return options;
}

if (process.argv[1]?.endsWith("server.js")) {
  const options = cliOptions(process.argv.slice(2));
  const result = await startServer(options);
  console.log(`字幕翻译可视化服务已启动：${result.url}`);
  console.log("等待 Agent 通过 visualizer:bridge 报告翻译进度……");
}
