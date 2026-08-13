---
name: xhs-publisher
slug: dqsjqian-xhs-publisher
displayName: 小红书笔记发布
version: 1.0.0
description: |
  小红书笔记「登录 + 发布」通用 skill。输入本地 markdown 文案 + 图片，通过 xiaohongshu-mcp 一键发布图文笔记并回查 note_id。
  只负责登录与发布，不负责内容创作（文案、配图由调用方自己准备）。
  触发词：发布小红书、发小红书笔记、xhs 发布、xhs publish、小红书登录、把这篇 md 发到小红书。
  依赖：本机已安装 xiaohongshu-mcp（v2.4.3+）。
description_zh: 小红书笔记登录与发布
description_en: Xiaohongshu login & publish
disable: false
agent_created: true
---

# xhs-publisher — 小红书登录与发布

只做两件事：**登录**、**发布**。不碰内容创作。给一个 markdown 文案 + 若干图片路径，产出一个已发布的图文笔记（含 note_id）。

## 何时用

- 已有文案和配图，要推到小红书。
- 定时任务 / 自动化里的发布环节。
- 只想接好「最后一公里」——把本地素材变成已发布笔记。

## 前置条件（一次性）

1. **xiaohongshu-mcp ≥ v2.4.3**（旧版会报「没有找到发布 TAB - 上传图文」）。macOS Apple Silicon：

   ```bash
   curl -sL -o /tmp/xhs-mcp \
     "https://github.com/xpzouying/xiaohongshu-mcp/releases/download/v2.4.3/xiaohongshu-mcp-darwin-arm64"
   install -m 755 /tmp/xhs-mcp ~/.local/bin/xiaohongshu-mcp
   ```

   首次启动会下载内置 Chromium（约 150MB，1.5 分钟，仅一次）。Linux x64 / Windows 把文件名换成对应平台即可。

2. **启动 MCP 服务**（macOS 直接 nohup，官方 start-mcp.sh 的 Xvfb 逻辑只适用 Linux 无头服务器，在 macOS 会失败）：

   ```bash
   COOKIES_PATH="$HOME/.xiaohongshu/cookies.json" \
     nohup ~/.local/bin/xiaohongshu-mcp -port ":18060" \
     > "$HOME/.xiaohongshu/mcp.log" 2>&1 &
   ```

   端口默认 18060，可用 `XHS_MCP_URL` 覆盖（本 skill 脚本读取该环境变量）。

3. **登录**（cookies 约 30 天过期，过期需人工扫码）：
   - 检查：`python3 scripts/publish.py check`
   - 未登录 → 调 `get_login_qrcode` 取二维码给用户，用小红书 App 扫码 + 点「确认登录」。
   - App 扫码后若显示 6 位核对验证码，**直接在 App 确认即可，无需回填**。

## 发布用法

```bash
# 检查 MCP 服务 + 登录状态
python3 scripts/publish.py check

# 发布单篇（标题缺省取 md 第一行 `# 标题`，可用 --title 覆盖）
python3 scripts/publish.py /path/to/note.md

# 批量发布目录下所有 .md
python3 scripts/publish.py --dir /path/to/posts/
```

脚本内部走 MCP Streamable HTTP（长超时 300s，比官方 mcp-call.sh 的 120s 更稳），发布后自动调 `get_my_profile` 回查并打印 `NOTE_ID`。

### markdown 输入格式约定

```markdown
# 标题（≤20 字）
正文第一段……（口语化，可带 emoji）

#话题1 #话题2 #话题3
---
## 配图（可选：表格列出图片路径，相对路径相对于 md 所在目录）
| # | 文件 |
|---|------|
| 1 | ./img/cover.jpg |
| 2 | ./img/chart.png |
```

- 标题：`# ` 开头的那行；超过 20 字会告警，建议 `--title` 传入短标题。
- 正文：标题之后、`---` 分隔线之前的所有内容（含 `#话题` 行）。
- 标签：从正文里的 `#话题` 自动提取；重复自动去重。
- 图片：从表格里任意 `.jpg/.png/.jpeg/.webp` 路径提取，按出现顺序上传；至少 1 张。

## Pitfalls（踩过的坑）

1. **MCP 必须 ≥ v2.4.3**：旧版发布报「没有找到发布 TAB - 上传图文」+ 反复「发布 TAB 被遮挡」，是小红书创作者中心改版、旧选择器失效。
2. **登录二维码只调一次**：`get_login_qrcode` 单会话约束，「开新的取消旧的」。连续调用会让用户扫到被取代的旧码 → 表现为「明明已登录但 check 仍未登录」。
3. **macOS 别走官方 start-mcp.sh**：`ensure_display` 缺 Xvfb 会 exit 1。headless 默认 true，直接 nohup 二进制即可。
4. **配图路径要精确到扩展名**：表格里路径后常带全角括号尺寸注释 `（1920×1280）`，解析用 `[\w\-./]+\.(?:jpg|png|jpeg|webp)` 精确匹配，别用 `[^\s）)]+`（会连括号内容一起吞 → 图片文件不存在 → 发布卡死超时）。
5. **发布超时**：单篇约 2 分钟（上传多图 + 填标题正文 + 点标签）。官方 mcp-call.sh 的 curl `--max-time 120` 会超时返回空（服务端其实会继续并成功）。本脚本自带 300s 长超时。
6. **note_id 不在 publish 返回值里**：`publish_content` 成功只回「内容发布成功: &{Title...}」，note_id 要用 `get_my_profile` 从 feeds 按标题匹配，脚本已内置。
7. **cookies 服务端会提前失效**：客户端 expires 可能显示很久，但服务端长期不用会踢。自动化开始先 `check`，未登录先扫码再继续。

## 验证清单

- [ ] `publish.py check` 返回「已登录」
- [ ] 标题 ≤ 20 字、正文 ≤ 1000 字、图片 ≥ 1 张
- [ ] 发布后拿到 `NOTE_ID`，`get_my_profile` 里标题能对上

## 依赖

- **xiaohongshu-mcp**：底层发布引擎（开源 <https://github.com/xpzouying/xiaohongshu-mcp>）。本 skill 只负责流程编排 + 解析 + 长超时调用；MCP 工具清单（check_login_status / publish_content / get_my_profile / get_login_qrcode 等）以该仓库 README 为准。
