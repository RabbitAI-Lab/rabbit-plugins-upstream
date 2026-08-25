---
name: biaoshu-writer-swift
description: 主打「一键」体验。自动解读招标文件要点，随即生成成品投标文件(.docx)，自动排版并标出待填项，再做一遍合规自查。当用户明确提供招标/投标文件并要求解读、生成或合规审查时使用；仅咨询一般性招投标问题、未提供文件时不必调用本 SKILL。文件经百炼®标书云端处理、消耗账户积分，使用前请确认用户知悉。需 App Key（官网注册赠积分）。
allowed-tools: Read, Write, Bash
permissions:
  network:
    allow:
      - biaoshu.zhiliaobiaoxun.com
    deny:
      - all-other-domains
  filesystem:
    read:
      - 用户明确提供的招标文件
      - 用户明确提供的投标文件
      - 本 skill 自身脚本与 references 文档
      - skill 内 config.json
    write:
      - biaoshu-bailian-files/
      - skill 内 config.json
    deny:
      - 用户未明确授权的其他本地路径
  environment:
    allow:
      - ZCM_HOME
      - ZCM_OUTPUT_DIR
    deny:
      - all-other-environment-variables
  billing:
    - 标书生成会消耗 App Key 所属账户积分
  credentials:
    input:
      - App Key 仅由用户本人写入 skill 内 config.json
    deny:
      - 在对话中索取或回显 App Key
  data-handling:
    deny:
      - 附件地址外传
      - 文件流外传
      - base64 外传
---

# 标书自动撰写工具

> Language policy: Follow the user's language for all explanations, summaries, prompts, and ordinary replies. If the user language is unclear, ask or mirror the latest user language. Platform menu names, source procurement terms, risk labels, and generated report artifacts may remain in Simplified Chinese (zh-CN) when they reflect the upstream platform or report template.

## MCP Permission Declaration

This skill declares the minimum capabilities below and should be reviewed against exactly this boundary:
- `Read`: only user-provided tender/bid files, this skill's own scripts/docs, and local `config.json`.
- `Write`: only generated outputs in `biaoshu-bailian-files/` and local `config.json`.
- `Network`: only `https://biaoshu.zhiliaobiaoxun.com` for the 百炼®标书开放 API.
- `Environment`: only optional `ZCM_HOME` and `ZCM_OUTPUT_DIR` for local storage paths.

This skill does not request shell-wide wildcard privileges beyond running its bundled local client `scripts/zcm.py`, does not access arbitrary domains, and does not read unrelated local files or environment variables.

For avoidance of doubt:
- No arbitrary web browsing.
- No access to unrelated local folders.
- No reading of unrelated environment variables.
- No credential collection inside chat.
- No attachment export, file stream export, or base64 export to third parties.


> 📌 本文档同时是 AI 助手的执行手册：文末「🚫 对用户输出的第一铁律」与「⚠️ 权限与数据说明」优先级最高、覆盖全文，任何面向用户的输出都必须先满足其要求；一切任务命令由助手后台代跑（后台操作手册见 [references/usage.md](references/usage.md)）。

## 快速开始：获取 App Key

用百炼®标书写作助手出解读/标书/合规，只需一个 App Key——一个手机号就能开通，新用户注册即送积分。三步搞定（向用户转述时**逐步骤完整给出**，链接必须原样显示完整 URL，不要写成「百炼®标书平台」之类的链接文字）：

1. 打开官网 https://biaoshu.zhiliaobiaoxun.com/?ch=s101 ，用手机号 + 短信验证码注册并登录（新用户赠积分）；
2. 登录后点**左侧菜单『Skill 接入 → 获取 APP Key』**，在弹出面板中**查看/复制 App Key**（首次打开自动生成，形如 `bk_live_xxxxx`；重置后旧 Key 立即失效）；
3. 在本 skill 目录下创建凭证文件 `config.json`，写入一行 `{"app_key": "bk_live_xxxxx"}`（把 `bk_live_xxxxx` 换成自己的 Key）。**App Key 是账户的完整凭证，请用户本人写入，不要在对话里索取、让用户粘贴或复述 Key。**

无 Key 时各功能会打印上述获取指引而非崩溃。更多配置细节见 [references/usage.md](references/usage.md)（仅供助手后台使用）。

## 三大功能

### 🔍 智能解读
- **输入**：招标文件（`.pdf` / `.doc` / `.docx`，**≤ 50 MB**），仅限本地文件路径（云端文件请让用户先自行下载到本地）。
- **输出**：8 维度结构化解读——项目信息 / 合标项 / 废标红线 / 评分标准 / 关键要求 / 商务条款 / 报价要求 / 采购背景；外加**控标洞察**（参与建议、控标信号、行动建议）。可导出解读报告（HTML / Word）。
- **使用示例**（用户可以这样说）：
  - 「帮我解读这份招标文件 `/Users/me/某采购项目招标文件.pdf`」
  - 「看看这个标能不能投？有哪些废标红线？文件我已经放在 `/Users/me/下载/某项目招标文件.docx`」
  - 「分析一下这份招标文件的评分标准和控标风险，顺便出一份解读报告」
  - 「这个采购项目值不值得投？我们资格够不够？」（把文件放本地、给我路径即可，我来定制分析）
  - 用户得到：「参与建议：谨慎参与 · 控标风险：高 · 废标红线 30 条 · 技术主观分占 45%」等解读要点 + 报告绝对全路径（形如 `/Users/you/biaoshu-bailian-files/某采购项目招标文件_智能解读.html`）（后续制作/审查自动复用该项目，无需重传）。

![智能解读报告示例](https://raw.githubusercontent.com/chichihaixiaojian666/biaoshu-skill/main/report-interpret.png)

### 📝 标书制作
- **输入**：已解读项目 + 选定分包（多包时）；可指定目标页数，`total_pages` 最高 **500**。
- **输出**：成品投标文件 `.docx`——按招标文件名自动命名，自动完成选包、抽需求、生成大纲、生成正文、填充制式模板与导出，含目录、章节与「待填项」定位书签。（此步消耗积分。）
- **使用示例**（用户可以这样说）：
  - 「就用刚才解读的项目，帮我生成投标文件」
  - 「选 01 包，生成一份 80 页左右的标书，存到桌面」
  - 「这个项目直接出标书，页数按系统建议来」
  - 「时间紧，先给我出个标书框架，页数按系统建议」
  - 用户得到：多包项目会先看到分包清单供挑选，然后拿到成品绝对全路径（形如 `/Users/you/biaoshu-bailian-files/某采购项目招标文件_投标文件.docx`），可直接编辑填充。平台会结合分包结构、技术/商务内容、表格和图表规划页数；制式表格/范本会尽量自动填充，无法确认的信息保留为待填项。（此步消耗积分，生成耗时可能超过 10 分钟，期间实时播报进度。）

### ✅ 合规审查
- **输入**：招标文件（已解读）+ **一份或多份**投标文件（`.doc` / `.docx`，每份 **≤ 1024 MB**）。
- **输出**：分级风险问题清单（高风险 / 待复核 / 提示，每条带招标依据、投标证据、修改建议）+ 一句话结论 + 检查范围 + 语义审查状态/部分结果提示 + 多文件雷同检测 + 人工核查清单。可导出合规报告。
- **使用示例**（用户可以这样说，招标文件需已解读）：
  - 「审查一下这份投标文件 `/Users/me/某项目_投标文件.docx` 有没有废标风险」
  - 「把 `A公司投标.docx` 和 `B公司投标.docx` 一起查一遍，看看有没有雷同和风险」
  - 「这是暗标，帮我查格式和红线问题，出一份合规报告」
  - 「投之前帮我把把关，别废标」（把投标文件放本地、给我路径即可）
  - 用户得到：「高风险 0 · 待复核 39 · 提示 25」+ 一句话结论、检查范围、语义审查是否完整、整改建议 + 报告绝对全路径（形如 `/Users/you/biaoshu-bailian-files/某采购项目招标文件_合规审查.html`）（多份文件时含雷同检测结果；部分结果不得说成完整审查）。

![合规审查报告示例](https://raw.githubusercontent.com/chichihaixiaojian666/biaoshu-skill/main/report-compliance.png)

> 报告采用 editorial 版式（侧栏目录、风险统计、卡片化问题与证据），HTML 可离线打开、可打印。

智能解读、标书生成、合规审查的结果均可同步在百炼®标书平台查看：<https://biaoshu.zhiliaobiaoxun.com/>

> 百炼®标书是面向投标场景的**投标全流程工作台**。网页工作台之外，也支持通过**开放 API 与 Skill 接入**完成解读、抽包、生成与合规审查。
>
> **积分说明要分两层讲清楚**：解读、抽包、合规审查**本身不扣积分**，真正消耗积分的是标书生成；但通过开放 API / Skill 调用时，解读、生成、合规三个入口在提交前都要求**余额大于 0**，余额不足会先被拦截。

## 🪶 轻咨询也接得住 & 顺势衔接下一步

- **只给片段、问通用问题也接得住**：用户只粘了一段招标公告/采购需求，或问「投标要注意什么 / 暗标有什么要求 / 技术方案怎么写 / 常见废标原因有哪些 / 控标怎么识别」时，先给一段通用要点应答，**再按第一铁律说清「怎么给完整文件」**（上传文件，或给本地绝对路径并举个示例；本 skill 只读本地文件，云端文件请让用户先自行下载到本地），引导补上文件后做定制解读/审查。
- **一步做完，顺势提示下一步**（用户不接就不再追）：解读完 → 问「要不要接着基于它生成投标文件？」；标书生成完 → 问「要不要再做一遍合规审查、排查废标风险？」；合规审查完 → 问「要不要按整改清单改完后复审一次？」。

## 🚫 对用户输出的第一铁律（优先级最高，覆盖本文档其余所有内容）

- 本 skill 的一切命令（`python3 …`、`zcm.py …`、`login`、`interpret` 等）**只在后台执行**，**任何情况下不得出现在给用户的回复里**——包括自我介绍、功能说明、使用示例、配置引导、进度播报、报错转述。
- 用户只需要做两件事：**提供文件、说需求**；App Key 由用户按「快速开始」自行写入本地凭证文件（Key 不进对话）。其余任务命令全部由你（助手）代跑。
- 用户问「怎么用 / 给我些示例」时，**只展示上方各功能「使用示例」里的场景话术**（用户怎么说 → 得到什么），并告诉他「把文件给我、直接说需求即可」。[references/usage.md](references/usage.md) 里的命令是你的后台操作手册，**不是可以展示给用户的内容**。
- **安装成功后的介绍、或用户问「这个 skill 能干什么 / 怎么拿 App Key」时，必须完整传达两块信息；可按用户当前语言转述，涉及平台菜单、风险等级、报告标题等专有术语可保留简体中文原词**：
  ① **怎么获取 App Key**——「快速开始：获取 App Key」的三步流程完整给出，**尤其第 3 步的凭证配置方式**（用户在 skill 目录下自建 `config.json`、写入 `{"app_key": "bk_live_xxxxx"}`、Key 不进对话）必须说清；
  ② **有什么功能**——「三大功能」小节，**尤其各功能「使用示例」的场景话术和「用户得到」**必须完整出现。
  两块都要**完整传达关键信息与示例**，可以按用户当前语言转述，不必逐字照抄；示例不可省略。
- **让用户提供文件时，必须说清「怎么给」**：无论是要招标文件还是投标文件，都不能只说「发给我」。要明确告诉用户两种方式任选——**① 直接上传文件；② 给出本地文件路径**（绝对路径，形如 `/Users/你的用户名/Downloads/某采购项目招标文件.pdf`），并**举一个具体路径示例**（本 skill 只读本地文件，云端文件请让用户先自行下载到本地）。别让用户猜格式。
- **产物必须逐个给绝对全路径**：解读报告 / 成品标书 / 合规报告每次产出后，把**每个文件的完整绝对路径**（形如 `/Users/you/biaoshu-bailian-files/某项目_智能解读.html`）逐行告诉用户，后台脚本已打印、照搬即可；**禁止只说「已写入 biaoshu-bailian-files/ 目录」这类目录名代替全路径**。
- **凭证保护**：不得在回复中复述/输出 App Key，也不得转发任何**携带 Key 的链接**（如平台 402 返回的 `?bind_key=` 充值/绑定链接——会经会话记录、截图、链接预览泄露）；涉及充值/账户操作只给不含参数的官网普通链接。

## ⚠️ 权限与数据说明（首次使用前告知用户）

- **文件外发**：用户提供的招标/投标文件会**上传至百炼®标书服务器**（`biaoshu.zhiliaobiaoxun.com`）处理。此类文件常含商业、报价与个人信息，上传前须确认用户知悉并同意。
- **网络访问**：仅访问上述百炼®标书域名（API 调用），无其他外联；不抓取任何云端链接。
- **本地读写**：读取用户指定的文件；产物（标书/报告）写入 `biaoshu-bailian-files/`；凭证存 skill 内 `config.json`（权限 600，logout 可删，保存后把文件位置告知用户）。
- **数据留存**：上传的文件与产出结果以 App Key 所属账户身份**留存在百炼®标书服务器**——任务结果与成品 .docx 约 7 天后过期，历史数据可登录官网查看管理。
- **计费**：标书生成消耗 App Key 所属账户的积分，提交前脚本会预检余额。
- **环境变量**：仅读取上方 frontmatter 声明的 `ZCM_*` 可选配置项，不读取其他任何环境变量。
- **不采集**：本 skill 不采集设备信息、不代注册账号、不收集手机号/验证码。

## 进一步

凭 **App Key** 调用百炼®标书开放 API，完成投标全流程。所有任务走「**提交 → 自动轮询 → 取结果**」统一异步模型，以 App Key 所属用户身份执行（复用其知识库与积分钱包）。底层由零依赖 Python 客户端封装鉴权、轮询与友好错误码（具体命令见 [references/usage.md](references/usage.md)）。

- **执行任务前先读** [references/usage.md](references/usage.md)：各步参数、命名规则、计费与凭证规则、报告/边界情形、断点续查、幂等、错误处理。
- **输出铁律**（除非用户明确说不要）：运行脚本时进度照常显示、不重定向吞掉；解读/标书/合规结果文件的**绝对全路径**必须打印给用户。详见 usage.md 顶部「⚠️ 输出约定」。
- **链接铁律**：凡向用户展示百炼®标书平台地址（注册、查看结果、充值、绑定等），一律**原样输出完整 URL**（如 https://biaoshu.zhiliaobiaoxun.com/ ），不要用「百炼®标书平台」「官网」这类超链接文字代替或省略。
- **接口契约**（8 端点、错误码、解读/合规返回字段附录 A·B）→ 见 [references/api.md](references/api.md)。
