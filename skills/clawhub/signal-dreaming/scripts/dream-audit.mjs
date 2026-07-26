#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import {
  DAILY_RE,
  canonicalRoot,
  exists,
  fail,
  memoryScopeSnapshot,
  parseDreamLog,
  safePath,
  sha256File,
} from "./common.mjs";

const SECRET_PATTERNS = [
  ["github-token", /(?:github_pat_[A-Za-z0-9_]{20,}|gh[po]_[A-Za-z0-9]{20,})/],
  ["openai-key", /sk-[A-Za-z0-9_-]{20,}/],
  ["aws-access-key", /AKIA[0-9A-Z]{16}/],
  ["google-api-key", /AIza[0-9A-Za-z_-]{35}/],
  ["telegram-token", /[0-9]{8,12}:AA[A-Za-z0-9_-]{30,}/],
  ["slack-token", /xox[baprs]-[A-Za-z0-9-]{10,}/],
  ["private-key", /-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----/],
  ["credential-url", /x-access-token:[A-Za-z0-9_-]{20,}@/],
];

function push(result, level, code, message, detail = {}) {
  result[level].push({ code, message, ...detail });
}

async function scanSecrets(root, relatives) {
  const findings = [];
  for (const relative of relatives) {
    const resolved = await safePath(root, relative, { mustExist: true, kind: "file", rejectSymlink: true });
    const content = await fs.readFile(resolved.real, "utf8");
    const categories = SECRET_PATTERNS.filter(([, expression]) => expression.test(content)).map(([category]) => category);
    if (categories.length) findings.push({ file: relative, categories });
  }
  return findings;
}

async function auditSize(root, result) {
  const memory = await safePath(root, "MEMORY.md", { mustExist: true, kind: "file", rejectSymlink: true });
  const bytes = (await fs.stat(memory.real)).size;
  result.memoryBytes = bytes;
  if (bytes > 10_240) push(result, "errors", "MEMORY_HARD_LIMIT", "MEMORY.md exceeds 10 KiB");
  else if (bytes > 8_192) push(result, "warnings", "MEMORY_SOFT_LIMIT", "MEMORY.md exceeds the 8 KiB target");
}

async function auditPointers(root, result) {
  const memory = await safePath(root, "MEMORY.md", { mustExist: true, kind: "file", rejectSymlink: true });
  const content = await fs.readFile(memory.real, "utf8");
  const pointers = [...content.matchAll(/(?:^|[\s(`])((?:memory\/)[A-Za-z0-9._/-]+\.md)(?=$|[\s)`.,;:])/gm)]
    .map((match) => match[1]);
  for (const pointer of new Set(pointers)) {
    try {
      await safePath(root, pointer, { mustExist: true, kind: "file", rejectSymlink: true });
    } catch {
      push(result, "errors", "BROKEN_POINTER", `MEMORY.md points to a missing or unsafe file: ${pointer}`, { file: pointer });
    }
  }
  result.memoryPointers = [...new Set(pointers)].toSorted();
}

async function auditDiary(root, result) {
  const diary = await safePath(root, "memory/dream-log.md", { mustExist: true, kind: "file", rejectSymlink: true });
  const parsed = parseDreamLog(await fs.readFile(diary.real, "utf8"));
  result.diary = {
    entries: parsed.entries.length,
    lastDreamNumber: parsed.max,
    gaps: parsed.gaps,
  };
  if (parsed.entries.length > 30) push(result, "errors", "DIARY_TOO_LONG", "dream diary contains more than 30 entries");
  if (parsed.malformed.length) push(result, "errors", "DIARY_MALFORMED", "dream diary contains malformed headings");
  if (parsed.duplicates.length) push(result, "errors", "DIARY_DUPLICATE", "dream diary contains duplicate numbers");
  if (parsed.descending.length) push(result, "errors", "DIARY_DESCENDING", "dream diary numbers are out of order");
  if (parsed.gaps.length) push(result, "warnings", "DIARY_GAPS", "dream diary contains number gaps");
}

async function auditManifest(root, manifest, result, options = {}) {
  if (!manifest || manifest.schema !== "signal-dreaming.run-manifest.v3") {
    push(result, "errors", "MANIFEST_SCHEMA", "run manifest is missing or unsupported");
    return;
  }
  const planned = new Set(manifest.plannedFiles.map((file) => file.path));
  const allowUnchanged = new Set(options.allowUnchanged ?? []);
  for (const file of manifest.plannedFiles) {
    if (file.existed) {
      const backup = await safePath(root, file.backupPath, { mustExist: true, kind: "file", rejectSymlink: true });
      const backupHash = await sha256File(backup.real);
      if (backupHash !== file.originalSha256) {
        push(result, "errors", "BACKUP_HASH", `backup hash mismatch for ${file.path}`, { file: file.path });
      }
    }
  }

  let currentScope;
  try {
    currentScope = await memoryScopeSnapshot(root);
  } catch (error) {
    push(result, "errors", error.code ?? "SCOPE_ERROR", error.message);
    return;
  }
  for (const [relative, originalHash] of Object.entries(manifest.scopeSnapshot)) {
    const currentHash = currentScope[relative];
    if (currentHash === undefined) {
      push(result, "errors", "UNPLANNED_DELETE", `file disappeared during the run: ${relative}`, { file: relative });
    } else if (currentHash !== originalHash && !planned.has(relative)) {
      push(result, "errors", DAILY_RE.test(path.basename(relative)) ? "DAILY_LOG_CHANGED" : "UNPLANNED_CHANGE",
        `unplanned file changed during the run: ${relative}`, { file: relative });
    }
  }
  for (const relative of Object.keys(currentScope)) {
    if (!(relative in manifest.scopeSnapshot) && !planned.has(relative)) {
      push(result, "errors", "UNPLANNED_CREATE", `unplanned Markdown file appeared during the run: ${relative}`, { file: relative });
    }
  }
  for (const file of manifest.plannedFiles) {
    if (!(file.path in currentScope)) {
      push(result, "errors", "PLANNED_FILE_MISSING", `planned file is missing: ${file.path}`, { file: file.path });
      continue;
    }
    if (file.existed && currentScope[file.path] === file.originalSha256 && !allowUnchanged.has(file.path)) {
      push(result, "errors", "PLANNED_FILE_UNCHANGED", `planned file was not changed: ${file.path}`, { file: file.path });
    }
  }
}

export async function auditWorkspace(workspaceInput, options = {}) {
  const root = await canonicalRoot(workspaceInput);
  const result = {
    schema: "signal-dreaming.audit.v3",
    ok: false,
    root,
    errors: [],
    warnings: [],
    secretFindings: [],
    semanticReviewRequired: [],
  };
  try {
    await auditSize(root, result);
    await auditPointers(root, result);
    await auditDiary(root, result);
    if (options.manifest) await auditManifest(root, options.manifest, result, options);
    const files = options.files?.length ? options.files : ["MEMORY.md", "memory/dream-log.md"];
    const safeFiles = [];
    for (const relative of files) {
      try {
        const resolved = await safePath(root, relative, { mustExist: true, kind: "file", rejectSymlink: true });
        safeFiles.push(resolved.relative);
        if (resolved.relative.startsWith("memory/") && resolved.relative !== "memory/dream-log.md"
          && !DAILY_RE.test(path.basename(resolved.relative))) {
          result.semanticReviewRequired.push(resolved.relative);
        }
      } catch (error) {
        push(result, "errors", error.code ?? "UNSAFE_PATH", error.message);
      }
    }
    result.secretFindings = await scanSecrets(root, safeFiles);
    for (const finding of result.secretFindings) {
      push(result, "errors", "SECRET_PATTERN", `suspected credential category in ${finding.file}`, {
        file: finding.file,
        categories: finding.categories,
      });
    }
  } catch (error) {
    push(result, "errors", error.code ?? "AUDIT_ERROR", error.message);
  }
  result.semanticReviewRequired = [...new Set(result.semanticReviewRequired)].toSorted();
  result.ok = result.errors.length === 0;
  return result;
}

async function main() {
  const args = process.argv.slice(2);
  const workspace = args.shift();
  if (!workspace) throw fail("USAGE", "usage: dream-audit.mjs <workspace-root> [--manifest file] [touched-file ...]");
  let manifest;
  const files = [];
  while (args.length) {
    const arg = args.shift();
    if (arg === "--manifest") {
      const file = args.shift();
      if (!file) throw fail("USAGE", "--manifest requires a JSON file");
      manifest = JSON.parse(await fs.readFile(file, "utf8"));
    } else files.push(arg);
  }
  const result = await auditWorkspace(workspace, { manifest, files });
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  if (!result.ok) process.exitCode = 2;
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? "").href) {
  main().catch((error) => {
    process.stderr.write(`${JSON.stringify({ ok: false, code: error.code ?? "ERROR", message: error.message })}\n`);
    process.exitCode = 2;
  });
}
