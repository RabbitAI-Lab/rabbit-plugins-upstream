# Personal Skill Builder · 个人技能工坊

**作者：FueTsui · 首个公开版本：1.0.0 · [MIT No Attribution (MIT-0)](LICENSE)**

通过一问一答，把个人经验、材料和重复工作整理成可复用的 SKILL。向导吸收你主动补充的信息，动态查漏；信息足够就制作，并用实际证据核对结果。

## 开始使用

将本仓库复制为 `personal-skill-builder` 目录，放入支持 SKILL.md 的工具所使用的技能目录，保留相对资源路径。例如 Codex 的 `~/.codex/skills/personal-skill-builder`。也可以让 AI 显式读取本目录的 [SKILL.md](SKILL.md)。

> 使用 $personal-skill-builder，帮我创建个人技能。每次只问一个关键问题，吸收我主动补充的要求，信息足够就生成并验证。

已有技能时可以说：

> 使用 $personal-skill-builder，依据我的新材料升级这个技能，保留仍有效的要求，并检查受影响的场景。

## 工作方式

- 每轮只解决一个决策问题，不要求填写问卷；可以自由回答、“不知道”或“先给建议”。
- 已知信息直接采用；确定推导注明依据；低风险可逆默认可直接应用，重要事实和个人规则不猜。
- 支持开放领域和多种能力组合，不限定行业或流程分支数量。
- 采用用户最新明确要求；恢复旧会话时重算待答问题，避免重复询问。
- 交付可复用技能及必要资源，区分结构检查、真实任务验证和宿主自动触发。

文本向导可由支持技能的 AI 使用。可选本地检查工具使用 Python 3.10+ 标准库。

## 本地验证

先创建技能目录之外的 personal-skill-builder-checks 输出目录，再在仓库根目录运行：

```text
python scripts/toolkit.py audit . --output ../personal-skill-builder-checks/audit.json
python scripts/toolkit.py plan assets/experiment-suite.json --skill . --output ../personal-skill-builder-checks/run.json --rounds 2 --variants candidate
python scripts/toolkit.py evaluate ../personal-skill-builder-checks/run.json --output ../personal-skill-builder-checks/evaluation.json
```

`plan` 只生成实验计划。先在独立上下文执行真实请求，保存每轮输出、实际文件和判断依据，再评估；工具不会调用模型或自动执行用户任务。完整协议见 [评估方法](references/evaluation.md) 和 [覆盖设计](references/coverage.md)。

实验集中的领域仅是合成验证样本，可依据自己的任务增删。模板记录由 AI 维护，不需要用户填写。读取失败夹具 `U13-damaged.xlsx` 被刻意制作成无效文件，用于验证诚实失败和恢复；它不是用户业务表格。实验输入只读，测试产物保存在技能目录之外。

## 目录

- `SKILL.md`：技能入口。
- `references/`：访谈、合成与评估细则。
- `assets/`：内部记录模板、实验设计和合成材料。
- `scripts/toolkit.py`：离线结构检查与实验记录评估。
- `agents/openai.yaml`：Codex 展示与启动信息。

## 验证边界与版本

一次检查通过只适用于实际验证的版本、材料与环境，不代表所有未来输入或模型都正确。自动触发、目标软件显示效果和外部操作需要各自的真实证据。

公开发行版本记录在 [VERSION](VERSION) 和 [CHANGELOG.md](CHANGELOG.md)。JSON 中的 `schema_version` 及文档中的记录格式 v1/v2 是数据协议版本，与首次公开发行的 1.0.0 无关。

Copyright © 2026 FueTsui. 本项目按 [MIT No Attribution (MIT-0)](LICENSE) 发布。
