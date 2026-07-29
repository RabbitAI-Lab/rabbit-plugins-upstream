import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const skillRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const script = path.join(skillRoot, "scripts", "project-gov.mjs");
const expectedSkillVersion = "0.3.5";
const sandbox = fs.mkdtempSync(path.join(os.tmpdir(), "project-gov-v027-"));
let sequence = 0;

function write(root, rel, content) {
  const abs = path.join(root, rel);
  fs.mkdirSync(path.dirname(abs), { recursive: true });
  fs.writeFileSync(abs, content, "utf8");
  return abs;
}

function createProject(name) {
  sequence += 1;
  const root = path.join(sandbox, `${String(sequence).padStart(2, "0")}-${name}`);
  write(root, "AGENTS.md", "# AGENTS.md\n");
  write(
    root,
    "PROJECT_START_HERE.md",
    "# PROJECT_START_HERE.md\n\n## 项目路径\n\n- 当前项目根目录。\n\n## 启动入口\n\n1. 读取五件套。\n",
  );
  write(
    root,
    "STATUS.md",
    "# STATUS.md\n\n## 当前状态\n\n| 项目 | 状态 | 依据 |\n| --- | --- | --- |\n| 回归 | 正常 | 本地夹具 |\n\n## 验证\n\n| 验证项 | 结果 | 层级 |\n| --- | --- | --- |\n| 基线 | 通过 | 主线 |\n\n## 风险\n\n- 无\n\n## 关键引用\n\n- 无\n",
  );
  write(
    root,
    "TODO.md",
    "# TODO.md\n\n## 下一步\n\n| 优先级 | 事项 | 完成条件 |\n| --- | --- | --- |\n| P1 | 回归 | 通过 |\n\n## 待确认\n\n| 事项 | 影响 |\n| --- | --- |\n| 无 | 无 |\n",
  );
  write(
    root,
    "HANDOFF.md",
    "# HANDOFF.md\n\n## 语义检查点\n\n- 最后语义检查点：2026-07-28 08:00 +08:00\n- 检查点后变化：已核对\n\n## 接手顺序\n\n1. 读取五件套。\n\n## 已证伪路线\n\n| 路线/假设 | 证伪证据（一行） | 关闭日期 | 复开条件 |\n| --- | --- | --- | --- |\n\n## 关键索引\n\n| 类型 | 路径 | 用途 |\n| --- | --- | --- |\n| 状态 | `STATUS.md` | 当前状态 |\n\n## 未决上下文\n\n- 无\n",
  );
  write(
    root,
    "历史记录/00-历史总目录.md",
    "# 历史总目录\n\n| history-id | 日期 | 标题 | 路径 | 状态 |\n| --- | --- | --- | --- | --- |\n",
  );
  write(
    root,
    "证据库/总索引/证据总目录.md",
    "# 证据总目录\n\n| evidence-id | run_id | task_id | 来源 | 摘要 | 路径 | 采纳状态 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
  );
  write(
    root,
    "项目物料/INDEX.md",
    "# 项目物料索引\n\n| material-id | 路径 | hash | 来源 | 用途 | 状态 |\n| --- | --- | --- | --- | --- | --- |\n",
  );
  return root;
}

function run(command, root, extra = [], maxBuffer = 8 * 1024 * 1024) {
  const result = spawnSync(
    process.execPath,
    [script, command, "--root", root, ...extra, "--json"],
    { encoding: "utf8", maxBuffer },
  );
  const raw = result.stdout.trim() || result.stderr.trim();
  let json = null;
  try {
    json = raw ? JSON.parse(raw) : null;
  } catch {
    // Some output-size regressions are asserted before JSON details are needed.
  }
  return { ...result, json };
}

function propose(root, name, actions) {
  const operation = write(root, `${name}.operation.json`, `${JSON.stringify({
    schema_version: 1,
    plan_id: name,
    actions,
  }, null, 2)}\n`);
  const out = path.join(root, ".project-gov", "plans", `${name}.json`);
  return {
    ...run("propose", root, ["--plan", operation, "--out", out]),
    out,
  };
}

function apply(compiledPlan) {
  const result = spawnSync(process.execPath, [script, "apply", "--plan", compiledPlan, "--json"], {
    encoding: "utf8",
    maxBuffer: 8 * 1024 * 1024,
  });
  const raw = result.stdout.trim() || result.stderr.trim();
  return { ...result, json: JSON.parse(raw) };
}

function mutate(root, rel, transform) {
  const abs = path.join(root, rel);
  fs.writeFileSync(abs, transform(fs.readFileSync(abs, "utf8")), "utf8");
}

function age(abs, days = 40) {
  const old = new Date(Date.now() - days * 24 * 60 * 60 * 1000);
  fs.utimesSync(abs, old, old);
}

function rels(items) {
  return (items || []).map((item) => typeof item === "string" ? item : item.rel);
}

function assertRejected(result, message) {
  assert.notEqual(result.status, 0, message);
  assert.equal(result.json?.ok, false, result.stdout || result.stderr);
}

function assertCrLfOnly(text, label) {
  assert.match(text, /\r\n/, `${label} lost CRLF`);
  assert.equal(/(^|[^\r])\n/.test(text), false, `${label} introduced bare LF`);
}

function physicalCount(layout, nestedKey, flatKey) {
  const nested = layout?.[nestedKey];
  if (typeof nested === "number") return nested;
  if (typeof nested?.count === "number") return nested.count;
  return layout?.[flatKey];
}

try {
  // 1. A junction into a non-governance part of the same project is still an escape.
  {
    const root = createProject("junction-boundary");
    const ordinary = path.join(root, "ordinary-output");
    fs.mkdirSync(ordinary);
    fs.symlinkSync(ordinary, path.join(root, "历史记录", "linked-output"), "junction");
    const escaped = propose(root, "junction-escape", [
      { kind: "write_file", path: "历史记录/linked-output/probe.md", content: "# probe\n", overwrite: false },
    ]);
    assertRejected(escaped, "same-project junction must be rejected during propose");
    assert.equal(fs.existsSync(escaped.out), false);

    const normal = propose(root, "normal-governance-child", [
      { kind: "write_file", path: "历史记录/正常目录/probe.md", content: "# probe\n", overwrite: false },
    ]);
    assert.equal(normal.status, 0, normal.stderr);
    assert.equal(normal.json.ok, true);
  }

  // 2. Cache inventory is read-only and never deletes project data.
  {
    const root = createProject("read-only-cache-inventory");
    const compiled = propose(root, "compiled-plan", []);
    assert.equal(compiled.status, 0, compiled.stderr);
    age(compiled.out);
    const backup = path.join(root, ".project-gov", "backups", "legacy-backup");
    fs.mkdirSync(backup, { recursive: true });
    write(backup, "probe.txt", "old\n");
    age(path.join(backup, "probe.txt"));
    age(backup);
    const preview = run("prune", root, ["--older-than-days", "30"]);
    assert.equal(preview.status, 0, preview.stderr);
    assert.equal(preview.json.mode, "read_only_inventory");
    assert.equal(preview.json.automatic_delete, false);
    assert.ok(rels(preview.json.items).some((rel) => rel.endsWith("compiled-plan.json")), preview.stdout);
    assert.ok(rels(preview.json.items).some((rel) => rel.endsWith("legacy-backup")), preview.stdout);
    const applied = run("prune", root, ["--older-than-days", "30", "--apply"]);
    assertRejected(applied, "cache inventory must reject delete mode");
    assert.equal(fs.existsSync(compiled.out), true);
    assert.equal(fs.existsSync(backup), true);
  }

  // 3. Table contracts use exact aliases and reject ambiguity or duplicate IDs.
  {
    const aliases = createProject("table-exact-aliases");
    mutate(aliases, "历史记录/00-历史总目录.md", (text) => text
      .replace("history-id", "历史编号")
      .replace("路径", "原件路径"));
    mutate(aliases, "证据库/总索引/证据总目录.md", (text) => text
      .replace("evidence-id", "证据编号")
      .replace("run_id", "执行批次")
      .replace("task_id", "任务编号")
      .replace("路径", "原件路径"));
    mutate(aliases, "项目物料/INDEX.md", (text) => text
      .replace("material-id", "物料编号")
      .replace("路径", "原件路径")
      .replace("hash", "哈希"));
    assert.equal(run("validate", aliases).status, 0, "supported exact aliases must pass");

    const fuzzy = createProject("table-fuzzy-alias");
    mutate(fuzzy, "历史记录/00-历史总目录.md", (text) => text.replace("history-id", "历史编号值"));
    assertRejected(run("validate", fuzzy), "fuzzy alias must not pass");

    const duplicateColumn = createProject("table-duplicate-column");
    mutate(duplicateColumn, "STATUS.md", (text) => text
      .replace("| 项目 | 状态 | 依据 |", "| 项目 | 状态 | 状态 | 依据 |")
      .replace("| --- | --- | --- |", "| --- | --- | --- | --- |"));
    assertRejected(run("validate", duplicateColumn), "duplicate required column must fail");

    const duplicateId = createProject("table-duplicate-index-id");
    mutate(duplicateId, "历史记录/00-历史总目录.md", (text) => `${text}| M-20260728-001 | 2026-07-28 | A | a.md | active |\n| M-20260728-001 | 2026-07-28 | B | b.md | active |\n`);
    assertRejected(run("validate", duplicateId), "duplicate index ID must fail");

    const secondCandidate = createProject("table-second-contract-candidate");
    mutate(secondCandidate, "STATUS.md", (text) => text.replace(
      "| 回归 | 正常 | 本地夹具 |",
      "| 回归 | 正常 | 本地夹具 |\n\n说明。\n\n| 项目 | 状态 | 依据 |\n| --- | --- | --- |\n| 重复 | 正常 | 不允许 |",
    ));
    assertRejected(run("validate", secondCandidate), "second contract-candidate table must fail");

    const prelude = createProject("table-non-contract-prelude");
    mutate(prelude, "STATUS.md", (text) => text.replace(
      "## 当前状态\n\n| 项目 |",
      "## 当前状态\n\n| 说明 | 值 |\n| --- | --- |\n| 范围 | 回归 |\n\n| 项目 |",
    ));
    assert.equal(run("validate", prelude).status, 0, "non-contract explanatory table must not be mistaken for contract");
  }

  // 4. A truncated 5,010-file scan can never claim migration is up to date.
  {
    const root = createProject("markdown-scan-limit");
    for (let index = 0; index < 5010; index += 1) {
      write(root, `bulk/${String(index).padStart(4, "0")}.md`, "\n");
    }
    const migration = run("migrate-check", root);
    assert.ok(migration.status !== 0 || migration.json?.indeterminate === true, migration.stdout);
    assert.notEqual(migration.json?.up_to_date, true, migration.stdout);
  }

  // 5. IDs hidden in comments or fenced code cannot resolve a live reference.
  {
    const root = createProject("hidden-id-reference");
    mutate(root, "STATUS.md", (text) => text.replace("- 无\n", "- EV-20260728-001\n- EV-20260728-002\n"));
    mutate(root, "证据库/总索引/证据总目录.md", (text) => `${text}\n<!-- EV-20260728-001 -->\n\n\`\`\`text\nEV-20260728-002\n\`\`\`\n`);
    const result = run("validate", root);
    assertRejected(result, "comment/fence IDs must not satisfy references");
    const unresolved = result.json.report.references.unresolved.map((item) => item.id);
    assert.ok(unresolved.includes("EV-20260728-001"), result.stdout);
    assert.ok(unresolved.includes("EV-20260728-002"), result.stdout);
  }

  // 6. Every text-edit action preserves CRLF, including the existing block action.
  for (const test of [
    {
      name: "crlf-append",
      action: { kind: "append_after", path: "STATUS.md", after: "# STATUS.md", match: "exact", content: "\n说明：追加。" },
    },
    {
      name: "crlf-line-replace",
      action: { kind: "replace_line_contains", path: "STATUS.md", contains: "## 风险", replacement: "## 风险" },
    },
    {
      name: "crlf-block-replace",
      action: { kind: "replace_block_exact", path: "STATUS.md", old_block: "- 无\n\n## 关键引用", replacement: "- 风险已核对\n\n## 关键引用" },
    },
  ]) {
    const root = createProject(test.name);
    const target = path.join(root, "STATUS.md");
    fs.writeFileSync(target, fs.readFileSync(target, "utf8").replace(/\n/g, "\r\n"), "utf8");
    const prepared = propose(root, test.name, [test.action]);
    assert.equal(prepared.status, 0, `${prepared.stdout}\n${prepared.stderr}`);
    const applied = apply(prepared.out);
    assert.equal(applied.status, 0, applied.stderr);
    assertCrLfOnly(fs.readFileSync(target, "utf8"), test.name);
  }

  // 7. Invalid 1 MiB enum input is rejected without echoing the payload.
  {
    const root = createProject("bounded-invalid-enum");
    const huge = "非法层级".repeat(Math.ceil((1024 * 1024) / Buffer.byteLength("非法层级", "utf8")));
    mutate(root, "STATUS.md", (text) => text.replace("| 基线 | 通过 | 主线 |", `| 基线 | 通过 | ${huge} |`));
    const result = run("validate", root, [], 4 * 1024 * 1024);
    assert.notEqual(result.status, 0);
    assert.ok(Buffer.byteLength(result.stdout, "utf8") < 128 * 1024, `stdout was ${Buffer.byteLength(result.stdout, "utf8")} bytes`);
    assert.equal(result.stdout.includes(huge.slice(0, 4096)), false, "invalid value was echoed verbatim");
  }

  // 8. A mkdir must have a same-plan write descendant.
  {
    const orphanRoot = createProject("orphan-mkdir");
    const orphan = propose(orphanRoot, "orphan-mkdir", [
      { kind: "mkdir", path: "历史记录/空治理目录" },
    ]);
    assertRejected(orphan, "orphan governance mkdir must fail");

    const populatedRoot = createProject("populated-mkdir");
    const populated = propose(populatedRoot, "populated-mkdir", [
      { kind: "mkdir", path: "历史记录/有内容" },
      { kind: "write_file", path: "历史记录/有内容/记录.md", content: "# 记录\n", overwrite: false },
    ]);
    assert.equal(populated.status, 0, populated.stderr);
  }

  // 9. Migration check gives a shallow legacy-root hint without deep directory scanning.
  {
    const root = createProject("physical-layout");
    write(root, "01-遗留说明.md", "# 遗留说明\n");
    const migration = run("migrate-check", root);
    assert.ok(migration.json?.physical_layout, "migrate-check must expose shallow physical_layout");
    assert.ok(physicalCount(migration.json.physical_layout, "root_numbered_markdown", "root_numbered_markdown_count") >= 1);
    assert.ok(!(migration.json.migration_items || []).some((item) => item.code.includes("root_numbered_markdown")));
  }

  // 10. Entry/handoff coverage is mandatory and migrate-check states its scope.
  {
    const missingEntry = createProject("missing-start-entry");
    mutate(missingEntry, "PROJECT_START_HERE.md", () => "# PROJECT_START_HERE.md\n");
    assertRejected(run("migrate-check", missingEntry), "project path/start entry are required");

    const missingHandoff = createProject("missing-handoff-context");
    mutate(missingHandoff, "HANDOFF.md", (text) => text
      .replace(/## 接手顺序[\s\S]*?(?=## 已证伪路线)/, "")
      .replace(/## 未决上下文[\s\S]*$/, ""));
    assertRejected(run("migrate-check", missingHandoff), "handoff order/pending context are required");

    const scoped = run("migrate-check", createProject("migrate-coverage"));
    assert.ok(scoped.json && Object.hasOwn(scoped.json, "checked"), "migrate-check must report checked");
    assert.ok(scoped.json && Object.hasOwn(scoped.json, "not_checked"), "migrate-check must report not_checked");
    assert.ok(scoped.json && Object.hasOwn(scoped.json, "coverage_scope"), "migrate-check must report coverage_scope");
    assert.ok(Array.isArray(scoped.json.checked));
    assert.ok(Array.isArray(scoped.json.not_checked));
    assert.ok(scoped.json.coverage_scope !== null && scoped.json.coverage_scope !== "");
  }

  // 11. Material verification checks file content, not merely the presence of a hash column.
  {
    const root = createProject("material-hash-truth");
    const material = Buffer.from("first material payload\n", "utf8");
    write(root, "项目物料/原件/sample.txt", material);
    const expected = crypto.createHash("sha256").update(material).digest("hex");
    mutate(root, "项目物料/INDEX.md", (text) => `${text}| MAT-20260728-001 | 项目物料/原件/sample.txt | ${expected} | 本地 | 回归 | active |\n`);

    const verified = run("verify-materials", root);
    assert.equal(verified.status, 0, verified.stderr);
    assert.equal(verified.json.complete, true, verified.stdout);
    assert.equal(verified.json.matched_count, 1, verified.stdout);
    assert.equal(verified.json.matched_sample[0].path, "项目物料/原件/sample.txt", verified.stdout);

    write(root, "项目物料/原件/sample.txt", "changed material payload\n");
    const stale = run("verify-materials", root);
    assertRejected(stale, "stale material hash must fail verification");
    assert.equal(stale.json.mismatch_count, 1, stale.stdout);
  }

  // 12. Reordered/custom index columns cannot bypass duplicate IDs or second-table ambiguity.
  {
    const duplicate = createProject("reordered-index-duplicate");
    mutate(duplicate, "历史记录/00-历史总目录.md", () => [
      "# 历史总目录",
      "",
      "| 分类 | 日期 | history-id | 标题 | 路径 | 状态 |",
      "| --- | --- | --- | --- | --- | --- |",
      "| A | 2026-07-28 | M-20260728-001 | A | a.md | active |",
      "| B | 2026-07-28 | M-20260728-001 | B | b.md | active |",
      "",
    ].join("\n"));
    assertRejected(run("validate", duplicate), "reordered ID column must still be unique");

    const ambiguous = createProject("reordered-second-table");
    mutate(ambiguous, "STATUS.md", (text) => text.replace(
      "| 回归 | 正常 | 本地夹具 |",
      "| 回归 | 正常 | 本地夹具 |\n\n说明。\n\n| 状态 | 依据 | 项目 |\n| --- | --- | --- |\n| 正常 | 第二张 | 重复 |",
    ));
    assertRejected(run("validate", ambiguous), "reordered second contract table must be ambiguous");
  }

  // 13. Material verification refuses discontinuous or structurally invalid index data.
  {
    const root = createProject("material-discontinuous");
    const first = Buffer.from("first\n", "utf8");
    const second = Buffer.from("second\n", "utf8");
    write(root, "项目物料/原件/first.txt", first);
    write(root, "项目物料/原件/second.txt", second);
    const firstHash = crypto.createHash("sha256").update(first).digest("hex");
    const secondHash = crypto.createHash("sha256").update(second).digest("hex");
    mutate(root, "项目物料/INDEX.md", (text) => `${text}| MAT-20260728-001 | 项目物料/原件/first.txt | ${firstHash} | 本地 | 回归 | active |\n\n| MAT-20260728-002 | 项目物料/原件/second.txt | ${secondHash} | 本地 | 回归 | active |\n`);
    assertRejected(run("verify-materials", root), "discontinuous material rows must not be silently ignored");
  }

  // 14. Migration readiness includes semantic declarations and physical-scan completeness.
  {
    const semantic = createProject("migrate-semantic-invalid");
    mutate(semantic, "HANDOFF.md", (text) => text.replace("2026-07-28 08:00 +08:00", "not-a-date"));
    const semanticResult = run("migrate-check", semantic);
    assertRejected(semanticResult, "invalid semantic checkpoint must block migration freshness");
    assert.equal(semanticResult.json.up_to_date, false, semanticResult.stdout);

  }

  // 15. The tool cache itself cannot be redirected through a same-project junction.
  {
    const root = createProject("governance-cache-junction");
    const ordinary = path.join(root, "ordinary-cache");
    fs.mkdirSync(ordinary);
    fs.symlinkSync(ordinary, path.join(root, ".project-gov"), "junction");
    const redirected = propose(root, "cache-junction", []);
    assertRejected(redirected, ".project-gov junction must block propose output");
    assert.equal(fs.existsSync(path.join(ordinary, "plans", "cache-junction.json")), false);
  }

  // 16. A line-replacement action rejects multiline content; block replacement handles it.
  {
    const root = createProject("multiline-line-replacement");
    const rejected = propose(root, "multiline-line-replacement", [{
      kind: "replace_line_contains",
      path: "STATUS.md",
      contains: "## 风险",
      replacement: "## 风险\n\n- 新增",
    }]);
    assertRejected(rejected, "replace_line_contains must remain single-line");
  }

  // 17. Material report fields are bounded and Windows alternate data streams are rejected.
  {
    const root = createProject("material-output-bound");
    const payload = Buffer.from("bounded\n", "utf8");
    write(root, "项目物料/原件/bounded.txt", payload);
    const hash = crypto.createHash("sha256").update(payload).digest("hex");
    const hugeId = "M".repeat(1024 * 1024);
    mutate(root, "项目物料/INDEX.md", (text) => `${text}| ${hugeId} | 项目物料/原件/bounded.txt | ${hash} | 本地 | 回归 | active |\n`);
    const bounded = run("verify-materials", root, [], 4 * 1024 * 1024);
    assert.equal(bounded.status, 0, bounded.stderr);
    assert.ok(Buffer.byteLength(bounded.stdout, "utf8") < 128 * 1024, `material stdout was ${Buffer.byteLength(bounded.stdout, "utf8")} bytes`);

    if (process.platform === "win32") {
      const ads = createProject("material-ads");
      const base = write(ads, "项目物料/原件/base.txt", "base\n");
      const adsPath = `${base}:hidden`;
      fs.writeFileSync(adsPath, "hidden\n", "utf8");
      const adsHash = crypto.createHash("sha256").update(fs.readFileSync(adsPath)).digest("hex");
      mutate(ads, "项目物料/INDEX.md", (text) => `${text}| MAT-20260728-009 | 项目物料/原件/base.txt:hidden | ${adsHash} | 本地 | 回归 | active |\n`);
      assertRejected(run("verify-materials", ads), "NTFS alternate data stream must not be verified as a regular file");
    }
  }

  // 18. Version, help text and reference documentation describe the same cache behavior.
  {
    const help = spawnSync(process.execPath, [script, "--help"], {
      encoding: "utf8",
      maxBuffer: 1024 * 1024,
    });
    assert.equal(help.status, 0, help.stderr);
    assert.match(help.stdout, /Read-only cache inventory:/);
    assert.match(help.stdout, /prune only inventories old \.project-gov cache; it never deletes files\./);
    assert.doesNotMatch(help.stdout, /project-gov prune[^\r\n]*--apply/);

    const cliDoc = fs.readFileSync(path.join(skillRoot, "references", "project-gov-cli.md"), "utf8");
    const stateDoc = fs.readFileSync(path.join(skillRoot, "references", "project-state.md"), "utf8");
    const skillSource = fs.readFileSync(path.join(skillRoot, "SKILL.md"), "utf8");
    assert.match(cliDoc, /`prune` 是只读盘点命令/);
    assert.match(cliDoc, /符号链接和目录联接不会被跟随或展开/);
    assert.doesNotMatch(cliDoc, /prune[^\r\n]*--apply/);
    assert.doesNotMatch(cliDoc, /专用所有权标记/);
    assert.doesNotMatch(cliDoc, /`inspect`[^\r\n]*physical_layout/);
    assert.match(cliDoc, /`migrate-check（迁移检查）`[^\r\n]*`physical_layout（物理布局）`/);
    assert.match(stateDoc, /`migrate-check` 只浅层列出根目录编号文档/);
    for (const phrase of [
      "**很轻**",
      "**很狠**",
      "**很稳**",
      "**使用方法：**",
      "https://github.com/haoyun18881-beep/project-delivery-engine",
    ]) {
      assert.ok(skillSource.includes(phrase), `SKILL.md marketing contract missing: ${phrase}`);
    }

    const inspected = run("inspect", createProject("inspect-contract"));
    assert.equal(inspected.status, 0, inspected.stderr);
    assert.equal(inspected.json.skill_version, expectedSkillVersion, inspected.stdout);
    assert.equal(Object.hasOwn(inspected.json, "physical_layout"), false, inspected.stdout);

    const quickstart = fs.readFileSync(path.join(skillRoot, "references", "quickstart-faq.md"), "utf8");
    assert.match(skillSource, /references\/quickstart-faq\.md/);
    assert.match(quickstart, /## 一个完整例子/);
    assert.match(quickstart, /## 什么时候会触发/);
    assert.match(quickstart, /## 常见问题/);
    assert.match(quickstart, /## 出错时怎么处理/);

    const cacheRoot = createProject("prune-link-contract");
    const cacheTarget = path.join(cacheRoot, "cache-target");
    fs.mkdirSync(cacheTarget, { recursive: true });
    write(cacheRoot, "cache-target/sentinel.txt", "keep\n");
    fs.mkdirSync(path.join(cacheRoot, ".project-gov", "plans"), { recursive: true });
    fs.symlinkSync(cacheTarget, path.join(cacheRoot, ".project-gov", "plans", "redirected"), "junction");
    const inventory = run("prune", cacheRoot, ["--older-than-days", "0"]);
    assert.equal(inventory.status, 0, inventory.stderr);
    assert.equal((inventory.json.items || []).some((item) => item.rel.endsWith("/redirected")), false);
    assert.equal(fs.readFileSync(path.join(cacheTarget, "sentinel.txt"), "utf8"), "keep\n");
  }

  // 19. Empty material indexes state their narrow verification scope without failing an empty project.
  {
    const root = createProject("material-empty-scope");
    const empty = run("verify-materials", root);
    assert.equal(empty.status, 0, empty.stderr);
    assert.equal(empty.json.ok, true, empty.stdout);
    assert.equal(empty.json.complete, true, empty.stdout);
    assert.equal(empty.json.verification_scope, "indexed_rows_only", empty.stdout);
    assert.equal(empty.json.indexed_count, 0, empty.stdout);
    assert.equal(empty.json.checked_count, 0, empty.stdout);
    assert.ok(empty.json.warnings.includes("material_index_empty_no_files_verified"), empty.stdout);
  }

  // 20. External paths are redacted and independent hash/path failures are reported together.
  {
    const root = createProject("material-redacted-reasons");
    const sensitivePath = "C:\\Synthetic Sensitive\\customer-video.mp4";
    mutate(root, "项目物料/INDEX.md", (text) => `${text}| MAT-20260728-010 | ${sensitivePath} | not-a-sha256 | 外部 | 回归 | active |\n`);
    const result = run("verify-materials", root);
    assertRejected(result, "invalid hash and external path must both be reported");
    assert.doesNotMatch(result.stdout, /Synthetic Sensitive|customer-video\.mp4/);
    assert.equal(result.json.unverifiable.length, 1, result.stdout);
    const record = result.json.unverifiable[0];
    assert.equal(record.path, null, result.stdout);
    assert.equal(record.path_kind, "absolute", result.stdout);
    assert.equal(record.path_redacted, true, result.stdout);
    assert.equal(record.reason, "hash_not_sha256", result.stdout);
    assert.deepEqual(record.reasons, ["hash_not_sha256", "absolute_path_not_verified"], result.stdout);
  }

  // 21. Every structured result is versioned, compiled plans bind the version, and old plans fail before locking.
  {
    const root = createProject("versioned-json-contract");
    for (const [command, extra] of [
      ["inspect", []],
      ["validate", []],
      ["ids", ["--date", "20260728"]],
      ["startup", []],
      ["migrate-check", []],
      ["verify-materials", []],
      ["prune", ["--older-than-days", "0"]],
    ]) {
      const result = run(command, root, extra);
      assert.equal(result.status, 0, result.stderr);
      assert.equal(result.json.skill_version, expectedSkillVersion, `${command}: ${result.stdout || result.stderr}`);
    }

    const proposed = propose(root, "versioned-plan", []);
    assert.equal(proposed.status, 0, proposed.stderr);
    assert.equal(proposed.json.skill_version, expectedSkillVersion, proposed.stdout);
    const compiled = JSON.parse(fs.readFileSync(proposed.out, "utf8"));
    assert.equal(compiled.compiled_schema_version, 2);
    assert.equal(compiled.skill_version, expectedSkillVersion);

    const applied = apply(proposed.out);
    assert.equal(applied.status, 0, applied.stderr);
    assert.equal(applied.json.skill_version, expectedSkillVersion, applied.stdout);

    const stalePlan = write(root, "stale-version.plan.json", `${JSON.stringify({
      ...compiled,
      skill_version: "0.3.1",
    }, null, 2)}\n`);
    const staleApply = apply(stalePlan);
    assertRejected(staleApply, "stale skill plans must be rejected");
    assert.equal(staleApply.json.skill_version, expectedSkillVersion, staleApply.stdout || staleApply.stderr);
    assert.match(staleApply.json.error, /Compiled plan version incompatible/);
    assert.equal(fs.existsSync(path.join(root, ".project-gov", "apply.lock")), false);
    assert.equal(fs.existsSync(path.join(root, ".project-gov", "backups")), false);

    const failed = run("inspect", root, ["--unsupported", "value"]);
    assertRejected(failed, "error JSON must carry the running skill version");
    assert.equal(failed.json.skill_version, expectedSkillVersion, failed.stdout || failed.stderr);
  }

  // 22. Literal material paths preserve legal leading underscores instead of verifying a decoy file.
  {
    const root = createProject("material-literal-path");
    const decoy = Buffer.from("decoy payload\n", "utf8");
    write(root, "artifact.txt", decoy);
    const decoyHash = crypto.createHash("sha256").update(decoy).digest("hex");
    mutate(root, "项目物料/INDEX.md", (text) => `${text}| MAT-20260728-011 | \`_artifact.txt\` | ${decoyHash} | 本地 | 回归 | active |\n`);

    const result = run("verify-materials", root);
    assertRejected(result, "a missing underscored path must not verify the undecorated decoy");
    assert.equal(result.json.matched_count, 0, result.stdout);
    assert.equal(result.json.missing_count, 1, result.stdout);
    assert.equal(result.json.missing[0].path, "_artifact.txt", result.stdout);
    assert.ok(result.json.missing[0].reasons.includes("missing"), result.stdout);
  }

  // 23. Managed project files cannot be read through a directory junction outside the project.
  {
    const root = createProject("managed-core-junction");
    const external = path.join(sandbox, `external-managed-${sequence}`);
    write(
      external,
      "INDEX.md",
      "# EXTERNAL_INDEX_MARKER\n\n| material-id | 路径 | hash | 来源 | 用途 | 状态 |\n| --- | --- | --- | --- | --- | --- |\n",
    );
    fs.rmSync(path.join(root, "项目物料"), { recursive: true, force: true });
    fs.symlinkSync(external, path.join(root, "项目物料"), "junction");

    for (const command of ["inspect", "verify-materials"]) {
      const result = run(command, root);
      assertRejected(result, `${command} must reject a redirected managed index`);
      assert.match(result.json.error, /managed_project_path_redirected:项目物料\/INDEX\.md/);
      assert.doesNotMatch(result.stdout || result.stderr, /EXTERNAL_INDEX_MARKER/);
    }
  }

  // 24. Apply preserves a pre-existing backup base and refuses a redirected backup base before locking or writing.
  {
    const preservedRoot = createProject("backup-base-preserved");
    const preservedPlan = propose(preservedRoot, "backup-base-preserved", []);
    assert.equal(preservedPlan.status, 0, preservedPlan.stderr);
    const preservedBase = path.join(preservedRoot, ".project-gov", "backups");
    fs.mkdirSync(preservedBase);
    const preservedApply = apply(preservedPlan.out);
    assert.equal(preservedApply.status, 0, preservedApply.stderr);
    assert.equal(fs.existsSync(preservedBase), true);
    assert.deepEqual(fs.readdirSync(preservedBase), []);

    const redirectedRoot = createProject("backup-base-junction");
    const redirectedPlan = propose(redirectedRoot, "backup-base-junction", []);
    assert.equal(redirectedPlan.status, 0, redirectedPlan.stderr);
    const external = path.join(sandbox, `external-backups-${sequence}`);
    fs.mkdirSync(external);
    write(external, "sentinel.txt", "keep\n");
    const redirectedBase = path.join(redirectedRoot, ".project-gov", "backups");
    fs.symlinkSync(external, redirectedBase, "junction");

    const redirectedApply = apply(redirectedPlan.out);
    assertRejected(redirectedApply, "a redirected backup base must block apply");
    assert.match(redirectedApply.json.error, /managed_project_path_redirected:\.project-gov\/backups/);
    assert.equal(fs.lstatSync(redirectedBase).isSymbolicLink(), true);
    assert.deepEqual(fs.readdirSync(external), ["sentinel.txt"]);
    assert.equal(fs.existsSync(path.join(redirectedRoot, ".project-gov", "apply.lock")), false);
  }

  console.log("project-gov regression tests: PASS");
} finally {
  fs.rmSync(sandbox, { recursive: true, force: true });
}
