// 同步状态持久化：每个来源一个独立文件（sync-state/<source>.json），
// 保证三个来源的同步任务可以并行运行、各自提交，互不冲突。
import fs from "node:fs";
import path from "node:path";

function stateFile(root, source) {
  return path.join(root, "sync-state", `${source}.json`);
}

export function loadState(root, source) {
  const file = stateFile(root, source);
  if (!fs.existsSync(file)) return {};
  try {
    return JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (e) {
    console.warn(`[state] ${file} 解析失败，按空状态处理: ${e.message}`);
    return {};
  }
}

export function saveState(root, source, state) {
  const file = stateFile(root, source);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const tmp = file + ".tmp";
  fs.writeFileSync(tmp, JSON.stringify(state, null, 2) + "\n");
  fs.renameSync(tmp, file);
}
