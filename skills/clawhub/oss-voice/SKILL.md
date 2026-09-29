---
name: oss-voice
description: 仓库文档与脚手架场景的写作风格（腾讯三标杆仓蒸馏）。被 oss-workflow S3 调度时，写/改仓库文档（README/CHANGELOG 等）——不持有场景触发词，由路由层统一接管。给 oss-scaffold 脚手架场景提供文档风格时也走本 skill。风格规则蒸馏自 WeKnora / TencentDB-Agent-Memory / teamai-cli 三仓真实 PR 与 README 语料（2026-09-28 全量重抓：4243 篇 PR + 1894 issue + 3386 条维护者评论）。PR/Issue 文案不走本 skill（归 oss-contribution 的 references）。多语言文档管理（多语同步 glob 规则 / BCP-47 命名 / 结构对齐验收 / docs 双轨制——原 oss-i18n skill，v0.2.1 并入）见 §7；不用于 UI 组件库的 i18n 实现（vue-i18n/react-intl 代码级）。产出后必须配合 humanizer 去 AI 腔、zh-tech-writing 定中文句式排版。触发词（能力词，场景词让渡给 oss-workflow）：仓库文档写作、文档风格、多语言文档管理、贡献指南写作、CHANGELOG 维护、oss voice、文档整理、国际化、i18n、多语同步、翻译管理locale。
metadata:
  openclaw:
    requires:
      bins: [git, npx]
---

## §0 场景闸门

本 skill 是被调度成员，不是场景入口。若当前任务会写 GitHub（提 PR / 评论 issue / commit / push / 建仓）且 .oss-task/ 下无 CHECKLIST.md：**先停下**，加载 routing/oss-workflow 按 §1 识别场景并实例化清单，再继续执行本 skill 对应步骤。无清单裸奔 = 违规交付（#752 实战：T1 裸奔 320s 被作者中止，61% 时间损耗）。运行时另有 penguin-guard 硬闸（PreToolUse）拦截无清单的 gh/git push 类命令。

# oss-voice：仓库文档与脚手架风格（三标杆仓蒸馏）

## 0. 边界与流水线

- 只管**仓库文档与脚手架场景**：README / CHANGELOG / CONTRIBUTING / docs / INSTALL 的内容与结构。PR 文案、Issue 回复模板在 `oss-contribution` 的 references。
- 多语言文档管理（原 oss-i18n skill，v0.2.1 并入）在本 skill §7——文档层 i18n；UI 组件库的 i18n 实现（vue-i18n / react-intl 代码级）不在本 skill。
- 定稿顺序：本 skill 出初稿 → `humanizer` 去 AI 腔 → `zh-tech-writing` 定中文句式。两 skill 属路由层 oss-workflow §3「文档推荐」档：缺失时警告并在产出标注「未润色」后继续，不硬停；oss-contribution 侧 R13/R16 门禁仍按其管线裁决。
- 语料边界（2026-09-28 全量重抓，`corpus/three-repos-raw/`）：4243 篇 PR（WeKnora 2517 + Agent-Memory 1096 + teamai-cli 630）+ 1894 issue + 3386 条维护者评论。v0.1.1 的「WeKnora 无 PR 语料」「WeKnora 维护者评论为 0」两处结论均为当时抓取遗漏，已被全量数据推翻；原「调研拆解来源」规则已升级为 PR 号实证。v0.2.0 扩至 org 级 12 头部仓（+ncnn/MMKV/tinker/omi/wujie/vConsole/tdesign/Hippy/spring-cloud-tencent/AI-Infra-Guard）与 298 仓结构层扫描（`corpus/org-sweep/`）；[DNA] 增补条目见 §9。
- V2 扩充语料（2026-09-29）：`corpus/org-sweep/readme-real/` 275 仓 README 全量脚本统计 + Round 1 Top 50 六维度蒸馏（`corpus/org-sweep/drafts/dna-round1-top50.md`，15 篇精读）。新增规则见 §1.1/§1.2/§2.1/§3 的「V2 扩充」标记，均带双层证据（Round 1 Top 50 精读 + 全量 275 复核，明细 `corpus/org-sweep/dna/readme-scan-v2-full275.json`），只加不改既有规则。

## 1. 语言跟随仓库受众（先判语言再动笔）

实测分布（PR 正文，2026-09-28 全量）：teamai-cli 英 582 / 中 8 / 混 40；Agent-Memory 英 715 / 中 41 / 混 340；WeKnora 英 1659 / 中 166 / 混 617。**teamai-cli 与 Agent-Memory 英文主导（≥90%）；WeKnora 是中文社区型仓（含中文 PR 占 31%，维护者评论中文主导 67%）**。语言档位按仓分：国际化仓英文主文件 + 中文对照；中文社区型仓（微信群 / 国内活动入口）中英双语并重。中文出现在三类场景：

1. 面向中文读者的专属文档（`INSTALL_CN.md`、微信群二维码、SkillHub 镜像提示）——如 `docs(install-cn)` PR 全文中文（Agent-Memory#1259）；中文正文 PR 另有 WeKnora#3793、#3617（fix(wiki) 类），Agent-Memory#1449
2. 讨论串已用中文提问——维护者跟中文（teamai-cli#341「这个目前优先级比较低，预计要年底」）
3. 双语模板的中文半边（`Description | 描述` 式模板，Agent-Memory 仓 PR 模板即此）

规则：**目标文件现有语言 = 写作语言**；双语仓库（README.md + README.zh-CN.md）两边都要改，内容对齐而非机器互译；只放中文内容的入口（如 SkillHub 提示词）**不扩散到其他语种**（teamai-cli#745 明确只改 `README.zh-CN.md`，理由是「避免在其他语种文档里引入语言不匹配的内容」）。

### 1.1 V2 扩充 · 新仓语言按生态位分层（既有仓仍守「现有语言 = 写作语言」）

新仓/建仓场景的语言决策三路分派，不一刀切选英文：**出海型库/框架** → 英文主文件 + 中文对照（命名按 §7.2 规则 I2）；**国内客户端/游戏生态工具** → 纯中文 README（不建英文空文件，QQ 群支持体系）；**微信核心链路基础设施** → 双语并置（锚点同文件或双文件）。证据：Top 50（星数降序）en 23 / zh 16 / mixed 11 三分天下，en 仓均星 9,246 > mixed 8,540 > zh 7,046（相关非因果——星数由生态位决定，README 是放大器）；34% 仓提供独立中文 README 文件；全量 275 复核 en 170 / zh 70 / mixed 35，中文原生仓集中在腰部（xLua / QMUI_Android / secguide / westore 均纯中文，面向国内开发者）。双语并置与微信链路强相关：Top 50 内 mixed 仓 55% 带生产背书——越是微信核心链路仓越倾向双语输出。（Round 1 `corpus/org-sweep/drafts/dna-round1-top50.md` §1.4/§3.2/§3.3 + 全量 275 复核 2026-09-29；注意：父任务描述的「Top 50 = 92% 中文」与 Round 1 实测 zh 16/50 = 32% 不符，本条采用实测口径）

### 1.2 V2 扩充 · 生产背书句式：有真实背书才写，没有不装

定位句（首段/一句话定位）有真实生产落地时用具名背书替代自证形容：MMKV「mobile key-value storage framework **used in the WeChat application**」、mars「cross-platform infrastructure component **developed by WeChat Mobile Team**. It has been **proved to be effective by billions of WeChat users**」、matrix「APM **used in Wechat** to monitor, locate and analyse performance problems」。反模式：无真实背书时写 high-performance / reliable / battle-tested / 亿级验证——无证据的自证形容即破绽（生产检验替代自证，Round 1 §5.1）。频率证据：Top 50 内 30%（15 仓）有明确「used in / proved by / billions of」表述、38% 提及微信；全量 275 严格背书句式仅 11 仓（libco / libpag / matrix / MMKV / ncnn / paxosstore / phxpaxos / phxqueue / soter / wcdb / Wechat-YATT）——背书是少数派资产不是标配，70% 仓没有也不装。与 §9 D3 的关系：D3 因盲评降级为对照档案，本条以 275 全量统计重新立证并收敛为「有则用、无不装」。（Round 1 §3.1 + 全量复核 2026-09-29）

## 2. README 三档结构

| 档 | 适用 | 形态 | 样板 |
|---|---|---|---|
| 重 | 平台型项目 | 顶部锚点导航 + Overview + Quick Start 三入口 + What's New + Product Tour + 架构图 + 特性大表 + 客户端矩阵 + 独立文档站 + Contributing + License，四语 README | WeKnora |
| 中（默认） | 服务/组件 | Highlights（含基准表）→ Overview → 核心技术图 → Quick Start 按客户端分路径 → 参数三级折叠（🟢日常/🟡高级/🔴完整）→ 主题拆分 README 文件族（INSTALL/deployment/docker） | Agent-Memory |
| 轻 | CLI 工具 | README 即落地页：Logo → 徽章行 → 语言切换 → 一句话定位 → Why（before/after 配图）→ Quick Start → 支持矩阵表 → Learn More → 贡献者墙 | teamai-cli |

重档实证（WeKnora PR）：固定段序与锚点 **#3676**（`header → overview → quick start → what's new → screenshots → architecture → features → clients and ecosystem → docs → contributing`，Quick Start 提到第二屏、部署多入口表、七节客户端内容合一表）；Product Tour 内嵌 **#3117**；hero/能力卡双语双主题 **#3679**；特性大表 42 行收敛为 7 行、明细外链 docs 页 **#3688**；架构图随版本再生成 **#2585**/#2107。

共性硬规则（三仓全有）：

- 顶部顺序固定：Logo → 徽章行 → 语言切换 → 一句话定位
- Quick Start 给**可直接复制的命令块**，路径 ≤3 条
- 特性/生态用**表格**不用长段落；无数据写 `—`
- **README 减肥**：架构、能力矩阵细节移 docs/——teamai-cli#722 把五份 README 砍成落地页，架构细节移 `docs/product-overview.md`；WeKnora#3688 特性表 42 行 → 7 行、明细外链 docs 页，#3676 原则句「No core content is removed; long material moves into tables or collapsible blocks」（长内容进表格/折叠块，不删核心内容）。README 超过 ~200 行就该拆
- 多语言同步改动：#767 一个 PR 同步改五份 README（`README.md` `README.zh-CN.md` `README.ja.md` `README.ko.md` `README.th.md`），矩阵结构逐语言一致；WeKnora#2757 一处修正同步四份（`README.md` / `README_CN.md` / `README_JA.md` / `README_KO.md`），#2574 显式以 EN/CN 为基准对齐 JA/KO——**基准语言先行，其余语种对齐**

### 2.1 V2 扩充 · 三档扩五档（275 README Round 1 实测，按目标仓形态对号入座）

上表重/中/轻三档在 275 全量语料中细分出五个结构模板 + 1 个变体（Round 1 Top 50 十五篇精读定型，全量复核各档频率）：

| 模板 | 适用 | 形态要点 | 样板（全量频率） |
|---|---|---|---|
| T1 产品落地页 | 平台型产品 | hero 图（双主题）→ 徽章墙 → Overview → Quick Start → What's New → Product Tour 逐特性截图 → 架构 → 特性表 → Contributors 墙 → License | WeKnora；BrowserSkill / AI-Infra-Guard 同族（≈重档） |
| T2 多平台同构教程 | 跨平台基础库 | 徽章 → 语言切换 → 定位句 → `# X for {Platform}` 逐平台复制同构骨架（Features → Getting Started → Quick Tutorial → Performance），字面同构仅换平台名，不跨平台合并叙述 | MMKV 五平台 / matrix 四份同构；全量 275 中 H1 同构式仅 2 仓——多平台库专用形态，不外推到单平台仓 |
| T3 索引目录 | 老牌重仓 | logo → 定位段（EN+ZH）→ Quick Start 直给命令 → 正文极薄 → 大量 wiki/docs 链接导流，尾部「主题→链接」大表收束 | ncnn（尾部 wiki 大表）、weui、secguide（纯中文极简版）（≈中/轻档） |
| T4 概念宣言 | 个人/作者风格仓 | **宣言先于教程**：方法论/理念 bullet 墙开场（westore 五条 OOP/Passive View 原则、puerts WHAT/WHY/HOW 三问、omi emoji 特性 bullet + 代码首屏即出）→ 安装 → 案例 demo → 原理深潜 → Contributors | westore、omi、xLua、puerts——原三档未覆盖，作者人格最强 |
| T5 学术成果 | 研究/数据集仓 | H1 → 成果 bullet（数据规模 + 精度直接进首段）→ Updates 时间线（含论文录用动态）→ 操作节 → Results 表 → **Citation BibTeX 代码块收尾** | tencent-ml-images（17,609,752 URL + 80.73% top-1 进首段）、MimicMotion / MedicalNet / FaceDetection-DSFD |
| T6 双语拼接（变体） | 微信链路双语仓 | T2/T3 内容 EN 版 + ZH 版用锚点首尾相接同文件（matrix 850 行 = iOS/Android × 英/中 四份同构），文件长度翻倍是 mixed 仓 median 17K 的直接原因 | mars、matrix、puerts |

选择规则：先判目标仓/新仓形态再选模板，**不跨形态混装**（T5 仓不硬加 Contributors 墙，T4 仓不套徽章墙）。T5 在全量 275 中占 68 仓（24.7%，含 BibTeX 块）——学术仓是 org 长尾主体之一，原三档表未覆盖，这是扩档的最大增量。与 §9 退出阀的关系：DNA 批次曾因「统一 modern 模板」拉低盲评可识别性而整批降级——本表按仓形态分派并标注各档频率，写作时对号入座而非全局套用，避免重蹈覆辙。（Round 1 §2.2 + 全量 275 复核 2026-09-29）

## 3. 语言硬参数（实测）

中文句长（维护者评论语料，n=188）：中位 **25 字**，P25–P75 = **11–45 字**，P90 = 68 字。超出 P75 的句子拆句。英文句中位 72 字符（n=1418），复杂约束用列表不堆长句。

- 感叹号 **0.3 个/千字**、问号 0.3 个/千字——情绪不进正文（社区公告类例外，如 Good First Issue 帖用 🎉）
- 标题 Conventional Commits：`type(scope): 描述`——**按仓分层，跟随目标仓**。强治理仓 84–98%（teamai-cli 98% / tdesign 94% / WeKnora 92%，v0.1.1 口径的 90% 即此类）；老基础库仓 4–13%（ncnn 4% / MMKV 8% / tinker 13%，org 级 11,488 篇 PR 实测复核，dna-2026-09-28）。给弱治理仓提 PR 时标题跟仓内惯用格式（多为普通祈使句），不强制 CC；scope 是模块名（`docs(install-cn)` `fix(pull)` `feat(models)`）
- 列表条目一个约束一件事；参数/厂商对比一律表格（lyingbug 的 rerank 协议表：厂商 × 为什么对不上，WeKnora#3512）
- 数字代形容词：`95.7% → 89.5%`（Agent-Memory#120 命中率对比表）、`290 files, 4313 passed, 1 skipped`（teamai-cli#675）
- **V2 扩充 · 性能声明个位精度**：性能/规模数字给到个位——`80.73%` top-1（tencent-ml-images 首段）、`17,609,752` URL、宿主增量 `15KB，160 方法数`（Shadow）——从不写「快了很多」「高性能」「轻量级」（Round 1 §4.2）。全量 275 复核：28 仓含小数精度百分比共 225 处、体积/方法数类精确数字 29 处。与上条「数字代形容词」及下条「数字密度节制」构成三段式：形容词 → 换成个位精度数字 → 有基准处精确、无基准处定性
- 数字密度节制：精确数字只给有基准或可复现来源的对比处；不是每个卖点都配数字，一处精确 + 其余定性才是真实节奏——「每个卖点后缀一个恰好精确的数字」在盲评中被判为最强 AI 破绽（`analysis/blind/VERDICT.md` 2026-09-28；盲评证据，非语料证据）
- 验证写实证：69% 的 PR 验证段含真实命令（`npx tsc --noEmit` / `git diff --check`），66% 含具体通过数字；纯文档 PR 也写「Documentation-only change; no runtime test suite run」（Agent-Memory#855）

## 4. CHANGELOG 风格

- **一行一条、面向用户效果**，不面向 diff：写「members can scope docs per project」，不写「修改 pull.ts」
- 破坏性变更单独归入 Breaking Changes 段并给迁移口径：teamai-cli#710「which is why this is filed as breaking and the changelog entry sits under Breaking Changes」，正文同时写清谁受影响（`every pull fails until the entry and its directory are renamed together`）
- 条目改动纪律：rebase 冲突时「keep #713's line above it, take this PR's text」（teamai-cli#710）——已有条目不被覆盖
- 三仓均无 Keep a Changelog 声明（WeKnora 2517 篇 PR 复核仍无实证）；等价格式约定是**每版本向 CHANGELOG.md 追加整节 release notes**——WeKnora#2585/#2107/#1822 措辞跨版本重复（`Add comprehensive vX.Y.Z release notes to CHANGELOG.md`），且链接必须可点击、历史文字保留（#3580）
- 面向用户的措辞要能被 grep 验证：#816 验收标准含「A grep for the old per-entry and duplicate-error wording finds nothing stale」——改口径必须清旧词

## 5. docs / CONTRIBUTING 规则

- **文档漂移是 bug**：#767 把支持矩阵里 3 个 `—` 改成 `✓`，定性「documentation drift: the matrix contradicts the shipped, tested behavior」——文档与代码不一致按 bug 修，纯文档 PR 也走完整验证
- **何时触发文档更新（显著变更过滤，吸收自 warp oz-skills docs-update，2026-09-28）**：新公共 API/CLI 参数/配置项、默认值变更、破坏性改动、安装步骤变化——必更文档。跳过：内部重构、私有函数改名、测试调整、纯格式化。拿不准跳不跳：倾向跳过并在 PR 描述里留一句「文档影响：无/待评估」
- 命令可照做：CONTRIBUTING 的 clone/分支命令必须真实可跑——Agent-Memory#939 修复文档里不存在的分支名（`The documented branch names do not exist, so a new contributor cannot follow the commands as written`）
- 死链即修：#1110 删除指向不存在文件的引用（`following the documentation leads to dead links`）
- 文档站是重档配套（WeKnora）：website-docs 创建 **#2350**（46 篇约 16000 行，六分部组织）、官网域名接入 **#2576**、站点写作规范 **#3095**（`website-docs/README.md`）、`website-docs/` 为唯一文档源、旧 `docs/` 正文删除 **#3580**（README 只留入口，正文住文档站）
- 中文文档细则（20 字分句、中英空格、全角标点）交给 zh-tech-writing；本 skill 只管内容与结构

## 6. 反模式（≥8 条，见到即改）

| 不要 | 要（依据） |
|---|---|
| README 塞架构细节、命令全表 | 砍成落地页，细节进 docs/（teamai-cli#722；WeKnora#3688） |
| 特性写长段落 | 表格 + `—` 占位（三仓特性表通例） |
| 中文入口的内容同步进其他语种 | 只改对应语种文件（teamai-cli#745） |
| 支持矩阵与代码行为脱节 | 以 shipped 行为准改 `✓`/`—`（#767） |
| 贡献指南写不存在的分支/URL | 逐一核对可执行性（Agent-Memory#939/#1148） |
| CHANGELOG 写「优化了若干问题」 | 一行一条用户可感知效果 + 破坏性入 Breaking Changes（#710） |
| 验证写「测试通过」 | 贴命令 + 通过数字；纯文档则写明 no runtime test（#855） |
| 双语文件只改一边 | 两边同 PR 改、内容对齐（teamai-cli#767 五语；WeKnora#2757 四语） |
| 文档改动不留验证 | git diff --check + 渲染预览 + 链接解析（#722 的 Test Plan） |
| 两套文档并存 | 唯一文档源，旧目录清掉（WeKnora#3580 删 87 篇迁移后旧文） |
| 每个能力缺口都补 RFC/roadmap/issue 链接 | 待办不对称是常态，缺口可以就写成缺口（盲评 VERDICT：系统性「可信度补丁」是生成痕迹） |
| 刻意点缀幽默/金句装人味 | 人味来自具体事实与数字，不来自段子（盲评 r2：点缀痕迹反被判为破绽） |
| 多语文件命名一套仓库混两套 | 仓内统一：README_CN.md 系（WeKnora）或 README.zh-CN.md 系（teamai-cli），不可混用（#2757/#767） |
| 对外声明用「全量/完全/所有」等总括词 | 定位句的每个词都要能被 evidence 文件背书；覆盖不到的写清来源分际（penguin-oss-suite README 定位句两次过度声明实测教训：全量→三源分说） |

## 7. 多语言管理（原 oss-i18n，v0.2.1 并入）

> 文档层 i18n：README/docs/CHANGELOG 的多语同步、命名与验收。UI 组件库的 i18n 实现（vue-i18n / react-intl 代码级）不在本节。语料：WeKnora 366 + teamai 47 条 i18n 相关 PR + 12 仓 skeleton README 分布，12 条规则候选全录 `corpus/org-sweep/drafts/out-oss-i18n.md`。

### 7.1 多语同步制度化（规则 I1，最硬）

- teamai#607 把多语同步写进 AGENTS.md：所有语言版本（README.md 及全部 README.*.md）必须同 PR 全部改完并保持一致。
- **用 glob 不硬编码清单**：改前先 `ls README*` 确认清单，新加语言文件自动纳入规则，不依赖人记住有哪些语言。不译的文件不创建（teamai#2 删 README.en.md——英文是默认）。与 oss-dev「跨工件同步判据」同门：代码改动联动文档，文档改动联动多语。

### 7.2 语言选择与命名（规则 I2）

- 英文默认是**开仓显式决策**，不是后加的（teamai#2 开仓当天对调 README.md/README.zh-CN.md，"targeting a global audience"）。
- 命名两派并存：大写下划线系 `README_CN.md`（WeKnora/AIG 系，AIG 9 语收 `readme/` 子目录 + 旗帜链接）vs 小写 BCP-47 系 `README.zh-CN.md`（teamai 系）；tdesign 两种混用是反例。单文件内嵌多语切换：12 仓零案例。
- 规则 I2：新仓选英文主 README → `README.md` 英文 + `README.zh-CN.md` 中文；已有仓跟随其命名系不改。

### 7.3 翻译验收 = 结构对齐，无回译

- 验收 = 标题层级与英文源匹配 + 语言切换链接 resolve（teamai#584 Test Plan）；术语/命令/代码不译是硬约束（#584 原文）；没有仓做「翻译回来对比原文」的回译校验。
- 多语漂移按 bug 定性（WeKnora#767 五语支持矩阵不同步 = documentation drift，处置见 §5）。
- EN/CN 基准先行、JA/KO 滞后补齐型 sync PR 合法（WeKnora#2574）；外部母语贡献者是日/韩翻译主要来源（#222/#490/#668/#2757）——翻译贡献门槛低于代码贡献。

### 7.4 docs/ 目录双轨制（规则 I3）

- 子目录派 `docs/en/page.md` + `docs/zh/page.md`（omi / vConsole）vs 文件后缀派 `page.en.md` + `page.zh.md` 同目录（teamai）；各链各语言文档（teamai#202 每种语言链自己的 docs 索引）。
- 规则 I3：新仓选子目录派（更易扩展非拉丁字母语言）；已有仓跟随。

### 7.5 非 README 的多语现状

- CHANGELOG / CONTRIBUTING：12 仓全单语。
- Issue 模板：收拢到英文（WeKnora#1289 统一为英文模板）。
- 发版 PR：必带全语 README highlights（teamai#1307 五语版本并列）。
- 中文专属内容不扩散到其他语言（teamai#745，场景三分法见 §1）。

## 8. 证据与出处速查

- 语料（2026-09-28 全量重抓）：`corpus/three-repos-raw/`（pulls / issues / maintainer-comments 三类 JSONL + summary.json）；分析产物在 `analysis/`
- WeKnora 重档 / 多语 / CHANGELOG / 文档站实证：`analysis/out-voice-weknora.md`（R1–R5 逐条引句）
- README 减肥：`pr/Tencent-teamai-cli__722.md`（v0.1.1 语料）+ WeKnora#3688/#3676
- 五语同步矩阵：`pr/Tencent-teamai-cli__767.md`；四语同步：WeKnora#2757/#2574
- 文档漂移修复：`pr/Tencent-teamai-cli__770.md`（零字节占位文件的指路注释）
- Breaking Changes：`pr/Tencent-teamai-cli__710.md`
- 中文场景三分法：`pr/TencentCloud-TencentDB-Agent-Memory__1259.md`、`issues/Tencent-teamai-cli__341.md`、`pr/Tencent-teamai-cli__745.md`；扩样 WeKnora#3793/#3617、Agent-Memory#1449、teamai-cli#534/#468
- 语言/句长/标点参数：`corpus/three-repos/issues/` 76 条维护者评论实测（v0.1.1 口径，统计脚本见 INDEX.md）；语言分布全量口径见 §1

未在语料中找到：三仓均无 Keep a Changelog 格式声明的直接证据（WeKnora 2517 篇 PR 复核仍无，等价约定见 §4）。WeKnora 维护者评论语料已补齐（967 条，2026-09-28），语气蒸馏归 oss-persona。

## 9. [DNA] 对照档案（批次 dna-2026-09-28，11 条均实证；**已按 §2 退出阀降级**）

> 状态：v0.2.0 盲评中评审以 D11/D4/D2 条目为破绽 ≥2 次（生成件呈现「统一 modern 模板」而真实仓风格杂糅），触发退出阀——本节从规则降级为**对照档案**：写作时不主动套用；仅当目标仓自身已呈现对应惯例时参照执行。回滚条件：下轮盲评显示套用不再拉低可识别性，或作者裁决恢复。

- **D1 PR 正文必含「边界/局限」小节**：方案后单列一节穷举不解决/不支持/留后续，条目化（12 代表 PR 中 8 篇：WeKnora#2234 十六条、ncnn#6933 No 清单、wujie#1082 ✅/❌ 表）
- **D2 验证状态三态分级**：已验证（附命令+通过数）/ 仅静态审查 / 尚未验证分开陈述；checklist 未完成项留 `[ ]` 并写原因（WeKnora#2234、ncnn#6933 Provenance 节、spring-cloud-tencent#1815）
- **D3 腾讯系 App 具名背书句**：首屏定位后一句 "used in … such as QQ, WeChat" 式具名落地，不用 widely used 泛称（ncnn / MMKV / Hippy）
- **D4 社区入口给可执行群号/二维码**：QQ 群号、微信群码、Discord 至少其一；不写「欢迎加入社区」空话（ncnn 三群+入群答案、vConsole `QQ Group: 497430533`）
- **D5 多平台库按平台同构重复**：`# X for <Platform>` 小节复用同构 Features/Quick 模板 + 本平台命令，不跨平台合并叙述（MMKV 五平台、ncnn 下载矩阵）
- **D6 emoji 全有或全无**：系统化（每章一头）或全零，禁零星点缀；矩阵符号 ✓/—/→ 不计 emoji（12 仓实测：零 6 仓 / 系统化 3 仓 / 点缀仅 1 仓 1 处）
- **D7 次要内容 `<details>` 折叠，主线不折**：截图组、历史版本、备用安装、长引用收折叠；最新版本与主安装路径保持展开（vConsole 7 组截图、WeKnora 版本史）
- **D8 长周期 PR 按轮次追加不改写**：每轮新增 `Review round N.` 段，旧轮保留；更新锚 `Latest update: <hash>` 逐 commit 说明（teamai-cli#698 追加至 22 轮、ncnn#6933）
- **D9 生产安全警示写进 README 正文**：内网部署、隐私不收集、无鉴权警告用 GitHub alert（`[!WARNING]`）或专章（WeKnora、MMKV 隐私专章、AI-Infra-Guard 公网警告）
- **D10 双语 PR 平行段**：`## 中文` / `## English` 两段同构对照，先母语后英文，信息量对齐（vConsole#738、AI-Infra-Guard#446）
- **D11 特性三/四词经开篇**：定位句后 3–4 个加粗双词特性词，各配一行落地证据，不另起长段落（MMKV efficient/small/easy-to-use、wujie 四词经）

护栏：DNA 条目数 ≤ 语料证据条目的 50%（本批 11 条，合规）；DNA 条目不得冒充语料证据；盲评若连续暴露 DNA 条目拉低生成质量，整批降级为验证对照。





