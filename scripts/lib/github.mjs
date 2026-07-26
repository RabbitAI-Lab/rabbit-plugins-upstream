// GitHub 仓库拉取工具：仓库信息 + tarball 下载解压到临时目录。
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fetchJson, fetchBuffer } from "./http.mjs";

const TOKEN = process.env.GITHUB_TOKEN || "";

export function ghHeaders() {
  const h = { accept: "application/vnd.github+json" };
  if (TOKEN) h.authorization = `Bearer ${TOKEN}`;
  return h;
}

// key: "owner/repo" → { pushedAt, branch }
export async function getRepoInfo(key) {
  const info = await fetchJson(`https://api.github.com/repos/${key}`, { headers: ghHeaders() });
  return { pushedAt: info.pushed_at, branch: info.default_branch };
}

/**
 * 下载并解压仓库 tarball 到临时目录。
 * @returns {{ dir: string, cleanup: () => void }} dir 为解压后的仓库根目录
 */
export async function fetchRepoDir(key, branch) {
  const tarBuf = await fetchBuffer(`https://api.github.com/repos/${key}/tarball/${branch}`, {
    headers: ghHeaders(),
    timeoutMs: 300_000,
  });
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "gh-repo-"));
  try {
    const tarFile = path.join(tmp, "repo.tar.gz");
    fs.writeFileSync(tarFile, tarBuf);
    execFileSync("tar", ["-xzf", tarFile, "-C", tmp], { stdio: "pipe" });
    fs.rmSync(tarFile);
    const top = fs.readdirSync(tmp).find((d) => fs.statSync(path.join(tmp, d)).isDirectory());
    if (!top) throw new Error("tarball 解压后为空");
    return { dir: path.join(tmp, top), cleanup: () => fs.rmSync(tmp, { recursive: true, force: true }) };
  } catch (e) {
    fs.rmSync(tmp, { recursive: true, force: true });
    throw e;
  }
}
