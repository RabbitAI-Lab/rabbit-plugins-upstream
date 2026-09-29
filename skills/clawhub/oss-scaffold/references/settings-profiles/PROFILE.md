# Tencent OSS org settings profile（penguin-oss-suite v0.2.0 / T3）

蒸馏自 `corpus/org-sweep/` 对 Tencent org 298 仓的结构层扫描。覆盖率权威数字取自 `settings-summary.json`（不改写）；语言层/目录层交叉数字由 `_tools/repo-index.tsv`（295 个非 holdout 仓的程序化索引）复算得出；CI 骨架形态取自 15 个含 workflow 正文的仓共 127 份 workflow 正文。细读抽样 27 仓（星序头部 + 7 语言覆盖）：WeKnora, ncnn, puerts, TNN, MMKV, Tendis, wepy, cherry-markdown, xLua, Shadow, TencentKona-8, Firestorm, BrowserSkill, teamai-cli, tmagic-editor, tdesign-vue-next, AI-Infra-Guard, PocketFlow, CodeAnalysis, libpag, tdesign, tdesign-miniprogram, QMUI_iOS, vap, tquic, YOLO-Master, secguide。

holdout 三仓（Hippy / wujie / spring-cloud-tencent）未参与本文件任何统计，仅用于 HOLDOUT-CHECK.md 判据比对。

## 1. org 级组件基线（298 仓，summary 原数）

| 组件 | 覆盖 | 比例 | 代表仓（非 holdout，星序） |
|---|---|---|---|
| CONTRIBUTING | 93/298 | 31.2% | tinker, QMUI_Android, ncnn, MMKV, wepy, Shadow, AI-Infra-Guard, tdesign-vue-next, TencentKona-8 |
| CI（.github/workflows 有内容） | 83/298 | 27.9% | WeKnora, ncnn, wepy, MMKV, xLua, Shadow, BrowserSkill, AI-Infra-Guard, puerts, cherry-markdown |
| issue 模板 | 61/298 | 20.5% | ncnn, MMKV, vConsole, puerts, TNN, tdesign 系, tinker, QMUI_Android, QMUI_iOS |
| SECURITY.md | 22/298 | 7.4% | WeKnora, MMKV, AI-Infra-Guard, cherry-markdown, cloudbase-framework, tquic, TencentKona 全系(5), openclaw |
| CODEOWNERS | 13/298 | 4.4% | tdesign 系(vue-next/vue/react/mobile-vue/mobile-react/miniprogram), openclaw, clawhub, setup-tencent-kona, ray, kuberay, BlazerML-tvm |
| PR 模板（has 口径） | 3/298 | 1.0% | YOLO-Master, Firestorm, Femas |
| FUNDING.yml | 1/298 | 0.3% | MMKV |

## 2. CI 骨架形态（127 份有正文的 workflow 统计）

正文来源 15 仓：WeKnora, ncnn, wepy, xLua, Shadow, BrowserSkill, AI-Infra-Guard, puerts, libpag, teamai-cli, tmagic-editor, cherry-markdown, TNN, tdesign, Tendis。

**触发器**：`push` 78/127（61%）与 `pull_request` 74/127（58%）双触发是主流形态；其中带 `paths` 过滤 58/127（46%），是头部 C++/Go 仓（ncnn 全系、WeKnora）的显著习惯，配 `!negate` 排除（ncnn windows.yml）。`workflow_dispatch` 29/127（23%）常留给发布/手动流；`schedule` 仅 4 份（ncnn CodeQL 周扫、tdesign 定时任务）。

**并发与权限**：`concurrency` + `cancel-in-progress` 65/127 与 64/127（约半数），写法固定为 `group: <wf名>-${{ github.ref }}`。显式 `permissions` 81/127（64%），其中最小权限 `contents: read` 71/127（56%）——这是 org 内最值得复用的硬惯例（ncnn、WeKnora、cherry-markdown、BrowserSkill 全系遵守）。

**矩阵**：`strategy.matrix` 25/127（20%），集中在 TS/Python/Go 的多版本矩阵（teamai-cli node 20/22/24 × ubuntu/macos；WeKnora mcp-server python 3.10–3.13；WeKnora cli 三平台 go）。C++ 仓不用矩阵，改用「每平台一个 workflow 文件」拆分（ncnn 45 个文件按 os/arch 拆，TNN 6 个、android/ios/linux-x86/macos 各一），并配 `fail-fast: false`（16 处）。

**Runner**：`ubuntu-latest` 89/127（70%）为默认；Windows/macOS 只出现在跨端 C++ 仓（ncnn windows*/mac*、libpag macos）；self-hosted 11 处（ncnn `[self-hosted, linux, centos]` 跑 riscv 模拟）。

**发布流三形态**：
1. `push: tags` → 构建 → `upload-artifact` → GitHub Release（softprops/action-gh-release 5 处、ncipollo/create-release 3 处）：ncnn、wepy、AI-Infra-Guard、BrowserSkill；
2. `release: published` 事件 → maven/gradle publish（Shadow release.yml）；
3. `workflow_dispatch` + tag 输入手动发布（xLua publish.yml、puerts unity_publish.yml）。
tag 触发共 13/127（10%）。

**checkout 版本代际**：v7 47 / v6 30 / v4 14 并存——v7 集中在 ncnn 与 tdesign 系，v6 在 WeKnora/cherry-markdown/BrowserSkill，v4 在 Shadow/puerts/teamai-cli/libpag/AI-Infra-Guard。新仓从 v6/v7 起步即可。

**两个 CI 家族**（workflow 名词频证据）：
- 传统 CI 族：`ci.yml`(11) `build.yml`(6) `test.yml`(8) `release.yml`(10) `publish.yml`(8) `unittest.yml`(4) `codeql-analysis.yml`(3) `build-{linux,windows,macos,cross-compile}.yml`——构建/测试/发布主线。
- TDesignOteam 社区机器人族（tdesign 系 + openclaw 系 + cherry-markdown）：`pull-request.yml`(13) `preview-publish.yml`(12) `issue-welcome.yml`(11) `issue-help-wanted.yml`(11) `issue-mark-duplicate.yml`(11) `pr-spelling.template.yml`(11) `auto-release.yml`(10) `issue-shoot.yml`(10) `issue-need-reproduce.yml`(10) `pkg-pr-new.yml`(9) `pr-comment-ci.yml`(7) `pr-compressed-size.yml`(7)，通过 `uses: TDesignOteam/workflows/.github/workflows/reusable-*.yml@main` 复用，且普遍带 `if: github.repository == 'Tencent/xxx'` 主仓守卫（tdesign 8 处）。另有腾讯特色 `sync-to-cnb.yml` / `sync-cnb.yml` 镜像同步流（tdesign、cherry-markdown）。

## 3. 模板惯例

**issue 模板**（61/298 = 20.5%）：目录形态为主——`ISSUE_TEMPLATE/` 目录在 295 非 holdout 仓出现 58 次（与 has 口径 61 一致量级），单文件 `ISSUE_TEMPLATE.md` 形态仅 wepy 等少数。tdesign 系在目录里另放 `issue-shoot.md`（机器人联动）。模板文件正文本次扫描未抓取，骨架按 GitHub 标准 forms 形态给出（见 ISSUE_TEMPLATE/）。

**PR 模板——双口径必须分开**：summary 的 has 口径仅 3/298（1.0%：YOLO-Master, Firestorm, Femas），但目录级实测 `.github/pull_request_template.md` / `PULL_REQUEST_TEMPLATE.md` 存在于 39/295（13.2%）个非 holdout 仓（WeKnora、wepy、AI-Infra-Guard、teamai-cli、tdesign 全系、cherry-markdown 等）。两个口径都低于 20% 建骨架阈值，本版不建 PR 模板骨架；蒸 profile 时按「issue 模板必有、PR 模板约 1/8 仓有」记录。

## 4. 安全文件与 CODEOWNERS

SECURITY.md 22/298（7.4%），分布高度家族化：TencentKona 系列 5 仓全有（Java JDK 线），tdesign/openclaw 新式 TS 仓、AI 安全类仓（AI-Infra-Guard、AICGSecEval）、基础设施仓（ray、tencent-goosefs-rust-sdk）是主力；55 个 C++ 仓里只有 MMKV 1 个。CODEOWNERS 13/298（4.4%），12 个非 holdout 全部是 tdesign 家族或 openclaw/clawhub 系 + 镜像仓（ray/kuberay）——即 CODEOWNERS 是「TDesignOteam 治理模式」的组件，不是 org 通用组件。两者覆盖率均 <20%，不建骨架。

## 5. metadata 惯例（295 非 holdout 仓实测）

- **license**：`NOASSERTION`（自定义/非标文本 license）225/295（76.3%），API 无 license 字段 28/295，MIT 19、Apache-2.0 13、BSD-3-Clause 4、GPL-2.0 3、AGPL-3.0 1、GPL-3.0 1、MIT-0 1。腾讯开源仓以「LICENSE.txt 非标文本」为主体（ncnn/MMKV/xLua 均为 LICENSE.TXT），新式 TS 仓（tdesign 系、BrowserSkill）用 MIT。
- **topics**：182/295（61.7%）零 topics；113 仓有 topics 且头部集中——WeKnora 20 个、ncnn 20 个、AI-Infra-Guard 20 个、MMKV 15 个；产品家族仓（tdesign 系）稳定 4–6 个。topics 是头部大仓行为，长尾基本不用。
- **has_discussions**：39/295（13.2%）。开启名单头部化：WeKnora、ncnn、MMKV、omi、Shadow、QMUI_iOS、puerts、libpag、cherry-markdown、tdesign 系、TencentKona 系——约 2/3 的开启仓在星序前 100。
- **has_wiki**：263/295（89.2%）——GitHub 默认开启，无区分信号；ncnn 专门用 `sync-wiki.yml` 同步 wiki，说明 wiki 有实际使用。
- **根目录文件**：CHANGELOG 64/295（21.7%）、CITATION.cff 9/295（3.1%，学术仓 ncnn/YOLO-Master/MimicMotion 等）。`README_CN` / `README.zh_CN` 双语 README 是常态（ncnn、wepy、MMKV、libpag、AI-Infra-Guard、TNN 等）。

## 6. 分语言组件率（has 口径，非 holdout 295 仓）

| 语言 | n | ci | issue 模板 | contributing | security | codeowners |
|---|---|---|---|---|---|---|
| Python | 100 | 15% | 8% | 24% | 4 | 1 |
| C++ | 55 | 15 (27.3%) | 8 (14.5%) | 13 (23.6%) | 1 | 0 |
| TypeScript | 27 | 20 (74.1%) | 16 (59.3%) | 14 (51.9%) | 4 | 8 |
| Java | 23 | 10 (43.5%) | 2 (8.7%) | 15 (65.2%) | 7 | 0 |
| JavaScript | 17 | 5 (29.4%) | 7 (41.2%) | 5 (29.4%) | 2 | 0 |
| Go | 10 | 2 (20%) | 1 | 1 | 1 | 0 |
| Objective-C | 8 | 0 | 2 | 3 | 0 | 0 |
| C | 5 | 1 | 2 | 3 | 0 | 0 |
| Vue | 5 | 4 (80%) | 4 (80%) | 2 | 0 | 1 |

stars≥1000 子群条件率：C++(n=25) ci 36%/issue 28%/contributing 32%；TypeScript(n=9) ci 78%/issue 67%/contributing 44%；Java(n=10) contributing 60%/ci 20%/issue 20%；Python(n=16) contributing 50%/ci 25%。

读法：TypeScript（tdesign/openclaw 家族）是治理最全的语言；Java 的 CONTRIBUTING 是最强惯例（65%）而 issue 模板几乎不装；Objective-C 仓零 CI；Python 长尾仓多（100 仓）摊薄所有率。

## 7. 预测规则（供 HOLDOUT-CHECK.md 使用，先于读 holdout 数据固定）

对任一语言为 L、stars≥1000 的仓，预测其「应有」组件集合 = 以下三层并集：

1. **语言强惯例**：lang_rate(comp, L) ≥ 40%；
2. **org 惯例且语言不反常**：org_rate(comp) ≥ 20% 且 lang_rate(comp, L) ≥ 15%；
3. **大仓子群惯例**：rate(comp | L, stars≥1000) ≥ 25%。

组件域限定 7 类：issue_template / pr_template / security_md / codeowners / contributing / funding / ci。预测只输出集合，不含形态。

按此规则推导（数字见 §1 §6）：C++ → {ci, contributing, issue_template}（层3 大仓率 36/32/28%）；TypeScript → {ci, issue_template, contributing}（层1 全过）；Java → {ci, contributing}（issue 语言率 8.7%、大仓率 20% 均不达）。

## 8. 管理面：不可公开观测清单

扫描对全部 295 非 holdout 仓统一标记 4 项 `not_publicly_observable`：`branch_protection`（分支保护规则）、`required_reviews`（必需评审人数）、`secret_scanning`（密钥扫描开启状态）、`code_scanning_alerts`（代码扫描告警）。这四项是 org 管理面配置，公开 API 不可断言，本 profile 对它们不产出任何惯例结论；oss-scaffold 对新建仓只负责文件层（本 profile 的骨架），管理面需在 GitHub 仓库 Settings 手工配置。

## 9. 骨架文件清单（本目录）

| 文件 | 依据 |
|---|---|
| ci/ci-cpp.yml | ncnn（paths 过滤/concurrency/contents:read/cmake+ctest/多平台拆分）+ Tendis（lint→build needs 链）+ ncnn/TNN tag 发布 |
| ci/ci-typescript.yml | teamai-cli（matrix node×os/npm ci/vitest/coverage/build needs）+ cherry-markdown（timeout/最小权限） |
| ci/ci-java.yml | Shadow（commitlint+gradle+setup-java temurin+release→publish） |
| ci/ci-python.yml | WeKnora mcp-server（matrix python/contents:read/build 非 PR/PyPI OIDC） |
| ci/ci-go.yml | WeKnora cli（paths/shell bash/matrix os/setup-go cache/vet/coverage）+ go-lint |
| ci/ci-vue.yml | tdesign 家族（pnpm/主仓守卫/PR 触发构建/词频 preview-pkg 模式） |
| ISSUE_TEMPLATE/bug_report.md, feature_request.md | 覆盖率 61/298 = 20.5% ≥ 20%；目录形态 58/295 |
| CONTRIBUTING.md | 覆盖率 93/298 = 31.2% ≥ 20% |

**不建骨架并说明**（阈值 20%）：PR 模板——has 口径 3/298（1.0%），目录口径 39/295（13.2%），双口径均 <20%；SECURITY.md——22/298（7.4%），且家族化分布（Kona 系/tdesign 系）无 org 通用性；CODEOWNERS——13/298（4.4%），12/13 为 TDesignOteam 治理模式组件；FUNDING.yml——1/298（0.3%）。Objective-C 无 CI 骨架——该语言 8 仓 ci=0，无实测形态可蒸。

复算脚本与索引：`_tools/`（build-index.ps1 → repo-index.tsv；stats2–4.ps1；wf-fingerprint.ps1）。

