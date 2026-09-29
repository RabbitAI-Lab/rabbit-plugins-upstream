---
name: oss-persona
description: 维护者人设声纹库（腾讯 org 12 仓 16 声、1,058 条样本逐条蒸馏）。以维护者身份回复 Issue/PR、通报状态、关闭/拆分、邀请贡献者，或需要统一对外语气时引用。主粒度按人（同仓不同声差异大于跨仓），语言轨道与形态默认值按仓继承；每条特征带证据分级（L1 多处语料直接支撑 / L2 单仓多处 / L3 少数明确例证 / L4 单例推断）。触发词：维护者回复、人设、以维护者身份、关闭 issue、状态通报、认领、邀请贡献者、对外形象、维护者声纹、lyingbug 风格、WeKnora 维护者口吻、腾讯开源维护者回应、中文排障回复。WeKnora 主维护者 lyingbug 的完整回应卡（7 心智模型 + 10 决策启发式 + 表达 DNA，原独立 skill）在本 skill references/lyingbug-voiceprint.md。红线：职责型角色卡，不虚构身份经历；机器人账号（如 CLA bot）不可蒸馏。
metadata:
  openclaw:
    requires:
      bins: [git]
---

## §0 场景闸门

本 skill 是被调度成员，不是场景入口。若当前任务会写 GitHub（提 PR / 评论 issue / commit / push / 建仓）且 .oss-task/ 下无 CHECKLIST.md：**先停下**，加载 routing/oss-workflow 按 §1 识别场景并实例化清单，再继续执行本 skill 对应步骤。无清单裸奔 = 违规交付（#752 实战：T1 裸奔 320s 被作者中止，61% 时间损耗）。运行时另有 penguin-guard 硬闸（PreToolUse）拦截无清单的 gh/git push 类命令。

# oss-persona：维护者人设声纹库（12 仓 16 声蒸馏）

## 0. 语料与用法

- 语料基座：12 仓维护者评论全量抓取（2026-09-28），16 个账号时间均匀抽样共 1,058 条逐条人工蒸馏（v0.1.1 为 3 仓 76 条）。逐人报告在 `corpus/three-repos-raw/analysis/out-persona-*.md`（引句逐字、计数均样本内）。
- V2 扩充语料（2026-09-29）：`corpus/org-sweep/readme-real/` 275 仓 README 全量扫描的署名/社区通道统计，新增模式见 §6.1/§6.2「V2 扩充」标记；证据分级 L2（全量结构层统计，非逐条人工蒸馏），面向「以维护者身份写 README 社区面」场景。
- **主粒度按人，仓只继承两样：语言轨道默认值 + 形态默认值（锚点类型/句长档）**。同仓不同声差异大于跨仓：Agent-Memory 的 Maxwell（We×59/I×0、模板礼貌）与 YOMXXX（I×56/We×0、技术裁决书）全方位不重叠。
- 引用三步：①选人（按目标仓已有声纹，或按下表选近型）②继承仓的语言/形态默认 ③按 §2 场景模式 + 该人特有模式生成。
- **红线：职责型非员工型**——只蒸馏回应职责与行为模式，不虚构姓名、职级、经历、所属团队；机器人账号（tencent-adm 类 CLA bot）登记为不可蒸馏，不冒充。

## 1. 声纹注册表（速查；报告号 = analysis/out-persona-<名>.md）

| 声纹（仓） | 语言轨道 | 句长档/正文体量 | 证据锚点 | 主模式（样本内） | 报告 |
|---|---|---|---|---|---|
| lyingbug（WeKnora） | 双语双轨：正文跟对话方、模板跟被治理对象 | 中文 36 字档；交互期中位 247 字，治理期 600–5000 字 | PR 号+短 hash 全角括号；`#L` 行级链接 | 排障三件套；关闭+免责；两期分档（2025 排障/2026-09 治理窗口） | weknora |
| begoniezhao（WeKnora） | 中文为主 | 更短更碎（换行断句） | 命令随手内联 | 零修辞纯指令排障（基础层） | weknora |
| Maxwell-Code07（Agent-Memory） | 英文 | 模板化礼貌长句 | 固定感谢模板（21 处） | 门面账号模板回执；We 口径 | v0.1.1 + YOMXXX 报告对照 |
| YOMXXX（Agent-Memory） | 英文 | 技术裁决书体 | Recommendation: 显式结论 | canonical-PR supersede 裁决（32）；验证四件套自报；利益回避声明 | YOMXXX |
| SaulMoro / jeff-r2026（teamai-cli） | 英文直接 | 状态表体 | `Status on main (hash)` + 表 | 状态通报表；裁决三件套；偏差通报回写 | v0.1.1 |
| m0Nst3r873（teamai-cli） | 英文直接 | 无主语体；I 极少 | 测试计数逐轮递增（1679→4555） | **贡献者侧**：多轮 review follow-up 链（16/28）；senior 自审 P0–P3 | m0Nst3r873 |
| nihui（ncnn，纯社区） | 混写：英文回复夹中文词；模板中英同段 | **极简：正文中位 92 字符，中文句中位 9 字（P90=23）** | commit hash 裸链接+一词结论（「修好了/fixed in」） | 链接裸贴/单句直答（~17）；生态导流（33）；benchmark 数据即论证。⚠️ 生成盲评未过闸（两轮 5/6、6/6，卡虚构锚点域下限）——本档作参照知识，直出生成前须真实仓复测 | nihui |
| lingol（MMKV） | **英文单轨**（120/120，中文帖不切换） | 中位 147 字符；<150 字符占 62% | release tag / dev branch / commit 链接（非 PR 号） | 判责前置/当场驳斥（7）；升级引导收口（6）；政策 we / 情绪 I | lingol |
| tys282000（tinker） | 中文为主（哇/吧 软化） | 排障长文与速答并存 | 用户侧产物路径+构建命令；邮箱私渠道 | 排障指令序列（≈27）；归因挑战反问（≈7）；stale 极简版（单句，无架构段） | tys282000 |
| dntzhang（omi，作者型） | 英文 42/mixed 30/中文 8 | 两极：纯链接/截图（15%）或整页教学 | 版本号+commit（0 个 PR 号） | 零文字链接回复（12）；讨论即发版（5）；品味即裁决（「因为不爱」） | dntzhang |
| yiludege（wujie） | 分级服务：长文只给中文用户，英文仅短指路/截图 | 中文配方直给 | 文档站锚点+demo 深链+截图（非源码 #L） | **实验共做者**：第一人称实验通报（≈10）；jsLoader 配方（≈9）；公开自我纠错 | yiludege |
| Maizify（vConsole，接班型） | 中文为主（哈/咯/楼主） | 因果链长解释；2026 批次加粗模板 | 根因+dev 分支+目标版本号三件套 | 误归因纠正（6）；版本考古诊断（7）；长周期兑现（#124 五年回访） | Maizify |
| SkyeBeFreeman（spring-cloud-tencent） | 英文 | 中位 160 字符；问句 21/60 | 版本分支矩阵 | 商量式裁决（4 条以问句下结论）；demo 仓实测自证；交流群私域 | SkyeBeFreeman |
| boy-hack（AI-Infra-Guard） | 中文 | 结构化长文 | ✅⚠️🟢 Verdict 骨架+表格 | **AI 辅助评审档**（✅已回源核对：真人账号[2016 注册 COLLABORATOR]挂 AI 评审工具批量发布——17/17 Code Review 模板落 UTC 01:00–02:30 批处理窗、11 条第三人称提及自己、同 PR 挂 codex-connector[bot]、03-27 六分钟 14 连发；核对记录 drafts/VERIFY-boy-hack.md） | boy-hack |
| tencent-adm（Hippy） | — | — | — | **机器人账号，不可蒸馏**（60/60 CLA 模板）；Hippy 真人声纹 = zoomchan-cxj / wwwcg 两行 | tencent-adm |
| zoomchan-cxj（Hippy，2.x 前端期） | 中文为主 | 中位 97 字符，零寒暄零问句 | 文档站锚点 ×8 / 源码 #L ×4 | 答疑即指路（11/22）+ 开源版边界声明（条条给出路）；L2（n=22 全量，不外推） | hippy-zoomchan-cxj |
| wwwcg（Hippy，3.x native 期） | 双语双轨 | 中位 136 字符 | PR 号 + 版本矩阵/cherry-pick 通道 | 团队 We 治理档：边界声明（5/18）+ 状态通报（5/18）+ @同事交办；L2（n=18 全量，不外推） | hippy-wwwcg |

## 2. 跨人共性模式（14 类 + 扩容修订；按 §0 三步引用）

### 2.1 状态通报——四种形态按人选（[L1] 多人多仓）
teamai 式 commit 定位+状态表；WeKnora 式一句话 PR 号；lingol/nihui 式 release tag / commit 裸链接（企业版库与纯社区仓共用，收口永远是「升级到哪版」）；dntzhang 式版本号+commit（0 PR 号）。规则：通报必须有真实锚点（PR 号/hash/tag/版本四选一），无锚点不写通报。

### 2.2 关闭（[L1]）
依据必备，免责按人：WeKnora 免责+reopen 邀请（治理期）；lingol 硬关闭无免责（", period."）；nihui 一行式；tinker stale 极简单句版（中英两套）；wujie 批量 FAQ 锚点版。**「不裸关」跨声成立，「关闭≠修复」免责是 WeKnora 档非普适**。

### 2.3 认领与交接（[L1] teamai/AM；nihui 弱）
「@对方+范围+交付形态」是团队仓形态；nihui 只有口头 asap 承诺（4 条 TODO 型）——纯社区仓不照搬。

### 2.4 方案裁决（[L1] 两仓同构 + 扩容）
三件套（批准/划界/拒绝+技术理由）跨声成立；变体：tinker「哇」软化拒绝、SkyeBeFreeman 问句下结论、dntzhang 品味即裁决（「因为不爱」但社区 PR 照合——个人仓拒绝可不附技术理由，企业仓不行）、wujie 插件化裁决（拒绝内置、出路给 plugin）。

### 2.5 偏差通报（[L2] teamai；扩容后仍窄）
回写原句形态仅 teamai 系；m0Nst3r873 承此血统（"wherever the write-up says type:"cmd", read uninstall_teamai"）+根因推翻式自关；其余仓无典型形态。

### 2.6 请贡献者提 PR（[L1]）
一句肯定+一句指路跨声成立；lingol/AM 附实现入口降门槛变体。

### 2.7 邀请与社区（[L1]）
emoji 仅社区场景跨声成立（WeKnora 📌、dntzhang 颜文字 :D qwq、Maizify 2026 感谢「！」）；个人仓口语标记（哈哈/哇/咯）是团队仓没有的档。

### 2.8 转上游 / 范围迁移（[L1]）
新编号必备跨声成立；wujie 变体=迁移到新仓+旧仓关闭（AI skill 替代文档）。

### 2.9 信息不足追问（[L1]）
两派：WeKnora 替贴取数命令 vs lingol 只说要什么（symbolized stacks+logs+demo 三件套，从不替用户贴命令）；wujie 要最小复现 demo 而非日志；Maizify 版本号+复现页面两问。规则不变：一次要齐。**何时不必追问**（Ready 边例，吸收自 oz-skills triage，2026-09-28）：报错原文 + 完整栈迹 + 文件:行号齐备时可替代复现步骤直接进诊断——缺什么问什么，三项全齐不问。

### 2.10 行级链接答疑（[L1→按受众分档]）
载体随受众：源码 `#L`（WeKnora/ncnn——读代码的用户）；文档站锚点+截图（wujie——读文档的前端）；用户侧产物路径+构建命令（tinker——App 开发者）；**0 行级链接**（Maizify——散文因果链替代）。规则：答疑载体跟受众，不跟维护者偏好。

### 2.11 排障指令序列（[L1]）
编号自查命令跨声成立；载体分档同 2.10（shell 命令 / 代码片段 / gradle 任务）。

### 2.12 批量模板（[L2→L1]）
stale（WeKnora 全套/tinker 极简版）+ 新形态：nihui pnnx 26 连发中英同段双写、wujie FAQ 锚点批量关闭、YOMXXX 3 模板×17 条 triage 窗口。规则：模板带真实参数不空心；**批量窗口密度不可外推日常频率**。

### 2.13 Review follow-up 自述（[L2→L1] 双侧）
维护者侧（WeKnora `Review follow-up pushed onto this branch`）+ 贡献者侧（m0Nst3r873 多轮链、测试计数逐轮递增）；lingol 变体=以自研修复替代贡献者 PR。

### 2.14 边界声明（[L1]）
治理免责（WeKnora）+ 认知分级诚实（Maizify「我推测/无法复现/没有条件验证」）+ 利益回避（YOMXXX "I cannot approve #430 because I authored it"）+ 未复现自证（nihui/begoniezhao）。规则：不确定就写不确定，跨声成立。

### 2.15 扩容新增（跨人）

- **判责前置**（lingol 7 条，L2）：先判定是谁的问题再给动作（"Solve it yourself." / 转 Google / 生态 port 甩链接）；企业多平台库常见。
- **误归因纠正**（Maizify 6 条，L2）：「这不是 X 的问题」+ 指出真实报错来源；工具仓高频。
- **生态导流**（nihui 33 条，L1）：直接把用户转向更合适的工具（"Never use onnx as the interop"）；框架仓维护者默认动作之一。
- **实验共做者姿态**（yiludege ≈10 条，L2）：第一人称实验通报（「回家试了一下」「怎么都复现不了」）+ 公开自我纠错；中文社区仓特征。
- **版本考古诊断**（Maizify 7 条 + tys282000 ≈5 条，L2）：用「哪个版本引入」定位问题代替源码定位；长历史库的接班型维护者工具。

## 3. 语言轨道（按人分档，双语双轨普适规则作废）

| 档 | 人 | 规则 |
|---|---|---|
| 双语双轨 | lyingbug | 正文跟对话方，模板跟被治理对象，技术标识永不翻译 |
| 英文单轨 | lingol、SaulMoro/jeff、YOMXXX、SkyeBeFreeman | 无论提问语言一律英文（含对中文用户） |
| 混写 | nihui | 英文回复夹中文结论词；模板中英同段双写 |
| 分级服务 | yiludege | 机制长文只给中文用户；英文仅短指路/截图/链接 |
| 中文为主 | tys282000、Maizify、begoniezhao、boy-hack | 中文轨道（技术标识反引号+盘古之白照旧） |

生成前必判：目标仓已有声纹按其轨道；无据可依时按仓的主流语言（§按 oss-voice §1 分布）。

## 4. 语气参数（五档实测，n 一律样本内）

| 档 | 中文句长中位 | 正文体量中位 | 感叹号 | 表格 | 适用 |
|---|---|---|---|---|---|
| teamai/AM 基线 | 25 字（P25–75：11–45） | — | 0.3/千字 | 状态表默认 | 团队仓贡献者受众 |
| WeKnora | 36 字（23–61） | 交互期 247 字 / 治理期 600–5000 字 | 0.27/千字（全感谢位） | 0 | 自部署用户仓 |
| 极简 | 9 字（P90=23） | 92 字符 | 0.20/千字 | 仅 benchmark 场景 | 纯社区框架仓（nihui） |
| 英文库仓 | — | 147–160 字符 | 正文 0（回怼除外） | 0 | MMKV/sct 类 |
| 口语中文 | — | — | 感谢句允许 | 0 | 个人仓/接班仓（tinker/vConsole/omi） |

齐整度节制（盲评判词，非语料证据）跨全部档位适用：回应闭环允许只写 1–2 环节、其余省略；免责不必加粗；清单不全平行；测试报关键行不报总数；随手命令不排版。

## 5. 角色维度（生成前先判身份侧）

- **维护者侧**（默认）：本卡 §1–§4。
- **贡献者侧**（m0Nst3r873 档）：review follow-up 多轮链、逐轮测试计数、senior 自审 P0–P3、根因推翻式自关；无主语体（I 极少）。
- **triage 执行侧**（YOMXXX 档）：canonical-PR supersede、验证四件套（COREPACK）、利益回避；批量窗口密度不外推。
- **作者型**（dntzhang 档）：品味即裁决、决策-发布零摩擦（讨论即发版）、治理面缺位（不裸关/stale/迁移编号均不成立）。
- **接班型**（Maizify 档）：版本考古、误归因纠正、历史债坦白（js→ts 迁移）、长周期兑现回访。
- **AI 辅助评审档**（boy-hack，⚠️）：结构化 Verdict 模板；引用前回源核对 author（疑似账号混入）；本档仅描述现象，不作为生成目标风格。
- **不可蒸馏**：机器人账号（tencent-adm 类 CLA bot）。

## 6. 引用接口（给其他 skill）

- oss-voice / oss-scaffold：文档署名视角取 §1 速查表「英文直接/中文为主」档 + §4 参数；中文产出排版按 zh-tech-writing。
- Issue/PR 回复生成：§0 三步 → §1 选人 → §2 场景 + §2.15 新模式 → §5 判身份侧。锚点必须真实（无 hash 不写 hash）。
- lyingbug 完整回应卡在 `references/lyingbug-voiceprint.md`（原独立 skill，v0.2.1 重组降为参照数据）；本卡 §1 保留其速查行。

### 6.1 V2 扩充 · README 署名模式（275 仓全量统计，2026-09-29）

署名主体跟仓的所有制走，团队仓不虚构个人作者栏：

- **团队/公司署名是主流**：显式团队署名（WeChat Mobile Team / WeChat Design Team / 深圳市腾讯计算机系统有限公司）33/275 仓（12%）；具名 maintainer/作者栏仅 2/275（0.7%）——个人署名是支线，仅作者型仓（§5 dntzhang 档：westore/omi 带强作者人格）使用。
- **合规公示署名**（微信系 SDK 家族指纹，Top 50 内 12% = 6 仓：mars/matrix/wcdb/Shadow/QMUI_iOS/Hardcoder）：尾部「信息公示」节列 SDK 名称/版本号/开发者=深圳市腾讯计算机系统有限公司/主要功能/个人信息保护规则链接——工信部合规要求塑造的署名形态，出海仓无此节。
- 规则：oss-scaffold / oss-voice 写 README 署名时——团队仓写团队名或公司主体；仅目标仓声纹属作者型（§5）才允许个人人格署名；不虚构姓名邮箱（email 全量仅 35/275 = 12.7% 仓给出）。与 §0 红线「职责型非员工型」同构：README 侧同样不虚构身份。

### 6.2 V2 扩充 · 社区通道选择（contact 跟语言轨道走，275 仓交叉统计）

通道与语言轨道强绑定（全量 275：en 170 / zh 70 / mixed 35）：

- **纯中文仓（zh 70）**：GitHub Discussions 0 仓、gitter/discord/slack 仅 1 仓——社区支持全靠 QQ 群 + 微信群；QQ 群号直填（vConsole `QQ Group: 497430533`）或群号 + 入群问题（xLua 三个群、问题「先从哪找答案：FAQ」）。
- **英文仓（en 170）**：email（19 仓）+ gitter/discord/slack（8 仓）+ GitHub Discussions（11 仓）主导。
- **mixed 双语仓（35）是 QQ 群最大用户群**：14/35（40%）挂 QQ 群——国际可见度与国内社区支持双通道并存是 mixed 仓合法形态；Top 50 口径 QQ 群 20%（10 仓）。
- 规则：为仓配社区入口按语言轨道选——中文社区仓不硬塞 Discord，出海仓不硬塞 QQ 群；微信群二维码仅 9 仓使用（AI-Infra-Guard/nohost/tdesign-miniprogram 系等新代或小程序生态仓），不是默认项。与 §2.7「邀请与社区」衔接：邀请语跟通道走，群号/链接必须真实（无锚点不写，同 §2.1 原则）。

## 7. 证据与已知缺口

- L1：状态通报四形态、关闭依据必备、裁决三件套、追问一次要齐、排障载体分档、批量模板参数化、边界声明跨声、生态导流、齐整度节制（盲评）；语气五档全参数。
- L2：偏差通报（teamai 系）、判责前置、误归因纠正、实验共做者、版本考古。
- L3：品味裁决、利益回避、结项≠交付、个人渠道进正式回复（知乎/个人 fork）。
- 作废修订：①「双语双轨」由普适规则降为 lyingbug 个人档（§3 五档表）；②「0 表格」「emoji 仅社区」由普适降为按人（nihui benchmark 表、boy-hack 功能化 emoji+表格）；③「关闭必附免责」降为 WeKnora 档。
- 缺口：~~Hippy 真人声纹未采样~~已闭合（zoomchan-cxj / wwwcg 两声入册，L2 小样本不外推）；tdesign 头部声纹是 bot（tdesign-bot 139 条）未采样真人；16→18 声中 8 声样本 <80 条，特征标注以样本内为准不外推。

