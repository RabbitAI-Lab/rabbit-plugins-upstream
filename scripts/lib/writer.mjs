// skill 目录写入器：内容哈希判重、原子替换、.upstream.json 溯源。
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

export function skillDir(root, source, id) {
  return path.join(root, "skills", source, id);
}

// files: Map<相对路径, Buffer>。返回目录内容的稳定哈希。
export function contentHash(files) {
  const h = crypto.createHash("sha256");
  for (const name of [...files.keys()].sort()) {
    h.update(name);
    h.update("\0");
    h.update(files.get(name));
    h.update("\0");
  }
  return h.digest("hex");
}

function readUpstreamMeta(dir) {
  try {
    return JSON.parse(fs.readFileSync(path.join(dir, ".upstream.json"), "utf8"));
  } catch {
    return null;
  }
}

/**
 * 写入一个 skill 目录。
 * @returns {"added"|"updated"|"unchanged"}
 */
export function writeSkill(root, source, id, files, meta) {
  const dir = skillDir(root, source, id);
  const hash = contentHash(files);
  const prev = readUpstreamMeta(dir);
  if (prev && prev.contentHash === hash) return "unchanged";

  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
  for (const [name, buf] of files) {
    // 防 zip-slip：拒绝绝对路径与 .. 逃逸
    const target = path.join(dir, name);
    if (!target.startsWith(dir + path.sep)) continue;
    // 异常 zip 结构（如同名文件与目录共存）不阻断整个 skill
    try {
      fs.mkdirSync(path.dirname(target), { recursive: true });
      fs.writeFileSync(target, buf);
    } catch (e) {
      console.warn(`  [writer] 跳过无法写入的文件 ${id}/${name}: ${e.message}`);
    }
  }
  const upstream = { ...meta, contentHash: hash, fetchedAt: new Date().toISOString() };
  fs.writeFileSync(path.join(dir, ".upstream.json"), JSON.stringify(upstream, null, 2) + "\n");
  return prev ? "updated" : "added";
}

export function removeSkill(root, source, id) {
  const dir = skillDir(root, source, id);
  if (!fs.existsSync(dir)) return false;
  fs.rmSync(dir, { recursive: true, force: true });
  return true;
}

// 收集磁盘上某目录的所有文件 → Map<相对路径, Buffer>
export function collectFiles(dir) {
  const files = new Map();
  const walk = (d, prefix) => {
    for (const entry of fs.readdirSync(d, { withFileTypes: true })) {
      const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
      const full = path.join(d, entry.name);
      if (entry.isDirectory()) walk(full, rel);
      else if (entry.isFile()) files.set(rel, fs.readFileSync(full));
    }
  };
  walk(dir, "");
  return files;
}
