## Description:

CSV转JSON工具 helps agents convert CSV input into JSON object arrays using Expanso Edge CLI or tool-protocol workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, independent builders, enterprise teams, and automation workflow users can use this skill to convert CSV content into structured JSON and integrate the result into API, data-sync, or workflow automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, and execution authority while its CSV conversion purpose is narrow.

Mitigation: Install only in a constrained agent profile and permit execution or file writes only for explicit CSV-to-JSON tasks in trusted working directories.

Risk: The source text describes broad API, command, and automation behavior that could activate outside CSV conversion.

Mitigation: Limit invocation triggers and user prompts to CSV-to-JSON conversion, and review planned commands or file writes before allowing them.

Risk: CSV inputs and JSON outputs may contain sensitive business data.

Mitigation: Use trusted inputs, avoid unnecessary logging, and review output handling before storing or sharing converted JSON.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/expanso-csv-to-json)
- [SkillHub homepage reference](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected agent output centers on CSV-to-JSON conversion guidance and JSON object-array results; the source also describes execution logs and status fields.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
