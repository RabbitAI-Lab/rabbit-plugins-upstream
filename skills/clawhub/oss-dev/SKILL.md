---
name: oss-dev
description: 腾讯开源仓实测开发流程纪律（流程侧，不做代码侧）——commit 粒度、CI 门禁、review 循环、分支策略、发布节奏五维度，蒸馏自 ncnn/teamai-cli/WeKnora/MMKV 等四代表仓 400 条 commit + 127 份 workflow + 12 仓 PR/review 语料。填 oss-contribution P4–P6 实现段的腾讯实测形态空档。写代码的最佳实践（TDD/调试/重构）归 superpowers 生态，本 skill 只管怎么组织开发。触发词：开发流程、commit 纪律、CI 配置、review 应答、分支策略、发布节奏、版本管理、oss dev。
metadata:
  openclaw:
    requires:
      bins: [git, gh]
---

## §0 场景闸门

本 skill 是被调度成员，不是场景入口。若当前任务会写 GitHub（提 PR / 评论 issue / commit / push / 建仓）且 .oss-task/ 下无 CHECKLIST.md：**先停下**，加载 routing/oss-workflow 按 §1 识别场景并实例化清单，再继续执行本 skill 对应步骤。无清单裸奔 = 违规交付（#752 实战：T1 裸奔 320s 被作者中止，61% 时间损耗）。运行时另有 penguin-guard 硬闸（PreToolUse）拦截无清单的 gh/git push 类命令。

# oss-dev：开发流程纪律（流程侧）

## 0. 定位与边界

- **只管流程，不管代码**：commit 怎么写、CI 怎么配、review 怎么应答、分支怎么选、版本怎么发——「怎么写出好代码」归 superpowers（TDD / systematic-debugging），本 skill 不重复。
- 与 oss-contribution 的关系：P4–P6 实现段插入本 skill 的对应规则；P0 选题、P8–P9 交付沿用 oss-contribution 主流程，本 skill 补 P9 的维护者侧形态。
- 语料：四仓各 100 条 commit（ncnn/teamai-cli/WeKnora/MMKV，2026-09-28）+ 127 份 workflow 正文 + 12 仓 PR/review 语料的蒸馏报告（`corpus/org-sweep/drafts/out-ossdev-*.md`）。计数均样本内。

## 1. commit 粒度纪律

| 规则 | 证据 | 边界 |
|---|---|---|
| CC 纪律在 PR 层执行，commit 层继承——squash-merge 是主通道（teamai 98–100% squash，commit CC 100% ≈ PR 98%） | 四仓实测 | WeKnora 直推也手写 CC（60% squash 但 CC 仍 100%）——强治理仓直推也守格式 |
| **一 commit 一件事是四仓共同底线**（真混合 ≤5%），治理强弱只差格式层（MMKV 直推也单意图：add ×25 / fix ×17 / harden ×6） | 四仓实测 | ncnn 有自洽 subsystem 前缀风格（`x86:` / `vulkan:` / `pnnx`），不是 CC 但同样自洽 |
| 直推 vs 团队流程的分界 = **PR 落地率**（不是 top1 作者占比）——ncnn top1 68% 但 98% 走 PR（团队流程）；MMKV top1 81% + PR ≤11%（真直推型） | ncnn vs MMKV | 判仓先查 `gh pr list --state merged --limit 20` 的 base 分布 |
| verified 率 ≈ 合并机制占比（WeKnora 60% = squash 60%），**不是个人签名纪律**——别把签名率当治理指标误判 | 四仓实测 | Shadow 的 commitlint job 把 commit 格式进 CI 门禁——格式纪律可制度化 |

## 2. CI 纪律

| 规则 | 证据 | 边界 |
|---|---|---|
| `contents: read` 是默认档——56% 仓显式声明、占显式权限仓的 88%；提权只发生在发布 job（`contents: write` / `id-token: write` OIDC） | 127 份 workflow | 新建 CI 顶层必写 `permissions: contents: read` |
| push + PR 双触发是默认档（61% / 58%）；PR-only 仅机器人族；schedule 慎用（4/127） | 同上 | 并发写法 100% 固定：`concurrency: group: ci-${{ github.ref }}` + `cancel-in-progress: true` |
| **零 retry**——失败处置靠步骤确定性，不靠重试；`fail-fast: false` 拉满失败面（4/6 骨架 + org 16 处） | 六语言骨架 + org 统计 | lint 软门（`|| true` 允许警告）/ format 硬门（`--Werror`）分层（ci-cpp 实测） |
| 条件 artifact：仅 master push / 主仓守卫 / 矩阵单格触发收集 | 六骨架 | timeout-minutes 四骨架缺失——新 CI 补上（防挂死） |

## 3. review 循环

| 规则 | 证据 | 边界 |
|---|---|---|
| **贡献者应答四件套**：逐条回应 + follow-up 自报（`Review follow-up pushed onto this branch:`）+ 精确测试计数收尾（1679→4555 逐轮递增）+ pre-existing failures 归因（「修复前就存在的失败，不属于本 PR」） | teamai 16/28 条实测 | 计数是逐轮累加不是每轮重测——写「本轮新增 X / 累计 Y」 |
| 维护者 review 分级：P0（功能回归）/ P1（必须修）/ P2（建议）/ P3（接口语义），自审报告含否定式（`No P0.`） | teamai senior 自审 4 条 | 分级数跟仓——只有两级时写 P1/P2 别硬造 P0 |
| **review 收口三锚点**：head-hash 对比声明（`Verified against main at <hash>`）+ 显式 APPROVED / 合入通报 + 真实测试总数 | WeKnora #1337 / #2908 | 无 hash 不写 hash（沿套件红线） |
| **跨工件同步判据**（吸收自 alibaba/open-code-review rule.json，2026-09-28）：代码改动必须同 PR 联动受影响的文档与测试——`git diff --name-only` 含代码文件但不含对应 .md / _test 文件时，review 必须 flag（除非显式标注「文档影响：无」） | ocr rule.json 三分类（代码/文档/测试） | 跨语言仓的文档文件名不一致，按仓配置映射 |
| **review 执行器分层**：`ocr review --format json`（alibaba open-code-review CLI，必装）跑确定性缺陷检测（NPE/线程安全/XSS/SQL 注入），skill 管流程与应答——**工具找缺陷，skill 管流程**，不重叠；ocr 缺失即硬停，无降级 | ocr 混合架构 | `npm install -g @alibaba-group/open-code-review`；npm 不可用时从 GitHub Release 下载对应平台二进制 |
| 多轮增量不改写历史轮——每轮新增段落（`Review round N.`），旧轮保留 | teamai #698 22 轮实测 | deferred 写法：`deliberately deferred to <issue#>，覆盖路径 <方案>` |

## 4. 分支策略（三分型判仓）

| 型 | 仓例 | 判据 | 代价 |
|---|---|---|---|
| 直推 master | ncnn（纯社区） | 近期合并 PR base 全在 master + 维护者历史回复含直推 hash | 无审查记录；靠维护者自测纪律 |
| PR 只进 dev | MMKV / vConsole（版本隔离型） | base 分布集中在 dev / beta | 贡献者多一步 rebase；接班重构期 PR 被批量替代关闭 |
| 版本火车 | spring-cloud-tencent（分支矩阵型） | 多版本分支（1.x/2.x/...）各有 PR + cherry-pick 通道 | 维护成本随版本数线性涨 |

- dev 隔离全套：dev 吸收一切 / master 只发版 / beta 当缓冲；贡献者 PR 过期时用「dev 已有实现 + hash」替代合入而非强 rebase。
- 目标分支探测（填 oss-contribution P0）：提 PR 前 `gh pr list --state merged --limit 10 --json baseRefName` 看 base 分布；选错 base 是最大退回原因。

## 5. 发布节奏（三判据选型 + 联动四步）

**三判据**：决策人数（单人→即发 / 团队→milestone）× 用户类型（C 端→快节奏 / B 端→版本火车）× 分发通道（npm/PyPI→tag 触发 / 源码编译→Release 附产物）。

**锚点随节奏四选一**：版本号（快节奏）/ release tag（版本隔离）/ dev branch（持续集成型）/ commit hash（直推型）——状态通报与升级引导统一用该锚点。

**milestone 联动四步**（WeKnora / MMKV / vConsole 实测）：

1. PR 合入通报（`#PR 号已合入 + 剩余范围新编号`）
2. tag → Release → CHANGELOG 追加（旧版本折叠进 `<details>`，最新展开；链接可点击）
3. 升级引导收口（关闭旧 issue 时给「升级到 vX.Y.Z + 新开条件」）
4. 事故响应：补救版本（vX.Y.Z+1）+ 废弃声明 + 回归 PR 挂 issue 号

## 6. 引用接口

- oss-contribution P4–P6 插入点：P4 实现前查 §4 分支策略定目标分支；P5 测试期用 §3 review 应答四件套；P6 收口用 §3 三锚点 + §1 commit 纪律。
- oss-scaffold 建仓时：§2 CI 纪律写入 ci.yml 骨架（已实装于 settings-profiles 六语言骨架，本 skill 是其规则侧文档）。
- oss-persona：维护者声纹的 review 侧形态（lyingbug 审查长文 / m0Nst3r873 follow-up 链）是本 skill §3 的人格化载体——流程规则选声纹，不是声纹定流程。

## 7. 证据与局限

- 全部数字样本内：四仓各 100 commit + 127 workflow + 12 仓 PR/review 报告转引；规则候选全录 `corpus/org-sweep/drafts/out-ossdev-{commit-ci,review-branch-release}.md`（28 条带完整证据链与边界）。
- 诚实标注：TDesign「周更」节奏是外部给定前提，语料内仅强治理指标可证（空 body 9.9% / CC 94%），规则 §5 未收录该节奏为实证。
- commit 样本 4 仓 × 100 条，未覆盖 tdesign/wujie 等前端仓的 commit 形态（后续可扩）。

