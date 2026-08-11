# BOSS 直聘安全操作纪律（R1–R12，泛化版）

> 本文件是 `boss-zhipin-copilot` 的**灵魂**。所有浏览器动作必须服从本纪律。
> 源于一次真实封号事故的第一性原理复盘：绕过运行时直连、无冷却、批量突发、撞墙后恢复自动化 = 封号。
> 适用于任何 Agent 产品（WorkBuddy / OpenClaw / Codex / Claude Code 等）。

---

## R1 只走 agent-browser-runtime 正门

- 所有浏览器动作只经 `./cli/brs.js`（或 `$BRS_JS`）→ broker(:17890) → companion extension → Chrome。
- **绝不**直连 CDP(:19223)、绝不 `Runtime.evaluate` 合成点击、绝不 `Input.dispatchMouseEvent`、
  绝不 `Page.navigate` 到 `?query=&city=&page=` 合成 URL。
- 初始 `browse-start` 允许用真实 entry URL（用户给的岗位链接 / BOSS 首页），之后的检索/翻页/筛选**必须走真实 UI**。

## R2 只真实光标

- 点击/键入只用 extension 的 `ui.click` / `ui.type`（真实光标移动+点击）。
- 禁止任何 `el.click()` 合成点击、`location` 跳转、dispatch DOM 事件。

## R3 限速强制

- 操作间间隔 ≥ `$ACTION_INTERVAL_SECONDS`（默认 5s），由 `common.sh` 的 `cooldown` 实现。
- 每日收藏 + 开聊总数 ≤ `$DAILY_CAP`（默认 100）。
- 无限速 = 不执行。**已落地实现**：`common.sh` 的 `bump_daily_cap` 在每个改状态动作
  （`process_job.sh` 的书签 / 发送）执行前跨调用持久化计数（落盘
  `${WORK_DIR:-.work}/.daily_action_count_YYYYMMDD`，按自然日隔离），超 `DAILY_CAP` 即 `exit 5` 停手。
- ⚠️ **hosted 边界（F11，仅适用于非 BOSS 站点）**：此模式浏览器由外部 Agent（如 Codex）端驱动，**本地代码层无法计数 / 强制日限额**，R3 限速仅以 `bz_emit_plan` 提示词「单日勿超 100」**文本提醒，无代码兜底**。**执行方须自律**，切勿误以为「已限速」而批量突发。⚠️ BOSS 直聘已 **R12 禁用任何扩展直控（含 codex hosted）**，请勿走此路径。

## R4 撞墙即停

- 遇验证码 / `verify.html` / 「安全验证」/ 滑块 → **立即停手、截图、交人工**。
- 冷却 **≥24h**，期间仅真人使用，**绝不**恢复自动化。
- 脚本 `exit 3`（撞墙码），不重试、不绕过。

## R5 授权门控

- 「改账号状态」动作（书签、发消息、投递）需用户**显式授权**：
  - 书签：用户授权「这批 / 全部」批次。
  - 发消息：**每岗**显式授权（`AUTHORIZED=1`）。
- 未授权只做浏览 / 截图 / 读元素 / 填表。

## R6 合并打开、避免无谓重开

- 同一任务内，能在一次详情页打开完成的动作合并到同次（书签 + 读JD + 授权则发消息）。
- 不按动作类型拆批重开同岗。具体同次哪些动作由当次任务决定。

## R7 预飞后复制

- 先用 **1 个岗位**端到端跑通整条路径（含选择器校验），确认无误后，
  其余岗位走**同一代码路径**复用。禁止先批量跑全部再修 bug。

## R8 单 lease 连续 tab

- 批量任务用一次 `browse-start` 拿一个 Tab Group，全程复用（用 `browse-nav` 切岗），
  禁止多进程反复杀重启（burst）。
- `process_job.sh` 支持传入 `--lease/--tab` 复用；省略则自管（简单场景）。

## R9 复核收敛

- 每步仅 1 个权威完成产物（如 `candidates.csv` / CSV 行数）。
- 产物出现后最多 1 次交叉校验，不反复轮询 / 反复 inspect。

---

## R10 发送幂等 / 防重复（断点续发安全）

- **任何「批量逐岗发送」编排（含 SKILL.md Step 5 官方循环）都必须有 done 状态追踪 + 幂等保证**：否则中断后重跑会重复发，属反作弊高风险 + 骚扰招聘方。
- **已发集合唯一真源 = 落盘 done 文件**；内存关联数组仅同跑内加速，必须与文件同步——发送成功须**同时** `printf '%s\n' >> DONE`（显式 LF，绝不写 `\r`）**且** `DONESET[$jid]=1`。只写内存不同步 = 续跑读到过期快照 = 重发。
- **key 必须归一化**：`read` / 比较前 `d="${d%$'\r'}"` 剥 `\r`。CRLF/LF 混行会把同一岗位存成 `BJ-EXT01` 与 `BJ-EXT01\r` 两个 key，跳过判定逐字节失配 → 误判"未发" → 重发。
  - 💥 **2026-07-28 真实事故根因**：`.work/_send_done.txt` 前段 python 写 CRLF、后段 bash `echo >>` 写 LF，混行；驱动内存集合与文件不同步、无并发锁 → `DONESET` 加载出 23 个 key（逻辑仅 19 岗）→ **EXT01/03/04/05 各被发 2 次**（BOSS 开场白气泡=2 实锤）。
- **并发锁**：发送前 `mkdir` 锁目录，实例重叠直接退出（"另一个发送实例正在运行"），杜绝双实例读过期快照重发。
- **启动即停**：done 已覆盖全部待发 → 直接退出，绝不空跑。
- **终态以 BOSS 实锤为准**：不轻信编排 rc 日志（中断 / 草稿失败码会误判）；某岗是否真发出以「继续沟通」按钮 / 开场白气泡数为准。
- 仍须遵守 R5（每岗授权）/ R4（撞墙停手）/ 通用红线（前台人工在环，禁无人值守后台）。

---

## 通用红线补强

- ⛔ **禁止频繁开关 tab**：一次 `browse-start` 后保持 tab 打开复用，结束/用户要求才 `browse-end`。
  频繁开关 = 反作弊高风险。
- ⛔ **禁止在本地 / 预览面板打开任何 BOSS 页面 HTML**：`browse-html` / `extract` 落盘的 HTML 仅供解析，
  绝不 `present` 或本地浏览器打开（会被误判为「用自己的浏览器操作 BOSS」）。所有交互只在运行时 Chrome（noVNC）内经 brs.js。
- ⛔ **UI 交互用语义化原语**：`ui move/click/scroll/type` 必须带 `--selector` 或 `--targetText`
  按真实元素定位，**禁止盲坐标点击**（防误触「立即沟通/投递」）。`scroll` 用 `--delta`。
- 🔒 **风险监测期最小动作**：账号刚解封 / 处于风控监测时，默认只读（browse-html / 增量扫描）；
  任何改状态动作须用户显式逐岗授权 + 预飞 1 岗。
- 🔒 **状态变更动作禁止无人值守后台**：书签 / 发送须**前台、逐岗、人工实时在环**执行，人可随时叫停。
  即使已 `AUTHORIZED=1`，也**禁止**委托无人值守后台 agent 批量跑——撞墙无人接手、无法中断、会话结束即死。
  仅**只读**操作（检索 / 读JD / 扫描）可后台。

---

## R11 登录态：失败驱动，禁止主动预飞

- **机制真相**：浏览器 runtime 用持久化 profile（cookie 在挂载卷），BOSS 登录态跨容器重启都在，仅 cookie 过期才失效（非每小时）。无需每轮校验。
- **默认信任「已登录」**：仅在真实操作卡住时才质疑。`check_logged_in` 仅由失败分支调用——搜到 0 卡片、或发送 UNKNOWN 时——命中登录页信号才置 `logged_out` + `exit 8`。
- **状态位置**：`<skill_root>/.state/login_state`（跟随 skill 自身安装目录，产品无关，适配 WorkBuddy/Claude Code/Codex/OpenClaw/Solo…；位于 skills 目录下非 git 仓库，不进 GitHub）。
- **自动恢复**：人工 noVNC 重登后，下一成功操作（搜到卡片 / 发送 SENT）自动置回 `logged_in`，无需额外握手。
- docker 启动 / 开 tab 是「直接去做、失败即 fail-loud」的必要动作，不算主动校验。

---

## R12 反作弊红线：只允许受控运行时，禁止任何浏览器扩展直控

- ⛔ **BOSS 直聘禁止任何 Agent 的浏览器扩展直控**——无论 WorkBuddy / Codex / Claude Code / OpenClaw / Solo，凡经浏览器扩展（如 Codex `@Chrome`、CloakBrowser 之类）直接驱动 BOSS 的行为，都属反作弊重点打击对象，会触发封号。
- ✅ **唯一 sanctioned 后端 = `brs`（agent-browser-runtime）**：受控 Chromium + 自带 companion 模拟真实光标/键鼠，与 Agent 解耦、跨平台（Docker）、对 BOSS 表现为真人操作。
- **硬失败而非文档约束**：`common.sh` 在加载后端时显式拒绝 `BZC_BACKEND=codex|cloak`（`exit 1` + 安装链接），把「禁止扩展直控」从事后文档升级为可执行拦截。`codex.sh`/`cloak.sh` 已移入 `backends/_deprecated/` 并加 ⛔ 头，仅供其他站点参考 `bz_*` 抽象。
- 新增浏览器后端同样须是「受控运行时」（真实光标 + 持久登录态 + 反检测），禁止扩展直驱式。


## 十、失败分类与恢复（异常 → 动作）

> 任何失败都要 **fail-loud 或受控重试**，**禁止静默吞错**（静默 = 误判 = 误触）。

| 异常 | 判定信号 | 动作 |
|---|---|---|
| 解析空字段 / 面板未渲染 | 解析 title/url 为空 | 先 `bz_wait` 等元素就绪 → 重试 1 次；仍空则 `FAIL_LOUD`，不静默 |
| 选择器漂移 / 失效 | 关键字段全空或选择器 0 命中 | 回 `boss_selectors.md` 复核并更新条目，**禁止绕过**（绕过=误触） |
| 撞验证墙 | 含「验证码/滑块/安全验证/请完成」 | `exit 3`，停手交人工，冷却 ≥24h，绝不恢复自动化 |
| 软限流（操作频繁提示） | 页面提示「操作频繁」 | 立即 `rate_backoff` 拉长间隔 + 暂停；仍触发则停手 |
| 部分加载（滚动未到底） | 卡数连续 2 轮不变但未达预期 | 等待稳定后重试滚动；仍不全则按已得数据继续，不卡死 |
| 网络 / CONNECT 失败 | 连接拒绝 / 超时 | 重连 1 次；仍失败则停手，不突发重试 |
| 凭证 / 扩展未连接 | `bz_status` 报 `extensionConnected:false` | `FAIL_LOUD`，等 noVNC 登录并确认扩展连接后再跑 |
| 日上限 | `bump_daily_cap` 超 `DAILY_CAP` | `exit 5` 停手，次日或显式调高配额 |
| 岗位已关闭/下架 | 页面含「职位已关闭」但无 `.btn-startchat` | `exit 6` 跳过该岗（**非撞墙**，不冷却），请在岗位库标记「岗位关闭」 |
| 登录态失效 | 搜索 0 结果且登录页信号 / 发送 UNKNOWN 且登录页信号 | 置 `logged_out` + `exit 8`，请人工 noVNC 重登（无需冷却）；重登后下一成功操作自动置回 `logged_in` |

---

## 接入检查（每次 BOSS 任务前）

- [ ] `brs status` 显示 `extensionConnected: true`？
- [ ] 只调 brs.js，无裸 CDP / 合成点击 / 查询串捷径？
- [ ] 限速已遵守（间隔≥5s、日≤100）？
- [ ] 撞墙会停手 ≥24h？
- [ ] 发消息每岗有用户授权？
- [ ] 批量发送编排有 done 追踪 + key 归一化 + 并发锁（R10）？
- [ ] 同岗无谓重开已避免（合并打开）？
- [ ] 预飞 1 岗后再复制其余？
- [ ] 单 lease 不杀重启？
- [ ] 复核只看 1 个权威产物？
