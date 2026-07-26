// 公共配置与工具。
export const MAX_ITEMS = Number(process.env.SYNC_MAX_ITEMS || 3000);
export const CONCURRENCY = Number(process.env.SYNC_CONCURRENCY || 6);

// 把任意 id 转成安全的目录名（保留可读性，替换路径分隔与空白）
export function safeName(s) {
  return s.replace(/[\\/:*?"<>|\s]+/g, "-").replace(/^-+|-+$/g, "");
}
