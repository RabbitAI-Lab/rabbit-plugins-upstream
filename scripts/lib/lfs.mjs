// Git LFS 指针检测与真实内容解析。
// GitHub tarball 中 LFS 文件只含指针文本；直接镜像会在 push 时被 GH008 拒收。
// 这里在写入前把指针替换为真实内容（公开仓库的 LFS batch API 无需额外权限）。
// 大文件下载走系统 curl（Node 内置 fetch 的 undici 有 300s body 超时，慢网络下不够用）。
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fetchJson } from "./http.mjs";

const POINTER_RE = /^version https:\/\/git-lfs\.github\.com\/spec\/v1\noid sha256:([0-9a-f]{64})\nsize (\d+)\n?/;

export function parseLfsPointer(buf) {
  if (buf.length > 1024) return null;
  const m = POINTER_RE.exec(buf.toString("utf8"));
  return m ? { oid: m[1], size: Number(m[2]) } : null;
}

function downloadFile(url) {
  const tmp = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "lfs-")), "obj");
  try {
    execFileSync("curl", ["-sfL", "--retry", "3", "--max-time", "1800", "-o", tmp, url], { stdio: "pipe" });
    return fs.readFileSync(tmp);
  } finally {
    fs.rmSync(path.dirname(tmp), { recursive: true, force: true });
  }
}

/**
 * 扫描 files（Map<路径, Buffer>），把其中的 LFS 指针替换为真实内容。
 * 任一对象解析失败直接抛出（由调用方记为 skill 失败，下轮重试），避免镜像进指针文件。
 * @returns {Promise<number>} 解析的 LFS 文件数
 */
export async function resolveLfsFiles(repoKey, files, headers = {}) {
  const pointers = [];
  for (const [name, buf] of files) {
    const p = parseLfsPointer(buf);
    if (p) pointers.push({ name, ...p });
  }
  if (!pointers.length) return 0;

  const res = await fetchJson(`https://github.com/${repoKey}.git/info/lfs/objects/batch`, {
    method: "POST",
    headers: {
      accept: "application/vnd.git-lfs+json",
      "content-type": "application/vnd.git-lfs+json",
      ...headers,
    },
    body: JSON.stringify({
      operation: "download",
      transfers: ["basic"],
      objects: pointers.map(({ oid, size }) => ({ oid, size })),
    }),
  });

  const byOid = new Map();
  for (const obj of res.objects || []) {
    if (obj.actions?.download?.href) byOid.set(obj.oid, obj.actions.download.href);
  }
  for (const p of pointers) {
    const href = byOid.get(p.oid);
    if (!href) throw new Error(`LFS 对象无下载地址: ${p.name} (${p.oid.slice(0, 12)})`);
    files.set(p.name, downloadFile(href));
  }
  return pointers.length;
}
