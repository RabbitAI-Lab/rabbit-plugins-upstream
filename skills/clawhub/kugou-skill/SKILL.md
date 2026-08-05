---
name: kugou-skill
description: |
  酷狗，酷狗音乐，酷狗skill，酷狗音乐skill，酷狗音乐助手
  提供歌曲搜索、每日推荐、相似推荐、收藏管理、听歌统计、酷狗榜单、创建歌单等功能。
  
  **触发场景**（满足任一即使用本技能）：
  - 用户要求推荐歌曲、听歌建议
  - 用户要求搜索歌曲、查找歌手作品
  - 用户要求查看音乐榜单（飙升榜、TOP500、抖音热歌等）
  - 用户要求查看收藏、最近播放、听歌统计
  - 用户要求创建歌单、自建歌单
  - 用户提供 secret（base64 字符串）要求登录或导入身份
  - Agent 在尝试扫码登录时遇到环境限制（无法发图片）→ 主动询问用户是否可提供 secret
  - 用户提到"酷狗"、"kugou"、"每日推荐"、"相似歌曲"
  
  **与其他音乐技能的区别**：酷狗音乐以推荐算法见长，榜单数据实时更新，适合获取热门歌曲和个性化推荐。
  
  安装方式：npm install -g @kg-ai/kugou-skill
---

# kugou-skill

## AI 使用工作流（优先阅读）

使用本工具时的标准流程：

```
1. 检查安装 → npm install -g @kg-ai/kugou-skill
2. 检查登录 → kugou-cli auth status
3. 登录决策（关键决策点，不要跳过）：
   ├─ 已登录（logged_in: true）→ 直接进入第 4 步
   ├─ 未登录 → 先询问用户："你手上是否已有可用的 base64 secret？"
   │   - 用户明确说"有" → 调 kugou-cli auth set-secret "<secret>"，跳过扫码
   │   - 用户说"没有"或不确定 → 走标准扫码流程
   │   - 当前环境无法渲染远程 URL 图片（纯文本 agent / 客户端无法访问外网 / 不支持 Markdown 渲染）→ 强制走 set-secret
   └─ 默认行为：除非用户明确说"我有 secret"，否则优先走扫码
4. 引导登录（详见 references/auth.md）：
   - 扫码：auth login 拿 `qrcode_image_url` → 用 Markdown 图片语法直接 inline 给用户（不要只给 URL）
   → 阶段 A：主动循环 auth status 最多 5 次（2-3s 间隔），覆盖秒扫
   → 阶段 B：5 次仍 waiting → 停下，主动提示用户扫码，等用户**主动回复"已扫码"**
   → 阶段 C：用户回复后调一次 status 验证；logged_in: true 即完成
   - 导入 secret：auth set-secret "<secret>" 一次完成
5. 执行用户请求的音乐命令（详见 references/music.md）
6. 解析 JSON 输出，按展示规范展示给用户（详见 references/output-format.md）
```

### 关键注意事项

- **登录流程极简**（详见 [references/auth.md](references/auth.md)）：
  1. `auth login` - 获取二维码，输出包含 `qrcode`（字符串标识，给上游用）和 `qrcode_image_url`（**酷狗上游的图片 URL**，Agent 用它渲染）
  2. **建议把二维码图片直接渲染到聊天窗口**（用户在窗口里能看到图片本身），**避免**只输出 URL 让用户手动打开：
     - 首选：在消息正文中输出 `![酷狗登录二维码](<qrcode_image_url>)` 这种 Markdown 图片语法，让客户端拉取并渲染该 URL
     - 备选：若平台支持把 URL 转为原生图片附件（image attach 工具等），可作为附件直接展示
     - **避免**输出"二维码 URL 是 xxx，请打开扫码"这种纯文字提示 —— 用户最好能直接在聊天窗口看到图片
     - **若当前 agent 工具集确认没有 URL 图片渲染能力**（纯文本通道、不支持 Markdown、客户端无法访问外网 URL）→ **跳过扫码**，直接告诉用户"当前环境无法显示二维码，请提供 base64 secret 字符串"并改走 `auth set-secret`
   3. **图片发送后两阶段行为（关键）**：
      - **阶段 A（主动轮询）**：图片刚展示，**先主动**循环调 `auth status` 最多 5 次（每次间隔 2-3 秒），覆盖用户秒扫的情况
      - **阶段 B（等待用户反馈）**：5 次仍 `waiting` → **停下来**，主动告诉用户："请用酷狗 APP 扫码登录，扫完后告诉我已扫码"，**不再调 status**，等用户**主动回复"已扫码"**才进入阶段 C
      - **阶段 C（验证登录）**：用户回复"已扫码" → 调一次 `auth status` 验证；返回 `logged_in: true` 继续执行，`scanned` 等几秒再调，`failed` 重新 `auth login` 拿新图
      - 若用户回复"没看到图片" / "图片打不开" → 立即放弃扫码，切换到 `set-secret` 路径
   4. `auth status` - **单次查询，不内部轮询**：每次调用只查一次扫码状态。完整流程见上方"两阶段行为"。**不要**等"内部已轮询"——根本不会自动轮询。
- **直接导入 secret 登录**：当用户**已经持有**一个有效的 base64 secret 字符串（从别处获取的），直接调用 `kugou-cli auth set-secret "<secret>"` 即可完成登录，**跳过扫码流程**。这与扫码登录保存到同一份 `auth.json`，效果完全一致。secret 字符串含 `+` `/` `=` 是正常的，shell 里务必用引号包起来。**何时考虑用 set-secret**：用户明确说"我有 secret"、当前环境无法渲染 `qrcode_image_url`、用户之前已经登录过想换设备。
- **登出 (auth logout)**：会**先**与服务端同步登出，**确认成功后才**清理本地登录态。失败时本地态保留、可重试；未登录时幂等直接返回成功。失败时 Agent **自动重试 1 次**（网络抖动常见），仍失败再询问用户是否重试，**不要**擅自清理本地文件。
- **登录态自动失效**：当任意 `music` 命令遇到登录态过期时，CLI 会**自动清理**本地登录态，并在 stderr 输出 `账号登录过期，请重新登录`，exit code 非 0。Agent 收到该错误后：
  1. **不要**自己再调一次 `music` 命令（会再次失败）
  2. **不要**手动清理本地文件
  3. **直接**引导用户重新登录：先问"你手上是否已有新 secret？"，有则 `auth set-secret`，没有则 `auth login` 走扫码
  4. 重新登录后，**先调 `auth status` 确认** `logged_in: true`，再重试之前失败的 `music` 命令
  - **状态字段差异**：`auth status` 在"无登录态"和"登录态过期被自动清理"两种场景下都返回 `{"logged_in": false}`（**不带 status 字段**）；"等待扫码"才返回 `{"logged_in": false, "status": "waiting"}`。Agent 区分场景应看 `music` 命令的 stderr 输出，不要只看 status 字段。完整状态表见 [references/auth.md#状态表](references/auth.md#状态表)。
- **音乐命令依赖登录**：除了 `auth`、`install`、`version`、`--help` 以外，所有 `music` 子命令都需要先登录。如果收到 `"not logged in"` 错误，引导用户执行登录流程。
- **自动更新机制**：每次启动任意命令时会自动检测 npm 远端版本，若有新版会**自动执行** `npm install -g @kg-ai/kugou-skill@latest`，无需手动 `kugou-cli update`：
  - 关闭自动检查：加 `--no-update-check` 标志，或设置环境变量 `KUGOU_CLI_NO_UPDATE_CHECK=1`
  - 手动检查/触发：`kugou-cli update` 跳过本地缓存直接查远端并自动安装；`kugou-cli update --check` 仅检查不安装
  - 非 npm 安装（手动编译/容器）会打印提示和升级命令但不会自动执行
- **输出均为 JSON**：所有命令输出原始 JSON 到 stdout，错误输出到 stderr。解析 `errcode` 字段判断成功与否（`0` 为成功）。
- **歌曲展示规范**（详见 [references/output-format.md](references/output-format.md)）：**禁止**只返回歌曲名、歌手名，**必须**以 Markdown 链接格式展示播放链接。
- **创建歌单的调用原则**（详见 [references/music.md#8-创建歌单](references/music.md#8-创建歌单)）：
  1. **被动调用**：必须用户**明确**要求创建歌单时才调用 `music create-playlist`，禁止在用户仅说"推荐/搜歌"时主动创建
  2. **主动询问**：当通过搜索、推荐（猜你喜欢/相似/文本）等方式给出一批歌曲后，**必须**询问用户是否需要将当前这批歌曲创建为歌单，等用户确认后再调用 `music create-playlist --songs "<mix_song_id 列表>"`

---

## 基础信息

- **npm 包**: @kg-ai/kugou-skill
- **二进制命令**: kugou-cli
- **安装方式**: `npm install -g @kg-ai/kugou-skill`

---

## 详细文档索引

| 文档 | 说明 |
|------|------|
| [references/auth.md](references/auth.md) | 认证命令：扫码登录、直接设置 secret、查看状态、登出 |
| [references/music.md](references/music.md) | 音乐命令：搜索、推荐、收藏、统计、榜单、创建歌单 |
| [references/install.md](references/install.md) | 安装命令：SKILL.md 安装到各平台 |
| [references/update.md](references/update.md) | 更新命令：检查/执行自动更新 |
| [references/output-format.md](references/output-format.md) | 输出格式与展示规范 |
| [references/error-handling.md](references/error-handling.md) | 错误处理与常见错误 |

---

## 完整使用流程

```bash
# 1. 登录（极简流程，详见 references/auth.md）
kugou-cli auth login                      # 获取二维码
# auth status 是单次查询，agent 需要外层循环调用，每次间隔 2-3 秒
kugou-cli auth status

# 1'. 或者直接导入已持有的 secret（跳过扫码）
kugou-cli auth set-secret "<base64-secret>"

# 2. 搜索歌曲
kugou-cli music search "周杰伦"

# 3. 获取猜你喜欢
kugou-cli music recommend guess

# 4. 查看我的收藏
kugou-cli music favorites

# 5. 查看最近播放
kugou-cli music recent

# 6. 查看听歌统计
kugou-cli music stats

# 7. 查看抖音热歌榜
kugou-cli music charts 52144

# 8. 创建歌单
kugou-cli music create-playlist "我的空歌单"
kugou-cli music create-playlist "我的批量歌单" --songs "32068120,233125060"
```
