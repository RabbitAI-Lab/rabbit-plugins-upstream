import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";

export const DAILY_RE = /^\d{4}-\d{2}-\d{2}(?:-[A-Za-z0-9._-]+)?\.md$/;
export const STATE_REL = "logs/signal-dreaming/state.json";
export const LOCK_REL = "logs/signal-dreaming/run.lock";
export const BACKUP_REL = ".backup/memory-dreams";

export function fail(code, message, detail = {}) {
  const error = new Error(message);
  error.code = code;
  Object.assign(error, detail);
  return error;
}

export async function exists(file) {
  try {
    await fs.access(file);
    return true;
  } catch {
    return false;
  }
}

export function isInside(root, target) {
  const rel = path.relative(root, target);
  return rel === "" || (!rel.startsWith(`..${path.sep}`) && rel !== ".." && !path.isAbsolute(rel));
}

export async function canonicalRoot(input) {
  if (!path.isAbsolute(input)) throw fail("ROOT_NOT_ABSOLUTE", "workspace root must be absolute");
  const root = await fs.realpath(input);
  const stat = await fs.stat(root);
  if (!stat.isDirectory()) throw fail("ROOT_NOT_DIRECTORY", "workspace root is not a directory");
  return root;
}

export function normalizeRelative(input) {
  if (typeof input !== "string" || !input || path.isAbsolute(input) || input.includes("\0")) {
    throw fail("UNSAFE_PATH", "path must be a non-empty workspace-relative path");
  }
  const portable = input.replaceAll("\\", "/");
  const normalized = path.posix.normalize(portable);
  if (normalized === ".." || normalized.startsWith("../") || normalized.startsWith("/")) {
    throw fail("UNSAFE_PATH", "path escapes the workspace");
  }
  return normalized;
}

async function nearestExistingParent(target) {
  let cursor = target;
  for (;;) {
    try {
      await fs.lstat(cursor);
      return cursor;
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
      const parent = path.dirname(cursor);
      if (parent === cursor) throw error;
      cursor = parent;
    }
  }
}

export async function safePath(rootInput, relativeInput, options = {}) {
  const root = await canonicalRoot(rootInput);
  const relative = normalizeRelative(relativeInput);
  const lexical = path.resolve(root, relative);
  if (!isInside(root, lexical)) throw fail("UNSAFE_PATH", "path escapes the workspace");
  const present = await exists(lexical);
  if (present) {
    const lst = await fs.lstat(lexical);
    if (options.rejectSymlink && lst.isSymbolicLink()) {
      throw fail("SYMLINK_OUTPUT", `symlink is not allowed for ${relative}`);
    }
    const real = await fs.realpath(lexical);
    if (!isInside(root, real)) throw fail("SYMLINK_ESCAPE", `${relative} resolves outside the workspace`);
    if (options.kind === "file" && !(await fs.stat(real)).isFile()) {
      throw fail("PATH_TYPE", `${relative} is not a regular file`);
    }
    if (options.kind === "directory" && !(await fs.stat(real)).isDirectory()) {
      throw fail("PATH_TYPE", `${relative} is not a directory`);
    }
    return { root, relative, lexical, real, present: true };
  }
  if (options.mustExist) throw fail("MISSING_PATH", `missing required path: ${relative}`);
  const parent = await nearestExistingParent(path.dirname(lexical));
  const realParent = await fs.realpath(parent);
  if (!isInside(root, realParent)) throw fail("SYMLINK_ESCAPE", `${relative} has a parent outside the workspace`);
  return { root, relative, lexical, real: lexical, present: false };
}

export async function sha256File(file) {
  const hash = crypto.createHash("sha256");
  hash.update(await fs.readFile(file));
  return hash.digest("hex");
}

export function sha256Text(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

export async function fileSnapshot(root, relative) {
  const resolved = await safePath(root, relative, { mustExist: true, kind: "file", rejectSymlink: true });
  const stat = await fs.stat(resolved.real);
  return {
    path: resolved.relative,
    sha256: await sha256File(resolved.real),
    size: stat.size,
    mtimeMs: Math.trunc(stat.mtimeMs),
  };
}

export async function readJson(file, label = file) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch (error) {
    throw fail("INVALID_JSON", `invalid JSON in ${label}: ${error.message}`);
  }
}

export async function writeJsonAtomic(file, value) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  const temp = `${file}.tmp-${process.pid}-${crypto.randomBytes(4).toString("hex")}`;
  await fs.writeFile(temp, `${JSON.stringify(value, null, 2)}\n`, { mode: 0o600 });
  await fs.rename(temp, file);
}

export async function writeTextAtomic(file, value) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  const temp = `${file}.tmp-${process.pid}-${crypto.randomBytes(4).toString("hex")}`;
  await fs.writeFile(temp, value, { mode: 0o600 });
  await fs.rename(temp, file);
}

export async function listDailyLogs(rootInput) {
  const root = await canonicalRoot(rootInput);
  const memory = await safePath(root, "memory", { mustExist: true, kind: "directory" });
  const names = await fs.readdir(memory.real, { withFileTypes: true });
  const logs = [];
  for (const entry of names) {
    if (!DAILY_RE.test(entry.name)) continue;
    if (!entry.isFile()) throw fail("UNSAFE_DAILY_LOG", `daily log is not a regular file: memory/${entry.name}`);
    logs.push(await fileSnapshot(root, `memory/${entry.name}`));
  }
  return logs.toSorted((a, b) => a.path.localeCompare(b.path));
}

export async function memoryScopeSnapshot(rootInput) {
  const root = await canonicalRoot(rootInput);
  const paths = ["MEMORY.md"];
  const memory = await safePath(root, "memory", { mustExist: true, kind: "directory" });
  for (const entry of await fs.readdir(memory.real, { withFileTypes: true })) {
    if (entry.name.endsWith(".md")) paths.push(`memory/${entry.name}`);
  }
  const files = {};
  for (const relative of paths.toSorted()) {
    const resolved = await safePath(root, relative, { mustExist: true, kind: "file", rejectSymlink: true });
    files[relative] = await sha256File(resolved.real);
  }
  return files;
}

export function parseDreamLog(content) {
  const valid = [];
  const malformed = [];
  const lines = content.replaceAll("\r\n", "\n").split("\n");
  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    const match = line.match(/^## 🌙 Dream #(\d+)(?: · .+)?$/);
    if (match) valid.push({ number: Number(match[1]), line: index + 1, text: line });
    else if (/^#{1,6}\s+.*\bDream\s*#/i.test(line)) malformed.push({ line: index + 1 });
  }
  const duplicates = [];
  const descending = [];
  const gaps = [];
  for (let index = 1; index < valid.length; index += 1) {
    const previous = valid[index - 1].number;
    const current = valid[index].number;
    if (current === previous) duplicates.push(current);
    else if (current < previous) descending.push({ previous, current });
    else if (current > previous + 1) gaps.push({ previous, current });
  }
  return {
    entries: valid,
    malformed,
    duplicates,
    descending,
    gaps,
    max: valid.length ? Math.max(...valid.map((entry) => entry.number)) : 0,
  };
}

export function trimAndAppendDream(content, entry) {
  const parsed = parseDreamLog(content);
  if (parsed.malformed.length || parsed.duplicates.length || parsed.descending.length) {
    throw fail("DIARY_INVALID", "dream diary headings are malformed or non-monotonic");
  }
  if (!Number.isSafeInteger(entry.number) || entry.number !== parsed.max + 1) {
    throw fail("DIARY_NUMBER", `next dream number must be ${parsed.max + 1}`);
  }
  if (typeof entry.timestamp !== "string" || !entry.timestamp.trim()
    || !["auto", "manual"].includes(entry.trigger)
    || !Number.isFinite(entry.durationMinutes) || entry.durationMinutes < 0
    || !Number.isSafeInteger(entry.newLogCount) || entry.newLogCount < 0
    || !Array.isArray(entry.changes) || !entry.changes.length
    || entry.changes.some((item) => typeof item !== "string" || !item.trim())
    || typeof entry.note !== "string" || !entry.note.trim()) {
    throw fail("DIARY_ENTRY_INVALID", "diary entry fields are missing or invalid");
  }
  const heading = `## 🌙 Dream #${entry.number} · ${entry.timestamp}`;
  const block = [
    heading,
    "",
    `**Trigger**: ${entry.trigger}`,
    `**Duration**: ~${entry.durationMinutes} minutes`,
    "",
    "### Signal summary",
    `- Changed daily logs: ${entry.newLogCount}`,
    "",
    "### What changed",
    ...entry.changes.map((item) => `- ${item}`),
    "",
    "### Note",
    entry.note,
    "",
  ].join("\n");
  const starts = parsed.entries.map((item) => item.line - 1);
  let prefix = content.trimEnd();
  if (parsed.entries.length >= 30) {
    const lines = content.split(/\r?\n/);
    const header = lines.slice(0, starts[0]).join("\n").trimEnd();
    const keepStart = starts[parsed.entries.length - 29];
    const retained = lines.slice(keepStart).join("\n").trimEnd();
    prefix = [header, retained].filter(Boolean).join("\n\n");
  }
  return `${prefix ? `${prefix}\n\n` : ""}${block}`;
}

export async function pathMap(root, relatives) {
  const result = {};
  for (const relative of relatives) {
    const resolved = await safePath(root, relative, { mustExist: true, kind: "file", rejectSymlink: true });
    result[relative] = await sha256File(resolved.real);
  }
  return result;
}
