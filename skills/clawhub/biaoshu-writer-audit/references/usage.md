# 执行细节（操作手册）

本文件是**执行任务时的完整操作指引**——做解读/制作/合规、生成报告、处理边界情形时按需查阅。接口契约与返回字段见 [api.md](api.md)。

> ⚠️ **数据外发与知情同意**：解读/制作/合规/查重都会把用户提供的文件**上传至百炼®标书云端**（`biaoshu.zhiliaobiaoxun.com`）处理，此类文件常含商业、报价与个人信息；**上传文件与结果会以账户身份留存在百炼®标书服务器**（结果/成品约 7 天过期，可登录官网查看管理）。**首次上传前必须确认用户知悉并同意**（完整披露见 SKILL.md「⚠️ 权限与数据说明」）。

## ⚠️ 输出约定（必须遵守，除非用户明确说不要）

运行 `zcm.py` 时**老老实实把脚本输出原样给用户看**，不得为了「省事/抽字段」把它藏起来：

1. **实时进度照常显示**：解读/抽包/生成/合规/查重都会把百分比+阶段（如 `[20%] 智能解读中`）打到 **stderr**；生成成品标书会优先展示细进度（如 `[47%] 生成内容 · 正在写正文 32/80 节 · 当前：项目实施方案 · 已用 6分钟`）。**不要 `2>` 重定向、不要吞掉**——用户要看到进度推进。需要后台实时播报时用 `progress-stream` + Monitor，而非把进度倒进文件。
2. **完整交付产物位置**：每次产出后，必须把以下信息明确告知用户：
   - 智能解读结果/报告（`*_智能解读.html` 等）
   - 成品标书默认给短时下载链接（含文件名、大小、有效期）；用户明确要本地文件时再下载为 `*_投标文件.docx`
   - 合规审查结果/报告（`*_合规审查.html` 等）

   脚本本身已打印这些信息（`generate` 默认打印下载链接；`result -o` 成功后打印本地全路径）；**别用 `>`/`2>` 把它们重定向掉**。若用 `--no-wait`，完成后须主动用 `download-url <job_id>` 补取成品链接，或在用户要求本地文件时用 `result <job_id> -o <路径>.docx` 下载。

   此外，解读/生成/合规/查重完成后脚本会打印一行 `💰 当前可用字数：X`——**照常转述给用户**，让其对可用字数与「够不够下一次」有数；查询失败时不打印，属正常，不必追问。

> 反例（禁止）：`python3 scripts/zcm.py generate <pid> > out.json 2> log` —— 这会同时藏掉进度和成品全路径。

3. **凭证/字数类提示不要把命令与 exit 码原样抛给用户**：缺 Key（exit 2）、可用字数不足（402）这类脚本输出是给你（助手）看的提示。你应当把它翻译成一句「用户下一步该做什么」（去官网拿 Key、按指引把 Key 写入 skill 目录下的 `config.json`、或打开官网购买会员/字数包）——不要让用户自己敲命令，也不要索取或代存用户的 Key。
4. **本手册里的一切命令永不面向用户**（SKILL.md 第一铁律）：命令只在后台执行；向用户介绍功能或举例时，用 SKILL.md 各功能「使用示例」的场景话术（用户怎么说 → 得到什么），不要把本文件的命令、参数、代码块贴进回复。

## 用法速查（完整流程）

```bash
# 1. 配凭证：用户在 skill 目录下自建 config.json 写 {"app_key":"bk_live_xxx"}（Key 不进对话）
python3 scripts/zcm.py me                            #    连通 + 可用字数自检
python3 scripts/zcm.py interpret 招标文件.pdf --report html   # 2. 解读 → project_id（+解读报告）
python3 scripts/zcm.py packages <project_id>         # 3. 抽包（多包才需选包）
python3 scripts/zcm.py generate <project_id>         # 4. 生成成品标书（消耗可用字数）
python3 scripts/zcm.py compliance <project_id> 投标文件.docx --report html --name 招标文件.pdf   # 5. 可选：标书审查
python3 scripts/zcm.py duplicate 投标A.docx 投标B.docx --tender-file 招标文件.pdf --legal-possession-attested --report html  # 6. 可选：标书查重（+查重报告）
```
招标文件支持 `.pdf/.doc/.docx`；标书审查和标书查重的投标文件支持 `.pdf/.doc/.docx`。全部自动轮询、实时播报后端进度。各步详解见下。

## 目录
- [第 1 步：凭证](#第-1-步凭证)
- [第 2 步：智能解读](#第-2-步智能解读)
- [第 3 步：抽取分包](#第-3-步抽取分包)
- [第 4 步：生成成品标书](#第-4-步生成成品标书)
- [第 5 步：标书审查](#第-5-步标书审查)
- [第 6 步：标书查重](#第-6-步标书查重)
- [报告生成与命名](#报告生成与命名)
- [关键约定](#关键约定)

---

## 第 1 步：凭证

凭证默认存在 **skill 内 `config.json`**（权限 600，含真实 Key——**绝不上传发布包/提交仓库**，发布包不含配置文件）。Api Key 只从 **skill 内 config.json** 读取（路径固定，不经环境变量、无旧目录回退、不可重定向）。

**只需 Api Key 一项**，由用户**自行到官网获取**（本 skill 不代注册、不收集手机号/验证码）。获取全路径（转述时逐步骤完整给出，链接原样显示完整 URL）：
打开官网 https://biaoshu.zhiliaobiaoxun.com/ → 手机号 + 短信验证码注册并登录（手机号注册赠 5 万字）→ 点**左侧菜单『Skill 接入 → 获取 Api Key』**，在弹出面板中查看/复制 Api Key（首次打开自动生成，形如 `bk_live_xxxxx`，重置后旧 Key 立即失效）。

**配置方式（唯一引导方式：用户本人写入本地凭证文件，Key 不进对话）**：
指导用户在本 skill 目录下创建 `config.json`，写入一行 `{"app_key": "bk_live_xxxxx"}`（把 Key 换成自己的）。**不要索取、让用户粘贴或在回复中复述 Key**（会话记录、截图、链接预览都可能泄露凭证）。可选字段仅保留 `output_dir` 成品存放目录；开放 API 地址固定为官方生产环境，不接受本地覆盖。配好后先跑 `me` 自检连通与可用字数。

- 缺凭证时脚本会打印官网获取指引并退出（码 2），把指引转述给用户即可。
- 先 `python3 scripts/zcm.py me` 确认连通与可用字数（生成会消耗可用字数）。

### 可用字数不足（402，给用户自助链接，skill 不代办）

可用字数不足时脚本会打印引导，照原样转达给用户，由用户**自行登录官网购买会员或字数包**后回到对话继续，Api Key 全程不变：入口 `https://biaoshu.zhiliaobiaoxun.com/recharge`（用注册手机号登录后操作）。

- 🔒 **凭证保护（强制）**：平台 402 错误体里的 `recharge_url` / `bind_url` **携带明文 `bind_key`（即用户的 Api Key）**——**一律不得把这类带 Key 的链接转发进对话**（会话记录、截图、链接预览都可能泄露 Key，他人拿到即可操作该账户）。只给上面这条不含任何参数的普通入口链接。
- ⛔ **禁止**：已有 Key 的用户，别引导他去官网「另注册新账号 / 另生成新 Key 再切换」——可用字数会留在孤立新账号上、还得换 Key。

## 第 2 步：智能解读

唯一招标文件入口；只在这步传一次，后续全程复用 `project_id`。

```bash
python3 scripts/zcm.py interpret /path/招标文件.pdf      # 仅本地路径
```
- 支持 `.pdf/.doc/.docx`，**≤ 50 MB**（超限脚本提前报错）。自动轮询，结束打印 `project_id`（**记下它**）+ **完整解读结果**。
- **不支持云端链接**：传入 http(s) 链接会被脚本直接拒绝（本 skill 不做任何远程抓取）。用户给的是链接时，请他先自行下载到本地，再提供本地路径。
- **直接把解读结果展示给用户**——含 8 维度 + 控标洞察：项目基本信息 / 合标项 / 废标项 / 评审项 / 关键要求 / 商务条款 / 报价要求 / 采购背景分析 / 控标洞察（`decision_analysis`）。挑重点讲（控标建议、废标红线、评分结构），别只丢 `project_id`。字段口径见 [api.md 附录 A](api.md)。
- 展示后**主动问是否生成解读报告**（见[报告生成与命名](#报告生成与命名)）。

## 第 3 步：抽取分包

```bash
python3 scripts/zcm.py packages <project_id>
```
- 把返回的 `packages` 呈现给用户挑选，收集选中的 `package_ids`。
- `max_total_pages` 当前上限为 **500**；用户想指定页数时，以抽包结果里的上限为准。
- `is_multi_package=false` → 跳过选包，第 4 步不带 `--package-ids`。

## 第 4 步：生成成品标书

**唯一消耗可用字数的步骤**，耗时较长。默认不下载本地文件，完成后输出短时下载链接：
- 用户只要成品 → 不传 `-o`，脚本完成后打印文件名、大小、下载链接和有效期。
- 用户明确要本地文件 → `-o <路径>`；想长期固定本地输出目录 → `login --output-dir <目录>`。

```bash
python3 scripts/zcm.py generate <project_id> --package-ids 11,12 --total-pages 80
# 需要本地文件时：python3 scripts/zcm.py generate <project_id> -o 投标文件.docx
# 非多包：python3 scripts/zcm.py generate <project_id>
```
- 自动轮询（默认超时 3600s，`--timeout` 可调）。完成后默认打印**成品下载链接**；如使用 `-o`，则打印**成品完整路径**+所在目录，**两项都告诉用户**。
- 后端会按「选包 → 抽需求 → 生成大纲 → 生成正文 → 填充制式模板 → 导出」串行完成；页数规划会综合分包结构、技术/商务内容、表格和图表，`total_pages` 最高 500。
- 制式表格/范本会尽量自动填充；无法确认的公司资料、日期、报价、签章等信息会保留为待填项，不要替用户编造。
- **跟用户解释字数计费时分两层说**：解读 / 标书审查 / 生成三个入口提交前都会先看可用字数，可用字数不足会被拦住；但**真正消耗可用字数的是生成**。不要把“提交前门槛”说成“解读/标书审查也会消耗字数”。
- ⏱ **生成可能耗时 >10 分钟**（实测 30 页约 15 分钟）。脚本本身轮询不会超时，但**前端/工具调用常有 ~10 分钟上限**会把命令杀掉——**注意：后端任务不受影响、仍在跑，切勿重新提交（会重复扣费）**。长任务推荐：`generate <pid> --no-wait` 拿 `job_id`，再用 `progress-stream <job_id>`（配合 Monitor 后台实时播报）续查到终态，最后 `download-url <job_id>` 取下载链接；用户明确要本地文件时再用 `result <job_id> -o <路径>.docx` 下载。万一命令被杀，用同一 `job_id` 续查即可，不要重发 generate。

## 第 5 步：标书审查

要**两样输入，都要让用户提供**：
1. **招标文件**（`.pdf/.doc/.docx`）→ 经第 2 步解读产出 `project_id`；已解读则复用，不重传。
2. **投标文件**：**一份或多份** `.pdf/.doc/.docx`，被审查对象（仅本地路径），**支持多选，最多 100 份**；**每份 ≤ 1024 MB**，**总大小不超过 2GB**。

```bash
python3 scripts/zcm.py compliance <project_id> /path/投标A.docx /path/投标B.docx
# 暗标/电子标：加 --blind / --electronic
# 敏感单位名称：加 --sibling-unit-names "甲公司,乙设计院"
# 关闭语义审查：加 --no-semantic-review
```
- **不支持云端链接**：传链接会被脚本拒绝，请用户先自行下载到本地。
- 审查选项与平台一致：暗标、电子投标、敏感单位名称、语义审查开关。关闭语义审查时只能表述为“规则类检查结果”，不能说成完整语义审查。
- **直接把合规结果展示给用户**——含 `summary`（风险计数 + 一句话结论 + 语义审查状态）、`partial_summary`（阶段性/部分结果统计）、`scope_summary_lines`（检查范围）、`issues[]`（风险等级/招标依据/投标证据/修改建议）、`similarity_issues[]`（多文件雷同）、`manual_items[]`（人工核查清单）。优先讲高风险、结论与审查完整性。字段见 [api.md 附录 B](api.md)。
- 若 `summary.conclusion_phase`、`summary.semantic_review` 或 `partial_summary` 表示语义审查处理中、部分完成或只完成规则检查，必须如实说明“当前为部分结果/语义审查未完整完成”，不要说成完整审查完成。
- `risk_level` 实测为 `high`/`review`/`tip`，脚本输出与报告**已自动转中文**（高风险/待复核/提示），直接用中文呈现。
- 未解读就调 → 409；投标文件缺失/类型不对 → 422（两份输入缺一不可）。
- 展示后**主动问是否生成合规报告**（见下）。

## 第 6 步：标书查重

用于比较不同主体投标文件之间的雷同/相似风险。它不是标书审查，也不判断投标文件是否合规；结果只作为提交前内部自查线索，不构成围标、串标或违法违规的法律认定。

发起前必须先问并得到用户确认：
「请确认你合法持有并有权处理本次上传的全部投标文件/招标文件。确认后我再发起标书查重。」

```bash
python3 scripts/zcm.py duplicate /path/A公司投标.docx /path/B公司投标.docx --legal-possession-attested --report html
# 可选关联招标文件，用于排除招标原文造成的共同表述：
python3 scripts/zcm.py duplicate /path/A公司投标.docx /path/B公司投标.docx /path/C公司投标.docx \
  --tender-file /path/招标文件.pdf --legal-possession-attested --report html
# 可选关闭维度：--no-image / --no-metadata / --no-semantic
# 默认排除招标文件原文共同表述；如用户明确要求不排除，可加 --include-tender-baseline
```

- 投标文件必须 **2-3 份**，支持 `.doc/.docx/.pdf`；单份 ≤ 1024 MB，总大小不超过 2GB。
- 招标文件可选 **1 份**，支持 `.doc/.docx/.pdf`，≤ 50 MB；用于降低招标原文共同表述对相似度的干扰。
- **不支持云端链接**：传链接会被脚本拒绝，请用户先自行下载到本地。
- 查重维度：连续文本/段落结构、图片相似、文档元数据、主体线索、招标基线。
- 查重完成后展示 JSON 里的核心结论，并在用户需要或命令带 `--report html|docx|both` 时生成本地 HTML/Word 查重报告。必须输出报告绝对路径。
- 查重报告只呈现文件对风险率、证据片段、图片/元数据/主体线索异常、修改建议；不要输出“已串标/确认围标”等定性结论。

## 报告生成与命名

解读/合规/查重结果可渲染成报告（HTML / Word），零依赖：

```bash
# 随命令一步出（默认 html；要 Word：--report both）
python3 scripts/zcm.py interpret 招标文件.pdf --report html
python3 scripts/zcm.py compliance <pid> 投标.docx --report html --name 招标文件.doc
python3 scripts/zcm.py duplicate 投标A.docx 投标B.docx --legal-possession-attested --report html
# 按 job_id 补出
python3 scripts/zcm.py report --job <JOB_ID> --name 招标文件.pdf            # html
python3 scripts/zcm.py report --job <JOB_ID> --name 招标文件.pdf --format both  # +Word
python3 scripts/zcm.py report --job <JOB_ID> --service bid_duplicate --format html
```
- **默认只出 HTML**；用户明确要 Word 才 `docx`/`both`。
- 命名：`招标文件名_智能解读` / `招标文件名_合规审查` / `标书查重_时间戳`。取名优先级：`--name` > 结果自动识别（`original_filename` / `project_info.项目名称` / 本地缓存）> `标签_时间戳`。
  - `interpret` 自动用上传文件名；`generate` 自动用缓存名；**`compliance`/`report --job` 拿不到招标文件名时务必带 `--name`**，否则退化时间戳。`bid_duplicate` 不依赖招标文件名时默认使用时间戳命名。
- 报告内容依赖后端按 [api.md 附录 A/B](api.md) 返回完整结果；合规 HTML 总览会展示检查范围、结论、语义审查状态和部分结果摘要；`/result` 只回句柄或字段空时，报告注明「无明细」而不报错。

## 知识库取数（供本地待填项回填）

当需要用企业资料辅助**本地**待填项回填时，不改走生成主流程，而是单独查询开放 API：

```bash
python3 scripts/zcm.py knowledge-base
python3 scripts/zcm.py knowledge-base company_profile
python3 scripts/zcm.py knowledge-base qualifications --page 1 --page-size 50
python3 scripts/zcm.py knowledge-base performances --page 1 --page-size 50
python3 scripts/zcm.py knowledge-base financial_reports --page 1 --page-size 50
```

- 返回按类别分组的结构化 JSON；分页类默认前 **50** 条。
- **明确排除**：历史标书库、标书模板库。
- 字段含义、可否直接回填、敏感字段边界见 [knowledge-fields.md](knowledge-fields.md)。

## 关键约定

- **必须输出完整路径**：解读报告 / 成品标书 / 合规报告生成后，把**每个文件的完整绝对路径**逐行告诉用户（脚本已用「已生成…/已下载…」打印绝对路径，照搬即可）——**不要只说落在某目录**。
- **进度播报（两阶段，必须这样做才能实时）**：Bash 工具不流式传输 stderr，`--no-wait` + `progress-stream` + Monitor 是唯一能让用户看到实时进度的方式。长任务（interpret / generate / compliance / duplicate）统一走以下三步：
  1. **提交**（同步，快）：加 `--no-wait`，Bash 运行后立即拿到 `job_id`。
  2. **实时监听**：`Bash(run_in_background=True)` 运行 `python3 scripts/zcm.py progress-stream <job_id>`，再用 Monitor 订阅该进程 stdout——每行状态变更即时通知 Claude，Claude 实时转达给用户（如「5% 准备文档」→「生成内容 47% · 正在写正文 32/80 节」→「导出 Word」→「完成」）。Monitor 的 description 用正常任务名，**不带「重试」等临时标签**——即使是 worker_lost 后重新提交的 job，新 job 已正常运行，描述应反映当前状态而非历史原因。长时间无新百分比时，也要按心跳句转达“任务仍在运行，已用 X 分钟”，避免用户误以为卡死。
  3. **取结果 + 生成报告 + 输出路径**：Monitor 收到 `[完成]` 后必须主动补齐后处理，三类任务各有对应步骤：
     - `interpret`：`result <job_id>`（提取 project_id）→ `report --job <job_id> --format html`（生成解读报告）→ 输出报告全路径
     - `generate`：`download-url <job_id>`（获取短时下载链接）→ 输出文件名、大小、有效期和下载链接；用户明确要本地文件时再 `result <job_id> -o <路径>.docx`
     - `compliance`：`result <job_id>`（打合规摘要）→ `report --job <job_id> --format html`（生成合规报告）→ 输出报告全路径
     - `duplicate`：`result <job_id>`（打查重 JSON 摘要）→ `report --job <job_id> --service bid_duplicate --format html`（生成查重报告）→ 输出报告全路径；如果用户明确不要报告，则只输出文件对风险率、证据片段与修改建议，不输出本地报告路径
     
     > `--no-wait` 跳过了同步模式的后处理，**AI 必须手动补**，否则报告文件不会生成，用户看不到路径。
  > 仅在用户不需要看进度或调试时才用单命令前台运行（无 `--no-wait`）。`packages` / `me` 等快速命令无需两阶段。
- **断点续查**：`job <job_id>` 查状态、`result <job_id> [-o file]` 取结果、`cancel <job_id>` 取消。
- **幂等**：网络重试给提交命令加 `--idempotency-key <UUID>`，避免重复建任务/重复扣费。
- **续接已有 project**：用户解读后直接说「帮我生成」，沿用 `project_id` 从第 3 步继续，不重传。
- **错误处理**：脚本已把 401/402/404/422/429 转中文。常见——402 可用字数不足让用户购买会员或字数包；整层 404 多为开放 API 总开关未开，让管理员开启；429 退避重试。完整对照见 [api.md](api.md)。
- **可用字数不足（402）**：先区分“提交前门槛”与“实际消耗”——开放 API / Skill 下，解读、生成、标书审查、标书查重提交前都要有可用字数；但真实消耗可用字数的是生成。脚本只打印**不含凭证参数的官网入口链接**，照原样转达即可；错误体里带 `bind_key` 的 `recharge_url`/`bind_url` 一律不转发（见第 1 步「凭证保护」）。
