---
name: sn-work-record
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

> Hermes 安装目录：`/root/.hermes/skills/sn-work-record`。当前发布包未包含文档中提到的 `sn-work-record` launcher，请直接使用 `scripts/` 下的 Python 入口。
>
> 所有 Python 脚本现在都带运行时自检：即使误用系统 `python3` 启动，也会优先自动切换到依赖完整的解释器。也可通过环境变量 `SN_WORK_RECORD_PYTHON` 显式指定解释器路径。

### 登录（自动执行，ddddocr 闭环）
```bash
python scripts/sn_oa_login.py [--credentials PATH] [--base-url http://X.X.X.X:PORT]
```
→ token 输出到 stdout（可 `| tee token.txt` 保存）

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
python scripts/query_fee_requests.py          # 自动复用缓存，不重新登录
python scripts/query_fee_requests.py --token <token>   # 显式指定，优先级最高
```

**写操作（提交/修改工时）在 401 时不会自动重试**，会清缓存后报错退出，避免重复提交；重新执行命令即可（会重新登录）。

已接入 `OAAuth` 的脚本：`query_fee_requests.py`、`query_time_entry.py`、`submit_time_entry.py`、`update_time_entry.py`、`get_time_entry_details.py`、`list_projects.py`。

> 缓存文件等同短期会话凭据（约 20 分钟有效），位于 `~/.cache/`（不在 `~/.hermes` 仓库内，不会被 git 提交）；需要强制重新登录时删掉 `~/.cache/sn-oa/token.enc` 与 `token.json` 即可。

### 提交工时
```bash
python scripts/submit_time_entry.py 2026-04-11 --job-desc "工时描述"
```
→ 内部调用 `POST /sn/timeEntry/saveOrUpdate`
> 默认优先使用凭据文件中的默认项目；支持 `--save-draft` 保存草稿，并会在直接提交时自动检查是否为工作日。凭据中没有默认项目时，**先询问用户选择哪个项目**，再显式传入 `--project-id/--project-name`。

### 修改工时记录
```bash
python scripts/update_time_entry.py <工时ID> --job-desc "新描述"
```
→ 内部调用 `PUT /sn/timeEntry/update`

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
→ 查询当前用户的报销/费用申请；`--with-progress` 会继续读取审批中申请的当前节点与审批人。可用 `--start-date`、`--end-date`、`--page`、`--size` 和 `--json`。

### 获取项目列表
```bash
python scripts/list_projects.py [--credentials PATH] [--base-url URL]
```
列出 OA 系统所有项目；**首次使用时必须让用户从中选择**，不要自行指定。

## 当前脚本

- `scripts/runtime_bootstrap.py`：运行时解释器自检/自动切换
- `scripts/sn_oa_login.py`：登录并输出 token；支持 `--fetch-only` / `--submit` 两阶段（agent 多模态优先）与默认 ddddocr 闭环
- `scripts/query_fee_requests.py`：查询报销申请状态，可选展开当前审批节点/审批人
- `scripts/list_projects.py`：查询项目列表（支持 `--json`）
- `scripts/submit_time_entry.py`：提交工时或保存草稿
- `scripts/query_time_entry.py`：查询某天工时列表
- `scripts/get_time_entry_details.py`：按工时 ID 查询详情
- `scripts/update_time_entry.py`：按工时 ID 修改描述或逻辑删除
- `scripts/oa_utils.py`：公共能力（登录、认证会话、状态映射、工时管理、报销列表/详情/审批进度查询、`fetch_captcha` / `submit_login` / `login_with_code` / `OAAuth` 会话缓存与自动续期）

## 凭证文件格式

存放在 `memory/sn-work-record-credentials.md`：

```markdown
# 蜀宁 OA 凭证

- **账号**: <手机号>
- **密码**: <密码>
- **Base URL**: http://<IP>:<PORT>
- **默认项目ID**: <your-project-id>（可选）
- **默认项目名称**: <your-project-name>（可选）
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

- **项目**：首次使用（凭据文件缺少「默认项目ID/默认项目名称」）时，**必须先询问用户要用哪个项目**，不要猜测、也不要沿用其他环境的值。执行 `list_projects.py` 把列表给用户选，确认后写入 `memory/sn-work-record-credentials.md`。
- **不写死真实项目值**：技能文档、示例与回复中一律用 `{projectName}` / `<your-project-id>` 占位，禁止出现真实项目名或项目 ID。
- **坑**：若凭据文件缺少默认项目，提交接口会收到 `projectId: "None"` 并返回 500 `JSON parse error ... Long from String "None"`。此时用 `list_projects.py --json` 取回项目 id，再以 `--project-id/--project-name` 显式传入。
- **批量提交**：逐日循环调用 `submit_time_entry()`，**登录一次复用同一个 session** 即可，不必每天重新登录（省验证码识别）
- **时长**：8h/天
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
👤 审批人：赵鑫炜（研发经理）
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
天域智慧 · ⏳ 审批中

2. 2026-06-18　¥411.20
天域智慧 · ✅ 已通过
```

## 自然语言示例

| 用户说 | 执行动作 |
|--------|---------|
| "今天填了工时" | `python scripts/submit_time_entry.py <日期> --job-desc "..."` 提交 8h 工时（默认项目） |
| "周一到周三做某个项目" | 批量提交多天 |
| "把昨天工时改成xxx" | 查昨天 → `update_time_entry.py` 修改描述 |
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

```
✅ {日期}({星期})工时提交成功！

• 日期：{fillDate}
• 项目：{projectName}
• 时长：{manHour}h
• 描述：{jobDesc}
• 状态：审批中 🟢
```

修改描述成功时输出：

```
✅ {日期} 工时描述已更新！

• 日期：{fillDate}
• 新描述：{jobDesc}
• 状态：审批中 🟢
```

## 环境要求

- Python 3
- ddddocr：`pip3 install ddddocr`
- chinese_calendar：`pip3 install chinese_calendar`（用于精确判断中国工作日/节假日）
- requests：`pip3 install requests`
- 凭据文件：`memory/sn-work-record-credentials.md`（明文或 .enc 加密均可）

> 说明：脚本会优先使用依赖完整的解释器。若环境特殊，可通过 `SN_WORK_RECORD_PYTHON=/path/to/python` 显式指定解释器路径。若需要单独准备虚拟环境，推荐名称优先使用 `sn_work_record_env`（也兼容 `oa_worktime_env`、`ddddocr_env`、`.venv`、`venv` 等常见命名）。

## 首次使用

1. 运行 `python scripts/sn_oa_login.py` 完成登录
2. 运行 `python scripts/list_projects.py` 获取项目列表，**询问用户选择哪个项目**
3. 用户确认后，把项目 ID 与名称写入凭据文件

## 增强说明

- 公共认证头逻辑已统一收口到 `oa_utils.py`，避免不同脚本各写一套导致认证不一致
- 项目列表脚本新增 `--json`，方便调试或二次处理
- 提交、查询、详情、修改四个工时脚本都走同一套登录与认证逻辑，减少后续维护成本
- 所有入口脚本已接入 `runtime_bootstrap.py`：若当前解释器缺少依赖，会自动切换到可用解释器再执行
- 解释器优先级支持环境变量 `SN_WORK_RECORD_PYTHON` 覆盖，也会自动探测常见虚拟环境名称
- 当前 ClawHub 1.4.3 发布包未包含 `sn-work-record` launcher；在 Hermes 中直接使用 `scripts/` 下的入口
- 目录说明已与实际文件对齐：提交/查询/详情/修改都已提供脚本，避免再次误判
