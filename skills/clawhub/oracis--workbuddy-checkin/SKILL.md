---
name: workbuddy-checkin
slug: workbuddy-checkin
displayName: WorkBuddy 每日签到领积分
version: 1.6.0
summary: 自动领取 WorkBuddy（原 CodeBuddy）每日签到积分，客户端没打开也能签到。合并 SkillHub 1.5.3 安全骨架（域名硬白名单 / 禁重定向 / JWT 脱敏 / 守卫路径加固）与 1.2.0 的 buildkey_direct.js（免调试端口、免 GUI、客户端不运行也能取 build key）；支持显式 token 与本机凭据双入口、多账号固定、漏签告警、签到周报、token 自动续期。脚本幂等、零依赖（仅 Python 标准库）。
license: MIT
description: 仅在用户明确指 WorkBuddy（原 CodeBuddy）客户端的每日签到积分时使用。触发语句如「领取 WorkBuddy 今日积分」「WorkBuddy 签到」「每日礼包」「checkin」「今天领了吗」「签到周报」，或定时任务明确要求执行 WorkBuddy 签到。若用户只说「签到」「领积分」而未指明平台，须先询问确认。接口规格与脚本已固化，无需重新逆向客户端。
category: office-efficiency
subCategories: [office-automation]
platforms: [windows, macos, linux]
allowed-tools: Bash, Read, Write
---

# WorkBuddy 每日签到领积分

直接调用 WorkBuddy 后端签到接口领取每日积分，**不需要打开或登录客户端**（本机有凭据即可）。幂等：当天已领会立即跳过。

## 何时使用

- 用户要求「领积分 / 签到 / 每日礼包 / checkin / 领取今日积分」
- 定时任务触发每日签到
- 用户问「今天领了吗 / 连续几天 / 签到周报 / 哪几天漏签了」
- 用户只说「签到」而未指明平台时，**先确认是哪个平台**再执行

## 能力边界（1.6.0 合并版）

这个技能合并了 SkillHub 上两条架构相反的分支，取长补短：

| 来源 | 吸收了什么 |
|---|---|
| 官方 1.5.3（已过审） | 域名硬白名单、强制 HTTPS/443、禁止重定向、校验响应 host、JWT 脱敏、守卫路径加固、显式凭据入口 |
| 社区 1.2.0 | `buildkey_direct.js`：以 `ELECTRON_RUN_AS_NODE` 直接读客户端原生绑定取 build key，免调试端口、免找 PID、**客户端不必运行** |
| 本机 1.4.1 | at-rest 信封解密、本地凭据选取、token 自动续期与安全写回 |

- 请求只发往 `copilot.tencent.com` 或 `www.workbuddy.cn`。白名单硬编码，**没有任何环境变量能放行到其它主机**；`WB_ENDPOINT` 只能在这两个域名间切换。
- 显式凭据模式（`WB_ACCESS_TOKEN` / `WB_TOKEN_FILE`）**不读也不写本机凭据文件**，续期后的新 token 只在本次进程内生效。
- 本机凭据模式会读客户端会话文件、必要时提取 build key、并在客户端未运行时安全写回续期后的 token；`WB_NO_LOCAL_AUTH=1` 可完全关闭这条回退。

> 发布提示：含「本机凭据自动读取」的包在 SkillHub 的 keen 扫描里可能被判 `malicious`（社区 1.2.0 即如此），1.5.3 拆分架构正是为过审。若发布被安全过滤拒绝，**停止重发**，改发只含显式凭据入口的干净主包，本机增强组件留本地使用。

## 凭据入口（按优先级）

| 顺序 | 入口 | 环境变量 | 说明 |
|---|---|---|---|
| 1 | 显式 token | `WB_ACCESS_TOKEN` | 明文 JWT；可另配 `WB_REFRESH_TOKEN` / `WB_USER_ID` / `WB_DOMAIN` |
| 2 | 显式 JSON 文件 | `WB_TOKEN_FILE` | 用户自己写的 `{"accessToken": "...", "refreshToken": "...", "uid": "...", "domain": "..."}`；拒绝符号链接 / reparse point |
| 3 | 本机客户端会话 | （默认回退） | 自动探测 `CodeBuddyExtension/Data/Public/auth/*.info`，at-rest 信封自动解密 |

入口 1/2 由 `token_provider.py` 提供，只要设置了就**不再碰本机文件**。入口 3 由主脚本提供，是定时任务能全自动的关键。`WB_NO_LOCAL_AUTH=1` 时入口 3 关闭，拿不到显式凭据会明确报错。

## 执行方式

```bash
python "<SKILL_DIR>/scripts/wb-checkin.py"
```

| 参数 | 作用 |
|---|---|
| 无参数 | 正常签到（幂等，已领则 `[SKIP]`） |
| `--status` | 只查状态不领取（含近 7 天漏签告警） |
| `--json` | 输出状态 JSON，附 `_meta`（uid/mode/endpoint）、`_gaps_7d`、`_recent_7d` |
| `--report` | 签到周报：本周进度、近 30 天签到率、漏签日期、连续天数 |
| `--accounts` | 列出本机凭据目录里的账号 uid（**不显示任何 token**） |
| `--uid <uid>` | 固定签到账号，等价环境变量 `WB_UID` |
| `--force` | 强制调领取接口（调试用） |
| `--no-refresh` | 禁止自动续期（排障用） |

退出码：`0` = 成功领取 / 今日已领 / 活动未开启 / 仅查询；`1` = 失败。仅需 Python 3.8+ 标准库；`buildkey_direct.js` / CDP 兜底链路才需要 Node.js。

### 脚本清单

| 文件 | 作用 |
|---|---|
| `wb-checkin.py` | 主流程（签到、状态、周报、账号、续期） |
| `token_provider.py` | 显式凭据入口（环境变量 / 指定 JSON 文件） |
| `at_rest.py` | at-rest 信封加解密（零依赖 AES-256-GCM） |
| `buildkey_direct.js` | **首选**免 GUI 取 build key（客户端不必运行） |
| `buildkey_bootstrap.py` | 自愈编排：direct 优先 → CDP 兜底 |
| `buildkey_cdp.js` / `attach_debug.js` / `extract_buildkey.js` | CDP 兜底与人工排障链路 |
| `wb-checkin-guard.py` | 系统计划任务守卫（当日完成标记 + 路径加固 + 固定账号） |

## 输出解读

- `[OK]` — 本次成功领取，带本次与累计积分
- `[SKIP]` — 今天已领过，或当前无进行中活动。**属正常，如实汇报，不要重试、不要加 `--force`**
- `[WARN]` — 近 7 天存在漏签，会列出具体日期；用 `--report` 看完整周报
- `[INFO]` — 仅查询 / 自动续期等状态提示
- `[FAIL]` — 失败，按下方处置

汇报给用户时保持简短：活动名称、连续签到天数、累计积分、本次是否领取、领了多少、有无漏签。不要复述实现细节。

## 故障处置

| 现象 | 处置 |
|---|---|
| `[INFO] 已自动续期…` | 正常。看后缀判断是否落盘：显式凭据模式不落盘；本机模式在客户端运行时不写回，否则原子替换并留 `.wb-bak` |
| `[FAIL]` + HTTP 401/403（且已尝试续期） | refreshToken 也过期（约 60 天没开客户端）。让用户**打开一次 WorkBuddy 客户端重新登录**，之后自动恢复。不要改脚本、不要动凭据文件 |
| `[FAIL] 凭据加载失败` | 报错里会列出尝试过的目录与本机可用 uid。指定 `--uid` 试试；非 Windows 可用 `WB_AUTH_DIR` 指定目录 |
| `[FAIL] endpoint 校验失败` | `WB_ENDPOINT` 只允许两个官方域名、必须 https、默认 443 端口，白名单无放行开关 |
| `[WARN] 自动提取 build key 失败` | 看 `direct=` 后缀。direct 失败时确认桌面端已安装、Node.js 可用；CDP 兜底还需客户端**正在运行**。也可用 `WB_APP_BINARY` / `WB_NODE` 指定路径 |
| `keyId mismatch` | 客户端升级换了 build key，自愈会先跑 direct；仍失败再按手动链路排查 |
| `[FAIL]` + 其它 HTTP 码 | 打印原始错误让用户判断，可能是活动规则变更，不要自行猜测重试 |

## 接口规格（逆向自客户端 `app.asar`，已实测）

- 后端 `endpoint`：`https://copilot.tencent.com`（备 `https://www.workbuddy.cn`）
- 查状态：`POST /v2/billing/meter/checkin-activity-status`，body `{}`
- 领积分：`POST /v2/billing/meter/daily-checkin`，body `{}`
- 续期：`POST /v2/plugin/auth/token/refresh`，body `{}`（**`/v2/auth/token/refresh` 是 404**，`/plugin` 前缀不可省）
- 请求头：`Authorization: Bearer <accessToken>`、`X-User-Id: <uid>`、`X-Domain: <auth.domain>`、`Content-Type/Accept: application/json`
- 续期额外头：`X-Refresh-Token: <refreshToken 明文>`、`X-Auth-Refresh-Source: plugin`
- 响应：`{code: 0, msg: "OK", requestId, data: {...}}`

`data` 字段（1.6.0 补齐，★ 为本次新增）：

| 字段 | 含义 |
|---|---|
| `active` | 活动是否进行中 |
| `today_checked_in` | 今日是否已签（**幂等判断依据**） |
| `streak_days` | 连续签到天数 |
| `daily_credit` / `today_credit` | 每日 / 今日积分 |
| `total_credits` | 活动内累计积分 |
| `week_checkin_days` / `week_progress` | 本周已签天数 / 进度（bool 数组，○/● 渲染） |
| `activity_name` / `theme_name` / `season` | 活动名 / 主题名 / 期数 |
| `start_time` / `end_time` | 活动时间范围 |
| ★ `checkin_dates` | 已签到日期数组（`YYYY-MM-DD`，倒序）。**周报与漏签告警的数据源** |
| ★ `is_streak_day` | 今天是否为连签奖励日 |
| ★ `next_streak_day` | 距下次连签奖励还差几天（0 = 无） |
| ★ `streak_bonus_days` / `streak_bonus_credit` | 连签奖励门槛天数 / 奖励积分 |
| ★ `claim_button_text` | 领取按钮文案（如「立即领取」） |
| ★ `action_button` | `{show, text, action}`，活动跳转按钮（如 `workbuddy://home?...`） |

`--json` 在原样输出 `data` 之外附加三个派生字段：`_meta`（uid / mode / endpoint / 时间）、`_gaps_7d`（近 7 天漏签日期）、`_recent_7d`（最近 7 天 ○/● 串）。

## 多账号与「签错人」（2026-11-11 实测踩坑）

凭据目录里可能同时存在多个账号的 `*.info`。旧版按「最新文件的 uid」猜目标账号，**客户端一切换账号，定时任务就把积分签到别人头上**：

- 守卫日志 11-08 / 11-09 / 11-10 分别记 3200 / 3300 / 3400 分
- 但当前活跃账号查出来只有 1900 分、`checkin_dates` 里 11-09 / 11-10 是空的
- 结论：不是漏签，是**签到对象串了**（文档里早先记的「两个工作区双跑导致累计对不上」同源）

修复：

1. `python wb-checkin.py --accounts` 列出所有 uid
2. 用 `--uid <uid>` 或 `WB_UID` 固定账号
3. 定时任务的部署目录放一个 `checkin-config.json`：`{"uid": "<你的 uid>"}`，守卫会把它作为 `WB_UID` 传给主脚本，并写进 `checkin-done.json` 的 `uid` 字段，便于核对「今天到底签给了谁」
4. `[WARN] 近 7 天有 N 天未签到` 与 `--report` 能第一时间发现串号/漏签

## build key 与免 GUI 取 key（1.6.0）

新版客户端的 token 是 at-rest 加密信封：

```json
"accessToken": { "$wbEncrypted": 1, "envelope": "<base64 of JSON>" }
```

信封为 `sym-v1` AES-256-GCM，`k0 = SHA256(atRestSecretKey)`，`keyId = SHA256(k0)[:16]`，AAD 结构见 `at_rest.py`。该模块内置纯 Python AES-GCM（有 `cryptography` 时优先用），同时提供 `seal()` 供续期写回。

build key 是**构建级常量**（同版本全安装一致），取出一次即可离线复用。缓存 `at_rest_buildkey.json`，查找顺序：环境变量 `WB_AT_REST_SECRET_KEY` → 脚本同目录 → `~/.workbuddy/scripts/`。

自愈顺序：

```
解密失败（缺 key / keyId mismatch）
  → buildkey_bootstrap.py
      → ① buildkey_direct.js   ELECTRON_RUN_AS_NODE 直接读原生绑定
           不要求客户端运行 / 不占 9229 / 不找 PID / 不开 GUI   ← 1.6.0 首选
      → ② buildkey_cdp.js     附加运行中客户端的 V8 inspector   ← 兜底
  → 写 at_rest_buildkey.json → 重试解密 → 正常签到
```

手动提取：

```bash
node "<SKILL_DIR>/scripts/buildkey_direct.js" --out "<缓存路径>"   # 首选
python "<SKILL_DIR>/scripts/buildkey_bootstrap.py"                 # 自动编排
```

> `buildkey_direct.js` 已实测：客户端未运行也能取到 key，且与原先 CDP 取到的值一致。
> 两个坑（改 CDP 代码时务必注意）：`process._debugProcess(pid)` 固定占 9229；关闭 inspector 会让 CDP 回包永远不来，结果必须先同步写出、关闭动作不能 await 回包。

## 登录态自动续期

`accessToken` 寿命 30 天，`refreshToken` 60 天。两层判断：事前解析 JWT `exp`，剩余 < 30 分钟先续；事后任意接口 401/403 立即续期并重试一次。token 有效时零额外请求。

写回仅发生在**本机凭据模式**，四道保护：客户端在跑就不写（避免抢文件）、写前重读做竞态检测、同目录 `O_EXCL` 排他锁、`.wb-tmp` → `os.replace()` 原子替换 + `.wb-bak` 备份。只改 `auth` 里的 token 与时间戳，其余字段原样保留；字段加密形态跟着原字段走。

> 实测：旧 `refreshToken` 在新 token 签发后仍可用，所以外部续期不会让正在运行的客户端掉线。

## 调度：系统计划任务（不要用客户端内置定时任务）

WorkBuddy 内置「定时任务」是 `LocalAutomationScheduler`，**客户端进程不运行就完全不触发**；曾因一次 run 挂住 144.9 小时导致连续 5 天漏签。要脱离客户端必须用操作系统级计划任务。

守卫语义：开机期间按频率轮询，今天没领到就继续试，领到了当天立刻收工（`checkin-done.json` 标记 + `checkin-os.log` 日志，`[FAIL]` 不写标记、下周期自动重试）。

Windows 推荐配置（本机已部署 `WorkBuddyCheckin`）：

- 动作：`pythonw.exe` 运行 `~/.workbuddy/scripts/wb-checkin-guard.py`（无窗口）
- 触发器 XML：`CalendarTrigger` + `Repetition`（`Interval=PT30M`、`Duration=PT23H55M`、`DaysInterval=1`）、`StartWhenAvailable=true`；XML 必须 UTF-16，`<StartBoundary>` 不晚于当天
- Git Bash 里 `schtasks` 要写双斜杠 `//create`
- 部署目录放 `checkin-config.json` 固定 uid；marker 会记录当天签到账号
- 不要在两个工作区各建同名任务 —— 会双跑且累计数据对不上

**2026-11-11 实测提醒**：本机 `checkin-done.json` 与 `checkin-os.log` 停在 11-10，当天无任何定时任务记录，而积分是客户端自己领的 —— 说明计划任务当天没触发。本次已把新脚本同步到部署目录、写入 `checkin-config.json`，并手工跑通守卫（marker 已更新到 11-11 且带 uid）。由于本机安全策略禁止调用 `schtasks.exe`，**任务本身是否启用仍需你在「任务计划程序」里确认**：查 `WorkBuddyCheckin` 的状态、上次运行时间与上次运行结果；若被禁用/丢失，用上面的 XML 重新导入。

## 注意

- 「从未登录过」无法签到 —— 凭据来自登录，凭空造不出来
- 本机凭据模式不需要客户端**正在运行**：有凭据 + build key 缓存即可；`buildkey_direct.js` 还能在客户端没开时补提 key
- 续期只用 `refreshToken`，不涉及账号密码、不做交互式登录
- build key 等同本机凭据的解密钥匙，`at_rest_buildkey.json` 不要外传；本 skill **不附带任何密钥**
- 自愈链路需要 Node.js；direct 链路还需要桌面端**已安装**（不必运行）
- 若仍要配 WorkBuddy 内置 RRULE 定时：`BYHOUR` 只接受单个整数，`BYHOUR=9,21` 会被拒；多时段用 `FREQ=HOURLY;INTERVAL=n`
- 凭据写回会留 `*.wb-bak`（写前备份），可手工回滚；`*.wb-lock` / `*.wb-tmp` 正常不残留
