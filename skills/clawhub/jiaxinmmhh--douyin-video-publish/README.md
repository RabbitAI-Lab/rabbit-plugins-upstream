# douyin-video-publish · 抖音自动发布

**内容做好之后，把它发出去的那一段。**

成品 mp4 和文案已经就绪，接下来要在抖音创作者中心重复这些动作：传视频、填标题、
写简介、加话题、选合集、勾定时、点发布。每条视频都要重来一遍，跟内容质量毫无关系，
但必须人肉完成。

这个 skill 把整段收敛成一条命令，并且支持**按天批量双更排期**：一次配好，让系列内容
自己一天一天往下发。

支持 WorkBuddy / QClaw / ima / Claude Code / Cursor。

## 它做什么

```bash
node scripts/dy-publish.js --ep 02 --time "2026-10-15 07:00"
```

自动从 `xip-ep02/` 读 `output.mp4` 和 `xhs-copy.txt`（标题 / 正文 / 话题），
完成：上传视频 → 填标题 → 写简介 + 话题 → 归入合集 → 设定时 → 发布。

批量双更排期（做系列内容时最省时间的用法）：

```bash
START_EP=04 END_EP=29 START_DAY=16 START_HOUR=07 zsh scripts/batch-dy.sh
```

26 条约半小时跑完，日志落在 `dy-batch.log`，末尾汇总成功 / 失败计数。

| 负责 | 不负责 |
|---|---|
| 上传成品视频 | 剪辑、合成、加字幕 |
| 填标题、简介、话题（纯文本 `#tag`） | 写文案、想选题 |
| 归入合集 | 做封面、生成素材 |
| 设定时 / 批量双更排期 | 删除已发布内容（有播放数据，本 skill 不做） |
| 发完之后：对账队列、清理重复预约 | 互动、评论、看数据 |

## 为什么自己写脚本很麻烦

抖音创作者中心是 Semi Design + React 控件，每个坑都能耗掉一小时：

- **定时控件是三段式日期时间输入**：input 可键入，但三击全选、`Meta+A` 都无效，
  打出来会变成 `2026-10-152026-10-16 07:00 01:15` 这种鬼东西
- **页面上有两个都含「合集」的下拉**：左边是合集**类型**（innerText 就是「合集」），
  右边才是选具体合集。用 `includes('合集')` 必然点错那个打不开的
- **上传进度浮层会吞点击**：85% 时已经出现「重新上传」，但「取消上传」还在，
  此时判定完成 → 右侧浮层挡住所有控件 → 后续全落空
- **简介是 editor-kit 富文本**，不是 textarea：按坐标点击在元素滚出视口时静默失败
- **列表是虚拟滚动**：`body.innerText` 一次只渲染约 12 条作品，直接抓会少一大半
- **定时预约的内容不在「审核中」筛选里**：它躺在「全部」里，显示为「定时发布中」

每一个的解法都固化在 `references/troubleshooting.md`。

## 安装

把整个目录放到 skills 目录下即可：

```
~/.workbuddy/skills/douyin-video-publish/     # WorkBuddy
~/.claude/skills/douyin-video-publish/        # Claude Code
```

依赖：`puppeteer-core`。

## 前置条件

1. 带远程调试端口启动 Chrome（用独立 profile，别污染常用浏览器）：

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 --user-data-dir=/Users/jx/ChromeAutomation &
```

2. 在这个浏览器里**登录抖音创作者中心**（creator.douyin.com）。会话会过期，
   掉登录时脚本会连续失败，退出码 3。
3. 跑之前清代理（本机自带透明代理会劫持 127.0.0.1 之外的一切）：

```bash
unset http_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY ALL_PROXY NODE_OPTIONS
export NO_PROXY='127.0.0.1,localhost'
```

## 用法

```bash
# 单条：从 xip-epNN 目录自动读视频和文案
node scripts/dy-publish.js --ep 02 --time "2026-10-15 07:00"

# 单条：手工指定
node scripts/dy-publish.js --file a.mp4 --title "标题" --desc "正文" \
  --topics "#a #b" --album "怎么活得更好" --time "2026-10-15 07:00"

# 演练：上传 + 填完所有字段，但不点发布
node scripts/dy-publish.js --ep 02 --time "2026-10-15 07:00" --dry

# 批量双更：07:00 / 19:00 交替，日期逐天顺延
START_EP=04 END_EP=29 START_DAY=16 START_HOUR=07 zsh scripts/batch-dy.sh

# 对账：哪些排上了、哪些没排
node scripts/dy-queue.js 全部          # 虚拟列表滚动累积抓取（对账主力）
node scripts/dy-status-list.js 全部    # 按审核状态快速筛
node scripts/dy-search.js "关键词"      # 站内搜索核查是否重复

# 建合集（首次或加新系列）
NAME="怎么活得更好" DESC="系列简介" COVER=/path/cover.png \
  node scripts/dy-create-collection.js

# 清理重复预约（默认 DRY，只报告不删）
KW="关键词" IDX=2 node scripts/dy-del-dup.js
KW="关键词" IDX=2 DEL=1 node scripts/dy-del-dup.js   # 真删
```

### 退出码

| 码 | 含义 |
|---|---|
| 0 | 成功 |
| 1 | 失败 |
| 2 | 参数错 |
| 3 | 登录态失效，需重新登录 |
| 4 | 超出定时窗口（**未发布**） |

## 硬约束（踩过就知道疼）

| 项 | 限制 |
|---|---|
| 定时发布 | **2 小时后 ~ 14 天内**，超出脚本直接中止 |
| 作品标题 | ≤30 字 |
| 作品简介 | ≤1000 字 |
| 合集标题 | ≤20 字 |
| 合集简介 | ≤200 字 |
| 合集封面 | 1080×1080、≤5M，**必填** |
| 每 14 天窗口 | 双更排期**最多 28 条**，更多要滚动窗口补排 |

## 安全设计

- 定时超出 14 天窗口 → **中止，不发布**（退出码 4）
- 标题 / 时间回填后二次校验，不符预期就停
- **不勾选任何 AI 生成声明**（「自主声明」保持留空）
- 删除仅限**重复的预约内容**；已发布作品一律不碰
- 批量跑挂一条不影响后面的，最后汇总计数，失败项单独重跑

## 已知限制

- ✅ 已跑通：上传、标题、简介 + 话题、合集、定时、批量双更、对账、建合集、清重复
- ⚠️ 定时预约内容**筛不出来**，只能在「全部」里靠文案区分
- ⚠️ 作品总数是最好用的校验器：排 N 条后总数应精确增加 N，多出来就是重复了

详见 `references/troubleshooting.md`。

## 相关

- 视频号发布见 `channels-video-publish`（DOM 结构完全不同，脚本不可互换）
- 小红书分发见 `xiaohongshu-video-publish`

## License

MIT
