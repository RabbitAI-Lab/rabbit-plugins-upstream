## Description:

图解 helps agents generate Mermaid, PlantUML, or ASCII diagrams from descriptions for architecture, flow, and sequence use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and team contributors use this skill to turn written system, process, or interaction descriptions into diagram source text for architecture diagrams, flowcharts, and sequence diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad file and command authority beyond diagram generation.

Mitigation: Use the skill for explicit diagram requests, restrict filesystem and shell access, and review any proposed command before execution.

Risk: Diagram descriptions or generated diagrams may expose sensitive system details or credentials.

Mitigation: Remove secrets and confidential details from prompts and review generated diagrams before sharing or publishing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/diagram)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Mermaid, PlantUML, ASCII, JSON examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagram source text and optional rendering or export commands; review generated commands before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
