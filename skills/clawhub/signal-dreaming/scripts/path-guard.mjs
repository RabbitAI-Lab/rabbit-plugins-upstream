#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
function reject(message) { const error = new Error(message); error.name = "PathSafetyError"; throw error; }
function stat(file) { try { return fs.lstatSync(file); } catch (error) { if (error?.code === "ENOENT") return null; throw error; } }
export function resolveWorkspaceRoot(raw) {
  if (typeof raw !== "string" || !raw.trim() || raw.includes("\0")) reject("invalid workspace root");
  const abs = path.resolve(raw);
  const st = stat(abs);
  if (!st || st.isSymbolicLink() || !st.isDirectory()) reject("workspace root must be a real directory");
  if (fs.realpathSync.native(abs) !== abs) reject("workspace root must be canonical; symlinked aliases are rejected");
  return abs;
}
export function normalizeRelativePath(raw, label = "path") {
  if (typeof raw !== "string" || !raw || raw.includes("\0")) reject(`invalid ${label}`);
  const slash = raw.replaceAll("\\", "/");
  if (path.posix.isAbsolute(slash) || path.win32.isAbsolute(raw)) reject(`absolute ${label} rejected`);
  if (slash.split("/").includes("..")) reject(`${label} contains .. traversal`);
  const rel = path.posix.normalize(slash);
  if (!rel || rel === ".") reject(`empty ${label}`);
  return rel;
}
function inside(root, target) {
  const abs = path.resolve(target);
  const rel = path.relative(root, abs);
  if (rel === ".." || rel.startsWith(`..${path.sep}`) || path.isAbsolute(rel)) reject("path escapes workspace");
  return abs;
}
export function assertNoSymlinkComponents(root, target, allowMissing = true) {
  const abs = inside(root, target);
  const rel = path.relative(root, abs);
  let cursor = root;
  for (const part of rel ? rel.split(path.sep) : []) {
    cursor = path.join(cursor, part);
    const st = stat(cursor);
    if (!st) { if (allowMissing) return abs; reject(`missing guarded path: ${cursor}`); }
    if (st.isSymbolicLink()) reject(`symlinked path component rejected: ${cursor}`);
  }
  return abs;
}
export function resolveInside(root, raw, options = {}) {
  const rel = normalizeRelativePath(raw, options.label);
  return assertNoSymlinkComponents(root, inside(root, path.resolve(root, rel)), options.allowMissing !== false);
}
export function ensureSafeDirectory(root, dir) {
  const abs = inside(root, dir);
  const rel = path.relative(root, abs);
  let cursor = root;
  for (const part of rel ? rel.split(path.sep) : []) {
    cursor = path.join(cursor, part);
    let st = stat(cursor);
    if (!st) { fs.mkdirSync(cursor, { mode: 0o700 }); st = fs.lstatSync(cursor); }
    if (st.isSymbolicLink() || !st.isDirectory()) reject(`unsafe directory component: ${cursor}`);
  }
  return abs;
}
export function safeRegularOrMissing(root, file) {
  const abs = assertNoSymlinkComponents(root, file, true);
  const st = stat(abs);
  if (!st) return "missing";
  if (st.isSymbolicLink() || !st.isFile()) reject(`non-regular file rejected: ${abs}`);
  return "file";
}
