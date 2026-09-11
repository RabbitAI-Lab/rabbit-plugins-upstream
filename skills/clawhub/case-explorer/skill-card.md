## Description:

25个实战案例智能匹配分析，对应全书案例，帮读者根据自身情况匹配最相关的案例并深度拆解成功因素。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cglt2026opc](https://clawhub.ai/user/cglt2026opc)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language readers and solo-business practitioners use this skill to match their own stage, business direction, challenges, and background against the AI超级个体 case library. The skill produces personalized case analysis, reusable action patterns, and a recommended reading order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share sensitive business or personal context while seeking case matches.

Mitigation: Keep sensitive details out of prompts where possible, or ask the agent to answer in chat only instead of writing them into a report.

Risk: The skill can write a localized Markdown report that may include user-provided details.

Mitigation: Confirm the filename and destination before file output, especially when the report contains sensitive or identifying information.

## Reference(s):

- [Bundled AI超级个体 case library](artifact/references/cases.json)
- [ClawHub skill page](https://clawhub.ai/cglt2026opc/skills/case-explorer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report or chat response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a localized Markdown case analysis report when the user requests or confirms file output.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
