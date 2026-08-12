---
name: kugou-skill
description: |
  酷狗，酷狗音乐，酷狗skill，酷狗音乐skill，酷狗音乐助手
  提供歌曲搜索、猜你喜欢、相似推荐、收藏管理、听歌统计、酷狗榜单、创建歌单等功能。

  **触发场景**（满足任一即使用本技能）：
  - 用户要求推荐歌曲、听歌建议
  - 用户要求搜索歌曲、查找歌手作品
  - 用户要求查看音乐榜单（飙升榜、TOP500、抖音热歌等）
  - 用户要求查看收藏、最近播放、听歌统计
  - 用户要求创建歌单、自建歌单
  - 用户提供 base64 secret 字符串要求登录或导入身份
  - Agent 在尝试扫码登录时遇到环境限制（无法发图片）→ 主动询问用户是否可提供 secret
  - 用户提到"酷狗"、"kugou"、"猜你喜欢"、"相似歌曲"
  - 用户要求让 PC/Mac 客户端播放歌曲、暂停、切歌、收藏、创建歌单
  - 用户提到酷狗 URL scheme（"kugou://" 或 "mackugou://"）
  - 用户提到"本机控制"、"控制酷狗客户端"

  **与其他音乐技能的区别**：酷狗音乐以推荐算法见长，榜单数据实时更新，适合获取热门歌曲和个性化推荐。

  安装方式：npm install -g @kg-ai/kugou-skill
---

# kugou-skill

## AI 使用工作流（优先阅读）

使用本工具时的标准流程：

```
1. 检查安装 → npm install -g @kg-ai/kugou-skill
2. 检查登录态 → kugou-cli auth status
3. 登录决策（按以下优先级严格判断，不要跳步）：
   ├─ 状态 a：已登录（logged_in: true）→ 跳到第 5 步
   ├─ 状态 b：未登录 + 用户**明确**说"我有 secret" → 调 `kugou-cli auth set-secret "<secret>"` 一次完成 → 跳到第 5 步
   ├─ 状态 c：未登录 + 当前环境**无法**渲染远程 URL 图片 **且** 无法读取本地二维码文件 → **强制**走 set-secret（同上）
   └─ 状态 d：未登录 + 其他所有情况 → 走扫码流程（第 4 步）

   注意：状态 b/c/d 互斥；不要在用户未明确给 secret 时擅自走 set-secret。
4. 引导登录——扫码（详见 references/auth.md）：
   - 执行 `auth login`，从输出读 `qrcode_img_url` 和 `qrcode_img_path`，按当前客户端能力选一种方式把二维码**直接展示给用户**
   - **阶段 A（主动轮询）**：图片刚展示，**主动**重试几次 `auth status`（每次隔几秒），覆盖用户秒扫场景
     - 任意一次返回 `logged_in: true` → 跳到第 5 步
     - 几次都返回 `waiting` 且未出现 `scanned` → 进入阶段 B
   - **阶段 B（等用户回复）**：停下，告诉用户"请用酷狗 APP 扫码登录，扫完后告诉我已扫码"，**不再调 status**，等用户**主动回复"已扫码"**
   - **阶段 C（验证一次）**：用户回复"已扫码"后，**调一次** `auth status`：
     - `logged_in: true` → 完成，跳到第 5 步
     - `scanned`（已扫但未确认）→ 等几秒再调一次，最多**额外**调几次，仍是 scanned 就告诉用户"手机端是否已点确认？"
     - `failed` 或 `{"logged_in": false}` → 重新 `auth login` 拿新图，从阶段 A 重新开始
5. 按请求类型分流：
   - **请求类型 A：控制已有歌 / 歌单 / 收藏**（用户已有 mixsongid 或 global_id）→ 直接执行 `control` 命令（详见 [references/control.md](references/control.md)），不需要先调 `music` 拿 ID
     - 例：`control play`、`control player --action pause`、`control favorite song --mixsongid <id>`、`control play-playlist --global-id <id>`
   - **请求类型 B：搜索后做某件事**（搜索歌曲/推荐/榜单 → 拿到 ID 后再做后续动作，如播放、收藏、建歌单）→ 先执行 `music` 命令拿数据，再按需转 `control`，详见 [references/music.md](references/music.md)
     - 例：先 `music search` 拿 mixsongid，再 `control play` 播放
     - 例：先 `music search-playlist` 拿 global_id，再 `control play-playlist` 播放
     - 例：先 `music search` 拿 mixsongids，再 `control playlist create --mixsongids` 创建客户端歌单
   - **请求类型 C：纯查询 / 统计 / 榜单**（不涉及本地客户端）→ 只走 `music` 命令
6. 解析 JSON 输出，按展示规范展示给用户（详见 [references/output-format.md](references/output-format.md)）
```

> **关键提醒**：**不要**在没有 mixsongid / global_id 的情况下盲目调用 `control` 命令（如 `control play --mixsongid ""`）—— `control` 命令在 ID 缺失时会报错。先用 `music` 命令把 ID 查出来，再传给 `control`。

---

## 关键注意事项

### 登录流程

`auth login` 命令输出三个字段供 Agent 选择二维码展示方式（详见 [references/auth.md](references/auth.md)）：

| 字段 | 用途 |
|------|------|
| `qrcode_img_path` | 本地二维码 PNG 文件路径 |
| `qrcode_img_url` | 远程二维码图片 URL |
| `qrcode` | 字符串标识，**Agent 不要使用**（仅供 CLI 内部） |

**根据当前客户端能力选择一种方式，把二维码图片直接展示在聊天窗口中**：

- 客户端支持读取或附加本地图片（如 Codex）→ 使用 `qrcode_img_path`，通过客户端的本地图片读取/附件能力展示
- 客户端支持 Markdown 外链图片（如 WorkBuddy）→ 在消息正文中输出 `![酷狗登录二维码](<qrcode_img_url>)`
- Agent 可以自行选择最适合当前环境的方式，不要同时展示两张二维码
- **不要**只把 URL 或本地路径作为普通文本发给用户，用户应直接看到二维码图片
- 首选方式展示失败时，立即切换到另一种方式：远程图片加载失败则尝试读取本地图片，本地图片无法读取则尝试远程 Markdown 图片
- 若两种方式都不可用 → 告诉用户"当前环境无法显示二维码，请提供 base64 secret 字符串"，改走 `auth set-secret`

**`auth status` 的调用约束**：

- 每次调用只查一次扫码状态，**不会内部自动轮询**。Agent 需要在外层按"阶段 A → 阶段 B → 阶段 C"循环调用（详见上方工作流第 4 步）
- 阶段 B 之后**不要**自己继续调用 status，等用户回复

### 直接导入 secret 登录

当用户**已经持有**一个有效的 base64 secret 字符串（从别处获取的），直接调用 `kugou-cli auth set-secret "<secret>"` 即可完成登录，**跳过扫码流程**——效果与扫码登录完全一致。secret 字符串含 `+` `/` `=` 是正常的，shell 里务必用引号包起来。

**何时考虑用 set-secret**：

- 用户明确说"我有 secret"
- 当前环境既无法展示远程图片也无法读取本地图片
- 用户之前已经登录过想换设备

### 登出

`auth logout` 命令：先与服务端同步登出，**确认成功后才**清理登录状态。失败时登录状态保留、可重试；未登录时幂等直接返回成功。

### 登录态自动失效

当任意 `music` 命令遇到登录态过期时，CLI 会自动取消登录（退出码非 0 + stderr 提示登录已过期）。Agent 收到该错误后：

1. **不要**自己再调一次 `music` 命令（会再次失败）
2. **直接**引导用户重新登录：先问"你手上是否已有新 secret？"，有则 `auth set-secret`，没有则 `auth login` 走扫码
3. 重新登录后，**先调 `auth status` 确认** `logged_in: true`，再重试之前失败的 `music` 命令

> Agent 不应依赖 stderr 文案字面量判断错误类型——以退出码和 references/error-handling.md 中的错误码说明为准。

### 音乐命令依赖登录

除了 `auth`、`install`、`version`、`--help` 以外，所有 `music` 子命令都需要先登录。如果 CLI 返回"未登录"错误，引导用户执行登录流程。

### 输出格式与成功判定

所有命令输出原始 JSON 到 stdout，错误输出到 stderr。**成功判定以退出码和 JSON 内的成功状态字段为准**（详见 [references/output-format.md](references/output-format.md)）。

### 歌曲展示规范

向用户展示音乐命令返回的歌曲列表时（详见 [references/output-format.md](references/output-format.md)）：

- **禁止**只返回歌曲名、歌手名
- **必须**以 Markdown 链接格式展示播放链接
- 正确格式：`[歌曲名 - 歌手名](https://www.kugou.com/...)`
- 禁止格式：`晴天 - 周杰伦`（无链接）、`歌曲名: 晴天, 歌手: 周杰伦`（无链接）

### 推荐理由规范

仅在 agent **主动推荐**场景下，歌曲列表之后**必须**追加一段 220-260 字的推荐理由（详见 [references/output-format.md#5-推荐理由主动推荐场景必写](references/output-format.md#5-推荐理由主动推荐场景必写)）：

- **触发**：`recommend guess / similar / text`、`charts`、`recommend-playlist`
- **不触发**：`search` / `search-playlist` / `favorites` / `recent` / `stats` / `playlist-songs`——用户主动查询不写
- **三层内容**：整体歌曲风格 + 匹配逻辑 + 挑 2-3 首基于行业认知的解读
- **字数硬约束**：220-260（含标点），超出或不足需重写

### 创建歌单的调用原则

详见 [references/music.md#7-创建歌单](references/music.md#7-创建歌单)：

1. **被动调用**：必须用户**明确**要求创建歌单时才调用，禁止在用户仅说"推荐/搜歌"时主动创建
2. **主动询问**：当通过搜索、推荐（猜你喜欢/相似/文本）等方式给出一批歌曲后，**必须**询问用户是否需要将当前这批歌曲创建为歌单，等用户确认后再调用
3. **硬性默认：优先客户端创建**：用户同意后**必须先尝试** `kugou-cli control playlist create`（在本地酷狗客户端内创建，详见 [references/control.md#10-playlist-create--创建歌单](references/control.md#10-playlist-create--创建歌单)），仅当客户端不可用（不支持的操作系统 / 未运行 / 无响应 / 调用失败）时才回退到云端 `music create-playlist`
4. **创建成功后主动询问是否播放**：无论走 `control playlist create` 还是 `music create-playlist`，**创建成功（返回成功状态）后必须主动询问用户"是否要播放这个歌单"**，等用户明确回复后再决定走哪条播放命令；用户拒绝则不做任何动作。播放路径选择：
   - 客户端可用：优先 `kugou-cli control play-playlist --global-id "<id>"`（详见 [references/control.md#12-play-playlist--播放整个歌单](references/control.md#12-play-playlist--播放整个歌单)）
   - 客户端不可用 / `play-playlist` 拿不到可用 ID：按 [references/music.md#72-云端歌单的播放控制浏览器打开-h5-链接](references/music.md#72-云端歌单的播放控制浏览器打开-h5-链接) 走"先探后告知"——用浏览器工具打开 H5 `song_list_url` 尝试点击播放；工具不可用时明确告知用户手动复制链接打开

---

## 基础信息

- **npm 包**: @kg-ai/kugou-skill
- **二进制命令**: kugou-cli
- **安装方式**: `npm install -g @kg-ai/kugou-skill`

> 关于更新：CLI 安装后会自动保持最新。具体更新机制与关闭开关见 [references/update.md](references/update.md)。如有版本相关问题，向该文档查证。

---

## 详细文档索引

| 文档 | 说明 |
|------|------|
| [references/auth.md](references/auth.md) | 认证命令：扫码登录、直接设置 secret、查看状态、登出 |
| [references/music.md](references/music.md) | 音乐命令：搜索、推荐、收藏、统计、榜单、创建歌单 |
| [references/control.md](references/control.md) | 控制命令：控制 PC/Mac 客户端播放、暂停、切歌、收藏、创建歌单等 |
| [references/install.md](references/install.md) | 安装命令：SKILL.md 安装到各平台 |
| [references/update.md](references/update.md) | 更新机制、版本检查、关闭自动更新 |
| [references/output-format.md](references/output-format.md) | 输出格式与展示规范 |
| [references/error-handling.md](references/error-handling.md) | 错误处理与常见错误 |

---

## 完整使用流程

```bash
# 1. 登录（详见 references/auth.md）
kugou-cli auth login                      # 获取二维码
# auth status 不会内部轮询；Agent 按"阶段 A → 阶段 B → 阶段 C"自行循环
kugou-cli auth status

# 1'. 或者直接导入已持有的 secret（跳过扫码）
kugou-cli auth set-secret "<base64-secret>"

# 2. 搜索歌曲
kugou-cli music search "周杰伦"

# 3. 获取猜你喜欢
kugou-cli music recommend guess

# 4. 查看我的收藏（返回最近若干首，不支持分页）
kugou-cli music favorites

# 5. 查看最近播放（返回最近若干条，不支持分页）
kugou-cli music recent

# 6. 查看听歌统计
kugou-cli music stats

# 7. 查看抖音热歌榜
kugou-cli music charts 52144

# 8. 创建歌单
# 优先走客户端路径（默认）：见 references/control.md §10
kugou-cli control playlist create --name "我的批量歌单" --mixsongids "32068120,233125060"
# 客户端不可用时才回退到云端（详见 references/music.md §7.1）：
kugou-cli music create-playlist "我的空歌单"
kugou-cli music create-playlist "我的批量歌单" --songs "32068120,233125060"

# 9. 搜索歌单（拿到 global_id 后可透传给 control play-playlist）
kugou-cli music search-playlist "周杰伦"
kugou-cli music playlist-songs "collection_3_938985631_304_0"

# 10. 控制本机酷狗客户端（仅 Windows / macOS，详见 references/control.md）
kugou-cli control play --mixsongid 32100650 --song-name "晴天" --singer-name "周杰伦"
kugou-cli control player --action pause
kugou-cli control favorite song --mixsongid 32100650
```
