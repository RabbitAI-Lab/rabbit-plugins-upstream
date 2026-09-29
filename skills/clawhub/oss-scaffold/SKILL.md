---
name: oss-scaffold
description: 从 0 搭建 GitHub 仓库全部组件的脚手架（腾讯三标杆仓规格）。输入项目名 + 一句话定位，一次性生成 README（三档形态）+ CHANGELOG + CONTRIBUTING + LICENSE + .github 模板 + CI 骨架 + docs 骨架 + .gitignore，并完成本地 git init/commit；推送 GitHub 前强制 R14 放行。文档风格引用 oss-voice，维护者语气引用 oss-persona，文档站调用 vitepress skill。触发词（能力词，场景词「建仓」让渡给 oss-workflow）：脚手架生成、从 0 生成组件、初始化组件、scaffold。
metadata:
  openclaw:
    requires:
      bins: [git, gh, python, node]
---

## §0 场景闸门

本 skill 是被调度成员，不是场景入口。若当前任务会写 GitHub（提 PR / 评论 issue / commit / push / 建仓）且 .oss-task/ 下无 CHECKLIST.md：**先停下**，加载 routing/oss-workflow 按 §1 识别场景并实例化清单，再继续执行本 skill 对应步骤。无清单裸奔 = 违规交付（#752 实战：T1 裸奔 320s 被作者中止，61% 时间损耗）。运行时另有 penguin-guard 硬闸（PreToolUse）拦截无清单的 gh/git push 类命令。

# oss-scaffold：从 0 建仓脚手架（三标杆仓规格）

## 0. 定位与依赖

一句话输入（项目名 + 一句话定位）→ 产出全组件仓库，本地 git 就绪。规格书 = 三仓共性提取（调研 5.5）。

| 依赖 | 用途 | 缺失时 |
|---|---|---|
| `oss-voice` | README/CHANGELOG/docs 的风格规则（§1 语言、§2 三档、§3 参数、§6 反模式） | 按 D1 用 `skills-link -Source` 补链安装或硬停 |
| `oss-persona` | README/CONTRIBUTING 中「维护者声音」段落的语气（§2 语气参数 + §3 引用接口） | 同上 |
| `vitepress` skill | 项目需要文档站时调用（D15），仅重档/明确要求时 | 未安装 → 硬停（零降级） |
| `humanizer` + `zh-tech-writing` | 产出的中文文档定稿必过（oss-voice §0 流水线） | 同上 |

## 1. 组件清单（默认全生成）

| # | 组件 | 路径 | 说明 |
|---|---|---|---|
| 1 | README | `README.md`（+ `README.zh-CN.md` 或多语） | 三档之一，默认中档（D14） |
| 2 | CHANGELOG | `CHANGELOG.md` | Keep a Changelog 骨架 + 首条记录 |
| 3 | CONTRIBUTING | `CONTRIBUTING.md` | 分支约定 + Conventional Commits + 验证命令 |
| 4 | LICENSE | `LICENSE` | MIT 默认；其他许可证先问用户 |
| 5 | Issue 模板 | `.github/ISSUE_TEMPLATE/bug_report.md` + `feature_request.md` | 骨架在 `references/templates/issue_template.md`（二合一，实例化时拆两文件） |
| 6 | PR 模板 | `.github/PULL_REQUEST_TEMPLATE.md` | 骨架在 `references/templates/pull_request_template.md` |
| 7 | CI 骨架 | `.github/workflows/ci.yml` | 按语言取 `references/settings-profiles/ci/ci-<lang>.yml`（cpp/typescript/java/python/go/vue 六型，298 仓实测形态蒸馏，惯例与证据见 `settings-profiles/PROFILE.md`）；最简 lint+test 占位，YAML 语法自足可跑 |
| 8 | docs 骨架 | `docs/` | index.md + 按档位拆分；文档站走 vitepress |
| 9 | .gitignore | `.gitignore` | 按语言选骨架：`references/templates/gitignore-node.md` / `references/templates/gitignore-python.md` / `references/templates/gitignore-go.md` |
| 10 | CHANGELOG 骨架 | — | `references/templates/changelog.md` |
| 11 | CONTRIBUTING 骨架 | — | `references/templates/contributing.md` |

## 2. 生成流程

```
P1 输入判定 → P2 档位判定 → P3 依赖自检 → P4 文件生成 → P5 本地 git → P6 推送门禁
```

- **P1 输入判定**：必备 = 项目名（`{{project_name}}`）+ 一句话定位（`{{one_liner}}`）。缺则问用户，一次问全。项目名与目标目录下已有同名目录/远端仓库冲突 → 走 §4-F1。
- **P2 档位判定**（D14）：

| 档 | 判定条件 | 样板 | 模板 |
|---|---|---|---|
| 重 | 平台型/多组件/需要独立文档站 | WeKnora | `references/templates/readme-heavy.md` |
| 中（默认） | 服务/组件/库 | Agent-Memory | `references/templates/readme-medium.md` |
| 轻 | CLI 工具/单一可执行 | teamai-cli | `references/templates/readme-light.md` |

  用户一句话可覆盖（「用轻档」「做成落地页」）；无表达时按定位关键词判定（平台→重，服务/SDK/库→中，CLI/命令行→轻），判不出默认中档。
- **P3 依赖自检**：按 §0 表逐项 probe DSH 技能体系在位性（看会话技能清单，或跑 `skills-doctor`）；缺失按 D1 处理。需要文档站（重档或用户明说）而 vitepress 缺失 → §4-F3。
- **P4 文件生成**：按 §1 清单逐个实例化模板（`references/templates/` 与 `references/settings-profiles/`——CI 按语言选型、issue 模板与 CONTRIBUTING 骨架取自 org 实测惯例），占位符 `{{project_name}}` / `{{one_liner}}` / `{{year}}` / `{{repo_owner}}` 全局替换；风格细则按 oss-voice §2–§8 执行（模板只给骨架，不复制风格规则）；「维护者声音」段落（README 的 Contributing 语气、CONTRIBUTING 的回应承诺）按 oss-persona §2 直接风格执行。中文产出定稿前过 humanizer + zh-tech-writing（oss-voice §0 流水线）。
- **P5 本地 git**：`git init` + `git add -A` + 首次 commit（`chore: init {{project_name}}`）自动完成，无需放行（D2）。
- **P6 推送门禁**（R14，同 oss-contribution 口径）：

```
gh repo create {{repo_owner}}/{{project_name}} --public --source . --push
```

  执行前必须把「将创建公开仓库 + 完整命令」呈给用户并拿到**放行原句**（如「推送」「创建并推送」）才算放行；「嗯」「继续」「好」等模糊表述 = 未放行。未放行 → 停在**本地就绪**状态：交付文件清单 + git log 首条 + 待执行命令，状态记 `PARTIAL`。不轮询、不超时自动放行、不把沉默当许可。

## 3. 语言规则

按 oss-voice §1：语言跟随目标受众。开源协作主语言是英文（三仓 PR 实测 97% 英文），故默认 `README.md` 英文 + `README.zh-CN.md` 中文对照；**用户明说中文时中文优先**（README.md 中文，问是否补英文版）；面向国内社区（微信群/公众号入口）→ 中文主 README。双语文件两边内容对齐，不是机器互译。

## 4. 失败分支（零降级）

| # | 场景 | 处置 |
|---|---|---|
| F1 | 目标目录已存在同名项目 / `gh repo view` 显示远端已占用该名 | 停止生成，列出冲突路径/远端，请用户改名或换目录；不覆盖任何已有文件 |
| F2 | 问语言/许可证/档位后用户不答 | 用默认值（中文优先级按 §3、MIT、中档）继续并在交付汇报中标注「默认值待确认」，不算失败 |
| F3 | vitepress skill 缺失或补装失败 | 硬停（D1+D15）：报告缺失项 + 官方来源，不生成降级版 docs 站、不手工替代 |
| F4 | 模板实例化后 `git init` 失败（权限/已非空 git 仓库） | 不覆盖已有 `.git/`；若目录已有仓库则跳过 init 只追加文件，commit 前列 diff 给用户确认 |
| F5 | `gh` 未安装或未认证 | 停在本地就绪，给出 `gh auth login` 指引；P6 不放行 |

## 5. 交付汇报（每次运行结束必给）

- 文件清单（路径 × 行数）+ 档位判定结论及依据
- 语言/许可证选择及是否默认值
- git 状态（首条 commit hash）与推送状态（已放行推送 / 本地就绪待放行）
- 待用户确认项（若有）

## 6. 边界

- 只管从 0 建仓；已有仓库的文档维护走 `oss-voice`，PR/Issue 流程走 `oss-contribution`，场景编排走 `oss-workflow`。
- 不复制 oss-voice/oss-persona 的规则内容，只引用条目号（如「按 oss-voice §2 三档结构」）。
- CI 只给最简骨架（lint+test 占位），不替用户选测试框架；占位命令必须是无依赖也能语法正确的形式。


