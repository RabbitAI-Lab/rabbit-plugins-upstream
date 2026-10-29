# 小红书视频上传 · xhs-publish

用 CDP 接管一个**真实已登录的 Chrome**，把做好的视频和文案送进小红书创作服务平台。不走非官方接口、不伪造签名。

## 它解决什么

视频做好了、文案写好了，剩下的是"传上去、填对字段、归对合集、别发错、事后能对账"。这件事人工做一条要 5 分钟，批量做容易漏、容易重、容易点错按钮。这个 skill 把这一公里脚本化，并且把踩过的坑全写下来了。

## 能力范围

- **上传与填稿**：视频上传、标题（React native setter）、正文（tiptap 整段 `execCommand`）、话题（必须下拉点选）、原创声明、合集归属
- **草稿与定时**：按钮在闭包 shadow DOM 里，用 CDP 坐标扫描定位；`暂存离开` 与 `发布` 严格区分，脚本永不点发布
- **全量核对**：服务端笔记（已发布/审核中/未通过）+ 草稿箱，与本地文案做模糊比对，输出「已发布 / 草稿 / 未通过 / 缺失」四分类
- **故障排查**：登录失效、主线程超时、草稿全量消失、按钮点不动、笔记被判未通过

## 快速开始

```bash
# 1. 确保 Chrome 开着 9222 调试端口且已登录小红书
curl -s --noproxy '*' http://127.0.0.1:9222/json/version

# 2. 单期入草稿箱
SERIES=xip EP=03 COLLECTION="怎么活得更好" NO_CHAPTER=1 node scripts/xhs-draft-ep.js
EP=03 node scripts/xhs-save-draft.js

# 3. 批量（后台跑）
SERIES=xip COLLECTION="怎么活得更好" zsh scripts/batch-drafts.sh 03 05 06

# 4. 核对覆盖
node scripts/xhs-full-scan.js && node scripts/xhs-coverage2.js
```

脚本依赖本机路径，用前先读 [`scripts/README.md`](scripts/README.md)。

## 三条铁律

**1. 草稿是浏览器本地存储，不在服务端**

小红书发布页原文：「草稿存储于当前使用的浏览器本地，在清除浏览器数据时会被删除」。物理位置 `Profile 1/IndexedDB/https_creator.xiaohongshu.com_0.indexeddb.leveldb`。

- 草稿**不跨浏览器**——自动化 Chrome 里的草稿，你在自己日常 Chrome 登录同一账号看不到
- **别 kill 这个调试 Chrome**。强杀后重启可能触发 `Creating DB ... since it was missing`，草稿全量归零
- 每批入库后立刻 dump 一次留档

**2. 脚本只存草稿，发布由真人点**

平台能识别脚本化批量发布。2026-09 有 5 条笔记被判「利用 AI 托管进行发文/互动」，处置结果「该篇笔记已不可被他人查看」。要让脚本定时发布，先明确接受这个风险。

**3. 引流红线全场景生效**

简介、背景图、笔记、评论、私信都禁止微信/QQ/手机号/二维码/外链，以及「加v」「vx」「私信领资料」「扣1」这类暗示。谐音、图片水印、大小号联动都能识别。唯一官方许可的入口是把小红书号设成微信号。

## 关键坑位（完整的在 SKILL.md）

| 坑 | 现象 | 正解 |
|---|---|---|
| playwright 连 CDP | 握手卡死 | 改用 puppeteer-core 的 `puppeteer.connect` |
| 登录态在 Default | 打开是空的 | `profile.last_used` 常是 `Profile 1` |
| 话题写成纯文本 | 话题没生效 | 必须下拉点选（ArrowDown + Enter） |
| 正文逐字输入 | 格式丢、话题重复 | 整段 `execCommand('insertText')` |
| 按文本找按钮 | 找不到 | 按钮在闭包 shadow DOM，只能坐标扫描 |
| 滚动取笔记列表 | 只拿到 10 条 / 超时 | 改走 API + `_webmsxyw` 签名 |
| 笔记列表接口返回空 | 误判"0 条已发布" | `tab=0` 返 `display_title`，`tab=1/2/3` 返 `title` |
| 定时超出 14 天 | 静默回退 | 窗口 = 2 小时后 ~ 14 天内 |

## 兼容性

作者在 macOS + Chrome 155 上验证（2026-09 ~ 2026-10）。小红书创作服务平台前端结构变化会影响选择器，`SKILL.md` 里的探测方法（而不是写死选择器）是应对变化的关键。
