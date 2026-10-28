---
name: sn-work-record
version: 1.14.1
author: chengcheng
license: MIT-0
platforms: [linux, macos]
description: "蜀宁 OA 工时与报销：填报/修改/查询工时，查看报销申请状态与审批进度。"
metadata:
  openclaw:
    requires:
      bins: [openssl]
    env: [OA_ENC_KEY]
  author: chengcheng
---

# 蜀宁 OA 工时与报销管理

## 快速开始

> 在已安装技能目录下运行 `scripts/` 中的 Python 入口；本发布包不提供 `sn-work-record` launcher，不要假定某个 agent 的安装路径。
>
> 所有 Python 脚本现在都带运行时自检：即使误用系统 `python3` 启动，也会优先自动切换到依赖完整的解释器。也可通过环境变量 `SN_WORK_RECORD_PYTHON` 显式指定解释器路径。

### 登录（自动执行，ddddocr 闭环）
```bash
python scripts/sn_oa_login.py [--credentials PATH] [--base-url http://X.X.X.X:PORT]
```
→ 登录入口可能把 token 输出到 stdout；交互任务优先让查询/提交入口通过 `OAAuth` 自动登录并复用受保护缓存，不把 token 打印到聊天、普通日志或用 `tee` 另存明文。必须单独登录时，在权限受限的本地进程内消费结果，只向用户报告认证状态。

### 登录（agent 多模态优先，推荐）
```bash
python scripts/sn_oa_login.py --fetch-only
# → JSON：uuid / image_path / data_url，不登录
python scripts/sn_oa_login.py --submit --uuid <uuid> --code <答案>
```
→ 由使用者当前 agent 的模型识别验证码；若被服务端拒绝，自动回退 ddddocr 重新取图登录。

## 验证码识别策略（agent 多模态优先 → ddddocr 兜底）

默认顺序：

1. **取图**：`--fetch-only` 取验证码，落盘到 `~/.cache/sn-oa/captcha_latest.jpg`，同时输出 `data_url`
2. **识别**：用使用者当前 agent 的多模态能力看图（Hermes 用 `vision_analyze`），得到算术答案
3. **提交**：`--submit --uuid <uuid> --code <答案>`
4. **兜底**：提交被拒（`验证码不正确`）时脚本自动回退 ddddocr，重新取图完成登录；`--no-ddddocr-fallback` 可关闭

登录成功后 token 会自动进缓存（见下节），因此**一次识别可以覆盖后续多轮查询**。

要点：

- 验证码按 `uuid` 校验，**不绑定 HTTP 会话**——取图与提交可跨进程/跨命令（已实测）
- 接口返回的 `img` 本身就是 data URL，前缀写 `image/png`，**实际字节是 JPEG**，落盘用 `.jpg`
- 让模型只输出表达式字符，算术在本地完成更稳（末尾干扰线可能被误当成运算符）
- 只把验证码图片交给模型，**不要附带账号、密码或 token**
- 独立脚本 / cron（没有 agent loop）没有视觉通路，继续用默认 ddddocr 闭环

### 跨 agent 通用性

该流程不绑定 Hermes；任何「模型多模态 + 能把图片喂进模型」的 agent（Claude Code、Codex CLI、OpenClaw 等）都适用。差异只在第 2 步怎么把图递给模型：

- 只支持文件路径的：读 `image_path`
- 支持 data URL 的：用 `data_url`
- 没有视觉通路的：跳过第 2 步，直接用默认 ddddocr 模式

### token 缓存与自动续期（默认自动生效）

登录成功后 token 会写入缓存，后续脚本**不需要显式传 token**：

- **加密存储**：有密钥（`OA_ENC_KEY` 或 `.cache/oa_enc_key`）时写 `~/.cache/sn-oa/token.enc`（AES-256-CBC，与凭据同一套密钥）；无密钥时降级为明文 `token.json`。两者都是 0600
- **账号绑定**：缓存只存账号指纹（哈希，不落明文账号），读取时校验 `base_url` + 账号指纹，**换账号后不会误用旧会话**
- 无 `--token` 时：优先读缓存 → 未超 20 分钟 TTL 就直接复用，**跳过验证码登录**
- 缓存缺失/过期/主机或账号不符：正常登录并把新 token 写回缓存
- 任意接口返回 `401`：自动清缓存 → 重新登录 → **重试一次**

```bash
python scripts/query_fee_requests.py          # 自动复用受保护缓存，不重新登录
```

**写操作（提交/修改工时）在 401 时不会自动重试**。普通提交现在由公共底层 API 执行同日核对、本地锁、持久写入意图与提交后只读核实：完全相同的有效已提交记录直接跳过，其他同日记录停止且不覆盖；超时或未知结果仅查询，不重发。历史未核实意图也禁止再次 POST。此保护不是跨机器/客户端的服务端 exactly-once 保证。草稿真实写入暂时 fail-closed，仍可 `--save-draft --preview`。详见 [提交去重与不确定写入保护](references/submission-idempotency.md)。

已接入 `OAAuth` 的脚本：`query_fee_requests.py`、`query_time_entry.py`、`submit_time_entry.py`、`update_time_entry.py`、`get_time_entry_details.py`、`list_projects.py`。

> 缓存文件等同短期会话凭据（约 20 分钟有效），位于 `~/.cache/`（不在 `~/.hermes` 仓库内，不会被 git 提交）；需要强制重新登录时删掉 `~/.cache/sn-oa/token.enc` 与 `token.json` 即可。

### 提交工时
```bash
python scripts/submit_time_entry.py 2026-04-11 --job-desc "工时描述"
```
→ 内部调用 `POST /sn/timeEntry/saveOrUpdate`
> 仅支持普通工作；事假、公休假等休假提交尚不可用。`--project`、`--fill-type`、`--project-phase`、`--work-type` 接受精确中文名称/标签或实时验证代码；时长必须明确或来自当前账号/地址绑定的已确认设置，无 8h 默认。项目名称和 boToPmStatus 每次从选中项目派生，不要求用户提供。所有默认代码亦重新 live 验证，查询失败不写入；单次覆盖不保存。加 `--preview --json` 使用相同提交前解析，仅预览、不创建草稿或工时、不改个人设置；默认输出名称，明确需要代码才加 `--include-codes`。真实写入前必须确认事实与授权。详见 [首次选择与确认、去重边界](references/personal-settings.md)。

### 润色后填报与中断续办

1. 先区分“仅润色”与“润色后填报”：用户明确要求两步时，将润色作为提交准备，不要只给文案或只跑预览就结束。保留原始工作事实和专有名称，不把口语扩写成未提供的上线、验收或完成成果；专有名称有实质歧义且无法从可信上下文核实才询问。
2. 用实际当前日期与用户时区解析“昨天”等相对日期，并在首次摘要中显示具体目标日期。恢复任务时沿用已确定日期，不因跨天或收到“继续”而重新计算目标。
3. 对同一使用者已有明确确认且仍适用于当前账号/系统的填报口径，可显式传入项目、类型、阶段、工作类型和时长，再进行 live 验证；不要把个人口径写死进技能或把单次参数覆盖当成已持久保存的设置。缺少确认或身份对应不明时，先补齐必要选择。
4. 按顺序执行当日只读查询 → 完整参数 `--preview --json` → 同参数真实提交。用户已授权填报且事实、字段齐全时，不因预览完成而再次索要同一授权；真实提交必须去掉 `--preview`，预览成功不等于填报成功。以公共提交保护的实时同日核对为最终写入门禁。
5. 中断后先判定最后完成的是查询、预览还是可能已发出的写入。若仅完成预览，按原日期和原文案继续受保护提交；若写请求可能已经发出但结果缺失，只读核实并遵守持久意图保护，不能因为“继续”而直接重发。收到 `submitted-confirmed` 且 `verified=true` 时，公共入口已经完成读回，可直接报告已提交并核验；其他结果按各自语义报告，不将 HTTP 成功当作核实成功。

### 修改工时记录
```bash
python scripts/update_time_entry.py <record-id> --job-desc "<new-description>" --preview
# 用户已明确授权撤回并重新提交后：
python scripts/update_time_entry.py <record-id> --job-desc "<new-description>" --withdraw-resubmit
```
→ 对审批中记录使用“查询原记录 → 撤回原审批 → 核实已撤回 → 携带原 ID 修改并重新提交 → 读回核验”的独立修改流程。撤回会影响现有审批，必须先告知并取得明确授权；`--preview` 只读，不撤回或写入。不得以新建记录、删除重建、修改状态字段等方式绕过限制，不删除或绕过普通提交保护日志。

不带 `--withdraw-resubmit` 的描述更新仍为旧的 `PUT /sn/timeEntry/update`；服务端可能拒绝审批中记录，不能宣称审批中总可直接改，也不得收到拒绝后自动撤回。原有 `--delete` 保持独立，不可与撤回重提组合。写入结果不明时只读核实，不盲目重跑；详见 [修改与撤回重提](references/amendment-workflow.md)。

### 查询工时列表
```bash
python scripts/query_time_entry.py 2026-04-10
```
→ 内部调用 `POST /sn/timeEntry/findEveryDayList`

### 获取工时详情
```bash
python scripts/get_time_entry_details.py <工时ID>
```
→ 内部调用 `GET /sn/timeEntry/details/<工时ID>`

> 注意：工时提交/查询/详情/修改接口统一通过完整认证会话发起，必须同时携带 `Authorization: Bearer {token}` 和 `Admin-OA-Token: {token}` 两个请求头。

### 查看报销申请状态
```bash
python scripts/query_fee_requests.py
python scripts/query_fee_requests.py --state 审批中 --with-progress
```
→ 查询当前用户的报销/费用申请；`--with-progress` 会展开返回申请的流程历史与当前节点。可用 `--start-date`、`--end-date`、`--page`、`--size` 和 `--json`。日期筛选须传完整时间：`--start-date "<YYYY-MM-DD> 00:00:00" --end-date "<YYYY-MM-DD> 23:59:59"`；服务端按 `yyyy-MM-dd HH:mm:ss` 解析，纯日期会被拒绝。

### 报销耗时与完成提醒

- 查询耗时先读 `--with-progress --json`，分别计算申请 `createdTime` 至今、本轮流程 `startEvent.createTime` 至今，以及各 `userTask` 的起止时间；待办节点用当前时间代替 `endTime`。使用带明确时区的实际当前时间与代码计算，不心算。
- 申请创建与本轮流程启动不一致时，同时说明两种口径；不能把两者之间的空档归责给某位审批人，也不能假定本轮历史包含此前审批。默认注明自然时间、包含周末与节假日；未结束只能说“已耗时”，不能声称总处理耗时或预计到账。
- 完成提醒固定追踪用户指定的申请 ID，而非每次重新选“最新一笔”；审批中静默，审批通过才报通过，驳回等结果单独说明。审批通过不等于打款到账。
- 建立定时提醒须实际运行查询并读回任务配置，明确检查频率、时区和通知渠道；不要声称已经验证尚未发生的完成通知。实施步骤见 [报销完成监控](references/reimbursement-monitoring.md)。

### 获取项目列表
```bash
python scripts/list_projects.py [--credentials PATH] [--base-url URL]
```
列出 OA 系统所有项目；**首次使用时必须让用户从中选择**，不要自行指定。

## 当前脚本

- `scripts/personal_settings.py`：账号/地址绑定的已确认设置、安全存储及严格字段校验
- `scripts/configure_personal_settings.py`：当前账号只读验证中文标签/代码，默认预览；明确 `--confirm-save` 后保存个人设置
- `scripts/oa_options.py`：只读项目与系统业务字典查询，boToPmStatus 由选中项目派生
- `scripts/runtime_bootstrap.py`：运行时解释器自检/自动切换
- `scripts/sn_oa_login.py`：登录并输出 token；支持 `--fetch-only` / `--submit` 两阶段（agent 多模态优先）与默认 ddddocr 闭环
- `scripts/query_fee_requests.py`：查询报销申请状态，可选展开当前审批节点/审批人
- `scripts/list_projects.py`：查询项目列表（支持 `--json`）
- `scripts/submission_guard.py`：公共提交保护（认证绑定、同日核对、一次写入、读回、私有持久日志与 POSIX 日锁）；只读 live 验证工具为 `tests/live_duplicate_readonly.py`
- `scripts/submit_time_entry.py`：普通工作中文/代码 live 解析，受保护提交或 `--preview` 只读预览；草稿仅支持预览，休假不可提交
- `scripts/query_time_entry.py`：查询某天工时列表
- `scripts/get_time_entry_details.py`：按工时 ID 查询详情
- `scripts/update_time_entry.py`：修改只读预览、明确授权的撤回重提；保留旧描述更新与独立逻辑删除
- `scripts/amendment_guard.py`：已有记录的状态流转、不可变字段、同日锁和持久修改意图保护
- `scripts/oa_utils.py`：公共能力（登录、认证会话、状态映射、工时管理、报销列表/详情/审批进度查询、`fetch_captcha` / `submit_login` / `login_with_code` / `OAAuth` 会话缓存与自动续期）

## 凭证文件格式

存放在 `memory/sn-work-record-credentials.md`：

```markdown
# 蜀宁 OA 凭证

- **账号**: <手机号>
- **密码**: <密码>
- **Base URL**: http://<IP>:<PORT>
旧凭据中的默认项目字段只兼容读取，提交不使用；个人设置单独存储。
```

支持加密存储（`.md.enc`），使用 AES-256-CBC + openssl，密钥通过 `OA_ENC_KEY` 环境变量或 `~/.openclaw/workspace/.cache/oa_enc_key` 提供。

### 凭据留存策略

- 用户只做一次查询时，使用权限受限的临时凭据文件，完成后删除。
- 用户希望以后直接查询时，应先征得同意，再加密持久保存；后续任务不得误删持久凭据，也不要再次索要密码。
- 凭据写入后必须实际验证解密、解析和登录成功，但验证输出禁止包含账号、密码、密钥或 token。
- 账号、密码、密钥和 token 不得写入 Hermes memory 或普通日志；memory 只可记录“已配置加密凭据”及非敏感路径。
- 完整的 Hermes 存储布局、复用流程与安全边界见 [`references/hermes-credential-storage.md`](references/hermes-credential-storage.md)。

## fillDate 格式

提交工时时 `fillDate` 使用纯日期格式 `YYYY-MM-DD` 即可（如 `2026-04-10`），API 不要求 `(周X)` 后缀。

## 默认配置

- **个人设置**：首次使用先运行 `scripts/oa_options.py`，由用户选择项目与适合岗位的字段，并确认实际时长。只读发现失败或字典未知时停止填写，索取 OA 表单标签/代码证据；不得猜测编号。
- **不写死真实项目值**：技能文档、通用示例与可复用配置说明使用 `{projectName}` / `<your-project-id>` 占位，不固化真实项目名或项目 ID；实际授权任务的预览与结果应显示用户选定或服务端核实的项目名称，以便核对，项目 ID 仍按隐私约定隐藏。
- **缺少字段**：提交和草稿都在认证前失败；底层接口在 POST 前再次检查，不再发送字符串 `None`。
- **批量提交**：逐日循环调用 `submit_time_entry()`，**登录一次复用同一个 session** 即可，不必每天重新登录（省验证码识别）
- **时长**：必须确认；无 8h/天默认值。单次命令行覆盖不保存。
- **状态**：`10` = 草稿，`20` = 审批中，`30` = 已审批

## 对话输出与隐私约定

- 默认回复中**不要主动暴露**项目 ID、工时记录 ID、项目配置值等内部标识。
- 查询结果默认只返回：日期、项目名称、时长、描述、状态、填写时间、更新时间。
- 只有在用户**明确要求查看 ID**，或执行修改/详情/删除等操作**确实必须引用 ID** 时，才展示对应 ID。
- 编写示例、文档、响应模板时，优先使用占位符（如 `<your-project-id>`、`<record-id>`），不要写入真实配置。
- 面向用户回复时可适量使用与状态相关的 emoji，保持简洁，不要每行堆叠表情。

### 报销查询输出约定

- 审批中用 `⏳`，已通过用 `✅`，已驳回用 `❌`，待提交用 `📝`。
- 默认不展示申请 ID、流程实例 ID、项目 ID 等内部标识。
- 不使用竖线压缩多个字段，也不在每行重复“状态”标签；移动端按两行一条记录展示。

#### 询问最新报销、状态或审批人

固定使用以下结构；“金额 + 状态”整行加粗。审批中展示节点和审批人，其他状态可省略这两行；公司不是必需字段，不默认展示。

```markdown
💰 最新报销

**¥{sumAmount}　{statusEmoji} {statusText}**

📁 项目：{projectName}
🔄 当前节点：{activityName}
👤 审批人：{assigneeName}
🕒 申请时间：{createdTime}
```

示例：

```markdown
💰 最新报销

**¥669.92　⏳ 审批中**

📁 项目：{projectName}
🔄 当前节点：商务负责人
👤 审批人：<审批人姓名>（<岗位>）
🕒 申请时间：2026-09-10 18:01
```

#### 询问历史申请记录、有哪些报销

标题后展示“项目 · 共 N 笔”，该汇总行加粗。每笔记录固定两行：第一行是序号、日期和金额，第二行是公司与状态；记录之间空一行。若项目不一致，则汇总行只写“共 N 笔”，并在每条记录第二行补充项目。驳回原因可另起第三行展示。

```markdown
💰 报销申请记录

**{projectName} · 共 {count} 笔**

1. {date}　¥{sumAmount}
{companyName} · {statusEmoji} {statusText}

2. {date}　¥{sumAmount}
{companyName} · {statusEmoji} {statusText}
```

示例：

```markdown
💰 报销申请记录

**{projectName} · 共 7 笔**

1. 2026-09-10　¥669.92
<公司名称> · ⏳ 审批中

2. 2026-06-18　¥411.20
<公司名称> · ✅ 已通过
```

## 自然语言示例

| 用户说 | 执行动作 |
|--------|---------|
| "今天填了工时" | `python scripts/submit_time_entry.py <日期> --job-desc "..."` 先确认完整字段与时长，再提交工时 |
| "周一到周三做某个项目" | 批量提交多天 |
| "把昨天工时改成xxx" | 查原记录并预览；审批中需另确认撤回影响，再用 `update_time_entry.py --withdraw-resubmit` 修改原记录并核验 |
| "查一下今天的工时状态" | `python scripts/query_time_entry.py <日期>` 查询 |
| "看看这条工时详情" | `python scripts/get_time_entry_details.py <工时ID>` |
| "把这条工时删掉" | `python scripts/update_time_entry.py <工时ID> --delete` |
| "查一下我的报销状态" | `python scripts/query_fee_requests.py` |
| "这笔报销到谁审批了" | `python scripts/query_fee_requests.py --state 审批中 --with-progress` |

## 节假日限制

以下节假日期间**不予填写工时**（2026年官方安排）：

| 节日 | 放假日期 |
|------|---------|
| 元旦 | 2026-01-01 ~ 2026-01-03 |
| 春节 | 2026-02-15 ~ 2026-02-23 |
| 清明节 | 2026-04-04 ~ 2026-04-06 |
| 劳动节 | 2026-05-01 ~ 2026-05-05 |
| 端午节 | 2026-06-19 ~ 2026-06-21 |
| 中秋节 | 2026-09-25 ~ 2026-09-27 |
| 国庆节 | 2026-10-01 ~ 2026-10-07 |

如遇节假日区间，回复：「节假日期间无需填写工时~」并拒绝提交。

## 提交成功输出模板

仅公共 API 返回 `submitted-confirmed` 后可使用成功模板。`skipped-existing` 回复“已有完全相同工时，未重复提交”；`observed-after-uncertain` 说明“写响应不确定，已只读核实匹配记录，未重发”。未核实/冲突不能套用成功模板；状态/缺字段与日志处理详见 [保护规则](references/submission-idempotency.md)。

```
✅ {日期}({星期})工时提交成功！

• 日期：{fillDate}
• 项目：{projectName}
• 时长：{manHour}h
• 描述：{jobDesc}
• 状态：{verifiedStateText}
```

修改描述成功时输出：

```
✅ {日期} 工时描述已更新！

• 日期：{fillDate}
• 新描述：{jobDesc}
• 状态：{verifiedStateText}
```

## 环境要求

- Python 3
- ddddocr：`pip3 install ddddocr`
- chinese_calendar：`pip3 install chinese_calendar`（用于精确判断中国工作日/节假日）
- requests：`pip3 install requests`
- 凭据文件：`memory/sn-work-record-credentials.md`（明文或 .enc 加密均可）

> 说明：脚本会优先使用依赖完整的解释器。若环境特殊，可通过 `SN_WORK_RECORD_PYTHON=/path/to/python` 显式指定解释器路径。若需要单独准备虚拟环境，推荐名称优先使用 `sn_work_record_env`（也兼容 `oa_worktime_env`、`ddddocr_env`、`.venv`、`venv` 等常见命名）。

## 首次使用

1. 使用已有凭据运行 `python scripts/oa_options.py`（只读）。
2. 请用户选择项目、填报类型、阶段、工作类型和实际时长；boToPmStatus 是项目/商机属性，由选中项目派生，不询问用户选择也不写死。通过 `configure_personal_settings.py --project "<项目名称>" --fill-type "<标签>" --project-phase "<标签>" --work-type "<标签>" --man-hour <时长>` 只读预览并验证；未知/歧义标签或不完整列表拒绝，详见 [首次选择与证据](references/personal-settings.md)。
3. 展示完整选择摘要，询问是否仅本次使用或持久保存。仅明确同意保存后运行 `scripts/configure_personal_settings.py --confirm-save`；不修改凭据，不自动迁移。

## 增强说明

- 公共认证头逻辑已统一收口到 `oa_utils.py`，避免不同脚本各写一套导致认证不一致
- 项目列表脚本新增 `--json`，方便调试或二次处理
- 提交、查询、详情、修改四个工时脚本都走同一套登录与认证逻辑，减少后续维护成本
- 所有入口脚本已接入 `runtime_bootstrap.py`：若当前解释器缺少依赖，会自动切换到可用解释器再执行
- 解释器优先级支持环境变量 `SN_WORK_RECORD_PYTHON` 覆盖，也会自动探测常见虚拟环境名称
- 当前 ClawHub 1.4.3 发布包未包含 `sn-work-record` launcher；在 Hermes 中直接使用 `scripts/` 下的入口
- 目录说明已与实际文件对齐：提交/查询/详情/修改都已提供脚本，避免再次误判
