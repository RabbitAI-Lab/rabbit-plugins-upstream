---
name: oss-format
description: 腾讯开源仓文档排版规则（规则层第五成员，19 仓 82 文件 + 298 仓组件基线蒸馏）。管「文档怎么排」：标题层级 / 加粗 / 列表嵌套 / 表格 vs 列表 / 代码块语言标注 / 徽章 / 图片 / emoji 分区，以及 CONTRIBUTING / LICENSE / SECURITY.md / CODE_OF_CONDUCT / .github Issue·PR 模板的骨架选型与门槛条款写法。内容写什么归 oss-voice，维护者口吻归 oss-persona，回复文案归 oss-contribution。触发词：排版、格式化、文档排版、仓库文档排版、贡献指南排版、贡献指南格式、LICENSE 选择、许可证、安全文档格式、SECURITY.md、CODE_OF_CONDUCT、行为准则、Issue 模板、PR 模板、.github 模板、oss format。不用于：文档内容与结构叙事（oss-voice）、中文句式细则（zh-tech-writing）、CI workflow 排版。
metadata:
  openclaw:
    requires:
      bins: [git, gh]
---

## §0 场景闸门

本 skill 是被调度成员，不是场景入口。若当前任务会写 GitHub（提 PR / 评论 issue / commit / push / 建仓）且 .oss-task/ 下无 CHECKLIST.md：**先停下**，加载 routing/oss-workflow 按 §1 识别场景并实例化清单，再继续执行本 skill 对应步骤。无清单裸奔 = 违规交付（#752 实战：T1 裸奔 320s 被作者中止，61% 时间损耗）。运行时另有 penguin-guard 硬闸（PreToolUse）拦截无清单的 gh/git push 类命令。

# oss-format：腾讯开源仓文档排版规则（docs-files 蒸馏）

> 语料：`corpus/org-sweep/docs-files/`（19 仓 82 文件全文，2026-09-29 gh api 抓取）+ `settings-profiles/PROFILE.md`（298 仓组件基线）+ README 两轮 DNA（`dna-round1-top50.md` / `dna-round2-mid50.md`）。证据全索引：`corpus/org-sweep/drafts/DOCS-FORMAT-DNA.md`。规则编号 F1–F37，每条带仓级证据。

## 0. 边界与分工

- **oss-voice 管写什么（内容），oss-format 管怎么排（排版）**：一句话定位怎么写、README 三档/五模板选型、CHANGELOG 措辞在 oss-voice；标题几层、加粗几处、表格还是列表、徽章怎么挂、模板骨架长什么样在本 skill。
- oss-persona（回复声纹）、oss-contribution（PR/Issue 文案）、penguin-methodology（执行纪律）不与本 skill 重叠。
- 产出顺序：oss-voice 定内容 → 本 skill 定排版 → humanizer 去 AI 腔 → zh-tech-writing 定中文句式。
- 两个前置判断（先做再排版）：**先判代再判星**（2015–2018 老仓 / 2023–2026 新仓形态差异大于星带差异）；**先查同家族仓**（腾讯内部模板按家族复制——MMKV/tinker/matrix/wcdb 的 CONTRIBUTING 逐字同构，tdesign 系 PR 模板逐字同构。给家族仓写文档，家族一致性 > org 一致性 > 行业最佳实践）。

## 1. 通用排版硬规则（F1–F7，全部文档类型适用）

- **F1 标题深度封顶 H3**：社区文档 H4+ 使用率实测 0–17%，正文最深 H3；H1 只给独立文档（CONTRIBUTING/SECURITY/CoC），**PR/Issue 模板永远不写 H1**，用 md frontmatter（`name/about/labels`）或 yml（`name/labels/title`）标识。（DOCS-FORMAT-DNA §1.2-1）
- **F2 加粗只给关键词与硬性条款，每文件 ≤5 处**：分支纪律（**Don't submit any PR on `master` branch**，MMKV）、禁令（**Do not disclose it as a public issue**，cherry-markdown）、时限承诺（**48 hours**，WeKnora）。禁整句/整段加粗。（§1.2-2）
- **F3 列表嵌套 ≤2 层**：28 个 prose 文件 100% 遵守。有序列表只用于步骤（PR 流程/复现步骤），无序列表只用于条件（检查单/条款），不混用。（§1.2-3）
- **F4 代码块语言标注**：老仓裸 fence 画 ASCII 图是历史形态；新写文档一律标注（`bash`/`text`/`html`），ASCII 分支图标 `text`。（§1.2-4）
- **F5 表格是 README 专属元素**：社区文档表格率 0–20%（唯二重用：MMKV SECURITY 版本支持表、cherry-markdown CONTRIBUTING 命令表）；社区文档的信息组织靠「节标题 + 编号步骤 + checkbox」。对比型/矩阵型信息才配表格，且无数据写 `—`。（§1.2-5 + oss-voice）
- **F6 emoji 三合法位置**：① 模板类型标签（🐛 Bug fix / ✨ New feature，WeKnora/tdesign）；② yml labels（`🐞bug,🧐unconfirmed`，tdesign/Hippy）；③ 2023+ 新仓 README 章节头。**非法位置：SECURITY 正文（⚠️ 警示符除外）、CoC、LICENSE、CONTRIBUTING 正文**——正式治理文档 emoji≈0 是铁律。（§L6）
- **F7 正式文档 100% 英文**：SECURITY 5/5、CoC 4/4、LICENSE 18/18 实测全英文，含中文主导社区（cherry-markdown SECURITY 英文正文只带 QQ 群号）。CONTRIBUTING 与 Issue/PR 模板跟随社区语言（中文仓用中文/`zh-CN.yml`，国际仓英文，APIJSON 式双语字段标签是唯一特例）。（§1.3）

## 2. README 排版（F8–F14，整合两轮 DNA 排版层）

- **F8 首屏四件套顺序固定**：Logo/hero（`<p align="center">`）→ 徽章行 → 语言切换行 → 一句话定位。28% 仓以 `#` H1 起手，更多仓第一行直接是居中图或徽章。（Round 1 §2.1）
- **F9 结构模板按仓型对号入座，不跨形态混装**：T1 产品落地页 / T2 多平台同构 / T3 索引目录 / T4 概念宣言 / T5 学术成果（BibTeX 收尾）/ T6–T8 变体——选型表在 oss-voice §2.1，本 skill 只管各模板的排版执行（T2 逐平台字面同构仅换名；T5 成果数字进首段 bullet）。（Round 1 §2.2 + Round 2 §2）
- **F10 徽章 4 枚中位、挂在首屏**：62% 仓有徽章，median 4.3 枚；老仓 CI+License+PRs welcome 三连起步，新仓加 Discussions/ pkg.pr.new。社区文档（CONTRIBUTING/SECURITY/模板）零徽章。（Round 1 §1.2 + 本轮 L6）
- **F11 图片四类各有位置**：品牌 logo/hero 首屏居中（94% 仓有图）；产品截图廊用 `<details>` 折叠（vConsole）或 Product Tour 逐节（WeKnora）；架构图独立节；QQ 群二维码嵌社区渠道节。家族仓引用主仓 raw URL 集中托管（tdesign 子仓）。（Round 1 §6.3 + Round 2 N11）
- **F12 emoji 全有或全无**：42 仓≈0，4 仓重度（teamai-cli/puerts/AI-Infra-Guard/TNN）——emoji 是 2023+ 新仓代际标记，不是 org 统一风格；给老仓补 README 不强加 emoji。（Round 1 §6.2）
- **F13 结尾三派选一**：License 一行链接收尾（约半数）/ 信息公示合规节（微信系 SDK 家族指纹：SDK名称/版本/开发者=深圳市腾讯计算机系统有限公司/隐私规则链接）/ 社区渠道收尾（QQ 群/Discussions/知乎）。（Round 1 §2.3）
- **F14 双语排版三形态**：独立中文文件（README_CN.md，34–36% 仓，跨带最稳指标）/ 同文件锚点拼接（T6，长度翻倍）/ 节级交替（sluaunreal）。仓内命名统一一套（README_CN.md 系或 README.zh-CN.md 系），不混用。（Round 1 §1.4 + Round 2 N3 + oss-voice §7）

## 3. CONTRIBUTING 骨架（F15–F19）

- **F15 四模板选型**：C1 家族型（Issues→PR→Branch Management→Code Style→License 五节，微信系标配）/ C2 commit 规范型（文档仓收窄到协作格式）/ C3 招募说理型（个人主导仓）/ C4 现代流程型（2024+ 默认）。新仓一律 C4。（§2.1）
- **F16 C4 骨架节序**：Before you start（查重 + 非平凡改动先开 issue + good first issue 指路）→ Local setup（版本要求 + 可复制命令）→ 贡献路径分型（列出「不动核心代码也能贡献」的方式：规则文件/文档/数据集）→ PR checklist（一 PR 一事）→ Response expectations（分诊时限 + ping 礼仪：一周后礼貌 ping 欢迎、48h 内不重复）→ Getting help（Discussions/Issues/SECURITY 三渠道分诊）。（AI-Infra-Guard CONTRIBUTING）
- **F17 分支模型显式化**：多分支仓必须写 Branch Management 节——三分支（master/dev/hotfix）各自用途 + **加粗禁令**（Don't submit any PR on `master`）+ ASCII 分支图（fence 标 `text`）。单分支仓写「从 `main` 拉 feature 分支」一句。（MMKV/tinker/matrix/wcdb 同构）
- **F18 PR 检查单 6 条形态**（C1 家族）：fork 拉分支 → 改 API 同步文档 → 新文件加版权头 → lint/checkstyle → **test and test again** → 提交到正确分支。命令必须真实可跑（Agent-Memory#939 反例：写了不存在的分支名）。
- **F19 贡献授权条款收尾**：「By contributing to {X}, you agree that your contributions will be licensed under its [LICENSE](./LICENSE)」——C1 家族固定收尾节；需要 CLA 的仓在此说明。（MMKV/tinker/matrix/wcdb）

## 4. LICENSE（F20–F24）

- **F20 腾讯公司仓用 wrapper 格式**：`Tencent is pleased to support the open source community by making {项目名} available.` + `Copyright (C) {年} {Tencent | THL A29 Limited, a Tencent company}. All rights reserved.` + binary/source 分别声明适用证 + 正文全文 + 第三方组件清单。wrapper 是 GitHub API 返回 NOASSERTION（76.3%）的原因，不是缺许可证。（§2.2）
- **F21 正文选型**：默认库/框架 BSD-3-Clause（老仓主体）或 MIT（2019+ 与含大量第三方组件的仓，如 WeKnora 158K 第三方清单）；Apache-2.0 用于生态型新仓（cherry-markdown）；GPLv2+CE 仅 JDK 发行版类（TencentKona）；**内容/文档仓用 CC-BY-SA-4.0（secguide）不用代码证**。社区/家族治理仓可用裸标准证（tdesign 系裸 MIT 署 TDesign）。
- **F22 文件命名按代际**：老仓 `LICENSE.TXT`（ncnn/MMKV/QMUI），新仓一律 `LICENSE` 无扩展名；同仓引用保持一致（CONTRIBUTING 收尾条款的链接指向实际文件名）。
- **F23 第三方组件清单进 LICENSE 文件尾**：组件名+版本+版权行+许可证，按许可证分组（omi 列 preact 三件套；WeKnora 引 `THIRD_PARTY_NOTICES.md` + licenses/ 目录）。改依赖必须同步这段清单。
- **F24 不自造许可证条款**：org 无自撰附加条款先例（Kona 的 "Tencent Modifications" 是 OpenJDK 生态标准写法）；需要特殊授权口径时走 wrapper 声明句，不改正文条款。

## 5. SECURITY.md（F25–F28）

- **F25 最低骨架三要素**：① 禁公开披露（加粗/⚠️，**DON'T open issues in public**）；② 私密通道（GitHub Security Advisories / private vulnerability reporting，备选团队邮箱）；③ 期望响应（48h 确认或 5 工作日分诊）。三要素缺一即不合格。（WeKnora S4 型）
- **F26 支持版本表放最前**（有多版本维护的仓）：`| Version | Supported |` 两列表，用 :white_check_mark: / :x:——这是 SECURITY.md 唯一合法表格。（MMKV）
- **F27 中文社区仓的通道例外**：私密通道可写 QQ 群私聊群主（cherry-markdown），但正文仍英文、仍保留「禁公开 issue」条款。安全通道跟随社区现实，语气不跟。（S3 型）
- **F28 安全属性即卖点的仓升 S5 超规格**：Required in Reports 要素清单（标题/严重度/影响/组件/PoC/环境/修复建议）+ Common False-Positive Patterns 预写误报清单 + Trust Model 信任边界 + Out of Scope 明确不收什么 + 披露时间线（Critical/High 14 天）+ 团队署名（朱雀 Lab 模式）。工具仓不抄这档。（AI-Infra-Guard）

## 6. CODE_OF_CONDUCT（F29–F31）

- **F29 直接用 Contributor Covenant，不原创**：4/4 全是 Covenant 原文搬运（v1.4 老仓 / v2.0 新仓），零自撰、零中文版。（§2.4）
- **F30 唯一必做动作：填联系方式**——Hippy 搬了 v2.0 全文却留着 `[INSERT CONTACT METHOD]` 占位符、tdesign-vue-next 联系方式为空，是 org 级反面教材。Enforcement 节的邮箱必须真实（MMKV guoling@tencent.com / AIG zhuque@tencent.com）。
- **F31 放置位置**：老仓根目录 `CODE_OF_CONDUCT.md`，新仓 `.github/CODE_OF_CONDUCT.md`（Hippy 式）；CoC 覆盖率仅个位数百分比且家族化——非治理型仓可不装，装就必须完整。

## 7. .github 模板（F32–F37）

- **F32 Issue 模板形态按代际选**：老仓/低维护仓 md（含 frontmatter `name/about`）；活跃新仓一律 yml issue-forms + `config.yml`。yml 的 `blank_issues_enabled: false` + `contact_links`（文档站 FAQ + Discussions）配套出现——把提问导流到文档是模板的一部分。（WeKnora）
- **F33 域拆分优于通用模板**（工具属性强的仓）：按用户实际问题域拆多模板（ncnn：bug / model-convert / quantization / others 四分；cherry-markdown：数字前缀 `1.bug_report.yml`…`6.vscode_plugin_feedback.yml` 排序六分 + other 兜底）。跨语言用户群用三语节标题（`## error log | 日志或报错信息 | ログ`）。（ncnn/cherry-markdown）
- **F34 门槛条款三档，默认中档**：教育型（搜索确认 checkbox + 最小复现链接教育 + 版本字段禁填 `latest`/`main` 并给查找路径，WeKnora/cherry）/ 限期型（「无清晰重现步骤不修复，need reproduction 7 天不补关闭」，tdesign/Hippy）/ 拒斥型（「无日志一周关闭」「模糊表达直接关闭」，MMKV/tinker——只适用于已有 issue 泛滥的中文高流量仓，新仓禁用）。
- **F35 PR 模板语言跟随社区语言**，骨架两型：英文标准五节（Summary / Type of change checkbox / How was this tested / Related issue / Checklist——AIG 型，Checklist 含「无硬编码密钥」）；中文家族型（tdesign：🤔性质 / 🔗相关 Issue / 💡背景方案 / 📝更新日志（monorepo 按包分节）/ ☑️自查清单 + ⚠️ 勾选全部选项）。重型工程仓加命令级 checklist（`git diff --check origin/main...HEAD`、lint `--new-from-rev`，WeKnora 型）+ Testing 节写 escape hatch（全仓检查被无关失败阻塞时，记录命令与失败）。
- **F36 必填字段最小集**（bug 类模板）：版本（具体版本号，禁 latest/main）、环境（OS/部署方式/平台）、复现步骤、期望 vs 实际结果、日志。外加一个搜索确认 checkbox。WeKnora 型加组件 dropdown 与 Log Collection Guide（按部署方式给命令）。
- **F37 CODEOWNERS/FUNDING 不是 org 通用组件**：CODEOWNERS 13/298 全部是 TDesignOteam 治理模式，FUNDING 1/298（MMKV）——非 tdesign 家族仓默认不建；社区招募机制（new-component 认领模板 + PMC 超期接手 + 问卷入群，tdesign）是家族特供，按需复制。（PROFILE §4）

## 8. 反模式速查（对应规则见括号）

| 不要 | 要 |
|---|---|
| 模板/SECURITY 写 H1 或 H4+ | frontmatter/yml 标识 + 正文封顶 H3（F1） |
| 整句/整段加粗强调 | 关键词与硬性条款 ≤5 处（F2） |
| SECURITY.md 里堆 emoji 装饰 | ⚠️ 警示符一枚即可，其余零 emoji（F6） |
| 中文仓的 SECURITY/CoC 写中文 | 正式文档一律英文（F7） |
| CONTRIBUTING 里用大表格铺流程 | 节 + 编号步骤 + checkbox（F5） |
| 裸 fence 画分支图 | ```text 标注（F4/F17） |
| CoC 搬完留 [INSERT CONTACT METHOD] | 装模板必填占位符（F30） |
| 自造许可证条款 | wrapper 声明 + 标准正文（F20/F24） |
| 新仓用一行式/须知型旧模板 | yml forms + config.yml 起步（F32） |
| 新仓写「无日志直接关闭」 | 教育型 + 限期型条款（F34） |
| 给 tdesign 家族仓写英文 PR 模板 | 家族一致性优先，先查同家族仓（§0/F35） |
| monorepo PR 模板不分包 | 更新日志按包分节（F35） |

## 9. 证据与更新

- 全量证据：`corpus/org-sweep/drafts/DOCS-FORMAT-DNA.md`（L1–L6 六层 + 19 仓组件矩阵 + 404 记录）；原文语料 `corpus/org-sweep/docs-files/{Repo}/{file}`（`__` 为路径分隔）；量化 `_stats.json`；manifest `_manifest.json`。
- 采样偏差声明：19 仓为 Top 头部混合样本（org 基线：CONTRIBUTING 31.2% / issue 模板 20.5% / SECURITY 7.4% / PR 模板 1–13.2%）——本 skill 规则描述「头部仓怎么做」，给长尾仓建议时按覆盖率降档表述。
- 5 个任务指定仓 404（tube/TMWorkflow/WeChat-Tencent/HunyuanOCR/tencent-ai-code），替补 5 仓已留痕（fetch-docs-r2.ps1）。



