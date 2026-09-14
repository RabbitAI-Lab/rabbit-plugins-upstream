---
name: xhs-note-batch-export
description: 批量导出指定小红书博主主页「笔记」tab 的全部公开笔记为本地 Markdown（每篇含标题/原文链接/正文/图片与视频 URL/互动数赞藏评），支持 count/offset/parallel。当用户要求"把某博主的小红书笔记全导出来""导出博主公开笔记用于个人学习/归档""小红书主页笔记备份/喂 AI 分析"时使用。
---

# xhs-note-batch-export

## 功能描述
把任意指定小红书博主的公开笔记批量导出为本地 Markdown 文件。每篇笔记一个 md，包含：标题、原文链接（带 xsec_token）、正文文字、图片/视频 URL（仅存 URL，不下载本地）、互动数（赞/藏/评）。用于对标分析、内容研究、长期备份、喂 AI 等场景。

## 前置条件
- wc3-chrome 扩展已安装，relay 服务已启动（Extension Relay HTTP API，端口 3459）
- 浏览器已登录小红书（未登录可能只能看到部分笔记或触发登录页）
- 本 skill 为纯浏览器自动化，不含 LLM 子会话，无需 pipeline 子会话服务

## 使用方式
```bash
node skill.mjs <input.json>
```
stdout 只输出一行 JSON：`{ status, summary, output_dir }`，status 为 `success` / `partial` / `failed`。

## 入参（input.json）
- `profileUrl`（string，必填）：博主小红书个人主页 URL，如 `https://www.xiaohongshu.com/user/profile/<24位hex>?xsec_token=...`
- `count`（number，可选，默认 10）：本次导出笔记数量上限；设 -1 或 0 表示导出全部可达笔记
- `offset`（number，可选，默认 0）：从第几篇开始导出（分批/断点续导）
- `parallel`（number，可选，默认 1，上限 3）：详情抓取并发 tab 数，超过 3 按 3 处理
- `outputDir`（string，可选，默认 `./xhs-note-batch-export-output/`）：md 输出目录；若提供 `output_dir`（绝对路径）则以它为准
- `output_files`（object，可选）：`{ data, result }` 自定义 data.md / res.json 文件名

## 输出格式
`<outputDir>/` 下每篇笔记一个文件 `<序号>_<笔记名>.md`（序号从 offset 延续递增，笔记名取标题去非法字符并截断 50 字符），外加汇总文件：

```
# <标题>
原文链接: https://www.xiaohongshu.com/explore/<note_id>?xsec_token=...
互动: 赞<赞数> 藏<藏数> 评<评论数>（互动数未读到标 (partial)）
---
<正文文字>
---
图片: <URL1> <URL2> ...（若有）
视频: <视频URL>（若有）
```

- `summary.json`：`{ total_exported, offset, count, parallel, total_available, skipped_partial: [note_id...], failures: [...] }`
- `res.json`：状态/摘要元信息（pipeline 约定）
- `data.md`：全部记录数据（pipeline 约定）

## 注意事项
- 博主主页是虚拟列表，DOM 只保留视口附近卡片，脚本通过滚动持续收集，进度以 note_id 去重集合判断
- 排序 = 博主主页笔记 tab 默认排序（最新发布在前），脚本按页面实际顺序取数，不做额外排序
- 详情抓取并发上限 3（`parallel`）；若页面跳转至登录/验证页，脚本会停止操作并提示用户手动处理，不自动重试
- 互动数渲染慢于正文，脚本会轮询最长约 18s，仍缺则该篇标记 `(partial)`
