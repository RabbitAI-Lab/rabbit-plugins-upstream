# HOLDOUT-CHECK — settings profile 判据自检（penguin-oss-suite v0.2.0 / T3）

holdout 三仓：Hippy / wujie / spring-cloud-tencent。三仓在整个蒸馏过程（PROFILE.md、骨架文件、全部统计）中被排除；本文件在预测固定之后才首次读取它们的 JSON。

## 1. 预测规则（引用 PROFILE.md §7，先于读数固定）

预测(仓, 语言 L, stars≥1000) = 以下三层并集，组件域 = {issue_template, pr_template, security_md, codeowners, contributing, funding, ci}：

1. 语言强惯例：lang_rate(comp, L) ≥ 40%；
2. org 惯例且语言不反常：org_rate(comp) ≥ 20% 且 lang_rate(comp, L) ≥ 15%；
3. 大仓子群惯例：rate(comp | L, stars≥1000) ≥ 25%。

判据：组件类型覆盖率（预测命中 / 实际存在）≥ 70% 为过；「profile 预测有、holdout 实际无」的组件类型记虚构，虚构 >1 即不过。

## 2. 逐仓预测 → 实测

### Hippy（预测语言：C++，跨端框架）

预测推导（C++: ci 27.3% / issue 14.5% / contributing 23.6%；stars≥1000 子群 ci 36% / issue 28% / contributing 32%）：
层2 → ci, contributing；层3 → ci, issue, contributing。**预测集合 = {ci, contributing, issue_template}**。

实测（settings/Hippy.json）：language=C++（预测语言正确），stars 8563。
`has`: ci=**True**, issue_template=**True**, pr_template=False, security_md=False, codeowners=**True**, contributing=**True**, funding=False。实际存在 = {ci, issue_template, codeowners, contributing}（4 类）。github_dir 另见 CODEOWNERS、CODE_OF_CONDUCT.md、PULL_REQUEST_TEMPLATE.md；40 个 workflow。

| 指标 | 值 | 判定 |
|---|---|---|
| 命中 | ci ✓、contributing ✓、issue_template ✓ = 3 | — |
| 覆盖率 | 3/4 = **75%** | ≥70% **过** |
| 虚构 | 0（codeowners 漏报属 miss，非虚构） | ≤1 **过** |

**结论：过**。miss = codeowners：C++ 非 holdout 仓 codeowners 0/55，Hippy 是该语言唯一异类，语言层无法预测。

### wujie（预测语言：TypeScript，微前端框架）

预测推导（TS: ci 74.1% / issue 59.3% / contributing 51.9%，层1 全过）：**预测集合 = {ci, issue_template, contributing}**。

实测（settings/wujie.json）：language=TypeScript（正确），stars 5048。
`has`: ci=**True**, issue_template=**True**, contributing=**True**，其余 False。实际存在 = {ci, issue_template, contributing}（3 类）。github_dir 另见 pull_request_template.md（has 口径未计入）；workflow 2 个（main.yml、pr-test.yml）。

| 指标 | 值 | 判定 |
|---|---|---|
| 命中 | 3/3 | — |
| 覆盖率 | 3/3 = **100%** | **过** |
| 虚构 | 0 | **过** |

**结论：过**。

### spring-cloud-tencent（预测语言：Java，Spring Cloud 微服务套件）

预测推导（Java: contributing 65.2% / ci 43.5% / issue 8.7%；stars≥1000 子群 contributing 60% / ci 20% / issue 20%）：层1 → contributing；层2 → contributing, ci；层3 → contributing。**预测集合 = {ci, contributing}**。

实测（settings/spring-cloud-tencent.json）：language=Java（正确），stars 3297。
`has`: ci=**True**, issue_template=**True**, contributing=**True**，其余 False。实际存在 = {ci, issue_template, contributing}（3 类）。github_dir 另见 PULL_REQUEST_TEMPLATE.md；workflow 4 个（junit.yml、license-checker.yml、release.yml、snapshot.yml）。

| 指标 | 值 | 判定 |
|---|---|---|
| 命中 | ci ✓、contributing ✓ = 2 | — |
| 覆盖率 | 2/3 = **66.7%** | <70% **不过** |
| 虚构 | 0 | **过** |

**结论：不过（覆盖率）**。miss = issue_template：Java 非 holdout 仓 issue 模板仅 2/23（8.7%），语言层证据明确指向「不装」，而本仓实装——spring-cloud-tencent 是 ASF 孵化项目，治理套件高于 org 平均，属语言分布外的特例。

## 3. 汇总

| 仓 | 语言 | 实际存在 | 预测 | 覆盖率 | 虚构 | 判定 |
|---|---|---|---|---|---|---|
| Hippy | C++ | 4 | 3 | 75% | 0 | 过 |
| wujie | TypeScript | 3 | 3 | 100% | 0 | 过 |
| spring-cloud-tencent | Java | 3 | 2 | 66.7% | 0 | 不过 |
| **合计** | — | 10 | 8 | **80% (8/10)** | **0** | 3 仓 2 过 |

- 组件类型覆盖率合计 8/10 = 80% ≥ 70%（按逐仓口径则 2/3 过）。
- **虚构总数 0**（≤1）。
- 两个 miss 均为「实际有、预测无」：codeowners（Hippy，C++ 语言 0/55 的异类）、issue_template（spring-cloud-tencent，Java 语言 8.7% 的少数派）。无一起因于 profile 凭空预测。

## 4. 判据外的口径发现（影响 PROFILE.md §3，已在该节记录）

三仓 github_dir 全部实际存在 `PULL_REQUEST_TEMPLATE.md`（Hippy 大写、wujie/spring-cloud-tencent 小写），但三者 `has.pr_template` 均为 False——与 org 级发现一致：has.pr_template 口径（3/298）系统性漏报目录级 PR 模板（非 holdout 实测 39/295）。使用 summary 的 pr_template 数字时须按「下界」理解。

Hippy 另呈现第三种 CI 家族形态：40 个 workflow 中 `gh_pr_*` / `gh_issue_*` / `gh_licence_checks` / `security_codeql_analyses` 自建机器人族（不同于 PROFILE.md §2 已归纳的传统 CI 族与 TDesignOteam 复用族），因属 holdout 未计入 PROFILE 统计，记录备查。

