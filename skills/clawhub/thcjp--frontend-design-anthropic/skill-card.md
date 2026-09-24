## Description:

前端设计-专业版 helps agents produce frontend design systems, component-library guidance, responsive UI code, accessibility checks, and performance review suggestions for product teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and product teams use this skill to generate or review frontend design-system assets, component-library patterns, responsive layouts, and accessibility improvements for commercial product work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to execute commands or write files without tightly scoped paths.

Mitigation: Use it only in a project workspace where frontend file generation or modification is intended, and inspect command arguments and output paths before execution.

Risk: The skill may involve license or API values during setup.

Mitigation: Keep license and API values in environment variables and avoid entering unrelated API keys or broad credentials.

Risk: The security scan verdict is suspicious because command execution, workspace writes, network/API use, and credentials are not fully scoped.

Mitigation: Review the skill before installing and limit use to expected frontend design-system and component-generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/frontend-design-anthropic)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell command examples, configuration notes, and JSON-style output contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to read, write, or execute commands in a frontend project workspace.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
