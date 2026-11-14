## Description:

以新玩家视角盲玩游戏构建，核对目标运行环境中的完整通关体验，并记录诊断与验收证据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

游戏开发者与 QA 人员可用此技能从首次游玩者的视角检查引导、交互、节奏、窄屏体验和存档恢复，再依据设计规范完成运行验收并整理问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because some paths referenced in the instructions were not present in the bundle.

Mitigation: Check the missing referenced paths and review the complete release bundle before deployment.

## Reference(s):

- [Blind playtest method](artifact/references/blind-playtest-method.md)
- [Runtime QA contract](artifact/references/qa-contract.md)
- [Game QA on ClawHub](https://clawhub.ai/worldwonderer/skills/game-qa)
- [Publisher profile](https://clawhub.ai/user/worldwonderer)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Screenshots]

**Output Format:** [Markdown playtest report and JSON verification record, with supporting screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records observed findings, complete-run evidence, and untested limitations.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
