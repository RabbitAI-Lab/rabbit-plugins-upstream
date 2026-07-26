// sync-state.json 读写：增量同步状态持久化。
import fs from "node:fs";
import path from "node:path";

export function loadState(root) {
  const file = path.join(root, "sync-state.json");
  if (!fs.existsSync(file)) return {};
  try {
    return JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (e) {
    console.warn(`[state] sync-state.json 解析失败，按空状态处理: ${e.message}`);
    return {};
  }
}

export function saveState(root, state) {
  const file = path.join(root, "sync-state.json");
  const tmp = file + ".tmp";
  fs.writeFileSync(tmp, JSON.stringify(state, null, 2) + "\n");
  fs.renameSync(tmp, file);
}
