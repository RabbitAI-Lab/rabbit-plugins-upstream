---
name: douyin-video-publish
slug: douyin-video-publish
displayName: 抖音自动发布
version: 1.0.0
description: 内容做好之后的抖音自动发布。成品视频 + 文案就绪后，一条命令完成上传、填标题、写简介与话题、归入合集、设定时发布；支持按天批量双更排期，一次配好让系列内容自己往下发。也能对账「哪些排上了哪些没排」、清理重复预约。当用户说「发抖音」「抖音定时发布」「抖音排期」「抖音上传视频」「抖音批量发布」「查抖音排了哪些」时使用。
agent_created: true
---

# 抖音自动发布

## 它接的是哪一段

**内容生产之后的那一段。**

成品 mp4 和文案已经就绪，接下来要在创作者中心重复这些动作：传视频、填标题、写简介、加话题、选合集、勾定时、点发布。每条视频都要重来一遍，跟内容质量无关，但必须人肉完成。

本 skill 把整段收敛成一条命令，并支持**按天批量双更排期**。

| 它负责 | 它不负责 |
|---|---|
| 上传成品视频 | 剪辑、合成、加字幕 |
| 填标题、简介、话题（纯文本 `#tag`） | 写文案、想选题 |
| 归入合集 | 做封面、生成素材 |
| 设定时 / 批量双更排期 | 删除已发布内容（有播放数据的，本 skill 不做） |
| 发完之后：对账队列、清理重复预约 | 互动、评论、看数据 |

## When to use

- 「把这条视频发抖音」「抖音定时 10-15 07:00」
- 「这 30 期排一下，每天早七点晚七点各发一条」
- 「抖音上哪些排上了哪些没排」
- 「有两条重复的，删掉一条」

## 前置条件

1. Chrome 带远程调试端口、独立 profile 启动：
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
     --remote-debugging-port=9222 --user-data-dir=/Users/jx/ChromeAutomation &
   ```
   在该浏览器里**登录抖音创作者中心**（creator.douyin.com）。会话会过期。
2. node 依赖：`puppeteer-core`（在 `/Users/jx/.workbuddy/binaries/node/workspace/node_modules`）
3. 跑之前清代理：
   ```bash
   unset http_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY ALL_PROXY NODE_OPTIONS
   export NO_PROXY='127.0.0.1,localhost'
   ```
   Bash 工具里需要 `dangerouslyDisableSandbox: true`。
4. ⚠️ **登录态掉时会连续失败**，先确认 9222 上能打开 creator.douyin.com。

## Workflow

### Step 1 — 单条发布

```bash
# 从 xip-epNN 目录自动读 output.mp4 + xhs-copy.txt（标题/正文/话题）
node scripts/dy-publish.js --ep 02 --time "2026-10-15 07:00"

# 或手工指定
node scripts/dy-publish.js --file a.mp4 --title "标题" --desc "正文" \
  --topics "#a #b" --album "怎么活得更好" --time "2026-10-15 07:00"

# 演练：填完不提交
node scripts/dy-publish.js --ep 02 --time "2026-10-15 07:00" --dry
```

退出码：`0` 成功｜`1` 失败｜`2` 参数错｜`3` 登录态失效｜`4` 超出定时窗口

### Step 2 — 批量双更排期

```bash
# 默认 ep04–ep29，从 10-16 07:00 起，07:00/19:00 交替
zsh scripts/batch-dy.sh

# 自定义窗口
START_EP=30 END_EP=30 START_DAY=29 START_HOUR=07 zsh scripts/batch-dy.sh
```

脚本逐条调用 `dy-publish.js`，日志写 `dy-batch.log`，末尾输出成功/失败计数。
**每条约 45–60 秒**（视频上传占大头），26 条约半小时。

### Step 3 — 对账

```bash
node scripts/dy-status-list.js 全部      # 概览
node scripts/dy-queue.js 全部            # 卡片式滚动累积抓取（虚拟列表，必须用这个）
node scripts/dy-search.js "标题关键词"    # 查某条是否重复/是否排上
```

### Step 4 — 建合集（首次或加新系列）

```bash
NAME="怎么活得更好" DESC="系列简介" COVER=/path/cover.png node scripts/dy-create-collection.js
```
封面必填：1080×1080、≤5M。传图后会弹裁剪框，脚本会自动点「保存」。

### Step 5 — 清理重复预约

```bash
KW="标题关键词" IDX=2 node scripts/dy-del-dup.js          # 默认 DRY
KW="标题关键词" IDX=2 DEL=1 node scripts/dy-del-dup.js    # 真删
```

## 硬约束（踩过就知道疼）

| 项 | 限制 |
|---|---|
| 定时发布 | **2 小时后 ~ 14 天内**（超出脚本直接中止，退出码 4） |
| 作品标题 | ≤30 字 |
| 作品简介 | ≤1000 字 |
| 合集标题 | ≤20 字 |
| 合集简介 | ≤200 字 |
| 合集封面 | 1080×1080、≤5M，**必填** |
| 每 14 天窗口 | 双更排期 **最多排 28 条**，更多要滚动窗口补排 |

## 关键坑位（改脚本前先读 `references/troubleshooting.md`）

1. **定时控件必须用 native setter 注入**：semi-datepicker 的 input 是可键入的，
   但三击全选 / Meta+A 都无效。要用 `Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set` + `dispatchEvent(new Event('input'))`，再回车。
2. **页面上有两个含"合集"的下拉**：左边是合集**类型**（innerText 就是"合集"），右边才是选具体合集（"请选择合集"）。用 `includes('合集')` 会点错。
3. **上传完成判据**：必须 `出现"重新上传" 且 不含"取消上传"`。只看前者会在 85% 就误判完成，此时右侧进度浮层仍在，会吞掉后续所有点击。
4. **标题 input 用 `input[placeholder*="作品标题"]`** 定位（maxLength 不稳定，测过是 -1）。
5. **简介是 editor-kit 富文本**：先在 `evaluate` 里 `focus()`，再用 CDP `Input.insertText` 整段注入。按坐标点击在元素滚出视口时会落空。
6. **话题不用点选**：纯文本 `#tag` 直接写进简介即可，无需从下拉选择。
7. **定时预约内容不在「审核中」筛选里**：审核状态只有 全部/已发布/审核中/未通过，预约内容在「全部」中显示为「定时发布中：X年X月X日 HH:mm」。
8. **列表是虚拟滚动**：`body.innerText` 一次只渲染约 12 条，必须滚动累积去重（`dy-queue.js`）。
9. **「删除作品」按钮可批量定位**：搜索过滤后按 index 取第 N 个即可，弹窗文案是「确定要移除此作品吗」。

## 安全规则（不要跳过）

- 定时超 14 天窗口 → **中止，不发布**
- 标题/定时回填后会二次校验，不符就停
- **不勾选任何 AI 生成声明**（「自主声明」保持留空）——这是用户明确要求
- 删除仅限**重复的预约内容**（无播放数据）；已发布作品不删
- 批量失败时脚本继续跑完剩余条目，最后汇总计数，失败项单独重跑

## 文件

- `scripts/dy-publish.js` — 主发布脚本
- `scripts/batch-dy.sh` — 批量双更排期
- `scripts/dy-queue.js` — 虚拟列表滚动累积抓取（对账主力）
- `scripts/dy-status-list.js` — 按审核状态快速筛
- `scripts/dy-search.js` — 站内搜索核查重复
- `scripts/dy-create-collection.js` — 建合集
- `scripts/dy-del-dup.js` — 清理重复预约（默认 DRY）
- `references/troubleshooting.md` — 踩坑详解

## 相关

- 视频号发布见 skill `channels-video-publish`（DOM 结构完全不同，脚本不可互换）
- 小红书分发见 skill `xiaohongshu-video-publish`

## 更新日志

### v1.0.0（2026-10-15）
- 首次落地：上传 / 标题 / 简介+话题 / 合集 / 定时 / 批量双更 / 对账 / 建合集 / 清重复
- 实测：xip 系列 28 期一次排完（10-15 ~ 10-28 双更），0 失败
