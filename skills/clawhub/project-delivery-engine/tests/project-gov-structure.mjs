import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const skillRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const script = path.join(skillRoot, "scripts", "project-gov.mjs");
const sandbox = fs.mkdtempSync(path.join(os.tmpdir(), "project-gov-structure-"));
let sequence = 0;

function write(root, rel, content) {
  const abs = path.join(root, rel);
  fs.mkdirSync(path.dirname(abs), { recursive: true });
  fs.writeFileSync(abs, content, "utf8");
}

function createProject(name) {
  sequence += 1;
  const root = path.join(sandbox, `${String(sequence).padStart(2, "0")}-${name}`);
  write(root, "AGENTS.md", "# AGENTS.md\n");
  write(root, "PROJECT_START_HERE.md", "# PROJECT_START_HERE.md\n\n## 项目路径\n\n- 当前夹具。\n\n## 启动入口\n\n1. 读取五件套。\n");
  write(root, "STATUS.md", "# STATUS.md\n\n## 当前状态\n\n| 项目 | 状态 | 依据 |\n| --- | --- | --- |\n\n## 验证\n\n| 验证项 | 结果 | 层级 |\n| --- | --- | --- |\n| 基线 | 通过 | 主线 |\n\n## 风险\n\n- 无\n\n## 关键引用\n\n- 无\n");
  write(root, "TODO.md", "# TODO.md\n\n## 下一步\n\n| 优先级 | 事项 | 完成条件 |\n| --- | --- | --- |\n\n## 待确认\n\n| 事项 | 影响 |\n| --- | --- |\n");
  write(root, "HANDOFF.md", "# HANDOFF.md\n\n## 语义检查点\n\n- 最后语义检查点：2026-07-28 02:00 +08:00\n- 检查点后变化：已核对\n\n## 接手顺序\n\n1. 读取五件套。\n\n## 已证伪路线\n\n| 路线/假设 | 证伪证据（一行） | 关闭日期 | 复开条件 |\n| --- | --- | --- | --- |\n\n## 关键索引\n\n| 类型 | 路径 | 用途 |\n| --- | --- | --- |\n| 状态 | `STATUS.md` | 当前状态 |\n\n## 未决上下文\n\n- 无\n");
  write(root, "历史记录/00-历史总目录.md", "# 历史总目录\n\n## 阅读说明\n\n| 如果要做 | 先读 |\n| --- | --- |\n\n## 最近历史索引\n\n| history-id | 日期 | 标题 | 路径 | 状态 | 自定义列 |\n| --- | --- | --- | --- | --- | --- |\n");
  write(root, "证据库/总索引/证据总目录.md", "# 证据总目录\n\n| evidence-id | run_id | task_id | 来源 | 摘要 | 路径 | 采纳状态 |\n| --- | --- | --- | --- | --- | --- | --- |\n");
  write(root, "项目物料/INDEX.md", "# 项目物料索引\n\n| material-id | 路径 | hash | 来源 | 用途 | 状态 |\n| --- | --- | --- | --- | --- | --- |\n");
  return root;
}

function run(command, root, extra = []) {
  const result = spawnSync(process.execPath, [script, command, "--root", root, ...extra, "--json"], {
    encoding: "utf8",
    maxBuffer: 16 * 1024 * 1024,
  });
  return {
    ...result,
    json: result.stdout.trim() ? JSON.parse(result.stdout) : JSON.parse(result.stderr),
  };
}

function mutate(root, rel, transform) {
  const abs = path.join(root, rel);
  fs.writeFileSync(abs, transform(fs.readFileSync(abs, "utf8")), "utf8");
}

function expectStructureError(result, prefix) {
  assert.notEqual(result.status, 0, `expected ${prefix}`);
  assert.ok(result.json.errors.some((error) => error.startsWith(prefix)), result.stdout);
}

function hashFile(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}

try {
  const valid = createProject("valid");
  const validResult = run("validate", valid);
  assert.equal(validResult.status, 0, validResult.stderr);
  assert.equal(validResult.json.ok, true);
  assert.equal(validResult.json.report.structure.ok, true);
  assert.ok(!validResult.json.warnings.includes("five_piece_remaining_below_2kib"));

  mutate(valid, "STATUS.md", (text) => `${text}\n\`\`\`text\n## 验证\n| 假 | 表 |\n| --- | --- |\n\`\`\`\n<!-- ## 验证 -->\n`);
  assert.equal(run("validate", valid).status, 0, "code/comment content must not create duplicate structure");

  const invalidLayer = createProject("invalid-layer");
  mutate(invalidLayer, "STATUS.md", (text) => text.replace("| 基线 | 通过 | 主线 |", "| 基线 | 通过 | 辅助 |"));
  expectStructureError(run("validate", invalidLayer), "structure_value_invalid:STATUS.md:验证");

  const missingTodo = createProject("missing-todo-section");
  mutate(missingTodo, "TODO.md", (text) => text.replace(/## 待确认[\s\S]*$/, ""));
  expectStructureError(run("validate", missingTodo), "structure_section_missing:TODO.md:待确认");
  const todoPath = path.join(missingTodo, "TODO.md");
  const beforeMigrationCheck = hashFile(todoPath);
  const migration = run("migrate-check", missingTodo);
  assert.notEqual(migration.status, 0);
  assert.equal(migration.json.automatic_rewrite, false);
  assert.ok(migration.json.migration_items.some((item) => item.code.startsWith("structure_section_missing:TODO.md:待确认")));
  assert.equal(hashFile(todoPath), beforeMigrationCheck, "migrate-check must be read-only");

  const optionalRoutes = createProject("optional-routes");
  mutate(optionalRoutes, "HANDOFF.md", (text) => text.replace(/## 已证伪路线[\s\S]*?(?=## 关键索引)/, ""));
  const optionalResult = run("validate", optionalRoutes);
  assert.equal(optionalResult.status, 0, optionalResult.stderr);
  assert.ok(optionalResult.json.warnings.includes("missing_handoff_falsified_routes"));

  const malformedRoutes = createProject("malformed-routes");
  mutate(malformedRoutes, "HANDOFF.md", (text) => text
    .replace("| 路线/假设 | 证伪证据（一行） | 关闭日期 | 复开条件 |", "| 路线/假设 | 证伪证据（一行） | 复开条件 |")
    .replace("| --- | --- | --- | --- |", "| --- | --- | --- |"));
  expectStructureError(run("validate", malformedRoutes), "structure_columns_missing:HANDOFF.md:已证伪路线");

  const brokenTable = createProject("broken-table");
  mutate(brokenTable, "HANDOFF.md", (text) => text.replace("| 状态 | `STATUS.md` | 当前状态 |", "\n| 状态 | `STATUS.md` | 当前状态 |"));
  expectStructureError(run("validate", brokenTable), "structure_table_discontinuous:HANDOFF.md:关键索引");

  const oldIndex = createProject("old-index");
  mutate(oldIndex, "历史记录/00-历史总目录.md", (text) => text
    .replace("| history-id | 日期 | 标题 | 路径 | 状态 | 自定义列 |", "| history-id | 类型 | 标题 | 位置 | 说明 |")
    .replace("| --- | --- | --- | --- | --- | --- |", "| --- | --- | --- | --- | --- |"));
  expectStructureError(run("validate", oldIndex), "structure_columns_missing:历史记录/00-历史总目录.md:root");

  const lowSpace = createProject("low-space");
  const beforePadding = run("inspect", lowSpace).json.five_piece.total_bytes;
  const targetBytes = 45 * 1024 - 1024;
  fs.appendFileSync(path.join(lowSpace, "AGENTS.md"), "x".repeat(targetBytes - beforePadding), "utf8");
  const lowSpaceResult = run("validate", lowSpace);
  assert.equal(lowSpaceResult.status, 0, lowSpaceResult.stderr);
  assert.ok(lowSpaceResult.json.warnings.includes("five_piece_remaining_below_2kib"));
  assert.equal(lowSpaceResult.json.report.five_piece.remaining_bytes, 1024);

  const startup = run("startup", createProject("startup"));
  assert.equal(startup.status, 0, startup.stderr);
  assert.match(startup.json.startup, /项目交付引擎判断/);
  assert.doesNotMatch(startup.json.startup, /项目总调度/);
  assert.doesNotMatch(fs.readFileSync(path.join(skillRoot, "SKILL.md"), "utf8"), /项目总调度/);

  console.log("project-gov structure regression tests: PASS");
} finally {
  fs.rmSync(sandbox, { recursive: true, force: true });
}
