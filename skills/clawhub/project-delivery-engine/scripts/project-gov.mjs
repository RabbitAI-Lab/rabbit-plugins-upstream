#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const FIVE_PIECE = [
  "AGENTS.md",
  "PROJECT_START_HERE.md",
  "STATUS.md",
  "TODO.md",
  "HANDOFF.md",
];

const INDEX_FILES = [
  "历史记录/00-历史总目录.md",
  "证据库/总索引/证据总目录.md",
  "项目物料/INDEX.md",
];
const GOVERNANCE_ROOT_DIRECTORIES = ["历史记录", "证据库", "项目物料"];

const FIVE_PIECE_LIMIT_BYTES = 45 * 1024;
const FIVE_PIECE_LOW_SPACE_BYTES = 2 * 1024;
const MARKDOWN_SCAN_LIMIT = 5000;
const MAX_ACTIONS = 200;
const MAX_ACTION_TEXT_BYTES = 512 * 1024;
const MAX_ANCHOR_TEXT_BYTES = 16 * 1024;
const MAX_MUTABLE_TEXT_FILE_BYTES = 2 * 1024 * 1024;
const MAX_MATERIAL_HASH_FILE_BYTES = 256 * 1024 * 1024;
const MAX_MATERIAL_REPORT_ITEMS = 100;
const MAX_MATERIAL_MATCH_SAMPLES = 20;
const MAX_PRUNE_REPORT_ITEMS = 100;
const MAX_STRUCTURE_ISSUES = 100;
const MAX_STRUCTURE_DETAIL_CHARS = 512;
const MAX_PHYSICAL_LAYOUT_SAMPLES = 20;
const SCRIPT_NAME = "project-gov";
const SKILL_VERSION = "0.3.4";
const COMPILED_SCHEMA_VERSION = 2;
const PROJECT_STRUCTURE_VERSION = 2;
const DEFAULT_PRUNE_AGE_DAYS = 30;
const BACKUP_OWNER_FILE = ".project-gov-owner.json";
const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const SKILL_DIR = path.resolve(SCRIPT_DIR, "..");
const SKILL_PATH = path.join(SKILL_DIR, "SKILL.md");
const RESERVED_PATH_SEGMENTS = new Set([".git", ".project-gov", "node_modules"]);
const PROJECT_ID_TOPIC_SEGMENTS_SOURCE = String.raw`(?:-[A-Z0-9]+)*`;
const PROJECT_ID_SEQUENCE_SOURCE = String.raw`\d{3}`;
const PROJECT_ID_BODY_SOURCE = String.raw`(?:MAT|EV|M)-\d{8}${PROJECT_ID_TOPIC_SEGMENTS_SOURCE}-${PROJECT_ID_SEQUENCE_SOURCE}`;
const PROJECT_ID_REGEX_SOURCE = `(?<![A-Za-z0-9_])(${PROJECT_ID_BODY_SOURCE})(?![A-Za-z0-9_-])`;

const PLACEHOLDER_PATTERNS = [
  /<placeholder>/i,
  /<YYYY-MM-DD\b[^>]*>/i,
  /<已核对或待确认>/,
  /TODO_FILL/i,
  /\bTBD\b/i,
  /待填写/,
  /未填写/,
];

const TABLE_HEADER_ALIASES = new Map([
  ["历史编号", "history-id"],
  ["history_id", "history-id"],
  ["history-id（历史编号）", "history-id"],
  ["history-id(历史编号)", "history-id"],
  ["证据编号", "evidence-id"],
  ["evidence_id", "evidence-id"],
  ["evidence-id（证据编号）", "evidence-id"],
  ["evidence-id(证据编号)", "evidence-id"],
  ["物料编号", "material-id"],
  ["material_id", "material-id"],
  ["material-id（物料编号）", "material-id"],
  ["material-id(物料编号)", "material-id"],
  ["执行批次", "run_id"],
  ["run-id", "run_id"],
  ["run_id（执行批次）", "run_id"],
  ["run_id(执行批次)", "run_id"],
  ["run-id（执行批次）", "run_id"],
  ["run-id(执行批次)", "run_id"],
  ["任务编号", "task_id"],
  ["task-id", "task_id"],
  ["task_id（任务编号）", "task_id"],
  ["task_id(任务编号)", "task_id"],
  ["task-id（任务编号）", "task_id"],
  ["task-id(任务编号)", "task_id"],
  ["哈希", "hash"],
  ["hash（哈希）", "hash"],
  ["hash(哈希)", "hash"],
  ["sha256", "hash"],
  ["sha-256", "hash"],
  ["原件路径", "路径"],
  ["路径（原件）", "路径"],
  ["路径(原件)", "路径"],
]);

function main() {
  try {
    const argv = process.argv.slice(2);
    const command = argv.shift();
    const opts = parseArgs(argv);

    if (!command || command === "help" || command === "--help" || command === "-h") {
      printHelp();
      return;
    }

    const handlers = {
      inspect: commandInspect,
      validate: commandValidate,
      ids: commandIds,
      startup: commandStartup,
      "migrate-check": commandMigrateCheck,
      "verify-materials": commandVerifyMaterials,
      prune: commandPrune,
      propose: commandPropose,
      apply: commandApply,
    };
    if (!handlers[command]) fail(`Unknown command: ${command}`, 2);
    validateCommandOptions(command, opts);
    return handlers[command](opts);
  } catch (error) {
    const payload = {
      ok: false,
      error: error.message || String(error),
      tool: SCRIPT_NAME,
      skill_version: SKILL_VERSION,
    };
    console.error(JSON.stringify(payload, null, 2));
    process.exitCode = process.exitCode || 1;
  }
}

function parseArgs(argv) {
  const opts = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg.startsWith("--")) {
      opts._.push(arg);
      continue;
    }

    const key = arg.slice(2);
    if (["json", "text", "apply"].includes(key)) {
      opts[toCamel(key)] = true;
      continue;
    }

    const next = argv[i + 1];
    if (next === undefined || next.startsWith("--")) {
      fail(`Missing value for --${key}`, 2);
    }
    opts[toCamel(key)] = next;
    i += 1;
  }
  return opts;
}

function validateCommandOptions(command, opts) {
  const allowed = {
    inspect: new Set(["root", "json"]),
    validate: new Set(["root", "json"]),
    ids: new Set(["root", "date", "json"]),
    startup: new Set(["root", "json", "text"]),
    "migrate-check": new Set(["root", "json"]),
    "verify-materials": new Set(["root", "json"]),
    prune: new Set(["root", "olderThanDays", "json"]),
    propose: new Set(["root", "plan", "out", "json"]),
    apply: new Set(["plan", "json"]),
  }[command];
  if (opts._.length > 0) fail(`Unexpected positional arguments: ${opts._.join(", ")}`, 2);
  const unknown = Object.keys(opts).filter((key) => key !== "_" && !allowed.has(key));
  if (unknown.length > 0) fail(`Unsupported option(s) for ${command}: ${unknown.join(", ")}`, 2);
  if (command === "startup" && opts.json && opts.text) {
    fail("startup accepts either --json or --text, not both", 2);
  }
}

function toCamel(value) {
  return value.replace(/-([a-z])/g, (_, ch) => ch.toUpperCase());
}

function printHelp() {
  console.log(`Usage:
  Read-only:
  ${SCRIPT_NAME} inspect --root <path> [--json]
  ${SCRIPT_NAME} validate --root <path> [--json]
  ${SCRIPT_NAME} ids --root <path> [--date YYYYMMDD|YYYY-MM-DD] [--json]
  ${SCRIPT_NAME} startup --root <path> [--json|--text]
  ${SCRIPT_NAME} migrate-check --root <path> [--json]
  ${SCRIPT_NAME} verify-materials --root <path> [--json]

  Read-only cache inventory:
  ${SCRIPT_NAME} prune --root <path> [--older-than-days <days>] [--json]

  Controlled writes:
  ${SCRIPT_NAME} propose --root <path> --plan <operation.json> [--out <root>/.project-gov/plans/<plan-id>.json] [--json]
  ${SCRIPT_NAME} apply --plan <prepared.json> [--json]

Rules:
  - inspect/validate/ids/startup/migrate-check/verify-materials are read-only.
  - prune only inventories old .project-gov cache; it never deletes files.
  - propose is dry-run only; it prepares and validates a file-operation plan.
  - apply holds an atomic project-local lock, revalidates actions, checks before_hashes, and rolls back failed writes.`);
}

function commandInspect(opts) {
  const root = resolveRoot(opts.root);
  const report = inspectProject(root);
  output(report, opts);
  if (!report.ok) process.exitCode = 1;
}

function commandValidate(opts) {
  const root = resolveRoot(opts.root);
  const report = inspectProject(root);
  const errors = report.errors;

  const validation = {
    ok: errors.length === 0,
    mechanical_ok: errors.length === 0,
    validation_kind: "mechanical",
    semantic_checked_by_tool: false,
    tool: SCRIPT_NAME,
    command: "validate",
    skill_version: SKILL_VERSION,
    project_structure_version: PROJECT_STRUCTURE_VERSION,
    root,
    errors,
    warnings: report.warnings,
    semantic_declaration: report.semantic_declaration,
    report,
  };

  output(validation, opts);
  if (!validation.ok) process.exitCode = 1;
}

function commandIds(opts) {
  const root = resolveRoot(opts.root);
  assertManagedCorePathsNotRedirected(root);
  const markdownScan = listMarkdownFiles(root);
  const date = normalizeDate(opts.date || currentLocalDate());
  const scanErrors = markdownScanErrors(markdownScan);
  const idData = collectIds(root, markdownScan.files, []);
  const ids = scanErrors.length === 0 ? nextIds(idData.all, date) : null;
  const result = {
    ok: scanErrors.length === 0,
    tool: SCRIPT_NAME,
    command: "ids",
    root,
    date,
    ids,
    markdown_scan: markdownScan.summary,
    errors: scanErrors,
  };
  output(result, opts);
  if (!result.ok) process.exitCode = 1;
}

function commandStartup(opts) {
  const root = resolveRoot(opts.root);
  const report = inspectProject(root);
  const startup = `[$project-delivery-engine](<${SKILL_PATH}>) 接续本项目。

项目根目录：
${root}

先读 AGENTS.md、PROJECT_START_HERE.md、HANDOFF.md、STATUS.md、TODO.md 的当前结论、索引和结尾；只有任务需要时再按索引深读历史记录、证据库、项目物料和专项文档。接到具体任务后由项目交付引擎判断建档、接续、执行、派兵或交接路线。`;

  const changesPending = report.semantic_declaration.changes_after_checkpoint === "待确认";
  const readinessErrors = [
    ...report.errors,
    ...(changesPending ? ["handoff_changes_not_reconciled"] : []),
  ];
  const ready = readinessErrors.length === 0;

  const result = {
    ok: ready,
    mechanical_ok: report.ok,
    validation_kind: "startup_readiness",
    semantic_checked_by_tool: false,
    tool: SCRIPT_NAME,
    command: "startup",
    root,
    startup: ready ? startup : null,
    errors: readinessErrors,
    semantic_declaration: report.semantic_declaration,
    warnings: [
      ...(report.warnings || []),
      ...report.files.five_piece.missing.map((file) => `missing:${file}`),
      ...report.files.indexes.missing.map((file) => `missing:${file}`),
      ...(report.five_piece.over_limit ? ["five_piece_over_45kb"] : []),
      ...(report.markdown_scan.truncated ? ["markdown_scan_truncated"] : []),
    ],
  };

  if (opts.json) {
    output(result, opts);
  } else if (result.ok) {
    console.log(startup);
  } else {
    console.error("startup_not_generated: readiness_gate_failed");
    console.error(`errors: ${result.errors.join(", ") || "none"}`);
  }

  if (!result.ok) process.exitCode = 1;
}

function commandMigrateCheck(opts) {
  const root = resolveRoot(opts.root);
  const report = inspectProject(root);
  const physicalLayout = inspectLegacyRootLayout(root);
  const missingFiles = [
    ...report.files.five_piece.missing,
    ...report.files.indexes.missing,
  ].map((rel) => ({
    code: `structure_file_missing:${rel}`,
    rel,
    section: null,
    detail: "required_file_missing",
  }));
  const scanItems = markdownScanErrors({
    truncated: report.markdown_scan.truncated,
    read_errors: report.markdown_scan.read_errors || [],
  }).map((code) => ({
    code,
    rel: null,
    section: null,
    detail: "migration_scan_incomplete",
  }));
  const semanticItems = report.semantic_declaration.errors.map((code) => ({
    code,
    rel: "HANDOFF.md",
    section: "## 语义检查点",
    detail: "semantic_declaration_invalid",
  }));
  const layoutItems = [
    ...(report.structure.issues_truncated ? [{
      code: "structure_issue_report_truncated",
      rel: null,
      section: null,
      detail: "migration_structure_report_incomplete",
    }] : []),
  ];
  const migrationItems = [
    ...missingFiles,
    ...report.structure.issues,
    ...semanticItems,
    ...scanItems,
    ...layoutItems,
  ];
  const indeterminate = scanItems.length > 0 || layoutItems.length > 0;
  const result = {
    ok: migrationItems.length === 0,
    tool: SCRIPT_NAME,
    command: "migrate-check",
    root,
    skill_version: SKILL_VERSION,
    target_project_structure_version: PROJECT_STRUCTURE_VERSION,
    up_to_date: migrationItems.length === 0 && !indeterminate,
    indeterminate,
    automatic_rewrite: false,
    migration_items: migrationItems,
    notices: report.warnings,
    checked: report.structure.checked,
    not_checked: report.structure.not_checked,
    coverage_scope: report.structure.coverage_scope,
    physical_layout: physicalLayout,
  };
  output(result, opts);
  if (!result.ok) process.exitCode = 1;
}

function commandPrune(opts) {
  const root = resolveRoot(opts.root);
  const olderThanDays = parseNonNegativeNumber(opts.olderThanDays ?? DEFAULT_PRUNE_AGE_DAYS, "--older-than-days");
  const result = inventoryGovernanceCache(root, olderThanDays);
  output(result, opts);
  if (!result.ok) process.exitCode = 1;
}

function commandVerifyMaterials(opts) {
  const root = resolveRoot(opts.root);
  const result = verifyMaterialHashes(root);
  output(result, opts);
  if (!result.ok) process.exitCode = 1;
}

function verifyMaterialHashes(root) {
  const rel = "项目物料/INDEX.md";
  const abs = path.join(root, rel);
  assertManagedPathNotRedirected(root, rel);
  const contract = CORE_TABLE_CONTRACTS.find((item) => item.rel === rel);
  const base = {
    tool: SCRIPT_NAME,
    command: "verify-materials",
    root,
    index: rel,
    algorithm: "sha256",
    verification_scope: "indexed_rows_only",
    max_file_bytes: MAX_MATERIAL_HASH_FILE_BYTES,
  };
  if (!fs.existsSync(abs) || !fs.statSync(abs).isFile()) {
    return {
      ...base,
      ok: false,
      complete: false,
      checked_count: 0,
      matched_count: 0,
      mismatches: [],
      missing: [],
      unverifiable: [],
      errors: [`material_index_missing:${rel}`],
    };
  }

  const text = readText(abs);
  const structureCollector = createStructureIssueCollector();
  inspectTableContract(text, contract, structureCollector);
  if (structureCollector.count > 0) {
    return {
      ...base,
      ok: false,
      complete: false,
      checked_count: 0,
      matched_count: 0,
      mismatches: [],
      missing: [],
      unverifiable: [],
      structure_issues: structureCollector.issues,
      structure_issues_truncated: structureCollector.truncated,
      errors: ["material_index_structure_invalid"],
    };
  }

  const lines = visibleMarkdownLines(text);
  const candidates = findContractTableHeaders(lines, 0, lines.length, contract);
  if (candidates.length !== 1) {
    return {
      ...base,
      ok: false,
      complete: false,
      checked_count: 0,
      matched_count: 0,
      mismatches: [],
      missing: [],
      unverifiable: [],
      errors: [candidates.length === 0
        ? "material_index_contract_table_missing"
        : `material_index_contract_table_ambiguous:${candidates.length}`],
    };
  }

  const headerIndex = candidates[0].index;
  const headers = splitMarkdownTableRow(lines[headerIndex]).map(normalizeTableHeader);
  const column = Object.fromEntries(headers.map((name, index) => [name, index]));
  const required = ["material-id", "路径", "hash"];
  const missingColumns = required.filter((name) => !Object.hasOwn(column, name));
  const duplicateColumns = required.filter(
    (name) => headers.filter((header) => header === name).length > 1,
  );
  if (missingColumns.length > 0 || duplicateColumns.length > 0) {
    return {
      ...base,
      ok: false,
      complete: false,
      checked_count: 0,
      matched_count: 0,
      mismatches: [],
      missing: [],
      unverifiable: [],
      errors: [
        ...(missingColumns.length > 0 ? [`material_index_columns_missing:${missingColumns.join(",")}`] : []),
        ...(duplicateColumns.length > 0 ? [`material_index_columns_duplicate:${duplicateColumns.join(",")}`] : []),
      ],
    };
  }

  let matchedCount = 0;
  let mismatchCount = 0;
  let missingCount = 0;
  let unverifiableCount = 0;
  let indexedCount = 0;
  const matchedSample = [];
  const mismatches = [];
  const missing = [];
  const unverifiable = [];
  let cursor = headerIndex + 2;
  while (cursor < lines.length && isMarkdownTableRow(lines[cursor])) {
    indexedCount += 1;
    const cells = splitMarkdownTableRow(lines[cursor]).map((cell) => String(cell || "").trim());
    const materialId = limitText(
      normalizeTableCell(cells[column["material-id"]]) || `line:${cursor + 1}`,
      MAX_STRUCTURE_DETAIL_CHARS,
    );
    const rawPath = cells[column["路径"]] || "";
    const rawHash = cells[column.hash] || "";
    const expected = normalizeSha256Cell(rawHash);
    const pathResult = resolveMaterialFileForHash(root, rawPath);

    const reasons = [
      ...(!expected.ok ? [expected.reason] : []),
      ...(!pathResult.ok ? [pathResult.reason] : []),
    ];
    if (reasons.length > 0) {
      const missingOnly = expected.ok && pathResult.reason === "missing";
      const target = missingOnly ? missing : unverifiable;
      if (missingOnly) missingCount += 1;
      else unverifiableCount += 1;
      pushLimited(target, {
        material_id: materialId,
        ...materialPathReport(pathResult),
        line: cursor + 1,
        reason: reasons[0],
        reasons,
      }, MAX_MATERIAL_REPORT_ITEMS);
      cursor += 1;
      continue;
    }

    let actual;
    try {
      actual = sha256(fs.readFileSync(pathResult.abs));
    } catch (error) {
      const reason = limitText(`read_failed:${formatFsError(error)}`, MAX_STRUCTURE_DETAIL_CHARS);
      unverifiableCount += 1;
      pushLimited(unverifiable, {
        material_id: materialId,
        ...materialPathReport(pathResult),
        line: cursor + 1,
        reason,
        reasons: [reason],
      }, MAX_MATERIAL_REPORT_ITEMS);
      cursor += 1;
      continue;
    }
    const record = {
      material_id: materialId,
      path: limitText(pathResult.rel, MAX_STRUCTURE_DETAIL_CHARS),
      line: cursor + 1,
      expected_sha256: expected.value,
      actual_sha256: actual,
    };
    if (actual === expected.value) {
      matchedCount += 1;
      pushLimited(matchedSample, {
        material_id: record.material_id,
        path: record.path,
        line: record.line,
      }, MAX_MATERIAL_MATCH_SAMPLES);
    } else {
      mismatchCount += 1;
      pushLimited(mismatches, record, MAX_MATERIAL_REPORT_ITEMS);
    }
    cursor += 1;
  }

  const checkedCount = matchedCount + mismatchCount;
  const complete = mismatchCount === 0
    && missingCount === 0
    && unverifiableCount === 0;
  return {
    ...base,
    ok: complete,
    complete,
    indexed_count: indexedCount,
    checked_count: checkedCount,
    matched_count: matchedCount,
    mismatch_count: mismatchCount,
    missing_count: missingCount,
    unverifiable_count: unverifiableCount,
    matched_sample: matchedSample,
    mismatches,
    missing,
    unverifiable,
    report_truncated: {
      matched: matchedCount > matchedSample.length,
      mismatches: mismatchCount > mismatches.length,
      missing: missingCount > missing.length,
      unverifiable: unverifiableCount > unverifiable.length,
    },
    warnings: indexedCount === 0 ? ["material_index_empty_no_files_verified"] : [],
    errors: [
      ...(mismatchCount > 0 ? ["material_hash_mismatch"] : []),
      ...(missingCount > 0 ? ["material_file_missing"] : []),
      ...(unverifiableCount > 0 ? ["material_hash_unverifiable"] : []),
    ],
  };
}

function pushLimited(target, value, limit) {
  if (target.length < limit) target.push(value);
}

function materialPathReport(pathResult) {
  return {
    path: pathResult.report_path ?? null,
    path_kind: pathResult.path_kind,
    path_redacted: pathResult.path_redacted === true,
  };
}

function normalizeSha256Cell(value) {
  const normalized = normalizeMarkdownCodeCellLiteral(value)
    .replace(/^sha-?256\s*:\s*/i, "")
    .trim()
    .toLowerCase();
  if (!normalized) return { ok: false, reason: "hash_missing" };
  if (!/^[a-f0-9]{64}$/.test(normalized)) return { ok: false, reason: "hash_not_sha256" };
  return { ok: true, value: normalized };
}

function resolveMaterialFileForHash(root, value) {
  const raw = normalizeMarkdownCodeCellLiteral(value);
  if (!raw) return materialPathFailure("path_missing", "missing", null, false);
  if (raw.length > MAX_STRUCTURE_DETAIL_CHARS) {
    return materialPathFailure("path_too_long", "invalid", null, true);
  }
  if (path.isAbsolute(raw) || /^[A-Za-z]:[\\/]/.test(raw)) {
    return materialPathFailure("absolute_path_not_verified", "absolute", null, true);
  }
  if (/^(?:https?:|[a-z][a-z0-9+.-]*:)/i.test(raw)) {
    return materialPathFailure("external_or_non_file_path", "external", null, true);
  }
  const segments = raw.replace(/\\/g, "/").split("/");
  if (segments.includes("..") || segments.includes("")) {
    return materialPathFailure("unsafe_relative_path", "unsafe_relative", null, true);
  }
  if (segments.some((segment) => (
    segment !== segment.trim()
    || segment.includes(":")
    || /\.$/.test(segment)
  ))) {
    return materialPathFailure("nonportable_path_segment", "unsafe_relative", null, true);
  }
  const normalized = segments.filter((item) => item !== ".").join("/");
  const abs = path.resolve(root, normalized);
  if (!isPathInside(root, abs)) {
    return materialPathFailure("path_outside_root", "outside_root", null, true);
  }
  let stat;
  try {
    stat = lstatIfPresent(abs);
  } catch (error) {
    return materialPathFailure(
      `stat_failed:${formatFsError(error)}`,
      "project_relative",
      normalized,
      false,
    );
  }
  if (!stat) return materialPathFailure("missing", "project_relative", normalized, false);
  if (stat.isSymbolicLink()) {
    return materialPathFailure("symbolic_link_not_verified", "project_relative_redirect", normalized, false);
  }
  if (!stat.isFile()) return materialPathFailure("not_regular_file", "project_relative", normalized, false);
  if (stat.size > MAX_MATERIAL_HASH_FILE_BYTES) {
    return materialPathFailure("file_over_hash_limit", "project_relative", normalized, false);
  }

  const realRoot = fs.realpathSync.native(root);
  const realAbs = fs.realpathSync.native(abs);
  if (!isPathInside(realRoot, realAbs)) {
    return materialPathFailure("junction_escape", "project_relative_redirect", normalized, false);
  }
  const expectedReal = path.resolve(realRoot, normalized);
  if (!sameResolvedPath(realAbs, expectedReal)) {
    return materialPathFailure(
      "junction_redirect_not_verified",
      "project_relative_redirect",
      normalized,
      false,
    );
  }
  return {
    ok: true,
    rel: normalized,
    abs,
    report_path: normalized,
    path_kind: "project_relative",
    path_redacted: false,
  };
}

function materialPathFailure(reason, pathKind, reportPath, pathRedacted) {
  return {
    ok: false,
    reason,
    report_path: reportPath,
    path_kind: pathKind,
    path_redacted: pathRedacted,
  };
}

function commandPropose(opts) {
  const root = resolveRoot(opts.root);
  const planPath = requireOption(opts.plan, "--plan is required");
  const plan = readJsonFile(planPath);
  const report = inspectProject(root);
  const compiled = compilePlan(root, plan, report);

  let outPath = null;
  let operationCleanup = null;
  if (opts.out && compiled.ok) {
    outPath = resolveCompiledPlanOutput(root, opts.out);
    writeAtomic(outPath, JSON.stringify(compiled, null, 2) + "\n");
    operationCleanup = cleanupProjectCacheArtifact(root, planPath, ["operations", "ops"]);
  }

  output(summarizeCompiledPlan(compiled, outPath, operationCleanup), opts);
  if (!compiled.ok) process.exitCode = 1;
}

function commandApply(opts) {
  const compiledPath = requireOption(opts.plan, "--plan <compiled.json> is required");
  const compiled = readJsonFile(compiledPath);
  let result = applyCompiledPlan(compiled);
  if (result.ok === true || result.rolled_back === true) {
    const planCleanup = cleanupProjectCacheArtifact(
      resolveRoot(compiled?.root),
      compiledPath,
      ["plans"],
    );
    result = {
      ...result,
      plan_cleanup: planCleanup,
      warnings: planCleanup.ok
        ? (result.warnings || [])
        : [...new Set([...(result.warnings || []), `compiled_plan_cleanup_failed:${planCleanup.error}`])],
    };
  }
  output(result, opts);
  if (!result.ok) process.exitCode = 1;
}

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function isNonEmptyString(value) {
  return typeof value === "string" && value.trim().length > 0;
}

function checkGovernanceSections(root) {
  const text = readTextIfPresent(path.join(root, "HANDOFF.md"));
  const lines = visibleMarkdownLines(text);
  const checks = [
    { key: "falsified_routes", heading: "## 已证伪路线", warning: "missing_handoff_falsified_routes" },
  ];
  const present = {};
  const warnings = [];
  for (const item of checks) {
    const found = lines.some((line) => line.trim() === item.heading);
    present[item.key] = found;
    if (!found) warnings.push(item.warning);
  }
  return { present, warnings };
}

const CORE_SECTION_CONTRACTS = [
  { rel: "PROJECT_START_HERE.md", section: "## 项目路径" },
  { rel: "PROJECT_START_HERE.md", section: "## 启动入口" },
  { rel: "HANDOFF.md", section: "## 接手顺序" },
  { rel: "HANDOFF.md", section: "## 未决上下文" },
];

const CORE_TABLE_CONTRACTS = [
  { rel: "STATUS.md", section: "## 当前状态", columns: ["项目", "状态", "依据"] },
  {
    rel: "STATUS.md",
    section: "## 验证",
    columns: ["验证项", "结果", "层级"],
    enums: { 层级: ["主线", "旁证"] },
  },
  { rel: "TODO.md", section: "## 下一步", columns: ["优先级", "事项", "完成条件"] },
  { rel: "TODO.md", section: "## 待确认", columns: ["事项", "影响"] },
  {
    rel: "HANDOFF.md",
    section: "## 已证伪路线",
    columns: ["路线/假设", "证伪证据（一行）", "关闭日期", "复开条件"],
    optional: true,
  },
  { rel: "HANDOFF.md", section: "## 关键索引", columns: ["类型", "路径", "用途"] },
  {
    rel: "历史记录/00-历史总目录.md",
    section: null,
    columns: ["history-id", "日期", "标题", "路径", "状态"],
    uniqueFirstColumn: true,
  },
  {
    rel: "证据库/总索引/证据总目录.md",
    section: null,
    columns: ["evidence-id", "run_id", "task_id", "来源", "摘要", "路径", "采纳状态"],
    uniqueFirstColumn: true,
  },
  {
    rel: "项目物料/INDEX.md",
    section: null,
    columns: ["material-id", "路径", "hash", "来源", "用途", "状态"],
    uniqueFirstColumn: true,
  },
];

function inspectCoreStructure(root) {
  const collector = createStructureIssueCollector();
  const checked = [];
  for (const contract of CORE_SECTION_CONTRACTS) {
    const abs = path.join(root, contract.rel);
    if (!fs.existsSync(abs) || !fs.statSync(abs).isFile()) continue;
    const before = collector.count;
    const result = inspectSectionContract(readText(abs), contract, collector);
    checked.push({
      kind: "section",
      rel: contract.rel,
      section: contract.section,
      present: result.present,
      ok: collector.count === before,
    });
  }
  for (const contract of CORE_TABLE_CONTRACTS) {
    const abs = path.join(root, contract.rel);
    if (!fs.existsSync(abs) || !fs.statSync(abs).isFile()) continue;
    const before = collector.count;
    const result = inspectTableContract(readText(abs), contract, collector);
    checked.push({
      kind: "table",
      rel: contract.rel,
      section: contract.section,
      ok: collector.count === before,
      columns: result.columns,
      table_count: result.table_count,
    });
  }
  return {
    ok: collector.count === 0,
    checked,
    issues: collector.issues,
    issue_count: collector.count,
    issues_truncated: collector.truncated,
    not_checked: [
      "business_semantics",
      "material_hash_truth_unless_verify_materials_command_is_run",
      "legacy_migration_completeness",
    ],
    coverage_scope: {
      core_files: [...FIVE_PIECE, ...INDEX_FILES],
      required_sections: CORE_SECTION_CONTRACTS.map((item) => `${item.rel}:${item.section}`),
      core_tables: CORE_TABLE_CONTRACTS.map((item) => `${item.rel}:${item.section || "root"}`),
      markdown_scan_limit: MARKDOWN_SCAN_LIMIT,
    },
  };
}

function inspectSectionContract(text, contract, collector) {
  const visible = visibleMarkdownLines(text);
  const headings = visible
    .map((line, index) => ({ line: line.trim(), index }))
    .filter((item) => item.line === contract.section);
  if (headings.length === 0) {
    recordStructureIssue(collector, structureIssue("section_missing", contract, null, "required_section_missing"));
  } else if (headings.length > 1) {
    recordStructureIssue(collector, structureIssue("section_duplicate", contract, headings[1].index + 1, "section_must_be_unique"));
  }
  return { present: headings.length > 0 };
}

function inspectTableContract(text, contract, collector) {
  const visible = visibleMarkdownLines(text);
  let start = 0;
  let end = visible.length;

  if (contract.section) {
    const headings = visible
      .map((line, index) => ({ line: line.trim(), index }))
      .filter((item) => item.line === contract.section);
    if (headings.length === 0) {
      if (!contract.optional) {
        recordStructureIssue(collector, structureIssue("section_missing", contract, null, "required_section_missing"));
      }
      return { columns: [], table_count: 0 };
    }
    if (headings.length > 1) {
      recordStructureIssue(collector, structureIssue("section_duplicate", contract, headings[1].index + 1, "section_must_be_unique"));
      return { columns: [], table_count: 0 };
    }
    start = headings[0].index + 1;
    const nextHeadingOffset = visible.slice(start).findIndex((line) => /^##\s+/.test(line.trim()));
    end = nextHeadingOffset === -1 ? visible.length : start + nextHeadingOffset;
  }

  const candidates = findContractTableHeaders(visible, start, end, contract);
  if (candidates.length === 0) {
    recordStructureIssue(collector, structureIssue("table_missing", contract, null, "required_table_missing"));
    return { columns: [], table_count: 0 };
  }
  if (candidates.length > 1) {
    recordStructureIssue(collector, structureIssue(
      "table_ambiguous",
      contract,
      candidates[1].index + 1,
      `contract_table_count:${candidates.length}`,
    ));
  }

  const seenFirstColumn = new Map();
  let firstColumns = [];
  for (const candidate of candidates) {
    const result = inspectContractTableAt(visible, candidate.index, end, contract, collector, seenFirstColumn);
    if (firstColumns.length === 0) firstColumns = result.columns;
  }
  return { columns: firstColumns, table_count: candidates.length };
}

function inspectContractTableAt(lines, headerIndex, end, contract, collector, seenFirstColumn) {
  const headerCells = splitMarkdownTableRow(lines[headerIndex]).map(normalizeTableHeader);
  const separatorIndex = headerIndex + 1;
  const separatorCells = separatorIndex < end && isMarkdownTableRow(lines[separatorIndex])
    ? splitMarkdownTableRow(lines[separatorIndex]).map((cell) => cell.trim())
    : [];
  const separatorValid = separatorCells.length === headerCells.length
    && separatorCells.every((cell) => /^:?-{3,}:?$/.test(cell));
  if (!separatorValid) {
    recordStructureIssue(collector, structureIssue("separator_invalid", contract, separatorIndex + 1, "table_separator_must_follow_header"));
    return { columns: headerCells };
  }

  const missingColumns = contract.columns.filter((column) => !headerCells.includes(column));
  if (missingColumns.length > 0) {
    recordStructureIssue(collector, structureIssue("columns_missing", contract, headerIndex + 1, `missing:${missingColumns.join(",")}`));
  }
  const duplicateColumns = contract.columns.filter(
    (column) => headerCells.filter((cell) => cell === column).length > 1,
  );
  if (duplicateColumns.length > 0) {
    recordStructureIssue(collector, structureIssue("columns_duplicate", contract, headerIndex + 1, `duplicate:${duplicateColumns.join(",")}`));
  }

  let cursor = separatorIndex + 1;
  while (cursor < end && isMarkdownTableRow(lines[cursor])) {
    const cells = splitMarkdownTableRow(lines[cursor]).map(normalizeTableCell);
    if (cells.length !== headerCells.length) {
      recordStructureIssue(collector, structureIssue("row_width_mismatch", contract, cursor + 1, `${cells.length}/${headerCells.length}`));
    } else {
      if (contract.uniqueFirstColumn) {
        const uniqueColumn = contract.columns[0];
        const uniqueColumnIndex = headerCells.indexOf(uniqueColumn);
        const value = uniqueColumnIndex === -1 ? "" : cells[uniqueColumnIndex];
        if (value) {
          if (seenFirstColumn.has(value)) {
            recordStructureIssue(collector, structureIssue(
              "duplicate_id",
              contract,
              cursor + 1,
              `${value}:first_seen_line:${seenFirstColumn.get(value)}`,
            ));
          } else {
            seenFirstColumn.set(value, cursor + 1);
          }
        }
      }
      for (const [column, allowed] of Object.entries(contract.enums || {})) {
        const columnIndex = headerCells.indexOf(column);
        if (columnIndex !== -1 && !allowed.includes(cells[columnIndex])) {
          recordStructureIssue(collector, structureIssue(
            "value_invalid",
            contract,
            cursor + 1,
            `${column}:${cells[columnIndex] || "empty"}`,
          ));
        }
      }
    }
    cursor += 1;
  }
  const laterTableOffset = lines.slice(cursor, end).findIndex(isMarkdownTableRow);
  if (laterTableOffset !== -1) {
    const laterIndex = cursor + laterTableOffset;
    const laterStartsNewTable = laterIndex + 1 < end && isMarkdownSeparatorRow(lines[laterIndex + 1]);
    if (!laterStartsNewTable) {
      recordStructureIssue(collector, structureIssue(
        "table_discontinuous",
        contract,
        laterIndex + 1,
        "table_rows_must_be_contiguous",
      ));
    }
  }
  return { columns: headerCells };
}

function findContractTableHeaders(lines, start, end, contract) {
  const candidates = [];
  for (let index = start; index < end; index += 1) {
    if (!isMarkdownTableRow(lines[index])) continue;
    const cells = splitMarkdownTableRow(lines[index]).map(normalizeTableHeader);
    const nextIsSeparator = index + 1 < end && isMarkdownSeparatorRow(lines[index + 1]);
    if (!nextIsSeparator) continue;
    const score = contract.columns.filter((column) => cells.includes(column)).length;
    candidates.push({ index, cells, nextIsSeparator, score });
  }
  if (candidates.length === 0) return [];
  const primary = contract.columns[0];
  const primaryMatches = candidates.filter((item) => item.cells.includes(primary));
  if (primaryMatches.length > 0) return primaryMatches;
  const best = [...candidates].sort((left, right) => right.score - left.score || left.index - right.index)[0];
  return best && best.score > 0 ? [best] : [];
}

function structureIssue(kind, contract, line, detail) {
  const sectionKey = contract.section ? contract.section.replace(/^##\s+/, "") : "root";
  return {
    code: `structure_${kind}:${contract.rel}:${sectionKey}`,
    rel: contract.rel,
    section: contract.section,
    line,
    detail: limitText(detail, MAX_STRUCTURE_DETAIL_CHARS),
  };
}

function createStructureIssueCollector() {
  return { issues: [], count: 0, truncated: false };
}

function recordStructureIssue(collector, issue) {
  collector.count += 1;
  if (collector.issues.length < MAX_STRUCTURE_ISSUES) {
    collector.issues.push(issue);
  } else {
    collector.truncated = true;
  }
}

function visibleMarkdownLines(text) {
  const state = { htmlComment: false, fence: null };
  return text.split(/\r?\n/).map((source) => {
    const line = stripHtmlComments(source, state);
    const fenceMatch = line.match(/^\s*(`{3,}|~{3,})/);
    if (state.fence) {
      if (fenceMatch && fenceMatch[1][0] === state.fence) state.fence = null;
      return "";
    }
    if (fenceMatch) {
      state.fence = fenceMatch[1][0];
      return "";
    }
    return line;
  });
}

function stripHtmlComments(source, state) {
  let line = source;
  let result = "";
  while (line.length > 0) {
    if (state.htmlComment) {
      const close = line.indexOf("-->");
      if (close === -1) return result;
      state.htmlComment = false;
      line = line.slice(close + 3);
      continue;
    }
    const open = line.indexOf("<!--");
    if (open === -1) return result + line;
    result += line.slice(0, open);
    state.htmlComment = true;
    line = line.slice(open + 4);
  }
  return result;
}

function isMarkdownTableRow(line) {
  const trimmed = String(line || "").trim();
  return trimmed.startsWith("|") && trimmed.endsWith("|") && splitMarkdownTableRow(trimmed).length >= 2;
}

function isMarkdownSeparatorRow(line) {
  if (!isMarkdownTableRow(line)) return false;
  const cells = splitMarkdownTableRow(line).map((cell) => cell.trim());
  return cells.length >= 2 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
}

function splitMarkdownTableRow(line) {
  const trimmed = String(line || "").trim().replace(/^\|/, "").replace(/\|$/, "");
  const cells = [];
  let current = "";
  let escaped = false;
  for (const character of trimmed) {
    if (escaped) {
      current += character;
      escaped = false;
    } else if (character === "\\") {
      current += character;
      escaped = true;
    } else if (character === "|") {
      cells.push(current);
      current = "";
    } else {
      current += character;
    }
  }
  cells.push(current);
  return cells;
}

function normalizeTableCell(value) {
  return String(value || "").trim().replace(/^[`*_]+|[`*_]+$/g, "").trim();
}

function normalizeMarkdownCodeCellLiteral(value) {
  const trimmed = String(value || "").trim();
  const match = trimmed.match(/^(`+)([\s\S]*?)\1$/);
  if (!match) return trimmed;
  let literal = match[2];
  if (
    literal.startsWith(" ")
    && literal.endsWith(" ")
    && /[^ ]/.test(literal)
  ) {
    literal = literal.slice(1, -1);
  }
  return literal;
}

function normalizeTableHeader(value) {
  const normalized = normalizeTableCell(value);
  const lookup = normalized.replace(/[A-Z]/g, (character) => character.toLowerCase());
  return TABLE_HEADER_ALIASES.get(lookup) || lookup;
}

function inspectLegacyRootLayout(root) {
  const rootNumberedMarkdown = fs.readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isFile() && /^\d{2,3}-.*\.md$/i.test(entry.name))
    .map((entry) => entry.name)
    .sort();
  return {
    root_numbered_markdown_count: rootNumberedMarkdown.length,
    root_numbered_markdown_sample: rootNumberedMarkdown.slice(0, MAX_PHYSICAL_LAYOUT_SAMPLES),
    interpretation: "shallow_inventory_only_semantic_judgment_required",
  };
}

function inspectProject(root) {
  const coreFiles = [...FIVE_PIECE, ...INDEX_FILES];
  assertManagedCorePathsNotRedirected(root);
  const fileRecords = coreFiles.map((rel) => inspectFile(root, rel));
  const fiveRecords = fileRecords.slice(0, FIVE_PIECE.length);
  const indexRecords = fileRecords.slice(FIVE_PIECE.length);

  const fiveTotal = fiveRecords.reduce((sum, item) => sum + (item.exists ? item.bytes : 0), 0);
  const markdownScan = listMarkdownFiles(root);
  const idData = collectIds(root, markdownScan.files, fileRecords);
  const references = checkReferences(root, idData);
  const placeholders = scanPlaceholders(root, fileRecords);
  const semanticDeclaration = inspectHandoffSemanticDeclaration(root);
  const governanceSections = checkGovernanceSections(root);
  const structure = inspectCoreStructure(root);

  const missingFive = fiveRecords.filter((item) => !item.exists).map((item) => item.rel);
  const missingIndexes = indexRecords.filter((item) => !item.exists).map((item) => item.rel);
  const errors = [];
  if (missingFive.length > 0) errors.push("missing_five_piece_file");
  if (missingIndexes.length > 0) errors.push("missing_index_file");
  if (fiveTotal > FIVE_PIECE_LIMIT_BYTES) errors.push("five_piece_over_45kb");
  if (references.unresolved.length > 0) errors.push("unresolved_references");
  if (idData.summary.definition_collisions.length > 0) errors.push("definition_id_collision");
  if (placeholders.length > 0) errors.push("template_placeholder_found");
  errors.push(...semanticDeclaration.errors);
  errors.push(...structure.issues.map((item) => item.code));
  errors.push(...markdownScanErrors(markdownScan));
  const remainingBytes = FIVE_PIECE_LIMIT_BYTES - fiveTotal;
  const warnings = [...governanceSections.warnings];
  if (remainingBytes >= 0 && remainingBytes < FIVE_PIECE_LOW_SPACE_BYTES) {
    warnings.push("five_piece_remaining_below_2kib");
  }

  return {
    ok: errors.length === 0,
    mechanical_ok: errors.length === 0,
    validation_kind: "mechanical",
    semantic_checked_by_tool: false,
    tool: SCRIPT_NAME,
    command: "inspect",
    skill_version: SKILL_VERSION,
    project_structure_version: PROJECT_STRUCTURE_VERSION,
    root,
    generated_at: new Date().toISOString(),
    threshold: {
      five_piece_limit_bytes: FIVE_PIECE_LIMIT_BYTES,
      label: "45 KiB (46,080 bytes)",
      low_space_warning_bytes: FIVE_PIECE_LOW_SPACE_BYTES,
    },
    files: {
      five_piece: {
        all_present: missingFive.length === 0,
        missing: missingFive,
        records: fiveRecords,
      },
      indexes: {
        all_present: missingIndexes.length === 0,
        missing: missingIndexes,
        records: indexRecords,
      },
    },
    five_piece: {
      total_bytes: fiveTotal,
      over_limit: fiveTotal > FIVE_PIECE_LIMIT_BYTES,
      remaining_bytes: remainingBytes,
    },
    markdown_scan: markdownScan.summary,
    ids: idData.summary,
    references,
    placeholders,
    semantic_declaration: semanticDeclaration,
    governance_sections: governanceSections.present,
    structure,
    warnings: [...new Set(warnings)],
    errors: [...new Set(errors)],
  };
}

function inspectFile(root, rel) {
  const abs = path.join(root, rel);
  if (!fs.existsSync(abs)) {
    return { rel, exists: false, bytes: 0, sha256: null };
  }
  const buffer = fs.readFileSync(abs);
  return {
    rel,
    exists: true,
    bytes: buffer.length,
    sha256: sha256(buffer),
  };
}

function inspectHandoffSemanticDeclaration(root) {
  const rel = "HANDOFF.md";
  const text = readTextIfPresent(path.join(root, rel));
  const lines = text.split(/\r?\n/).map((line, index) => ({
    index,
    text: index === 0 ? line.replace(/^\uFEFF/, "").trimEnd() : line.trimEnd(),
  }));
  const nonBlank = lines.filter((item) => item.text.trim().length > 0);
  const sectionHeadings = lines.filter((item) => item.text === "## 语义检查点");
  const checkpointOccurrences = lines.filter((item) =>
    /^ {0,3}-\s+最后语义检查点：/.test(item.text),
  );
  const changeOccurrences = lines.filter((item) =>
    /^ {0,3}-\s+检查点后变化：/.test(item.text),
  );
  const errors = [];

  if (sectionHeadings.length === 0) errors.push("handoff_semantic_section_missing");
  if (sectionHeadings.length > 1) errors.push("handoff_semantic_section_duplicate");

  let lastSemanticCheckpoint = null;
  let changesAfterCheckpoint = null;

  const canonicalHeading =
    nonBlank[0]?.text === "# HANDOFF.md" && nonBlank[1]?.text === "## 语义检查点";
  if (sectionHeadings.length === 1 && !canonicalHeading) {
    errors.push("handoff_semantic_section_not_at_top");
  }

  const canonicalCheckpointMatch = nonBlank[2]?.text.match(/^-\s+最后语义检查点：\s*(.*?)\s*$/);
  const canonicalChangeMatch = nonBlank[3]?.text.match(/^-\s+检查点后变化：\s*(.*?)\s*$/);

  if (checkpointOccurrences.length === 0) {
    errors.push("handoff_last_semantic_checkpoint_missing");
  } else if (checkpointOccurrences.length > 1) {
    errors.push("handoff_last_semantic_checkpoint_duplicate");
  } else if (checkpointOccurrences[0].index !== nonBlank[2]?.index) {
    errors.push("handoff_semantic_declaration_outside_section");
  } else if (!canonicalCheckpointMatch) {
    errors.push("handoff_semantic_declaration_not_canonical");
  } else {
    const value = canonicalCheckpointMatch[1]?.trim() || "";
    if (isValidSemanticCheckpoint(value)) {
      lastSemanticCheckpoint = value;
    } else {
      errors.push("handoff_last_semantic_checkpoint_invalid");
    }
  }

  if (changeOccurrences.length === 0) {
    errors.push("handoff_change_status_missing_or_invalid");
  } else if (changeOccurrences.length > 1) {
    errors.push("handoff_change_status_duplicate");
  } else if (changeOccurrences[0].index !== nonBlank[3]?.index) {
    errors.push("handoff_semantic_declaration_outside_section");
  } else if (!canonicalChangeMatch) {
    errors.push("handoff_semantic_declaration_not_canonical");
  } else {
    const value = canonicalChangeMatch[1]?.trim() || "";
    if (["已核对", "待确认"].includes(value)) {
      changesAfterCheckpoint = value;
    } else {
      errors.push("handoff_change_status_missing_or_invalid");
    }
  }

  return {
    rel,
    declarations_present: errors.length === 0,
    section_count: sectionHeadings.length,
    last_semantic_checkpoint: lastSemanticCheckpoint,
    changes_after_checkpoint: changesAfterCheckpoint,
    errors,
  };
}

function isValidSemanticCheckpoint(value) {
  const match = value.match(
    /^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}) (Z|UTC|[+-]\d{2}:\d{2}|[A-Za-z][A-Za-z0-9._+-]*(?:\/[A-Za-z0-9._+-]+)+)$/,
  );
  if (!match) return false;

  const [, yearText, monthText, dayText, hourText, minuteText, timezone] = match;
  const year = Number(yearText);
  const month = Number(monthText);
  const day = Number(dayText);
  const hour = Number(hourText);
  const minute = Number(minuteText);
  if (year < 1000 || !isValidCalendarDate(year, month, day) || hour > 23 || minute > 59) return false;

  if (/^[+-]/.test(timezone)) {
    const [, offsetHourText, offsetMinuteText] = timezone.match(/^[+-](\d{2}):(\d{2})$/) || [];
    const offsetHour = Number(offsetHourText);
    const offsetMinute = Number(offsetMinuteText);
    return offsetHour <= 14 && offsetMinute <= 59 && (offsetHour < 14 || offsetMinute === 0);
  }
  if (["Z", "UTC"].includes(timezone)) return true;

  try {
    new Intl.DateTimeFormat("en-US", { timeZone: timezone }).format();
    return true;
  } catch {
    return false;
  }
}

function listMarkdownFiles(root) {
  const results = [];
  const readErrors = [];
  let truncated = false;
  const skip = new Set([".git", "node_modules", ".project-gov"]);

  function walk(dir) {
    if (results.length >= MARKDOWN_SCAN_LIMIT) {
      truncated = true;
      return;
    }
    let entries = [];
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch (error) {
      readErrors.push({ rel: toRel(root, dir), code: error.code || "read_error" });
      return;
    }
    for (const entry of entries) {
      if (results.length >= MARKDOWN_SCAN_LIMIT) {
        truncated = true;
        return;
      }
      if (entry.isDirectory()) {
        if (skip.has(entry.name)) continue;
        walk(path.join(dir, entry.name));
      } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
        results.push(path.join(dir, entry.name));
      }
    }
  }

  walk(root);
  return {
    files: results,
    truncated,
    read_errors: readErrors,
    summary: {
      files_scanned: results.length,
      max_files: MARKDOWN_SCAN_LIMIT,
      truncated,
      read_errors: readErrors,
    },
  };
}

function markdownScanErrors(scan) {
  const errors = [];
  if (scan.truncated) errors.push("markdown_scan_truncated");
  if (scan.read_errors.length > 0) errors.push("markdown_scan_read_error");
  return errors;
}

function collectIds(root, markdownFiles, coreRecords) {
  const all = [];
  const definitionFiles = new Map();

  for (const abs of markdownFiles) {
    const rel = toRel(root, abs);
    const text = readText(abs);
    for (const id of extractProjectIds(text, { markdown: true })) {
      all.push({ id, rel });
    }
    const basename = path.basename(rel);
    const fileId = extractProjectIds(basename)[0];
    if (fileId) {
      mapPush(definitionFiles, fileId, rel);
    }
  }

  const byPrefix = { M: [], EV: [], MAT: [] };
  for (const item of all) {
    const prefix = item.id.startsWith("EV-") ? "EV" : item.id.startsWith("MAT-") ? "MAT" : "M";
    byPrefix[prefix].push(item.id);
  }

  const definitionCollisions = [];
  for (const [id, rels] of definitionFiles.entries()) {
    const unique = [...new Set(rels)];
    if (unique.length > 1) {
      definitionCollisions.push({ id, files: unique });
    }
  }

  return {
    all,
    definitionFiles,
    summary: {
      occurrence_count: all.length,
      sample: all.slice(0, 10),
      counts: {
        M: new Set(byPrefix.M).size,
        EV: new Set(byPrefix.EV).size,
        MAT: new Set(byPrefix.MAT).size,
      },
      max: {
        M: maxId(byPrefix.M),
        EV: maxId(byPrefix.EV),
        MAT: maxId(byPrefix.MAT),
      },
      definition_collisions: definitionCollisions,
    },
    coreRecords,
  };
}

function extractProjectIds(text, options = {}) {
  const source = options.markdown ? visibleMarkdownLines(String(text || "")).join("\n") : String(text || "");
  const regex = new RegExp(PROJECT_ID_REGEX_SOURCE, "g");
  const ids = [];
  let match;
  while ((match = regex.exec(source))) {
    ids.push(match[1]);
  }
  return ids;
}

function checkReferences(root, idData) {
  const unresolved = [];
  const uniqueIds = [...new Set(idData.all.map((item) => item.id))];
  const historyIds = new Set(
    extractProjectIds(readTextIfPresent(path.join(root, "历史记录/00-历史总目录.md")), { markdown: true }),
  );
  const evidenceIds = new Set(
    extractProjectIds(readTextIfPresent(path.join(root, "证据库/总索引/证据总目录.md")), { markdown: true }),
  );
  const materialIds = new Set(
    extractProjectIds(readTextIfPresent(path.join(root, "项目物料/INDEX.md")), { markdown: true }),
  );

  for (const id of uniqueIds) {
    let ok = false;
    if (id.startsWith("M-")) {
      ok = idData.definitionFiles.has(id) || historyIds.has(id);
    } else if (id.startsWith("EV-")) {
      ok = idData.definitionFiles.has(id) || evidenceIds.has(id);
    } else if (id.startsWith("MAT-")) {
      ok = materialIds.has(id);
    }
    if (!ok) unresolved.push({ id, reason: "no_definition_or_index_entry" });
  }

  return {
    unresolved,
    checked_id_count: uniqueIds.length,
  };
}

function scanPlaceholders(root, fileRecords) {
  const hits = [];
  for (const record of fileRecords.filter((item) => item.exists)) {
    const abs = path.join(root, record.rel);
    const lines = readText(abs).split(/\r?\n/);
    lines.forEach((line, index) => {
      if (PLACEHOLDER_PATTERNS.some((regex) => regex.test(line))) {
        hits.push({ rel: record.rel, line: index + 1 });
      }
    });
  }
  return hits;
}

function compilePlan(root, plan, report) {
  const violations = [];
  const warnings = [];
  const actions = Array.isArray(plan.actions) ? plan.actions : [];
  const planId = plan.plan_id || `plan_${Date.now()}`;

  if (plan.schema_version !== 1) violations.push("schema_version_must_be_1");
  if (!Array.isArray(plan.actions)) violations.push("actions_array_required");
  if (actions.length > MAX_ACTIONS) violations.push(`actions_exceed_limit_${MAX_ACTIONS}`);

  const compiledActions = [];
  const beforeHashes = {};
  const inMemory = new Map();
  for (const rel of FIVE_PIECE) {
    const abs = path.join(root, rel);
    if (fs.existsSync(abs)) inMemory.set(rel, readText(abs));
  }

  for (const [index, action] of actions.entries()) {
    const check = compileAction(root, action, index, inMemory);
    violations.push(...check.violations);
    warnings.push(...check.warnings);
    if (check.compiled && check.violations.length === 0) {
      compiledActions.push(check.compiled);
      for (const rel of check.touched) {
        if (!(rel in beforeHashes)) {
          const abs = path.join(root, rel);
          beforeHashes[rel] = pathFingerprint(abs);
        }
      }
    }
  }
  violations.push(...validateOrphanMkdirActions(root, compiledActions));

  const predictedFiveBytes = FIVE_PIECE.reduce((sum, rel) => {
    const text = inMemory.has(rel) ? inMemory.get(rel) : "";
    return sum + Buffer.byteLength(text, "utf8");
  }, 0);
  if (
    predictedFiveBytes > FIVE_PIECE_LIMIT_BYTES &&
    predictedFiveBytes >= report.five_piece.total_bytes
  ) {
    violations.push("predicted_five_piece_over_45kb_must_decrease");
  }
  const predictedRemainingBytes = FIVE_PIECE_LIMIT_BYTES - predictedFiveBytes;
  if (predictedRemainingBytes >= 0 && predictedRemainingBytes < FIVE_PIECE_LOW_SPACE_BYTES) {
    warnings.push("predicted_five_piece_remaining_below_2kib");
  }

  const compiled = {
    ok: violations.length === 0,
    tool: SCRIPT_NAME,
    command: "propose",
    compiled_schema_version: COMPILED_SCHEMA_VERSION,
    skill_version: SKILL_VERSION,
    compiled_at: new Date().toISOString(),
    root,
    plan_id: planId,
    before_hashes: beforeHashes,
    actions: compiledActions,
    predicted: {
      five_piece_total_bytes: predictedFiveBytes,
      over_45kb: predictedFiveBytes > FIVE_PIECE_LIMIT_BYTES,
      remaining_bytes: predictedRemainingBytes,
    },
    current: {
      five_piece_total_bytes: report.five_piece.total_bytes,
      over_45kb: report.five_piece.over_limit,
    },
    violations: [...new Set(violations)],
    warnings: [...new Set(warnings)],
  };

  return compiled;
}

function summarizeCompiledPlan(compiled, outPath, operationCleanup = null) {
  const actions = Array.isArray(compiled.actions) ? compiled.actions : [];
  const actionCounts = {};
  for (const action of actions) {
    actionCounts[action.kind] = (actionCounts[action.kind] || 0) + 1;
  }
  return {
    ok: compiled.ok,
    tool: compiled.tool,
    command: compiled.command,
    skill_version: compiled.skill_version,
    plan_id: compiled.plan_id,
    root: compiled.root,
    compiled_plan_path: outPath,
    operation_cleanup: operationCleanup,
    action_count: actions.length,
    action_counts: actionCounts,
    actions: actions.map((action) => ({ kind: action.kind, path: action.path })),
    predicted: compiled.predicted,
    current: compiled.current,
    violations: compiled.violations,
    warnings: operationCleanup?.ok === false
      ? [...new Set([...(compiled.warnings || []), `operation_cleanup_failed:${operationCleanup.error}`])]
      : compiled.warnings,
  };
}

function validateOrphanMkdirActions(root, actions) {
  const violations = [];
  for (const action of actions.filter((item) => item.kind === "mkdir")) {
    const abs = path.join(root, action.path);
    if (fs.existsSync(abs)) continue;
    const prefix = `${action.path}/`;
    const populatedByPlan = actions.some((item) => item.kind !== "mkdir" && item.path.startsWith(prefix));
    if (!populatedByPlan) violations.push(`orphan_mkdir_would_leave_empty_directory:${action.path}`);
  }
  return violations;
}

function compileAction(root, action, index, inMemory) {
  const violations = [];
  const warnings = [];
  const touched = [];
  const kind = action?.kind;
  const rel = action?.path;

  if (!kind || typeof kind !== "string") violations.push(`actions[${index}].kind_required`);
  if (!rel || typeof rel !== "string") violations.push(`actions[${index}].path_required`);
  if (violations.length > 0) return { violations, warnings, touched, compiled: null };

  const pathCheck = validateRelativePath(root, rel);
  if (!pathCheck.ok) violations.push(`actions[${index}].path_invalid:${pathCheck.error}`);
  if (pathCheck.ok && !isAllowedProjectPath(pathCheck.rel)) {
    const code = kind === "mkdir" && GOVERNANCE_ROOT_DIRECTORIES.includes(pathCheck.rel)
      ? "mkdir_top_level_governance_directory_not_allowed_use_index_file_or_subdirectory"
      : "path_not_allowed";
    violations.push(`actions[${index}].${code}`);
  }
  if (violations.length > 0) return { violations, warnings, touched, compiled: null };

  const normalizedRel = pathCheck.rel;
  touched.push(normalizedRel);

  if (kind === "mkdir") {
    const abs = path.join(root, normalizedRel);
    if (fs.existsSync(abs)) {
      if (!fs.statSync(abs).isDirectory()) {
        violations.push(`actions[${index}].mkdir_target_is_not_directory`);
      } else {
        warnings.push(`actions[${index}].directory_already_exists`);
      }
    }
    return {
      violations,
      warnings,
      touched,
      compiled: { kind, path: normalizedRel },
    };
  }

  if (kind === "write_file") {
    if (typeof action.content !== "string") violations.push(`actions[${index}].content_required`);
    if (utf8Bytes(action.content || "") > MAX_ACTION_TEXT_BYTES) {
      violations.push(`actions[${index}].content_exceeds_${MAX_ACTION_TEXT_BYTES}_bytes`);
    }
    if (hasPlaceholderContent(action.content || "")) violations.push(`actions[${index}].content_contains_placeholder`);
    const abs = path.join(root, normalizedRel);
    const exists = inMemory.has(normalizedRel) || fs.existsSync(abs);
    if (fs.existsSync(abs) && !fs.statSync(abs).isFile()) {
      violations.push(`actions[${index}].write_target_is_not_file`);
    }
    if (fs.existsSync(abs) && fs.statSync(abs).isFile() && fs.statSync(abs).size > MAX_MUTABLE_TEXT_FILE_BYTES) {
      violations.push(`actions[${index}].write_target_exceeds_${MAX_MUTABLE_TEXT_FILE_BYTES}_bytes`);
    }
    if (exists && action.overwrite !== true) violations.push(`actions[${index}].target_exists_without_overwrite`);
    if (violations.length === 0) inMemory.set(normalizedRel, ensureTrailingNewline(action.content || ""));
    return {
      violations,
      warnings,
      touched,
      compiled: { kind, path: normalizedRel, content: ensureTrailingNewline(action.content || ""), overwrite: action.overwrite === true },
    };
  }

  if (kind === "append_after") {
    if (typeof action.after !== "string") violations.push(`actions[${index}].after_required`);
    if (typeof action.content !== "string") violations.push(`actions[${index}].content_required`);
    if (utf8Bytes(action.after || "") > MAX_ANCHOR_TEXT_BYTES) {
      violations.push(`actions[${index}].after_exceeds_${MAX_ANCHOR_TEXT_BYTES}_bytes`);
    }
    if (utf8Bytes(action.content || "") > MAX_ACTION_TEXT_BYTES) {
      violations.push(`actions[${index}].content_exceeds_${MAX_ACTION_TEXT_BYTES}_bytes`);
    }
    if (hasPlaceholderContent(action.content || "")) violations.push(`actions[${index}].content_contains_placeholder`);
    const targetAbs = path.join(root, normalizedRel);
    if (!inMemory.has(normalizedRel) && (!fs.existsSync(targetAbs) || !fs.statSync(targetAbs).isFile())) {
      violations.push(`actions[${index}].append_target_is_not_file`);
    }
    if (fs.existsSync(targetAbs) && fs.statSync(targetAbs).isFile() && fs.statSync(targetAbs).size > MAX_MUTABLE_TEXT_FILE_BYTES) {
      violations.push(`actions[${index}].append_target_exceeds_${MAX_MUTABLE_TEXT_FILE_BYTES}_bytes`);
    }
    const existing = violations.length === 0 ? readForAction(root, normalizedRel, inMemory) : "";
    const after = action.after || "";
    const newline = preferredNewline(existing);
    const lines = existing.split(/\r?\n/);
    const matchMode = action.match === "contains" ? "contains" : "exact";
    const matches = lines
      .map((line, lineIndex) => ({ line, lineIndex }))
      .filter((item) => (matchMode === "contains" ? item.line.includes(after) : item.line === after));
    if (matches.length !== 1) violations.push(`actions[${index}].after_match_count_${matches.length}`);
    if (existing.includes(action.content || "")) warnings.push(`actions[${index}].content_already_present`);
    if (violations.length === 0) {
      const insertAt = matches[0].lineIndex + 1;
      const contentLines = ensureTrailingNewline(action.content).replace(/\r?\n$/, "").split(/\r?\n/);
      lines.splice(insertAt, 0, ...contentLines);
      const next = ensureTrailingNewlineWithStyle(lines.join(newline), newline);
      inMemory.set(normalizedRel, next);
    }
    return {
      violations,
      warnings,
      touched,
      compiled: { kind, path: normalizedRel, after, match: matchMode, content: ensureTrailingNewline(action.content || "") },
    };
  }

  if (kind === "replace_line_contains") {
    if (typeof action.contains !== "string") violations.push(`actions[${index}].contains_required`);
    if (typeof action.replacement !== "string") violations.push(`actions[${index}].replacement_required`);
    if (typeof action.replacement === "string" && /[\r\n]/.test(action.replacement)) {
      violations.push(`actions[${index}].replacement_must_be_single_line`);
    }
    if (utf8Bytes(action.contains || "") > MAX_ANCHOR_TEXT_BYTES) {
      violations.push(`actions[${index}].contains_exceeds_${MAX_ANCHOR_TEXT_BYTES}_bytes`);
    }
    if (utf8Bytes(action.replacement || "") > MAX_ACTION_TEXT_BYTES) {
      violations.push(`actions[${index}].replacement_exceeds_${MAX_ACTION_TEXT_BYTES}_bytes`);
    }
    if (hasPlaceholderContent(action.replacement || "")) violations.push(`actions[${index}].replacement_contains_placeholder`);
    const targetAbs = path.join(root, normalizedRel);
    if (!inMemory.has(normalizedRel) && (!fs.existsSync(targetAbs) || !fs.statSync(targetAbs).isFile())) {
      violations.push(`actions[${index}].replace_target_is_not_file`);
    }
    if (fs.existsSync(targetAbs) && fs.statSync(targetAbs).isFile() && fs.statSync(targetAbs).size > MAX_MUTABLE_TEXT_FILE_BYTES) {
      violations.push(`actions[${index}].replace_target_exceeds_${MAX_MUTABLE_TEXT_FILE_BYTES}_bytes`);
    }
    const existing = violations.length === 0 ? readForAction(root, normalizedRel, inMemory) : "";
    const newline = preferredNewline(existing);
    const lines = existing.split(/\r?\n/);
    const matches = lines
      .map((line, lineIndex) => ({ line, lineIndex }))
      .filter((item) => item.line.includes(action.contains || ""));
    if (matches.length !== 1) violations.push(`actions[${index}].contains_match_count_${matches.length}`);
    if (violations.length === 0) {
      lines[matches[0].lineIndex] = action.replacement;
      const next = ensureTrailingNewlineWithStyle(lines.join(newline), newline);
      inMemory.set(normalizedRel, next);
    }
    return {
      violations,
      warnings,
      touched,
      compiled: { kind, path: normalizedRel, contains: action.contains, replacement: action.replacement },
    };
  }

  if (kind === "replace_block_exact") {
    if (typeof action.old_block !== "string" || action.old_block.length === 0) {
      violations.push(`actions[${index}].old_block_required`);
    }
    if (typeof action.replacement !== "string") violations.push(`actions[${index}].replacement_required`);
    if (utf8Bytes(action.old_block || "") > MAX_ACTION_TEXT_BYTES) {
      violations.push(`actions[${index}].old_block_exceeds_${MAX_ACTION_TEXT_BYTES}_bytes`);
    }
    if (utf8Bytes(action.replacement || "") > MAX_ACTION_TEXT_BYTES) {
      violations.push(`actions[${index}].replacement_exceeds_${MAX_ACTION_TEXT_BYTES}_bytes`);
    }
    if (hasPlaceholderContent(action.replacement || "")) {
      violations.push(`actions[${index}].replacement_contains_placeholder`);
    }
    const targetAbs = path.join(root, normalizedRel);
    if (!inMemory.has(normalizedRel) && (!fs.existsSync(targetAbs) || !fs.statSync(targetAbs).isFile())) {
      violations.push(`actions[${index}].replace_target_is_not_file`);
    }
    if (fs.existsSync(targetAbs) && fs.statSync(targetAbs).isFile() && fs.statSync(targetAbs).size > MAX_MUTABLE_TEXT_FILE_BYTES) {
      violations.push(`actions[${index}].replace_target_exceeds_${MAX_MUTABLE_TEXT_FILE_BYTES}_bytes`);
    }
    const existing = violations.length === 0 ? readForAction(root, normalizedRel, inMemory) : "";
    const replacement = replaceBlockExactResult(existing, action.old_block || "", action.replacement || "");
    if (violations.length === 0 && replacement.match_count !== 1) {
      violations.push(`actions[${index}].old_block_match_count_${replacement.match_count}`);
    }
    if (violations.length === 0) inMemory.set(normalizedRel, replacement.next);
    return {
      violations,
      warnings,
      touched,
      compiled: {
        kind,
        path: normalizedRel,
        old_block: action.old_block,
        replacement: action.replacement,
      },
    };
  }

  violations.push(`actions[${index}].unknown_kind:${kind}`);
  return { violations, warnings, touched, compiled: null };
}

function applyCompiledPlan(compiled) {
  assertCompiledPlanVersion(compiled);
  const root = resolveRoot(compiled?.root);
  assertManagedCorePathsNotRedirected(root);
  assertTransactionBackupBaseSafe(root);
  const lock = acquireApplyLock(root, compiled?.plan_id);
  let result;
  let operationError = null;
  try {
    result = applyCompiledPlanLocked(root, compiled);
  } catch (error) {
    operationError = error;
  }

  const lockCleanup = releaseOwnedLock(lock);
  if (operationError) {
    if (!lockCleanup.ok) {
      operationError.message = `${operationError.message}; apply lock cleanup failed: ${lockCleanup.error}`;
    }
    throw operationError;
  }

  if (!lockCleanup.ok || lockCleanup.warnings.length > 0) {
    const warning = lockCleanup.ok
      ? `apply_lock_cleanup_fallback:${lockCleanup.warnings.join(" | ")}`
      : `apply_lock_cleanup_failed:${lockCleanup.error}`;
    return {
      ...result,
      lock_cleanup: lockCleanup,
      warnings: [...new Set([...(result.warnings || []), warning])],
    };
  }
  return result;
}

function assertCompiledPlanVersion(compiled) {
  const schemaVersion = compiled?.compiled_schema_version;
  const skillVersion = compiled?.skill_version;
  if (schemaVersion !== COMPILED_SCHEMA_VERSION || skillVersion !== SKILL_VERSION) {
    fail(
      `Compiled plan version incompatible: expected schema ${COMPILED_SCHEMA_VERSION} and skill ${SKILL_VERSION}; received schema ${String(schemaVersion ?? "missing")} and skill ${String(skillVersion ?? "missing")}. Run propose again.`,
      2,
    );
  }
}

function applyCompiledPlanLocked(root, compiled) {
  const preflight = preflightCompiledPlan(root, compiled);
  if (preflight.violations.length > 0) {
    fail(`Compiled plan failed apply preflight: ${preflight.violations.join(", ")}`, 2);
  }

  const beforeHashes = compiled.before_hashes;
  for (const rel of preflight.touched) {
    const actualFingerprint = pathFingerprint(path.join(root, rel));
    if (actualFingerprint !== beforeHashes[rel]) {
      fail(`Hash precondition failed for ${rel}`, 3);
    }
  }

  const backupRoot = path.join(
    root,
    ".project-gov",
    "backups",
    `${sanitizeName(compiled.plan_id || "plan")}_${Date.now()}`,
  );
  const changed = [];
  const unchanged = [];
  const backups = [];
  const originalStates = new Map();
  const createdDirectories = [];
  let backupBaseCreatedByTransaction = false;
  let backupRootCreatedByTransaction = false;

  try {
    const backupBase = path.dirname(backupRoot);
    assertTransactionBackupBaseSafe(root);
    if (!fs.existsSync(backupBase)) {
      fs.mkdirSync(backupBase);
      backupBaseCreatedByTransaction = true;
    }
    assertTransactionBackupBaseSafe(root);
    fs.mkdirSync(backupRoot);
    backupRootCreatedByTransaction = true;
    writeAtomic(path.join(backupRoot, BACKUP_OWNER_FILE), `${JSON.stringify({
      schema_version: 1,
      tool: SCRIPT_NAME,
      kind: "transaction_backup",
      root,
      plan_id: String(compiled.plan_id || "unknown"),
      created_at: new Date().toISOString(),
    }, null, 2)}\n`);
    for (const rel of preflight.touched) {
      const abs = path.join(root, rel);
      const state = describePath(abs);
      originalStates.set(rel, state);
      if (state.kind === "file") {
        const backupPath = path.join(backupRoot, rel);
        fs.mkdirSync(path.dirname(backupPath), { recursive: true });
        fs.copyFileSync(abs, backupPath);
        backups.push(toRel(root, backupPath));
      }
    }

    for (const action of preflight.actions) {
      const rel = action.path;
      const abs = path.join(root, rel);

      if (action.kind === "mkdir") {
        if (fs.existsSync(abs)) {
          unchanged.push(rel);
        } else {
          createdDirectories.push(...createDirectoryTracked(root, abs));
          changed.push(rel);
        }
        continue;
      }

      if (action.kind === "write_file") {
        if (fs.existsSync(abs) && action.overwrite !== true) fail(`Refusing to overwrite ${rel}`, 3);
        createdDirectories.push(...createDirectoryTracked(root, path.dirname(abs)));
        writeAtomic(abs, ensureTrailingNewline(action.content || ""));
        changed.push(rel);
        continue;
      }

      if (action.kind === "append_after") {
        const next = applyAppendAfter(readText(abs), action);
        writeAtomic(abs, next);
        changed.push(rel);
        continue;
      }

      if (action.kind === "replace_line_contains") {
        const next = applyReplaceLineContains(readText(abs), action);
        writeAtomic(abs, next);
        changed.push(rel);
        continue;
      }

      if (action.kind === "replace_block_exact") {
        const next = applyReplaceBlockExact(readText(abs), action);
        writeAtomic(abs, next);
        changed.push(rel);
        continue;
      }

      fail(`Unknown action kind during apply: ${action.kind}`, 3);
    }

    const validation = inspectProject(root);
    if (!validation.ok) {
      throw new Error(`Post-apply validation failed: ${validation.errors.join(", ")}`);
    }

    const backupCleanup = cleanupTransactionBackup(root, backupRoot, {
      backupBaseCreatedByTransaction,
      backupRootCreatedByTransaction,
    });
    return {
      ok: true,
      tool: SCRIPT_NAME,
      command: "apply",
      root,
      plan_id: compiled.plan_id,
      changed: [...new Set(changed)],
      unchanged: [...new Set(unchanged)],
      backups_retained: backupCleanup.ok ? [] : backups,
      backup_cleanup: backupCleanup,
      warnings: backupCleanup.ok ? [] : [`transaction_backup_cleanup_failed:${backupCleanup.error}`],
      rolled_back: false,
      validation: validationSummary(validation),
    };
  } catch (error) {
    const rollback = rollbackChanges(root, originalStates, backupRoot, changed, createdDirectories);
    const validation = inspectProject(root);
    const backupCleanup = rollback.ok
      ? cleanupTransactionBackup(root, backupRoot, {
        backupBaseCreatedByTransaction,
        backupRootCreatedByTransaction,
      })
      : { ok: false, removed: false, retained: true, error: "rollback_incomplete_backup_retained" };
    return {
      ok: false,
      tool: SCRIPT_NAME,
      command: "apply",
      root,
      plan_id: compiled.plan_id,
      error: error.message || String(error),
      changed_before_rollback: [...new Set(changed)],
      backups_retained: backupCleanup.ok ? [] : backups,
      backup_cleanup: backupCleanup,
      warnings: backupCleanup.ok ? [] : [`transaction_backup_retained:${backupCleanup.error}`],
      rolled_back: rollback.ok,
      rollback_errors: rollback.errors,
      validation: validationSummary(validation),
    };
  }
}

function acquireApplyLock(root, planId) {
  const governanceRoot = path.join(root, ".project-gov");
  const createdParent = !fs.existsSync(governanceRoot);
  fs.mkdirSync(governanceRoot, { recursive: true });
  const realRoot = fs.realpathSync.native(root);
  const realGovernanceRoot = fs.realpathSync.native(governanceRoot);
  if (!isPathInside(realRoot, realGovernanceRoot)) {
    fail(`Apply lock directory escapes the project through a symlink or junction: ${governanceRoot}`, 4);
  }
  const expectedRealGovernanceRoot = path.resolve(realRoot, path.relative(root, governanceRoot));
  if (!sameResolvedPath(realGovernanceRoot, expectedRealGovernanceRoot)) {
    fail(`Apply lock directory is redirected through a symlink or junction: ${governanceRoot}`, 4);
  }
  const lockPath = path.join(governanceRoot, "apply.lock");
  const owner = {
    owner_id: crypto.randomUUID(),
    pid: process.pid,
    plan_id: String(planId || "unknown"),
    created_at: new Date().toISOString(),
  };

  for (let attempt = 0; attempt < 4; attempt += 1) {
    try {
      createOwnedJsonLock(lockPath, owner);
      return { path: lockPath, owner_id: owner.owner_id, cleanup_empty_parent: createdParent, governanceRoot };
    } catch (error) {
      if (error.code !== "EEXIST") throw error;
    }

    const existing = readOwnedLock(lockPath, true);
    if (!existing) continue;
    if (!isReclaimableApplyLock(existing)) {
      fail(`Apply lock is active: ${lockPath} (pid ${existing.pid}, created ${existing.created_at})`, 4);
    }

    const reclaimPath = path.join(governanceRoot, "apply.lock.reclaim");
    const reclaimOwner = {
      owner_id: crypto.randomUUID(),
      pid: process.pid,
      plan_id: owner.plan_id,
      created_at: new Date().toISOString(),
      purpose: "stale-apply-lock-reclaim",
    };
    try {
      createOwnedJsonLock(reclaimPath, reclaimOwner);
    } catch (error) {
      if (error.code === "EEXIST") fail(`Apply lock reclamation is already in progress: ${reclaimPath}`, 4);
      throw error;
    }

    try {
      const current = readOwnedLock(lockPath, true);
      if (!current) continue;
      if (!isReclaimableApplyLock(current)) {
        fail(`Apply lock became active during stale check: ${lockPath}`, 4);
      }
      const stalePath = `${lockPath}.stale`;
      try {
        fs.renameSync(lockPath, stalePath);
      } catch (error) {
        if (error.code !== "ENOENT") throw error;
      }
    } finally {
      const reclaimCleanup = releaseOwnedLock({ path: reclaimPath, owner_id: reclaimOwner.owner_id });
      if (!reclaimCleanup.ok) {
        fail(`Failed to release apply lock reclamation guard: ${reclaimCleanup.error}`, 4);
      }
    }
  }

  fail(`Could not acquire apply lock after stale-lock retries: ${lockPath}`, 4);
}

function createOwnedJsonLock(lockPath, owner) {
  let fd;
  let created = false;
  try {
    fd = fs.openSync(lockPath, "wx", 0o600);
    created = true;
    fs.writeFileSync(fd, `${JSON.stringify(owner, null, 2)}\n`, "utf8");
    fs.fsyncSync(fd);
  } catch (error) {
    if (fd !== undefined) fs.closeSync(fd);
    fd = undefined;
    if (created && fs.existsSync(lockPath)) fs.unlinkSync(lockPath);
    throw error;
  } finally {
    if (fd !== undefined) fs.closeSync(fd);
  }
}

function readOwnedLock(lockPath, allowMissing = false) {
  let raw;
  try {
    raw = fs.readFileSync(lockPath, "utf8");
  } catch (error) {
    if (allowMissing && error.code === "ENOENT") return null;
    throw error;
  }

  let lock;
  try {
    lock = JSON.parse(raw);
  } catch {
    fail(`Existing lock cannot be validated and will not be removed: ${lockPath}`, 4);
  }
  const createdAt = Date.parse(lock?.created_at);
  if (
    !isPlainObject(lock)
    || !isNonEmptyString(lock.owner_id)
    || !Number.isInteger(lock.pid)
    || lock.pid <= 0
    || !isNonEmptyString(lock.plan_id)
    || !Number.isFinite(createdAt)
  ) {
    fail(`Existing lock metadata is invalid and will not be removed: ${lockPath}`, 4);
  }
  return lock;
}

function isReclaimableApplyLock(lock) {
  return !isPidAlive(lock.pid);
}

function isPidAlive(pid) {
  try {
    process.kill(pid, 0);
    return true;
  } catch (error) {
    return error.code !== "ESRCH";
  }
}

function releaseOwnedLock(lock) {
  const result = {
    ok: true,
    released: false,
    method: "not_acquired",
    warnings: [],
  };
  if (!lock) return result;

  try {
    if (!fs.existsSync(lock.path)) {
      return { ...result, released: true, method: "already_missing" };
    }
    const current = readOwnedLock(lock.path, true);
    if (!current) return { ...result, released: true, method: "already_missing" };
    if (current.owner_id !== lock.owner_id) {
      return {
        ...result,
        ok: false,
        method: "owner_mismatch",
        error: `Lock owner changed before cleanup: ${lock.path}`,
      };
    }

    try {
      fs.unlinkSync(lock.path);
      result.released = true;
      result.method = "unlink";
    } catch (unlinkError) {
      if (unlinkError.code === "ENOENT" || !fs.existsSync(lock.path)) {
        result.released = true;
        result.method = "already_missing";
      } else {
        const releasedPath = `${lock.path}.released`;
        try {
          fs.renameSync(lock.path, releasedPath);
          result.released = true;
          result.method = "rename_fallback";
          result.warnings.push(`unlink_failed:${formatFsError(unlinkError)}`);
        } catch (renameError) {
          return {
            ...result,
            ok: false,
            method: "release_failed",
            error: `unlink=${formatFsError(unlinkError)}; rename=${formatFsError(renameError)}`,
          };
        }
      }
    }

    if (lock.cleanup_empty_parent) {
      try {
        fs.rmdirSync(lock.governanceRoot);
      } catch (error) {
        if (!["ENOENT", "ENOTEMPTY", "EEXIST"].includes(error.code)) {
          result.warnings.push(`empty_lock_parent_cleanup_failed:${formatFsError(error)}`);
        }
      }
    }
    return result;
  } catch (error) {
    return {
      ...result,
      ok: false,
      method: "release_failed",
      error: formatFsError(error),
    };
  }
}

function formatFsError(error) {
  const code = error?.code ? `${error.code}:` : "";
  return `${code}${error?.message || String(error)}`;
}

function preflightCompiledPlan(root, compiled) {
  const violations = [];
  const actions = Array.isArray(compiled?.actions) ? compiled.actions : [];
  if (!compiled || compiled.tool !== SCRIPT_NAME || compiled.command !== "propose") {
    violations.push("compiled_plan_origin_invalid");
  }
  if (compiled?.compiled_schema_version !== COMPILED_SCHEMA_VERSION) {
    violations.push(`compiled_schema_version_must_be_${COMPILED_SCHEMA_VERSION}`);
  }
  if (compiled?.skill_version !== SKILL_VERSION) violations.push("compiled_skill_version_mismatch");
  if (compiled?.ok !== true) violations.push("compiled_plan_not_ok");
  if (!Array.isArray(compiled?.actions)) violations.push("compiled_actions_array_required");
  if (actions.length > MAX_ACTIONS) violations.push(`compiled_actions_exceed_limit_${MAX_ACTIONS}`);
  if (!compiled?.before_hashes || Array.isArray(compiled.before_hashes) || typeof compiled.before_hashes !== "object") {
    violations.push("compiled_before_hashes_object_required");
  }
  if (!Array.isArray(compiled?.violations)) violations.push("compiled_violations_array_required");
  if (Array.isArray(compiled?.violations) && compiled.violations.length > 0) {
    violations.push("compiled_plan_contains_violations");
  }
  const inMemory = new Map();
  for (const rel of FIVE_PIECE) {
    const abs = path.join(root, rel);
    if (fs.existsSync(abs)) inMemory.set(rel, readText(abs));
  }

  const currentFiveBytes = [...inMemory.values()].reduce(
    (sum, text) => sum + Buffer.byteLength(text, "utf8"),
    0,
  );
  const canonicalActions = [];
  const touched = new Set();
  for (const [index, action] of actions.entries()) {
    const check = compileAction(root, action, index, inMemory);
    violations.push(...check.violations);
    if (check.compiled && check.violations.length === 0) canonicalActions.push(check.compiled);
    for (const rel of check.touched) touched.add(rel);
  }
  violations.push(...validateOrphanMkdirActions(root, canonicalActions));

  const predictedFiveBytes = FIVE_PIECE.reduce((sum, rel) => {
    const text = inMemory.has(rel) ? inMemory.get(rel) : "";
    return sum + Buffer.byteLength(text, "utf8");
  }, 0);
  if (predictedFiveBytes > FIVE_PIECE_LIMIT_BYTES && predictedFiveBytes >= currentFiveBytes) {
    violations.push("predicted_five_piece_over_45kb_must_decrease");
  }

  const beforeHashes = compiled?.before_hashes || {};
  for (const rel of touched) {
    if (!Object.prototype.hasOwnProperty.call(beforeHashes, rel)) {
      violations.push(`before_hash_missing:${rel}`);
    }
  }
  for (const rel of Object.keys(beforeHashes)) {
    if (!touched.has(rel)) violations.push(`unexpected_before_hash:${rel}`);
  }

  return {
    actions: canonicalActions,
    touched: [...touched],
    violations: [...new Set(violations)],
  };
}

function validationSummary(validation) {
  return {
    ok: validation.ok,
    mechanical_ok: validation.ok,
    validation_kind: "mechanical",
    semantic_checked_by_tool: false,
    errors: validation.errors,
    warnings: validation.warnings,
    five_piece_total_bytes: validation.five_piece.total_bytes,
    over_45kb: validation.five_piece.over_limit,
    remaining_bytes: validation.five_piece.remaining_bytes,
    unresolved_references: validation.references.unresolved.length,
    semantic_declaration: validation.semantic_declaration,
    structure_ok: validation.structure.ok,
  };
}

function createDirectoryTracked(root, target) {
  if (!isPathInside(root, target)) fail(`Directory path escaped project root: ${target}`, 3);
  const missing = [];
  let current = path.resolve(target);
  while (!fs.existsSync(current)) {
    if (path.resolve(current) === path.resolve(root)) break;
    missing.push(toRel(root, current));
    const parent = path.dirname(current);
    if (parent === current) break;
    current = parent;
  }
  fs.mkdirSync(target, { recursive: true });
  return missing;
}

function rollbackChanges(root, originalStates, backupRoot, changed, createdDirectories = []) {
  const errors = [];
  for (const rel of [...new Set(changed)].reverse()) {
    const abs = path.join(root, rel);
    const state = originalStates.get(rel) || { kind: "missing" };
    try {
      if (state.kind === "file") {
        fs.copyFileSync(path.join(backupRoot, rel), abs);
      } else if (state.kind === "missing" && fs.existsSync(abs)) {
        const current = fs.lstatSync(abs);
        if (current.isDirectory()) fs.rmdirSync(abs);
        else fs.unlinkSync(abs);
      }
    } catch (error) {
      errors.push({ rel, error: error.message || String(error) });
    }
  }
  const directories = [...new Set(createdDirectories)]
    .sort((left, right) => right.split("/").length - left.split("/").length);
  for (const rel of directories) {
    const abs = path.join(root, rel);
    if (!fs.existsSync(abs)) continue;
    try {
      const current = fs.lstatSync(abs);
      if (!current.isDirectory()) throw new Error("rollback_created_directory_is_not_directory");
      fs.rmdirSync(abs);
    } catch (error) {
      errors.push({ rel, error: error.message || String(error) });
    }
  }
  return { ok: errors.length === 0, errors };
}

function cleanupTransactionBackup(root, backupRoot, options = {}) {
  const backupBase = path.resolve(root, ".project-gov", "backups");
  const target = path.resolve(backupRoot);
  const rel = toRel(root, target);
  const removeBackupBase = options.backupBaseCreatedByTransaction === true;
  const removeBackupRoot = options.backupRootCreatedByTransaction === true;
  if (path.dirname(target) !== backupBase || !isPathInside(backupBase, target)) {
    return { ok: false, removed: false, retained: true, rel, error: "transaction_backup_path_invalid" };
  }
  const baseCheck = validateExistingPathNotRedirected(root, backupBase);
  if (!baseCheck.ok) {
    return { ok: false, removed: false, retained: true, rel, error: `transaction_backup_base_redirected:${baseCheck.error}` };
  }
  if (!fs.existsSync(target)) {
    try {
      removeTransactionBackupBaseIfOwned(backupBase, removeBackupBase);
      return { ok: true, removed: false, retained: false, rel, method: "already_missing" };
    } catch (error) {
      return { ok: false, removed: false, retained: true, rel, error: formatFsError(error) };
    }
  }
  if (!removeBackupRoot) {
    return { ok: false, removed: false, retained: true, rel, error: "transaction_backup_not_created_by_current_run" };
  }
  try {
    const stat = fs.lstatSync(target);
    if (!stat.isDirectory() || stat.isSymbolicLink()) {
      return { ok: false, removed: false, retained: true, rel, error: "transaction_backup_not_owned_directory" };
    }
    const markerPath = path.join(target, BACKUP_OWNER_FILE);
    const marker = fs.existsSync(markerPath) ? JSON.parse(fs.readFileSync(markerPath, "utf8")) : null;
    if (
      !isPlainObject(marker)
      || marker.schema_version !== 1
      || marker.tool !== SCRIPT_NAME
      || marker.kind !== "transaction_backup"
      || !isNonEmptyString(marker.root)
      || !sameResolvedPath(marker.root, root)
    ) {
      return { ok: false, removed: false, retained: true, rel, error: "transaction_backup_marker_invalid" };
    }
    fs.rmSync(target, { recursive: true, force: false });
    removeTransactionBackupBaseIfOwned(backupBase, removeBackupBase);
    return { ok: true, removed: true, retained: false, rel, method: "remove_owned_transaction_backup" };
  } catch (error) {
    return { ok: false, removed: false, retained: true, rel, error: formatFsError(error) };
  }
}

function removeTransactionBackupBaseIfOwned(backupBase, removeBackupBase) {
  if (!removeBackupBase) return;
  try {
    fs.rmdirSync(backupBase);
  } catch (error) {
    if (!["ENOENT", "ENOTEMPTY", "EEXIST"].includes(error.code)) throw error;
  }
}

function cleanupProjectCacheArtifact(root, filePath, allowedParents) {
  const result = {
    ok: true,
    removed: false,
    rel: null,
    method: "not_project_cache_file",
  };
  if (!filePath || filePath === "-") return result;

  const abs = path.resolve(filePath);
  const governanceRoot = path.resolve(root, ".project-gov");
  const parent = allowedParents
    .map((name) => path.resolve(governanceRoot, name))
    .find((candidate) => sameResolvedPath(path.dirname(abs), candidate));
  if (!parent) return result;

  result.rel = toRel(root, abs);
  const pathCheck = validateExistingPathNotRedirected(root, abs);
  if (!pathCheck.ok) {
    return {
      ...result,
      ok: false,
      method: "refused_redirected_cache_file",
      error: pathCheck.error,
    };
  }

  const stat = lstatIfPresent(abs);
  if (!stat) return { ...result, method: "already_missing" };
  if (!stat.isFile() || stat.isSymbolicLink()) {
    return {
      ...result,
      ok: false,
      method: "refused_non_plain_cache_file",
      error: "cache_artifact_not_plain_file",
    };
  }

  try {
    fs.unlinkSync(abs);
    removeEmptyCacheDirectory(parent);
    removeEmptyCacheDirectory(governanceRoot);
    return { ...result, removed: true, method: "unlink_owned_workflow_artifact" };
  } catch (error) {
    return {
      ...result,
      ok: false,
      method: "cache_artifact_cleanup_failed",
      error: formatFsError(error),
    };
  }
}

function removeEmptyCacheDirectory(dir) {
  try {
    fs.rmdirSync(dir);
  } catch (error) {
    if (!["ENOENT", "ENOTEMPTY", "EEXIST"].includes(error.code)) throw error;
  }
}

function inventoryGovernanceCache(root, olderThanDays) {
  const governanceRoot = path.join(root, ".project-gov");
  const cutoffMs = Date.now() - olderThanDays * 24 * 60 * 60 * 1000;
  const items = [];
  const errors = [];
  if (fs.existsSync(governanceRoot)) {
    const pathCheck = validateExistingPathNotRedirected(root, governanceRoot);
    if (!pathCheck.ok) errors.push(`cache_root_invalid:${pathCheck.error}`);
  }

  for (const [name, kind] of [
    ["plans", "compiled_plan"],
    ["backups", "transaction_backup"],
    ["operations", "legacy_operation"],
    ["ops", "legacy_operation"],
  ]) {
    const parent = path.join(governanceRoot, name);
    if (errors.length > 0 || !fs.existsSync(parent)) continue;
    try {
      const parentStat = fs.lstatSync(parent);
      if (!parentStat.isDirectory() || parentStat.isSymbolicLink()) {
        errors.push(`cache_parent_invalid:${toRel(root, parent)}`);
        continue;
      }
      for (const entry of fs.readdirSync(parent, { withFileTypes: true })) {
        const abs = path.join(parent, entry.name);
        const stat = fs.lstatSync(abs);
        if (stat.isSymbolicLink() || stat.mtimeMs > cutoffMs) continue;
        items.push({
          kind,
          rel: toRel(root, abs),
          type: stat.isDirectory() ? "directory" : stat.isFile() ? "file" : "other",
          modified_at: stat.mtime.toISOString(),
          bytes: stat.isFile() ? stat.size : null,
        });
      }
    } catch (error) {
      errors.push(`cache_scan_failed:${toRel(root, parent)}:${formatFsError(error)}`);
    }
  }

  return {
    ok: errors.length === 0,
    tool: SCRIPT_NAME,
    command: "prune",
    mode: "read_only_inventory",
    automatic_delete: false,
    root,
    older_than_days: olderThanDays,
    cutoff: new Date(cutoffMs).toISOString(),
    item_count: items.length,
    items: items.slice(0, MAX_PRUNE_REPORT_ITEMS),
    errors: errors.map((item) => limitText(item, MAX_STRUCTURE_DETAIL_CHARS)),
    report_truncated: items.length > MAX_PRUNE_REPORT_ITEMS,
  };
}

function applyAppendAfter(existing, action) {
  const newline = preferredNewline(existing);
  const lines = existing.split(/\r?\n/);
  const matches = lines
    .map((line, lineIndex) => ({ line, lineIndex }))
    .filter((item) => (action.match === "contains" ? item.line.includes(action.after) : item.line === action.after));
  if (matches.length !== 1) fail(`append_after match count ${matches.length} for ${action.path}`, 3);
  const contentLines = ensureTrailingNewline(action.content || "").replace(/\r?\n$/, "").split(/\r?\n/);
  lines.splice(matches[0].lineIndex + 1, 0, ...contentLines);
  return ensureTrailingNewlineWithStyle(lines.join(newline), newline);
}

function applyReplaceLineContains(existing, action) {
  const newline = preferredNewline(existing);
  const lines = existing.split(/\r?\n/);
  const matches = lines
    .map((line, lineIndex) => ({ line, lineIndex }))
    .filter((item) => item.line.includes(action.contains));
  if (matches.length !== 1) fail(`replace_line_contains match count ${matches.length} for ${action.path}`, 3);
  lines[matches[0].lineIndex] = action.replacement;
  return ensureTrailingNewlineWithStyle(lines.join(newline), newline);
}

function applyReplaceBlockExact(existing, action) {
  const result = replaceBlockExactResult(existing, action.old_block, action.replacement);
  if (result.match_count !== 1) {
    fail(`replace_block_exact match count ${result.match_count} for ${action.path}`, 3);
  }
  return result.next;
}

function replaceBlockExactResult(existing, oldBlock, replacement) {
  const source = normalizeNewlines(existing);
  const target = normalizeNewlines(oldBlock);
  const nextBlock = normalizeNewlines(replacement);
  if (target.length === 0) return { match_count: 0, next: existing };
  const matchCount = countExactOccurrences(source, target);
  if (matchCount !== 1) return { match_count: matchCount, next: existing };
  const newline = existing.includes("\r\n") ? "\r\n" : "\n";
  const next = source.replace(target, nextBlock).replace(/\n/g, newline);
  return { match_count: 1, next };
}

function normalizeNewlines(value) {
  return String(value ?? "").replace(/\r\n?/g, "\n");
}

function countExactOccurrences(source, target) {
  let count = 0;
  let cursor = 0;
  while (target.length > 0) {
    const found = source.indexOf(target, cursor);
    if (found === -1) break;
    count += 1;
    cursor = found + target.length;
  }
  return count;
}

function readForAction(root, rel, inMemory) {
  if (inMemory.has(rel)) return inMemory.get(rel);
  const abs = path.join(root, rel);
  if (!fs.existsSync(abs)) fail(`Target file does not exist for action: ${rel}`, 2);
  const text = readText(abs);
  inMemory.set(rel, text);
  return text;
}

function hasPlaceholderContent(text) {
  return PLACEHOLDER_PATTERNS.some((regex) => regex.test(text));
}

function isAllowedProjectPath(rel) {
  if (FIVE_PIECE.includes(rel)) return true;
  if (INDEX_FILES.includes(rel)) return true;
  if (rel.startsWith("历史记录/")) return true;
  if (rel.startsWith("证据库/")) return true;
  if (rel.startsWith("项目物料/")) return true;
  return false;
}

function validateRelativePath(root, rel) {
  if (path.isAbsolute(rel) || /^[A-Za-z]:[\\/]/.test(rel)) {
    return { ok: false, error: "absolute_path_not_allowed" };
  }
  if (rel.includes("\0")) return { ok: false, error: "nul_byte_not_allowed" };
  const rawSegments = rel.replace(/\\/g, "/").split("/");
  if (rawSegments.includes("..")) {
    return { ok: false, error: "parent_traversal_not_allowed" };
  }
  const segments = rawSegments.filter((segment) => segment && segment !== ".");
  if (segments.length === 0) return { ok: false, error: "empty_path_not_allowed" };
  if (segments.some((segment) => RESERVED_PATH_SEGMENTS.has(segment.toLowerCase()))) {
    return { ok: false, error: "reserved_path_segment_not_allowed" };
  }
  if (segments.some((segment) => (
    segment !== segment.trim()
    || segment.includes(":")
    || /\.$/.test(segment)
  ))) {
    return { ok: false, error: "nonportable_path_segment_not_allowed" };
  }
  const normalized = segments.join("/");
  const abs = path.resolve(root, normalized);
  if (!isPathInside(root, abs)) return { ok: false, error: "path_outside_root" };

  const realRoot = fs.realpathSync.native(root);
  const existingAncestor = findExistingAncestor(abs);
  const ancestorStat = fs.lstatSync(existingAncestor);
  if (!sameResolvedPath(existingAncestor, root) && ancestorStat.isSymbolicLink()) {
    return { ok: false, error: "symlink_or_junction_redirect_not_allowed" };
  }
  if (existingAncestor !== abs && !ancestorStat.isDirectory()) {
    return { ok: false, error: "existing_ancestor_is_not_directory" };
  }
  const realAncestor = fs.realpathSync.native(existingAncestor);
  if (!isPathInside(realRoot, realAncestor)) {
    return { ok: false, error: "symlink_or_junction_escape" };
  }
  const ancestorRel = path.relative(root, existingAncestor);
  const expectedRealAncestor = path.resolve(realRoot, ancestorRel);
  if (!sameResolvedPath(realAncestor, expectedRealAncestor)) {
    return { ok: false, error: "symlink_or_junction_redirect_not_allowed" };
  }
  return { ok: true, rel: normalized, abs };
}

function validateExistingPathNotRedirected(root, target) {
  const realRoot = fs.realpathSync.native(root);
  const existingAncestor = findExistingAncestor(target);
  const ancestorStat = fs.lstatSync(existingAncestor);
  if (!sameResolvedPath(existingAncestor, root) && ancestorStat.isSymbolicLink()) {
    return { ok: false, error: "symlink_or_junction_redirect_not_allowed" };
  }
  const realAncestor = fs.realpathSync.native(existingAncestor);
  if (!isPathInside(realRoot, realAncestor)) {
    return { ok: false, error: "symlink_or_junction_escape" };
  }
  const ancestorRel = path.relative(root, existingAncestor);
  const expectedRealAncestor = path.resolve(realRoot, ancestorRel);
  if (!sameResolvedPath(realAncestor, expectedRealAncestor)) {
    return { ok: false, error: "symlink_or_junction_redirect_not_allowed" };
  }
  return { ok: true };
}

function assertManagedPathNotRedirected(root, rel) {
  const check = validateExistingPathNotRedirected(root, path.join(root, rel));
  if (!check.ok) fail(`managed_project_path_redirected:${rel}:${check.error}`, 4);
}

function assertManagedCorePathsNotRedirected(root) {
  for (const rel of [...FIVE_PIECE, ...INDEX_FILES]) {
    assertManagedPathNotRedirected(root, rel);
  }
}

function assertTransactionBackupBaseSafe(root) {
  const rel = ".project-gov/backups";
  assertManagedPathNotRedirected(root, rel);
  const abs = path.join(root, rel);
  const stat = lstatIfPresent(abs);
  if (!stat) return;
  if (!stat.isDirectory() || stat.isSymbolicLink()) {
    fail(`transaction_backup_base_not_plain_directory:${rel}`, 4);
  }
}

function findExistingAncestor(abs) {
  let current = abs;
  while (!lstatIfPresent(current)) {
    const parent = path.dirname(current);
    if (parent === current) return current;
    current = parent;
  }
  return current;
}

function isPathInside(root, candidate) {
  const normalize = (value) => (process.platform === "win32" ? value.toLowerCase() : value);
  const normalizedRoot = normalize(path.resolve(root));
  const normalizedCandidate = normalize(path.resolve(candidate));
  const rootWithSep = normalizedRoot.endsWith(path.sep) ? normalizedRoot : `${normalizedRoot}${path.sep}`;
  return normalizedCandidate === normalizedRoot || normalizedCandidate.startsWith(rootWithSep);
}

function sameResolvedPath(left, right) {
  const normalize = (value) => (process.platform === "win32" ? path.resolve(value).toLowerCase() : path.resolve(value));
  return normalize(left) === normalize(right);
}

function nextIds(allOccurrences, date) {
  const ids = allOccurrences.map((item) => item.id);
  return {
    history_id: nextId(ids, "M", date),
    evidence_id: nextId(ids, "EV", date),
    material_id: nextId(ids, "MAT", date),
    run_id: `run_${date}_${timeCompact()}_${crypto.randomBytes(3).toString("hex")}`,
  };
}

function nextId(ids, prefix, date) {
  const pattern = new RegExp(
    `^${prefix}-${date}${PROJECT_ID_TOPIC_SEGMENTS_SOURCE}-(${PROJECT_ID_SEQUENCE_SOURCE})$`,
  );
  let max = 0;
  for (const id of ids) {
    const match = id.match(pattern);
    if (match) max = Math.max(max, Number(match[1]));
  }
  if (max >= 999) fail(`ID sequence exhausted for ${prefix}-${date}`, 2);
  return `${prefix}-${date}-${String(max + 1).padStart(3, "0")}`;
}

function maxId(ids) {
  const sorted = [...new Set(ids)].sort();
  return sorted.length ? sorted[sorted.length - 1] : null;
}

function normalizeDate(value) {
  const input = String(value);
  if (!/^(?:\d{8}|\d{4}-\d{2}-\d{2})$/.test(input)) fail(`Invalid date: ${value}`, 2);
  const raw = input.replace(/-/g, "");
  const year = Number(raw.slice(0, 4));
  const month = Number(raw.slice(4, 6));
  const day = Number(raw.slice(6, 8));
  if (!isValidCalendarDate(year, month, day)) {
    fail(`Invalid calendar date: ${value}`, 2);
  }
  return raw;
}

function isValidCalendarDate(year, month, day) {
  if (year < 1 || month < 1 || month > 12 || day < 1) return false;
  const leapYear = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
  const daysInMonth = [31, leapYear ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return day <= daysInMonth[month - 1];
}

function currentLocalDate() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  return `${year}${month}${day}`;
}

function timeCompact() {
  const now = new Date();
  return [
    String(now.getHours()).padStart(2, "0"),
    String(now.getMinutes()).padStart(2, "0"),
    String(now.getSeconds()).padStart(2, "0"),
  ].join("");
}

function parseNonNegativeNumber(value, optionName) {
  const number = Number(value);
  if (!Number.isFinite(number) || number < 0) fail(`${optionName} must be a non-negative number`, 2);
  return number;
}

function resolveRoot(rootArg) {
  const root = path.resolve(rootArg || process.cwd());
  if (!fs.existsSync(root)) fail(`Root does not exist: ${root}`, 2);
  const stat = fs.statSync(root);
  if (!stat.isDirectory()) fail(`Root is not a directory: ${root}`, 2);
  return root;
}

function resolveCompiledPlanOutput(root, outArg) {
  const outPath = path.resolve(outArg);
  const planRoot = path.join(root, ".project-gov", "plans");
  if (!isPathInside(planRoot, outPath)) {
    fail(`Compiled plan output must stay under ${planRoot}`, 2);
  }
  if (path.extname(outPath).toLowerCase() !== ".json") {
    fail("Compiled plan output must use a .json extension", 2);
  }
  if (lstatIfPresent(outPath)) fail(`Refusing to overwrite compiled plan output: ${outPath}`, 2);

  const pathCheck = validateExistingPathNotRedirected(root, outPath);
  if (!pathCheck.ok) fail(`Compiled plan output path is redirected: ${pathCheck.error}`, 2);
  return outPath;
}

function requireOption(value, message) {
  if (!value) fail(message, 2);
  return value;
}

function readJsonFile(filePath) {
  if (filePath === "-") {
    return JSON.parse(fs.readFileSync(0, "utf8"));
  }
  const abs = path.resolve(filePath);
  return JSON.parse(fs.readFileSync(abs, "utf8"));
}

function readText(abs) {
  return fs.readFileSync(abs, "utf8");
}

function readTextIfPresent(abs) {
  return lstatIfPresent(abs) ? readText(abs) : "";
}

function describePath(abs) {
  const stat = lstatIfPresent(abs);
  if (!stat) return { kind: "missing", fingerprint: null };
  if (stat.isSymbolicLink()) return { kind: "symbolic_link", fingerprint: "symbolic_link" };
  if (stat.isDirectory()) return { kind: "directory", fingerprint: "directory" };
  if (stat.isFile()) return { kind: "file", fingerprint: sha256(fs.readFileSync(abs)) };
  return { kind: "other", fingerprint: `other:${stat.mode}` };
}

function lstatIfPresent(abs) {
  try {
    return fs.lstatSync(abs);
  } catch (error) {
    if (error?.code === "ENOENT") return null;
    throw error;
  }
}

function pathFingerprint(abs) {
  return describePath(abs).fingerprint;
}

function ensureTrailingNewline(text) {
  return text.endsWith("\n") ? text : `${text}\n`;
}

function preferredNewline(text) {
  return String(text || "").includes("\r\n") ? "\r\n" : "\n";
}

function ensureTrailingNewlineWithStyle(text, newline) {
  if (text.endsWith("\r\n") || text.endsWith("\n")) return text;
  return `${text}${newline}`;
}

function limitText(value, maxChars) {
  const text = String(value ?? "");
  if (text.length <= maxChars) return text;
  return `${text.slice(0, maxChars)}…[truncated:${text.length - maxChars}]`;
}

function utf8Bytes(text) {
  return Buffer.byteLength(text, "utf8");
}

function writeAtomic(abs, text) {
  fs.mkdirSync(path.dirname(abs), { recursive: true });
  const tmp = `${abs}.tmp-${process.pid}-${Date.now()}`;
  try {
    fs.writeFileSync(tmp, text, "utf8");
    fs.renameSync(tmp, abs);
  } catch (error) {
    if (fs.existsSync(tmp)) fs.unlinkSync(tmp);
    throw error;
  }
}

function sha256(buffer) {
  return crypto.createHash("sha256").update(buffer).digest("hex");
}

function mapPush(map, key, value) {
  if (!map.has(key)) map.set(key, []);
  map.get(key).push(value);
}

function toRel(root, abs) {
  return path.relative(root, abs).replace(/\\/g, "/");
}

function sanitizeName(value) {
  return String(value).replace(/[^A-Za-z0-9._-]/g, "_").slice(0, 120);
}

function output(data, opts) {
  const versioned = isPlainObject(data) && !Object.hasOwn(data, "skill_version")
    ? { ...data, skill_version: SKILL_VERSION }
    : data;
  if (opts.json) {
    console.log(JSON.stringify(versioned, null, 2));
    return;
  }
  if (versioned.command === "inspect" || versioned.command === "validate") {
    const report = versioned.report || versioned;
    console.log(`root: ${report.root}`);
    console.log("validation_kind: mechanical");
    console.log(`five_piece_total_bytes: ${report.five_piece.total_bytes}/${FIVE_PIECE_LIMIT_BYTES}`);
    console.log(`five_piece_remaining_bytes: ${report.five_piece.remaining_bytes}`);
    console.log(`five_piece_over_45kb: ${report.five_piece.over_limit}`);
    console.log(`missing_five_piece: ${report.files.five_piece.missing.join(", ") || "none"}`);
    console.log(`missing_indexes: ${report.files.indexes.missing.join(", ") || "none"}`);
    console.log(`unresolved_references: ${report.references.unresolved.length}`);
    console.log(`handoff_changes_after_checkpoint: ${report.semantic_declaration.changes_after_checkpoint || "missing"}`);
    console.log(`semantic_checked_by_tool: ${report.semantic_checked_by_tool}`);
    console.log(`mechanical_ok: ${report.mechanical_ok}`);
    console.log(`warnings: ${(report.warnings || []).join(", ") || "none"}`);
    console.log(`errors: ${report.errors.join(", ") || "none"}`);
    return;
  }
  console.log(JSON.stringify(versioned, null, 2));
}

function fail(message, code = 1) {
  const error = new Error(message);
  error.exitCode = code;
  process.exitCode = code;
  throw error;
}

main();
