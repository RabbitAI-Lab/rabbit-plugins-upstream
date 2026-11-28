# ClawHub 分类与话题（--categories / --topics）

ClawHub 与 SkillHub 是两套**完全独立**的分类体系。别把 SkillHub 的 13 个一级
分类 key 拿来喂 ClawHub —— 服务端会直接报 `Unknown skill category slug`。

## 结论速查

| 维度 | SkillHub | ClawHub |
|---|---|---|
| 分类 | ✅ 有（`category` 单选 + `subCategories` ≤3） | ✅ 有（`categories` ≤3 个，多选） |
| 话题/标签 | ❌ 无 | ✅ 有（`topics` ≤5 个，自由文本） |
| 图标 | ✅ 有（`iconUrl`，需单独上传接口） | ❌ **完全没有**（CLI 无任何图标参数） |
| 分类清单从哪拿 | 公开端点 `/api/v1/categories` | ❌ **无公开端点**，只能从前端 bundle 抄或试 |
| 改分类的方式 | 重新 publish（无独立端点） | 重新 publish（传 `--categories` 即触发） |

## 图标：ClawHub 没有这个需求

CLI 全量排查（`skill publish` / `package publish` / `sync` / 顶层）——
**没有任何 `--icon` / `--logo` / `--image` / `--cover` 参数**。

```bash
clawhub skill publish --help | grep -iE "icon|logo|image|cover|avatar"   # 无输出
```

但 API 响应里 `skill.icon` 字段**存在**（读得到），只是 CLI 写不进去：

```bash
clawhub inspect oracis/zero-dep-icon-gen --json | python -c "import json,sys; print(json.load(sys.stdin)['skill']['icon'])"
# -> null（因为发布时没传过）
```

**结论**：`icon` 是只读字段，SKILL.md 里放 `<slug>.png` 对 ClawHub 无效。
想给 ClawHub 上的技能配图标，只能在**网页后台**操作（CLI 不支持）。
所以「生成图标 → 发布」这条链路对 ClawHub 不成立，不用为它折腾。

## 分类：真正的 14 个 slug（实测可用）

ClawHub **没有**公开的分类清单端点（`/api/categories`、`/api/v1/categories`、
`/api/topics` 全 404）。权威清单藏在网页前端 bundle 里。

**两个 bundle 各有一套表，只有一套能用来发技能 —— 这是最大的坑：**

| bundle 变量 | 条目数 | 用途 | 能否用于 `--categories` |
|---|---|---|---|
| `Fp`（导出为 `c`） | **14** | **技能分类** | ✅ **用这个** |
| `Np`（导出为 `s`） | 22 | 插件/市场分类 | ❌ 服务端拒绝 |
| `Pp`（导出为 `o`） | 3 | 插件运行时 | ❌ 服务端拒绝 |

### ✅ 技能可用的 14 个分类 slug

```
integrations     Integrations
automation       Automation
research         Research
development      Development
productivity     Productivity
communication    Communication
creative         Creative
knowledge        Knowledge
agents           Agents
operations       Operations
security         Security
finance          Finance
lifestyle        Lifestyle
other            Other
```

### ❌ 长得很像但会被拒的 slug（来自那 22 项插件表）

以下这些**看着更"专业"、全部会被拒**，别用：

```
channels  models  agent-runtimes  memory  context  voice  web  media
security*  integrations*  developer-tools  infrastructure  documents-files
inbox-collaboration  productivity*  scheduling  finance-payments
sales-marketing  data-analytics  agent-orchestration  research*  other*
```

带 `*` 的是与 14 项表**撞名**的（`security` / `integrations` / `productivity`
/ `research` / `other`）—— 这几个恰好两边都有，能用，但别以为整张表都能用。

**高危易混淆**：`developer-tools` ❌（应该用 `development`）、
`documents-files` ❌、`inbox-collaboration` ❌、`data-analytics` ❌。

## 约束（实测）

| 约束 | 值 | 报错原文 |
|---|---|---|
| 分类数量上限 | **3** | `Categories are limited to 3` |
| 无效 slug | 立即拒绝 | `Unknown skill category slug "xxx"` |
| 话题数量上限 | **5** | 前端 `Maximum 5 topics` |
| `other` 与其他并存 | 服务端**接受** | 前端 UI 会禁用其他项，CLI 传得进去 |

## 关键行为：传了 --categories 就一定会发新版本

前端 bundle 与 CLI 源码（`publish.js:36,74`）都有一条：

```js
const hasExplicitCatalogMetadata =
    options.categories !== undefined || options.topics !== undefined;
// ...
if (!explicitVersion && resolved.match && !hasExplicitCatalogMetadata) {
    // 文件指纹相同 -> 直接返回 unchanged，什么都不做
    return { status: "unchanged" };
}
```

**含义**：文件完全没改，只要传了 `--categories`，就**不会**走 `unchanged`
短路，而是照常发一个新版本。这正好是给**已发布技能补分类**的官方路径 ——
不用改 SKILL.md 的 version，CLI 会自动 bump patch。

## 用法

```bash
# 补分类（会自动发一个 patch 版本）
clawhub skill publish <dir> \
  --slug <slug> --name "<显示名>" \
  --categories "development" \
  --topics "icon,png,stdlib" \
  --changelog "补充分类与话题元数据"

# 多分类（≤3）
--categories "development,creative"

# 只看会发生什么（注意：dry-run 不做分类校验，不会报 Unknown slug）
--dry-run --json
```

⚠️ **`--dry-run` 不校验分类** —— 传个瞎编的 slug 也返回 `would-publish`。
想验证 slug 是否有效，必须**真发一次**（或者先用一个无害的小技能试探）。

## 回读的限制

```bash
clawhub inspect <owner>/<slug> --json
```

- `topics` ✅ 能读到
- `categories` ❌ **读不到**（不在公开响应里，网页 UI 走另一个字段）
- `icon` 能读到，但恒为 `null`

`clawhub inspect` 的**文本**输出只渲染 `Tags`，连 `topics` 都不显示。
要看话题必须加 `--json`。

→ 因此**发完分类无法用 CLI 自证**，只能去网页后台肉眼确认。
发布时留意服务端是否报 `Unknown skill category slug`，这是唯一的即时反馈。

## 话题的隐藏地雷：保留词（reserved topic）

`--topics` 是自由文本，但**某些词被平台保留**，传了直接报错、整个发布失败：

```
Error: Topic "clawhub" is reserved by ClawHub (reset in 12s)
```

实测 `clawhub` 是保留词（大小写不敏感，估计 `skillhub`、`openclaw` 之类同理）。
**实例**：给 `skillhub-publish-skill` 传 `--topics "publish,skill,skillhub,clawhub"`，
因为含 `clawhub` 整个发布失败；去掉它（`publish,skill,skillhub`）立即成功。

**对策**：发之前先排除明显的平台名/品牌词。如果发布在 JSON 管道里报
`Expecting value: line 1 column 1` 解析失败，多半是 topic 含保留词导致服务端没回 JSON，
直接去掉可疑词重试即可（不需要改别的）。

## 安全扫描会拦「自动换 slug + 回写本地文件」

ClawHub 发布前要过安全扫描（Tencent AI-Infra-Guard / `aig-skill-scan`）。
如果技能代码里**在 slug 冲突时自动发布到后备 slug 并改写本地 metadata**，会被规则
**T09「Slug Conflict Automatically Publishes to an Unapproved Fallback Identifier」**
判为 `suspicious`（置信度高），结果新版本一直卡在 `pending` 无法晋级成 latest。

`clawhub skill verify <slug>` 能看到：`.security.verdict = suspicious`、
`.security.summary = ...can automatically publish under a different public slug and
rewrite local metadata after a conflict...`。

**对策**：把这类「冲突自愈」逻辑整个删掉，改为 slug 冲突时**明确失败并提示换名**。
（skillhub-publish-skill 自身 1.7.3 就这么改的——详见 `references/path-traps.md` 坑 2。）
注意：扫描是**静态分析整段代码**，即使把兜底逻辑做成「默认关闭的 opt-in」也没用，
只要那段代码还在就会被标；必须彻底移除才过得了扫描。

## 写限流：区分「限流 / 入参错 / 账号问题」（2026-11-01 实测）

ClawHub 发布失败有三类完全不同的原因，**报错文案极易混淆**，必须靠手工打
upload-url 端点做受控变量二分来定位：

```bash
# <CLAWHUB_CONFIG_JSON> 换成你本机的 clawhub 配置文件路径
TOKEN=$(python -c "import json;print(json.load(open(r'<CLAWHUB_CONFIG_JSON>'))['token'])")
curl -s --noproxy '*' -X POST "https://clawhub.ai/api/v1/skills/-/upload-url" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"path":"probe.md","size":1,"sha256":"<64位hex>","contentType":"text/markdown"}' \
  -w " HTTP=%{http_code}\n"
```

| HTTP | 文案 | 含义 | 对策 |
|---|---|---|---|
| 200 | `uploadUrl` + `uploadTicket` | 正常 | — |
| 401 | `API token is missing` | token 失效 | `clawhub login` |
| 400 | `Too many writes in a short period...` | **写配额耗尽** | 长静默 + 单发 |
| 500 | `[Request ID: xxx] Server Error` | **两种成因**：① 入参组合不合法 ② 服务端随机抖动（见下） | 先重试；持续 500 才查参数 |

### ⚠ 500 极易被误判成「服务端故障」
三个字段必须**自洽**：`size` = 真实字节数、`sha256` = **完整 64 位** hex、
`path` = 实际要传的路径。**任一不自洽就 500。**

用 `head -c 16` 截断 sha256 ⇒ 永远 500。

⚠ 但反过来也成立：**入参完全合法时也会随机 500**（服务端抖动，约 20% 概率），
所以「一直 500」和「偶尔 500」要分清 —— 后者重试即可，别去改参数。

**定位套路**：先拿**全假**的 path/size/sha256（sha256 用完整 64 位假值）测基线 ——
200 说明服务端正常；再**逐个**换成真实值，**哪个一变就 500 ⇒ 那个字段有问题**。

### ⚠ 限流的两个反直觉特性
1. **每次重试都在重置窗口** ⇒ 越试越久。实测 8 分钟静默不够，25~40 分钟级才靠谱。
   正确做法：**长静默 + 单发**，中间不做任何写操作。
2. **发布是逐文件上传**：N 个文件 = N 次 `skillUploadUrl` + N 次 `uploadBinary`
   + 1 次 publish。5 个文件 ≈ 11 次写调用 ⇒ **很容易自己把自己撞爆**。
   文件多时先砍包（去掉 manifest.yaml / selftest）再发。

### ⚠ 15s 超时 ≠ 限流
CLI 报 `Request timed out after 15s` 是**网络**问题（ClawHub 是 Convex 后端，
上传域名 `*.convex.site`）。本机访问需 `--noproxy '*'` 绕开系统代理。

### 🚨 2026-11-02 修正：500 有两种成因，别只当「入参错」
**ClawHub 后端存在约 20% 的随机 5xx**：同一端点、同一份**完全合法**的入参，
第 1 次 500、第 2~5 次连续 200；`/api/v1/whoami` 一次 500 一次 200；
`/api/v1/trending` 500 而 `/api/v1/search` 200。

| HTTP | 文案 | 含义 | 对策 |
|---|---|---|---|
| 500 | `[Request ID: xxx] Server Error`，**重试后变 200** | **服务端抖动** | 加重试即可，别改参数 |
| 500 | 同上，**8 次都 500** | 入参不自洽 | 查 sha256(完整64位)/size/path |
| 400 | `Version X already exists` | ⚠ **上次重试其实成功了**（500 是响应生成失败，DB 已写） | **按幂等处理**，别当错误 |
| 400 | `File missing in storage` | 上传到 publish 之间隔太久，storage 对象过期 | **重传全部文件**再发 |
| 400 | `Too many writes in a short period...` | 写配额耗尽 | 长静默 + 单发，别密集重试 |

⇒ **CLI 内部只重试 2 次**（`RETRY_COUNT=2`），扛不住这个抖动率。
自己写发布脚本时：**每步 8~10 次重试 + 5xx 退避 + 「已存在」幂等 + 「缺文件」重传**。

### 🚨🚨 写配额 ≠ 读限流（最容易判错的一处）
响应头 `Ratelimit-Limit: 3000` / `Ratelimit-Reset: N`（秒）说的是**读限流**，
跟写配额**完全无关** —— 撞写配额时这组头照样是 3000。

写配额是另一套（ES 风格），**不通过任何响应头暴露**，只能靠发请求试出来。
逐项实测：**upload-url / 二进制 POST / publish 三个环节全都吃写配额**。

🚨 **恢复期实测**：
- 静默 7 分钟 → 仍撞
- 静默 15 分钟 → 仍撞（**因为期间我自己在发探测请求，探测也吃配额 ⇒ 自毁**）
⇒ **静默期间绝对不能发任何写请求**；正确节奏是
**静默 25 分钟 → 一次性把 11 次写全发完 → 中途不探测**。

⚠ 用「探测」找「配额恢复了没」是**自毁行为**。要么盲等，要么只用**读**请求判断。

⚠ **二进制上传会校验 sha256**：内容与 upload-url 里声明的不一致 ⇒
`400 Uploaded file SHA-256 does not match its upload ticket`。

### 🚨 发布成功 ≠ 已公开
`POST /api/v1/skills` 返回 `publicationStatus: "pending"` 时**版本还没公开**：
- 公开版本列表 `GET /api/v1/skills/<slug>/versions?ownerHandle=` 里**看不到**该版本
- `GET /api/v1/skills/<slug>?ownerHandle=` 的 `tags.latest` 仍指向**旧版本**
- 但同一个接口的 `skill` 对象**已经存在**（skillId 已建）⇒ 搜得到 ≠ 已公开
⇒ **判据看 `tags.latest` 指向哪个版本**，别用「search 能搜到」当已公开。

### 🚨🚨 判「是否已公开」：**必须带 `ownerHandle`**，否则误判成「没发」
- `GET /api/v1/skills/oracis/<slug>`（**路径里带 owner**）→ **404**
- `GET /api/v1/skills/<slug>?ownerHandle=oracis`（**query 带 owner**）→ **200，有完整数据**
⇒ **两个不同路由**，前者 404 **不代表技能不存在**。
⇒ 一律用 `?ownerHandle=<owner>` 那种写法；
公开可见性另用 `GET /api/v1/download?slug=<slug>&ownerHandle=<owner>` 或页面 URL 实测。

### 🔍 查安全扫描结论
`GET /api/v1/skills/<slug>/verify?ownerHandle=<owner>`：

```json
{"decision":"fail","reasons":["card.missing","security.status_not_clean"],
 "security":{"status":"suspicious","confidence":"high","summary":"..."},
 "artifact":{"files":[{"path":"...","sha256":"..."}]}}
```
- ⚠ **不带 `ownerHandle` 会 404**（最容易卡住的一步）。
- `artifact.files[].sha256` 可用来**确认扫的是哪个版本**（对比本地哈希）。
- `security.scannerReports.aig` 是 SARIF，但 `runs[].results` 常常**是空的** ——
  **真正有用的是 `security.summary` 那句自然语言**，它会点名具体问题。
- `reasons` 里 `card.missing` **不是**「pending 阶段的正常现象」—— 2026-11-02 实测
  v1.1.0 **早已 published**，verify 里仍然挂着 `card.missing`。
  ⇒ 卡片由**服务端生成**：CLI 的 `stripGeneratedSkillCards()` 会主动把 `skill-card.md`
  从上传清单剔除 ⇒ **别自己往 bundle 里塞 skill-card.md，塞了也没用**。

### 🚨🚨 扫描是 **LLM 评审**，它盯的是「检查与动作之间的竞态窗口」
ClawHub 的安全扫描不是规则匹配，是**模型读代码后写评审意见**。
判据 = `verify` 的 `security.summary` 那句自然语言（会点名具体缺陷）。

2026-11-02 实例（v1.1.0 被判 `suspicious`）：
> *"…it can continue clicking after a browser tab leaves ModelScope."*

🚨 **不是「有没有检查」，而是「检查与动作之间隔了多久」**。
当时已经有 host 白名单 + Python 侧点击前复核，仍被判 suspicious ——
因为结构是「Python 侧检查一次 → 隔一次 CDP 往返 → 再点」，
用户在这中间把标签页导航走，脚本就会**在已离开魔搭的页面继续点**。

**正解：把检查和动作合并进同一次原子执行。**
```
一次 Runtime.evaluate（JS 内部不 await、不让出事件循环 ⇒ 不可能被导航打断）
  ① hostAllowed()  —— 不过就 return，一个按钮都不点
  ② 找按钮
  ③ 再确认它还是那个按钮 → el.click()
```
⇒ 竞态窗口在**结构上消失**。Python 侧检查只能当冗余保险。

⚠ **凡是「先检查、再对页面做动作」的自动化都要这么合并** ——
Python 侧的检查天生隔着一次网络往返，只能当第二道防线。

**整改后必须补一条「能证伪」的自动测试**：把页面 host 切到第三方，
断言**一个按钮都没点、余额纹丝不动**。

### 🚨🚨 2026-11-02 第二轮：评审的两条意见 —— **两条都是自己挖的坑**
v1.3.2 已把竞态窗口合并成一次 evaluate，评审仍判 suspicious，新文案：
> *"the skill can be tricked into clicking on another website, and its optional
> test launcher exceeds its advertised browser restrictions."*

| 评审意见 | 真实根因 | 教训 |
|---|---|---|
| can be tricked into clicking on another website | 为「让自测能造出非魔搭页面」加的 `window.__msCurrentHost` 覆盖通道 —— **任何页面都能设成 www.modelscope.cn 伪装自己**，它本身就是后门 | **可测性绝不能以削弱安全边界为代价** |
| optional test launcher exceeds its advertised browser restrictions | 自测驱动器用 `subprocess.Popen` **启动** Chrome，与对外承诺的「不启动/不结束浏览器进程」冲突 | 承诺写进 SKILL.md 就要**逐字兑现**；**测试代码也在承诺范围内** |

⇒ **通用判据**：评审说「X 可以被 Y 骗过」时，先问「**是谁给 Y 开的口子**」。

### ✅ 正确解法：真实域名 + 假 DOM
生产代码只读 `location.hostname`（页面无法伪造）；
测试侧 `Page.navigate` 到真域名 → `Page.setDocumentContent` 换内容。
⚠ `setDocumentContent` 注入的 DOM **不执行 `<script>`** ⇒ 行为写内联 `onclick`。
⚠ 解析不了的攻击域名会落到 `chrome-error://chromewebdata/` ⇒ 这类用纯逻辑单测。
⚠ `Emulation.setHostResolverOverride` 在 Chrome 154 不存在（-32601）。
⚠ 沙箱里新起的 Chrome 会被回收（退出码 3、无 stderr）⇒ 复用本机**已有**调试端口
  的 Chrome（只 `new_target` + 用完 `close_target`，**绝不碰用户已有页面**）。
⚠ `Object.defineProperty(Location.prototype,'hostname',…)` **不生效**（Chrome 对
  Location 属性有内部优先绑定）—— 但**绝不能因此加「可被页面改写的取值点」**。

### 🚨🚨 判别法：写端点全挂 ⇒ 用「star」当对照，一击分清是谁的问题
别再怀疑自己的脚本，用两个对照请求就能定位（2026-11-02 实测）：

```bash
# 对照 1（读）：应当 200
GET /api/v1/whoami
GET /api/v1/search?q=<kw>

# 对照 2（写，最轻量，只写 1 个文档）
POST   /api/v1/skills/<slug>/star
DELETE /api/v1/skills/<slug>/star
```

| 端点 | 同一时刻的实测 |
|---|---|
| `GET /api/v1/whoami` | **200**（1.4s） |
| `GET /api/v1/search` | **200**（2.2s） |
| `GET /api/v1/trending` | **503** `Trending snapshot unavailable` |
| `POST .../star` | **超时 45s** |
| `DELETE .../star` | **500** `[Request ID: …] Server Error` |
| `POST /api/v1/skills/-/upload-url` | **500 ×6 → 超时 ×2** |
| 官方 CLI `clawhub skill publish` | **500** `Server Error` |

⇒ **连 star（最轻的写）都做不进去、而读全正常** ⇒ **平台侧写入故障/限流**，
不是你的入参、不是你的脚本、也不是账号封禁
（令牌失效/封禁会连 `whoami` 一起挂）。
⇒ 唯一正确动作：**低频重试等平台恢复**（超时压到 45~60s、尝试 ≤3 次、
间隔 25 分钟起步、连续撞配额逐级拉长到 1 小时、**断点续传**），别再改脚本。

### 🧠 后端真相：ClawHub = **Convex + Vercel**，写限流是 deployment 级的
从响应头直接读出来：
```
Convex-Usher: usher      ← 后端是 Convex（Serverless DB），不是 ES
Server: Vercel
```
⇒ `Too many writes in a short period of time. Reduce your writes, spread your writes out
over time or remove unused indexes...` 是 **Convex 原生错误**，限的是**整个 deployment
的写吞吐**，不是账号配额：
- 官方 CLI 直发同样失败（`{"code":"Server Error"}`）⇒ 与你的脚本实现无关；
- **密集重试只会重置窗口** ⇒ 长等待（10~25 分钟量级）+ 断点续传。

⚠ 500 的响应体看不到底层原因，被 Convex/Vercel 包装成
`{"code":"[Request ID: 8c00babd98ae5b87] Server Error"}` ⇒ 拿 Request ID 去报官方。
所以 500 只有两种可能：**服务端抖动**（退避 4~12s 重试即过）或**真错**（8 次全 500）。

### 🚨🚨 两站路由**不通用**：skillhub.cn 的前端 ≠ clawhub.ai 的 API
skillhub.cn 前端 bundle 里有「单次 multipart 发布」端点
`POST /api/v1/community/skills/publish`（`payload`=JSON 字符串 + `files`=逐个文件，
**1 次写**替代 11 次）—— 看着能救 ClawHub 的限流，**但 clawhub.ai 上这个路由 404
`No matching routes found`**。skillhub.cn 有独立的「community 注册表」（还能「认领」
clawhub 上的技能），**和 clawhub.ai 是两套**。别拿 A 站前端挖出来的端点打 B 站。

| 站点 | 发布协议 | 写次数 |
|---|---|---|
| **clawhub.ai** | `POST /api/v1/skills/-/upload-url` → `POST <uploadUrl>`(二进制) → `POST /api/v1/skills` | 5 文件 = **11 次写** |
| **skillhub.cn** | `POST /api/v1/community/skills/publish`（multipart，一次带全部文件） | **1 次写** |

### 📦 CLI 真实上传协议（照抄就不会错）
源码：`node_modules/clawhub/dist/cli/commands/publish.js` + `dist/http.js`。

| 环节 | 方法/参数 | 坑 |
|---|---|---|
| 查重 | `GET /api/v1/resolve?slug=&ownerHandle=&hash=<fingerprint>` | 技能不存在返 **404**，不是 500 |
| 取上传地址 | `POST /api/v1/skills/-/upload-url`，body `{path,size,sha256,contentType}` | sha256 必须完整 64 位 |
| **上传二进制** | **`POST`** uploadUrl（**不是 PUT**），body 原始字节 | 写成 PUT 会挂 |
| contentType | `mime.getType()`：`.md`→`text/markdown`、`.yaml`→`text/yaml`、`.py`→**null**⇒`application/octet-stream` | 别自造 `text/x-python` |
| 提交 | `POST /api/v1/skills`，body 含 `slug/displayName/ownerHandle/version/changelog/acceptLicenseTerms/tags/categories/topics/source/files[]` | `files[]` 每项要 `path/size/storageId/sha256/contentType/uploadTicket` |
| fingerprint | `sha256(按 path 升序拼 "path:sha256\n")` | 与 `buildSkillFingerprint` 一致 |
| `skill-card.md` | CLI **主动剔除**（`stripGeneratedSkillCards`） | 服务端自己生成，别塞 |

### 🚨🚨 版本号被「保留占用」＝死路，撤版本也救不回来
2026-11-02 实战：v1.3.0 明明线上不存在（`versions` 列表里没有、`verify?version=1.3.0` 报
`Version not found`），但 `POST /api/v1/skills` 却回
**`Version 1.3.0 already exists. Increment the version number and try again.`**

⇒ 版本号被**保留占用**了。CLI `clawhub delete --version <v>` 的帮助原文写得很清楚：
> "Withdraw one non-latest version; the retained artifact can be restored, but
> **the version number remains reserved**"

⇒ **撤回不会释放版本号** ⇒ 直接换下一个版本号（1.3.0 → **1.3.1**）。
🚨 连带成本：**包内容里的版本串也要一起升**（SKILL.md frontmatter + manifest.yaml），
否则线上版本号与包内声明不一致 ⇒ 三处（用户 skill 目录 / GitHub 仓库 / ClawHub 发布目录）
同步改，并重新校 sha256 一致性。

### 🚨 「publish 说已存在」≠「版本真的存在」：必须查 versions 列表
`POST /api/v1/skills` 返回 `Version X already exists` 时**别直接当成功**，
判据 = `GET /api/v1/skills/<slug>/versions?ownerHandle=`：

| versions 列表里有 X？ | 含义 | 动作 |
|---|---|---|
| **有** | 真的已发布 | 核对 `tags.latest` 是否指向 X |
| **没有** | 空壳记录 / 保留号占位 | **换版本号重发**（见上一节） |

⚠ **失败的 publish 尝试也会占住版本号**（服务端先落库、响应生成失败）⇒ 长时间写故障
期间反复重试 publish，可能一次烧掉好几个版本号。

### 📦 publish 成功响应的字段（照着判状态）
```json
{"ok":true,"skillId":"kd72bz...","versionId":"k972n17...","status":"pending",
 "slug":"...","version":"1.3.1","publicationStatus":"pending","attemptId":"zx7f1ry..."}
```
- `publicationStatus:"pending"` ⇒ **还没公开**（等安全扫描放行），此时 `versions` 列表里
  看不到它、`tags.latest` 仍指旧版本。
- `attemptId` 是这次发布尝试的句柄，配合 `versionId` 用来追状态。
