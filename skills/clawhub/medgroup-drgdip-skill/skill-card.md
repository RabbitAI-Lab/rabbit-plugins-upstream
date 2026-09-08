## Description:

使用已在 OpenClaw 本机连接的 MedGroup MCP，查询 DRG/DIP 城市与规则、检索 ICD 编码、执行分组和结算测算、查询 CC/MCC。适用于医保分组、编码与规则核对；结果用于专业辅助。

This skill is ready for commercial/non-commercial use.

## Publisher:

[u201013903](https://clawhub.ai/user/u201013903)

### License/Terms of Use:

MIT-0

## Use Case:

External healthcare coding, billing, and operations users use this skill to query DRG/DIP city rules, search ICD codes, perform grouping checks, estimate settlement scenarios, and review CC/MCC status with MedGroup MCP results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MedGroup credentials could be exposed if entered into chat or saved in shared artifacts.

Mitigation: Configure the MedGroup key only in local MCP settings and do not paste keys into conversations, repositories, screenshots, or skill files.

Risk: Patient identifiers or sensitive health details could be shared unnecessarily during coding and settlement checks.

Mitigation: Use synthetic or de-identified data and avoid names, ID numbers, contact details, admission identifiers, and other direct identifiers.

Risk: DRG/DIP grouping or settlement results may be mistaken for final official determinations.

Mitigation: Treat outputs as professional assistance and scenario estimates; rely on clinical coding review, payer audit, and local official documents for final decisions.

## Reference(s):

- [MedGroup homepage](https://medgroup.medchat.fun)
- [ClawHub skill page](https://clawhub.ai/u201013903/skills/medgroup-drgdip-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tool-result summaries, parameter follow-up questions, and concise configuration or command guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a locally configured MedGroup MCP connection; settlement outputs are scenario estimates rather than official payment determinations.]

## Skill Version(s):

1.1.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
