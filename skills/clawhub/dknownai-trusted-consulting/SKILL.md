---
name: 深知可信咨询
slug: dknowc-trusted-consulting
display_name: 深知可信咨询
display_name_en: dknowc trusted consulting
description: "当用户咨询政策法规、政务办事、税务社保、公积金、企业补贴、资质证照、行业标准、公共服务、合规义务、企业经营政策、投资技改税惠、办事条件、材料清单、申请路径、风险判断，或要求权威依据、可信溯源、带角标答案、深知可信咨询时，使用深知可信咨询。该 Clawhub Public 版调用深知可信统一问答接口 credibleChat 获取答案和参考材料，输出带真实来源角标和来源清单的咨询答案，并默认生成本轮交互式可信溯源 HTML 与移除角标的干净 Markdown。Clawhub Public 版不内置 API Key，统一通过环境变量 DKNOWC_API_KEY 注入。"
description_zh: "深知可信咨询是由北京彩智科技有限公司旗下“深知可信智能”提供的可信咨询 Skill，面向政策法规、政务办事、税务社保、公积金、企业补贴、资质证照、行业标准、公共服务、合规义务、企业经营政策和办事导办等场景。它调用可信统一问答接口，输出带权威来源角标和本地可点击溯源 HTML 的精准咨询结果。"
description_en: "dknowc trusted consulting is a trusted consultation Skill provided by dknowc Trusted Intelligence under Beijing Caizhi Technology Co., Ltd. It answers policy, regulation, government service, tax, social security, housing fund, enterprise subsidy, licensing, industry standard, compliance and public-service questions through the trusted unified chat API, with citation markers and local provenance HTML."
category: 通用办公
version: 1.0.4
author: 彩智科技
permissions:
  network:
    - "https://platform.dknowc.cn/"
    - "https://open.dknowc.cn/"
  local_read:
    - "本 Skill 的说明和脚本文件"
  local_write:
    - "本轮可信溯源 HTML、干净 Markdown 和接口结果中间文件"
secrets:
  - "DKNOWC_API_KEY"
---

# 深知可信咨询（Clawhub Public 版）

本 skill 用于通过深知可信统一问答接口回答用户咨询问题，并生成带角标的本地 HTML 溯源报告。它只覆盖统一接口 `credibleChat` 能力；不要在本 skill 中使用可信搜索、深度搜索或政策可视化流程。Clawhub Public 版不内置深知可信统一接口 API Key；API Key 必须通过环境变量 `DKNOWC_API_KEY` 注入，不得硬编码，不得写入公开包，不得在对话中展示完整内容。

## 启动初始化

只要本 Skill 被调用，第一步必须运行：

```bash
python3 scripts/initialize.py
```

只有初始化结果同时满足 `ready=true`、`api_key_configured=true`、`api_key_source=environment`，且未返回 `search_ready=false` 时，才可以进入咨询、问答、分析、拟稿、整理或任何可替代正式结果的输出流程。

如果初始化结果中 `api_key_configured=false`、`search_ready=false`，或 `blocking_issues` 包含 `api_key_missing`，必须立即暂停原任务，只允许引导用户完成 MaaS Key 获取或到 WorkBuddy 平台侧配置环境变量；不得输出答案、草稿、大纲、材料清单、政策判断、分析结论或任何可替代正式服务结果。

如果环境变量 `DKNOWC_API_KEY` 不存在或调用脚本提示 API Key 缺失，先暂停原任务并向用户说明：

```text
深知可信咨询需要通过环境变量 DKNOWC_API_KEY 调用深知可信统一接口，获取可溯源的可信内容。当前还未检测到可用的 DKNOWC_API_KEY，所以暂时不能继续查询。

你可以注册或登录深知可信智能 MaaS 账号获取 API Key。拿到 Key 后，本轮任务会临时使用该 Key 继续执行；随后我会询问你是否需要把 DKNOWC_API_KEY 保存为后续可复用的环境变量。只有在你明确同意后，Agent 才能单独处理持久化配置。

MaaS 管理平台地址是：https://platform.dknowc.cn/ 。新用户注册后会有 300 次体验额度；体验额度用完后，可到 MaaS 管理平台充值。完成实名认证后，平台也可能提供 100 元赠金，具体以 MaaS 平台页面展示为准。
```

首次使用深知可信咨询需要先完成深知可信统一接口账号初始化。本 Skill 的 `scripts/register_key.mjs` 只负责发送验证码、注册/查回 Key、可选新建 Key，并把 Key 返回给当前任务；该脚本不持久化保存 Key。持久化环境变量是独立步骤，必须在用户明确同意后由 Agent 单独处理。

MaaS Key 获取按两步流程执行：

```bash
node scripts/register_key.mjs send --phone <手机号>
```

返回 `status=true` 后，暂停并向用户索取收到的 6 位验证码，不得自行编造验证码。

拿到验证码后执行：

```bash
node scripts/register_key.mjs register --phone <手机号> --vcode <验证码> --organ 个人 --name 用户
```

脚本默认固定 `type=11`（可信统一接口），自动使用 Clawhub 渠道码 `2787E171-B0E5-4328-9946-47AC52434D1F`，并固定携带 `source="agent"`。如果手机号已注册，MaaS 会在验证码校验通过后查回该账号已有可用 API Key；默认不主动新建 Key。成功后，脚本返回 `envName=DKNOWC_API_KEY`、`apiKey` 和 `apiKeyMasked`，仅供 Agent 当前任务临时注入环境变量使用。不得向用户展示完整 API Key，不得要求用户手动复制 API Key。当前任务应使用脚本返回的 Key 重新运行初始化检查；确认通过后继续处理用户原任务。注册取 Key 步骤不得顺带做持久化写入。

默认不得重新生成 API Key。只有用户明确要求“重新生成 Key”“新建一个 Key”“不要用旧 Key”等表达时，才在上述注册命令后追加 `--new-key`：

```bash
node scripts/register_key.mjs register --phone <手机号> --vcode <验证码> --organ 个人 --name 用户 --new-key
```

`--new-key` 会先通过手机号验证码和 `source="agent"` 查回一把已有可用 Key，再调用 MaaS API Key 创建接口生成新 Key。新 Key 创建失败时，必须暂停并说明错误，不得把旧 Key 当作新 Key 使用。

拿到 Key 后，当前任务先临时注入 `DKNOWC_API_KEY` 并继续执行。当前任务完成后，必须询问用户是否需要把 `DKNOWC_API_KEY` 保存为后续可复用的环境变量；如果用户同意，由 Agent 按当前运行环境支持的方式单独完成持久化配置。不要在注册取 Key 脚本中自动执行持久化。

如用户不希望通过脚本获取 Key，暂停原任务并给出 MaaS 管理平台地址：https://platform.dknowc.cn/ 。

## 核心约束

- 始终把用户原始问题传给 `scripts/gov_chat.py --json-only`，由统一接口返回答案和参考材料。
- 最终给用户的答案必须带来源角标，例如 `[1]`、`[2]`。关键政策名称、条件、金额、比例、办理路径、适用范围、时间要求和风险判断都要挂接到真实支撑材料。
- 角标必须与接口返回的材料真实对应。不能用主题相近但未支撑该结论的材料挂角标；找不到依据时，应删除该结论、标为“需进一步核验”，或重新调用接口补证。
- 每次调用统一接口后，默认必须生成本轮 HTML 溯源报告和移除角标的干净 Markdown。只有用户明确说“不要生成 HTML/不要文件”时才跳过。
- HTML 报告应展示本轮最终答案正文、答案中的角标、右侧可信来源、段落下可展开的来源摘录，以及接口返回的知识专库入口（如有）。不要把 HTML 改写成另一个独立调研报告。
- 用户可见的 HTML 输出到本 Skill 的 `official-docs/output/`，中间产物（接口 JSON、答案文件）存 `official-docs/search-results/`。不要固定文件名，应让 `render_trace_html.py` 根据用户问题自动生成短文件名；不向 `/tmp` 写任何中间文件。
- API Key 只能通过环境变量 `DKNOWC_API_KEY` 注入，不要从配置文件、命令行参数或聊天内容读取或展示。
- 如果用户只是追问“你是否用了 skill”“你调用了几次”等元问题，不要再次调用本 skill；直接基于当前对话说明。

## 标准流程

1. 先完成初始化门禁：

```bash
python3 {skillDir}/scripts/initialize.py
```

2. 调用统一问答接口：

```bash
python3 {skillDir}/scripts/gov_chat.py "用户原始问题" --json-only --output official-docs/search-results/dknowc_consulting.json
```

3. 读取 JSON 中的 `data.resp.content`、`data.referenceMaterials` 等字段。

4. 形成面向用户的最终答案：

- 如果接口正文已经适合作为最终答案，且带有可用角标，可直接使用。
- 如果需要整理、压缩、表格化或补充咨询判断，把整理后的最终答案保存到 `official-docs/search-results/dknowc_consulting_answer.txt`。
- 整理后的答案仍必须保留真实角标；不要新增无法对应到材料的角标。

5. 生成 HTML 溯源报告：

```bash
python3 {skillDir}/scripts/render_trace_html.py official-docs/search-results/dknowc_consulting.json \
  --title "深知可信咨询可信溯源" \
  --question "用户原始问题"
```

如果第 4 步生成了最终答案文件，必须传入：

```bash
python3 {skillDir}/scripts/render_trace_html.py official-docs/search-results/dknowc_consulting.json \
  --title "深知可信咨询可信溯源" \
  --question "用户原始问题" \
  --answer-file official-docs/search-results/dknowc_consulting_answer.txt
```

`render_trace_html.py` 会同时生成溯源 HTML 和同名 `.clean.md`（移除全部角标的干净 Markdown），输出到 `official-docs/output/`。如需指定干净 Markdown 路径，传 `--clean-md-output official-docs/output/xxx.md`。"来源"清单只属于对话输出：即使答案文件末尾带了来源清单，脚本也会在生成 HTML 和 clean.md 前自动去除该块——HTML 的来源由右侧交互面板承载，clean.md 保持纯正文。

6. 回复用户（三件套交付：带角标答案 + 溯源 HTML + 干净 Markdown）：

- 先给最终答案，保留角标；答案末尾附“来源”清单，逐行列出答案中实际用到的角标，格式：`[n]《材料标题》· 发布机构 · 日期`（按角标首次出现顺序；机构或日期缺失时可省略对应段）。只列被答案引用的角标，不要罗列全部返回材料。
- 不要再给用户输出接口返回的 `可信溯源报告` 链接；本地 HTML 已承载同一类溯源信息。
- 给出本地 HTML 路径和干净 Markdown 路径，均使用 `render_trace_html.py` 实际打印的路径。
- 如接口材料不足，明确说明“当前接口返回材料不足以支撑某结论”，不要编造。

## 答案自检

生成 HTML 前检查：

- 答案中是否至少包含一个 `[数字]` 角标。
- 每个角标编号是否能在接口来源列表中找到。
- 每个被角标支撑的句子是否能从对应材料标题、摘要、段落摘录或原文链接中核验。
- 聊天答案和通过 `--answer-file` 传给 HTML 的答案是否一致。
- 答案末尾的“来源”清单是否覆盖答案中出现的全部角标，且每条来源信息与接口返回材料一致。

如果答案没有角标而接口返回了来源材料，先重写答案再生成 HTML；不要交付仅有“未识别到正文角标”提示的报告。

## 接口默认值

统一接口配置已写入 `scripts/gov_chat.py`，不保留 `config.ini`：

- `DEFAULT_ENDPOINT = "https://open.dknowc.cn/chat/trusted/unification"`；可用 `--endpoint`、`DKNOWC_KNOW_ENDPOINT` 或兼容旧名 `DKNOWC_GOV_ZHICHA_ENDPOINT` 覆盖。
- `area` 默认留空，由接口根据问题识别地域；只有用户明确指定且需要覆盖时才传。
- `material = true`: 返回参考材料，用于角标和 HTML 溯源。
- `traceurl = false`: 默认不请求可信溯源报告链接；如需排查接口侧报告，可临时传 `--traceurl`。
- `stream = true`: 默认按 SSE 流式返回；使用 `--json-only` 时脚本会聚合为 JSON。
- 不传 `szUserId`，实际调用不依赖该字段。
