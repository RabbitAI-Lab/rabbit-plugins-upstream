import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { readFile, rm, writeFile, mkdtemp } from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import { tmpdir } from "node:os";
import test from "node:test";
import { promisify } from "node:util";

import type { TaskSnapshot } from "../src/common.js";
import { TaskManager } from "../src/task-manager.js";
import { startServer } from "../src/server.js";

const ROOT = path.resolve(process.cwd());
const PACKAGE_VERSION = (JSON.parse(readFileSync(path.join(ROOT, "package.json"), "utf8")) as { version: string }).version;
const FIXTURE = path.join(ROOT, "tests", "fixtures", "basic.srt");
const KARAOKE_FIXTURE = path.join(ROOT, "tests", "fixtures", "karaoke.ass");
const execFileAsync = promisify(execFile);

async function waitFor<T>(read: () => T, predicate: (value: T) => boolean): Promise<T> {
  const deadline = Date.now() + 15_000;
  while (Date.now() < deadline) {
    const value = read();
    if (predicate(value)) return value;
    await new Promise((resolve) => setTimeout(resolve, 25));
  }
  throw new Error("Timed out while waiting for visualizer task state");
}

async function waitForServerTask(baseUrl: string, id: string): Promise<void> {
  const deadline = Date.now() + 15_000;
  while (Date.now() < deadline) {
    const response = await fetch(`${baseUrl}/api/tasks/${encodeURIComponent(id)}`);
    const payload = (await response.json()) as { task: { status: string } };
    if (!["queued", "preparing", "translating", "validating", "composing"].includes(payload.task.status)) return;
    await new Promise((resolve) => setTimeout(resolve, 25));
  }
  throw new Error("Timed out while waiting for server task cleanup");
}

async function assertFrozenDuration(manager: TaskManager, task: TaskSnapshot): Promise<void> {
  assert.equal(Number.isFinite(task.durationMs), true);
  assert.equal(typeof task.finishedAt, "string");
  await new Promise((resolve) => setTimeout(resolve, 50));
  const later = manager.getTask(task.id);
  assert.equal(later.durationMs, task.durationMs);
  assert.equal(later.finishedAt, task.finishedAt);
}

test("TaskManager follows the real Python pipeline and preserves visual state", async () => {
  const dataDir = await mkdtemp(path.join(tmpdir(), "subtitle-visualizer-task-"));
  try {
    const manager = new TaskManager({ skillRoot: ROOT, dataDir });
    await manager.init();
    const created = await manager.createTask({ filePath: FIXTURE, targetLanguage: "zh-Hans", batchSize: 2 });
    const ready = await waitFor(() => manager.getTask(created.id), (task) => task.status === "awaiting_translation");

    assert.equal(ready.totalEntries, 2);
    assert.equal(ready.batchCount, 1);
    assert.equal(ready.entries[0]?.sourceText, "Hello there.");
    assert.equal(ready.entries[0]?.startMs, 1000);
    assert.equal(ready.events.at(-1)?.type, "task.ready");

    await manager.startBatch(created.id, 1);
    const responsePath = path.join(dataDir, "response.txt");
    await writeFile(
      responsePath,
      "⟦ID:000001⟧\n你好。\n⟦/ID:000001⟧\n\n⟦ID:000002⟧\n你好吗？\n⟦/ID:000002⟧\n",
      "utf8",
    );
    const validated = await manager.submitResponse(created.id, 1, responsePath, false);
    assert.equal(validated.status, "ready_to_compose");
    assert.equal(validated.completedEntries, 2);
    assert.equal(validated.batches[0]?.durationMs !== undefined, true);
    assert.equal(validated.entries[1]?.translatedText, "你好吗？");

    const outputPath = path.join(dataDir, "result.srt");
    const completed = await manager.compose(created.id, outputPath);
    assert.equal(completed.status, "completed");
    assert.equal(completed.outputFileName, "result.srt");
    assert.equal(completed.durationMs !== undefined, true);
    assert.match(await readFile(outputPath, "utf8"), /00:00:01,000 --> 00:00:02,500/);
    assert.match(await readFile(outputPath, "utf8"), /你好。/);
    assert.deepEqual(
      completed.events.map((event) => event.type),
      ["task.created", "task.preparing", "task.ready", "batch.started", "batch.validating", "batch.validated", "task.composing", "task.completed"],
    );
  } finally {
    await rm(dataDir, { recursive: true, force: true });
  }
});

test("bridge compose keeps collision safety and supports explicit overwrite", async () => {
  const dataDir = await mkdtemp(path.join(tmpdir(), "subtitle-visualizer-overwrite-"));
  const running = await startServer({ rootDir: ROOT, host: "127.0.0.1", port: 0, dataDir });
  try {
    const created = await running.manager.createTask({ filePath: FIXTURE, targetLanguage: "zh-Hans" });
    await waitFor(() => running.manager.getTask(created.id), (task) => task.status === "awaiting_translation");
    await running.manager.startBatch(created.id, 1);
    const responsePath = path.join(dataDir, "response.txt");
    await writeFile(
      responsePath,
      "⟦ID:000001⟧\n你好。\n⟦/ID:000001⟧\n\n⟦ID:000002⟧\n你好吗？\n⟦/ID:000002⟧\n",
      "utf8",
    );
    await running.manager.submitResponse(created.id, 1, responsePath, false);

    const outputPath = path.join(dataDir, "bridge-result.srt");
    const bridgePath = path.join(ROOT, "dist", "src", "agent-bridge.js");
    const bridgeArgs = ["compose", "--url", running.url, "--task", created.id, "--output", outputPath];
    await execFileAsync(process.execPath, [bridgePath, ...bridgeArgs], { cwd: ROOT });

    const reportPath = `${outputPath}.report.json`;
    await writeFile(outputPath, "sentinel output\n", "utf8");
    await writeFile(reportPath, "sentinel report\n", "utf8");

    let collisionError: { stdout?: string; stderr?: string } | undefined;
    try {
      await execFileAsync(process.execPath, [bridgePath, ...bridgeArgs], { cwd: ROOT });
    } catch (error) {
      collisionError = error as { stdout?: string; stderr?: string };
    }
    assert.ok(collisionError);
    assert.match(`${collisionError.stdout ?? ""}\n${collisionError.stderr ?? ""}`, /Output already exists/);
    assert.equal(await readFile(outputPath, "utf8"), "sentinel output\n");
    assert.equal(await readFile(reportPath, "utf8"), "sentinel report\n");

    await execFileAsync(process.execPath, [bridgePath, ...bridgeArgs, "--overwrite"], { cwd: ROOT });
    assert.match(await readFile(outputPath, "utf8"), /你好。/);
    assert.equal(JSON.parse(await readFile(reportPath, "utf8")).status, "composed");
  } finally {
    await new Promise<void>((resolve) => running.server.close(() => resolve()));
    await rm(dataDir, { recursive: true, force: true });
  }
});

test("terminal task durations stop after cancellation and failure", async () => {
  const dataDir = await mkdtemp(path.join(tmpdir(), "subtitle-visualizer-duration-"));
  try {
    const manager = new TaskManager({ skillRoot: ROOT, dataDir });
    await manager.init();

    const invalidPath = path.join(dataDir, "invalid-marker.srt");
    await writeFile(
      invalidPath,
      "1\n00:00:00,000 --> 00:00:01,000\n⟦ID:000001⟧\n",
      "utf8",
    );
    const prepareFailure = await manager.createTask({ filePath: invalidPath, targetLanguage: "zh-Hans" });
    const failedDuringPrepare = await waitFor(
      () => manager.getTask(prepareFailure.id),
      (task) => task.status === "failed",
    );
    await assertFrozenDuration(manager, failedDuringPrepare);

    const cancellation = await manager.createTask({ filePath: FIXTURE, targetLanguage: "zh-Hans" });
    await waitFor(() => manager.getTask(cancellation.id), (task) => task.status === "awaiting_translation");
    await manager.startBatch(cancellation.id, 1);
    const cancelled = await manager.cancel(cancellation.id);
    assert.equal(cancelled.status, "cancelled");
    await assertFrozenDuration(manager, cancelled);

    const persistedCancellation = JSON.parse(
      await readFile(path.join(dataDir, cancellation.id, "task.json"), "utf8"),
    ) as Record<string, unknown>;
    delete persistedCancellation.durationMs;
    delete persistedCancellation.finishedAt;
    await writeFile(
      path.join(dataDir, cancellation.id, "task.json"),
      `${JSON.stringify(persistedCancellation, null, 2)}\n`,
      "utf8",
    );
    const reloadedManager = new TaskManager({ skillRoot: ROOT, dataDir });
    await reloadedManager.init();
    const legacyCancelled = reloadedManager.getTask(cancellation.id);
    assert.equal(Number.isFinite(legacyCancelled.durationMs), true);
    await new Promise((resolve) => setTimeout(resolve, 50));
    assert.equal(reloadedManager.getTask(cancellation.id).durationMs, legacyCancelled.durationMs);

    const composeFailure = await manager.createTask({ filePath: FIXTURE, targetLanguage: "zh-Hans" });
    await waitFor(() => manager.getTask(composeFailure.id), (task) => task.status === "awaiting_translation");
    await manager.startBatch(composeFailure.id, 1);
    const responsePath = path.join(dataDir, "duration-response.txt");
    await writeFile(
      responsePath,
      "⟦ID:000001⟧\n你好。\n⟦/ID:000001⟧\n\n⟦ID:000002⟧\n你好吗？\n⟦/ID:000002⟧\n",
      "utf8",
    );
    await manager.submitResponse(composeFailure.id, 1, responsePath, false);
    await assert.rejects(() => manager.compose(composeFailure.id, dataDir));
    const failedDuringCompose = manager.getTask(composeFailure.id);
    assert.equal(failedDuringCompose.status, "failed");
    await assertFrozenDuration(manager, failedDuringCompose);
  } finally {
    await rm(dataDir, { recursive: true, force: true });
  }
});

test("local server exposes health and persisted task summaries", async () => {
  const dataDir = await mkdtemp(path.join(tmpdir(), "subtitle-visualizer-server-"));
  const running = await startServer({ rootDir: ROOT, host: "127.0.0.1", port: 0, dataDir });
  try {
    const healthResponse = await fetch(`${running.url}/api/health`);
    assert.equal(healthResponse.status, 200);
    const health = (await healthResponse.json()) as { status: string; service: string; version: string };
    assert.equal(health.status, "ok");
    assert.equal(health.service, "subtitle-visualizer");
    assert.equal(health.version, PACKAGE_VERSION);

    const iconsResponse = await fetch(`${running.url}/icons.js`);
    assert.equal(iconsResponse.status, 200);
    assert.equal(iconsResponse.headers.get("content-type"), "text/javascript; charset=utf-8");
    assert.match(await iconsResponse.text(), /subtitleVisualizerNativeIconRenderer/);

    const faviconResponse = await fetch(`${running.url}/favicon.ico`);
    assert.equal(faviconResponse.status, 200);
    assert.equal(faviconResponse.headers.get("content-type"), "image/png");
    assert.equal((await faviconResponse.arrayBuffer()).byteLength > 0, true);

    const brandResponse = await fetch(`${running.url}/assets/icon-large.png`);
    assert.equal(brandResponse.status, 200);
    assert.equal(brandResponse.headers.get("content-type"), "image/png");

    const initialAgentResponse = await fetch(running.url + "/api/agent");
    assert.equal(initialAgentResponse.status, 200);
    const initialAgent = (await initialAgentResponse.json()) as { agent: { agent: string; model: string; modelVersion?: string; modelSeries?: string; reasoningStrength?: string } };
    assert.equal(initialAgent.agent.agent, "等待 Agent 自报");
    assert.equal(initialAgent.agent.model, "等待模型自报");

    const reportAgentResponse = await fetch(running.url + "/api/agent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ agent: "Codex", model: "GPT", modelVersion: "5.6", modelSeries: "Sol", reasoningStrength: "high" }),
    });
    assert.equal(reportAgentResponse.status, 200);
    const reportedAgent = (await reportAgentResponse.json()) as { agent: { agent: string; model: string; modelVersion?: string; modelSeries?: string; reasoningStrength?: string; reportedAt?: string } };
    assert.equal(reportedAgent.agent.agent, "Codex");
    assert.equal(reportedAgent.agent.model, "GPT");
    assert.equal(reportedAgent.agent.modelVersion, "5.6");
    assert.equal(reportedAgent.agent.modelSeries, "Sol");
    assert.equal(reportedAgent.agent.reasoningStrength, "high");
    assert.equal(typeof reportedAgent.agent.reportedAt, "string");

    const createResponse = await fetch(`${running.url}/api/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        fileName: "browser-upload.srt",
        contentBase64: (await readFile(FIXTURE)).toString("base64"),
        targetLanguage: "zh-Hans",
      }),
    });
    assert.equal(createResponse.status, 202);
    const created = (await createResponse.json()) as { task: { id: string; agent?: string; model?: string; modelVersion?: string; modelSeries?: string; reasoningStrength?: string } };
    assert.equal(created.task.agent, "Codex");
    assert.equal(created.task.model, "GPT");
    assert.equal(created.task.modelVersion, "5.6");
    assert.equal(created.task.modelSeries, "Sol");
    assert.equal(created.task.reasoningStrength, "high");

    const legacyReportResponse = await fetch(running.url + "/api/agent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ agent: "Codex", model: "Legacy-Model" }),
    });
    assert.equal(legacyReportResponse.status, 200);
    const legacyAgent = (await legacyReportResponse.json()) as { agent: { model: string; modelVersion?: string; modelSeries?: string; reasoningStrength?: string } };
    assert.equal(legacyAgent.agent.model, "Legacy-Model");
    assert.equal(legacyAgent.agent.modelVersion, undefined);
    assert.equal(legacyAgent.agent.modelSeries, undefined);
    assert.equal(legacyAgent.agent.reasoningStrength, undefined);
    const listResponse = await fetch(`${running.url}/api/tasks`);
    const list = (await listResponse.json()) as { tasks: Array<{ id: string }> };
    assert.equal(list.tasks.some((task) => task.id === created.task.id), true);
    await waitForServerTask(running.url, created.task.id);
  } finally {
    await new Promise<void>((resolve) => running.server.close(() => resolve()));
    await rm(dataDir, { recursive: true, force: true });
  }
});

test("visualizer web surface is display-only and leaves task input to the Agent", async () => {
  const index = await readFile(path.join(ROOT, "web", "index.html"), "utf8");
  const app = await readFile(path.join(ROOT, "web", "app.ts"), "utf8");
  const icons = await readFile(path.join(ROOT, "web", "icons.ts"), "utf8");
  const styles = await readFile(path.join(ROOT, "web", "styles.css"), "utf8");
  assert.match(index, /翻译会话由/);
  assert.match(index, /id="agent-session-agent"/);
  assert.match(index, /页面只展示任务状态、过程记录和翻译结果。/);
  assert.doesNotMatch(index, /connection-pill/);
  assert.match(index, /id="live-dot"[^>]+data-status="checking"/);
  assert.match(index, /class="section-kicker">[\s\S]*class="live-dot"[\s\S]*class="agent-session-lines"/);
  assert.doesNotMatch(index, /<div class="topbar-actions">(?:(?!<\/div>)[\s\S])*class="live-dot"/);
  assert.match(index, /id="mobile-menu-toggle"[^>]+aria-controls="task-rail"/);
  assert.match(index, /id="mobile-menu-backdrop"/);
  assert.doesNotMatch(index, /当前页面只展示任务状态、过程记录和翻译结果。/);
  assert.doesNotMatch(index, /SKILL 版本/);
  assert.match(index, /program-repo-link[\s\S]*<strong id="program-version">/);
  assert.match(index, /id="detail-model"/);
  assert.match(index, /id="detail-agent"/);
  assert.match(index, /id="detail-stat-model"/);
  assert.match(index, /class="detail-stat detail-stat-model" aria-label="Agent 与模型"/);
  assert.match(index, /class="detail-meta-row"/);
  assert.match(index, /id="detail-actions"/);
  assert.match(index, /TRANSLATION STUDIO/);
  assert.doesNotMatch(index, /LOCAL TRANSLATION STUDIO/);
  assert.doesNotMatch(app, /data-task-model/);
  assert.match(app, /languageLabel\(task\.targetLanguage\)/);
  assert.match(app, /taskModelLabel\(task\)/);
  assert.match(app, /taskAgentLabel\(task\)/);
  assert.doesNotMatch(app, /metaText = [^\n]*taskModelLabel\(task\)/);
  assert.match(app, /detail-agent/);
  assert.match(app, /taskModelParts/);
  assert.match(app, /detailActions\.hidden/);
  assert.match(app, /dataset\.hasStage/);
  assert.doesNotMatch(app, /flow-event-scope|data-event-scope|eventScope/);
  assert.doesNotMatch(app, /模型 ·/);
  assert.match(app, /if \(parts\.length === 0\) return "待上报";/);
  assert.doesNotMatch(index, /<span>模型<\/span>/);
  assert.match(app, /modelVersion/);
  assert.match(app, /modelSeries/);
  assert.match(app, /reasoningStrength/);
  assert.match(app, /setConnectionStatus\("offline"\)/);
  assert.match(app, /setConnectionStatus\("online"\)/);
  assert.match(app, /function setMobileMenu\(open: boolean\)/);
  assert.match(app, /aria-expanded/);
  assert.doesNotMatch(index, /agent-profile-facts|agent-identity|agent-model/);
  assert.match(index, /id="program-version"/);
  assert.match(index, /class="program-repo-link" href="https:\/\/github\.com\/Lumen01\/agent-subtitle-translator"/);
  assert.match(index, /class="program-repo-link"[^>]*>Agent Subtitle Translator<\/a>/);
  assert.match(styles, /\.agent-program-meta a \{[\s\S]*color: var\(--ink-soft\);/);
  assert.doesNotMatch(styles, /\.connection-pill/);
  assert.match(styles, /\.live-dot\[data-status="offline"\] \{[\s\S]*background: var\(--danger\);/);
  assert.match(styles, /\.app-shell\.mobile-menu-open \.task-rail \{[\s\S]*position: fixed;/);
  assert.match(styles, /\.app-shell\.mobile-menu-open \.task-list \{[\s\S]*overflow-y: auto;/);
  assert.match(styles, /\.detail-stat-separator \{[\s\S]*color: var\(--ink-faint\);/);
  assert.match(styles, /\.detail-stat-model-value \{[\s\S]*flex: 1 1 auto;/);
  assert.match(styles, /\.detail-header \{[\s\S]*padding: 0 0 24px;/);
  assert.match(index, /rel="icon"[^>]+href="\/assets\/icon-small\.png"/);
  assert.match(index, /class="brand-mark"[^>]+src="\/assets\/icon-large\.png"/);
  assert.match(index, /data-sf-symbol="moon\.fill"/);
  assert.match(index, /data-sf-symbol="captions\.bubble\.fill"/);
  assert.match(index, /data-sf-symbol="square\.stack\.3d\.up\.fill"/);
  assert.match(index, /data-sf-symbol="clock\.fill"/);
  assert.match(index, /data-sf-symbol="cpu\.fill"/);
  assert.match(icons, /subtitleVisualizerNativeIconRenderer/);
  assert.match(icons, /data-fallback-symbol/);
  assert.match(icons, /captions\.bubble\.fill/);
  assert.match(icons, /square\.stack\.3d\.up\.fill/);
  assert.match(icons, /clock\.fill/);
  assert.match(icons, /cpu\.fill/);
  assert.match(app, /iconMarkup\("chevron\.down"\)/);
  assert.doesNotMatch(app, /data-batch-status-label/);
  assert.match(app, /data-batch-summary-detail/);
  assert.match(app, /data-batch-state/);
  assert.match(index, /data-sf-symbol="arrow\.down\.circle\.fill"/);
  assert.match(icons, /arrow\.down\.circle\.fill/);
  assert.match(icons, /download-circle/);
  assert.match(styles, /grid-template-columns: minmax\(230px, 0\.38fr\) minmax\(0, 0\.62fr\)/);
  assert.match(styles, /\.task-card-meta \{[\s\S]*grid-column: 2 \/ -1;/);
  assert.match(styles, /\.task-card-copy \{[\s\S]*grid-column: 2;/);
  assert.match(styles, /\.task-card-time \{[\s\S]*grid-column: 3;/);
  assert.match(styles, /\.task-status-mark \{[\s\S]*position: absolute;[\s\S]*top: 50%;[\s\S]*transform: translateY\(-50%\);/);
  assert.doesNotMatch(styles, /\.task-status-mark \{[\s\S]*top: 5px;/);
  assert.match(styles, /\.topbar \{[\s\S]*max-width: none;[\s\S]*margin: 0;/);
  assert.match(styles, /\.workspace \{[\s\S]*width: 100%;[\s\S]*max-width: none;[\s\S]*margin: 0;/);
  assert.match(styles, /\.detail-pane > #task-detail \{[\s\S]*max-width: 1440px;[\s\S]*margin-inline: auto;/);
  assert.match(styles, /\[data-theme="dark"\] \.task-card:not\(\.is-selected\) \{[\s\S]*background: var\(--surface-strong\);/);
  assert.match(styles, /\.download-button \{[\s\S]*padding: 8px 11px;/);
  assert.doesNotMatch(styles, /\.download-button \{\n  padding: 10px 13px;/);
  assert.match(styles, /\.flow-stage,\n\.flow-batches \{[\s\S]*overflow: auto;/);
  assert.match(styles, /\.flow-event-marker\[data-tone="active"\] \{ background: var\(--info\)/);
  assert.match(styles, /\.flow-list \{[\s\S]*display: block;[\s\S]*max-height: none;/);
  assert.match(styles, /@media \(max-width: 760px\) \{[\s\S]*\.detail-pane \{[\s\S]*padding-inline: 14px;/);
  assert.doesNotMatch(index, /type="file"/);
  assert.doesNotMatch(index, /id="target-language"/);
  assert.doesNotMatch(index, /id="create-task"/);
  assert.doesNotMatch(index, /id="cancel-task"/);
  assert.doesNotMatch(app, /contentBase64|file\.arrayBuffer|createTask\(/);
});

test("visual state records a failed validation, retry, and ASS degradation", async () => {
  const dataDir = await mkdtemp(path.join(tmpdir(), "subtitle-visualizer-retry-"));
  try {
    const manager = new TaskManager({ skillRoot: ROOT, dataDir });
    await manager.init();
    const created = await manager.createTask({ filePath: KARAOKE_FIXTURE, targetLanguage: "zh-Hans" });
    const ready = await waitFor(() => manager.getTask(created.id), (task) => task.status === "awaiting_translation");
    assert.equal(ready.warningCount, 1);
    assert.equal(ready.entries[0]?.degradation, "karaoke");

    await manager.startBatch(created.id, 1);
    const responsePath = path.join(dataDir, "karaoke-response.txt");
    await writeFile(responsePath, "⟦ID:000001⟧\n错误的结构\n⟦/ID:000001⟧\n", "utf8");
    await assert.rejects(() => manager.submitResponse(created.id, 1, responsePath, false));
    const failed = manager.getTask(created.id);
    assert.equal(failed.status, "retrying");
    assert.equal(failed.batches[0]?.status, "failed");
    assert.equal(failed.events.at(-1)?.type, "batch.failed");

    await manager.retryBatch(created.id, 1);
    await writeFile(responsePath, "⟦ID:000001⟧\n现在⟦BR1⟧卡拉 OK\n⟦/ID:000001⟧\n", "utf8");
    const validated = await manager.submitResponse(created.id, 1, responsePath, false);
    assert.equal(validated.status, "ready_to_compose");
    assert.equal(validated.batches[0]?.retryCount, 1);
    assert.equal(validated.warningCount, 1);

    const outputPath = path.join(dataDir, "karaoke.zh-Hans.ass");
    const completed = await manager.compose(created.id, outputPath);
    assert.equal(completed.status, "completed");
    const output = await readFile(outputPath, "utf8");
    assert.match(output, /现在\\N卡拉 OK/);
    assert.doesNotMatch(output, /\\(?:k|K|kf|ko)\d/);
  } finally {
    await rm(dataDir, { recursive: true, force: true });
  }
});
