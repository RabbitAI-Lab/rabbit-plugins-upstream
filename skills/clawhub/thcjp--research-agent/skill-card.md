## Description:

Conducts open-ended research on a topic, builds a living Markdown document, and supports interactive research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and automation users can use this skill to conduct open-ended topic research, process supporting files, and produce Markdown or structured research outputs. It is suited to general research and documentation workflows where broad agent permissions are reviewed before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request broad research, file handling, API, SEO, and shell-command authority across unclear or mixed use cases.

Mitigation: Review each run carefully and require explicit confirmation before the agent writes files, calls external services, or runs commands.

Risk: Research and file-handling workflows may expose sensitive files or credentials if the agent is given broad access.

Mitigation: Avoid providing sensitive files, secrets, or credentials unless they are necessary for the task and approved for this skill's execution context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/research-agent)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and plain text with optional shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution logs, status summaries, processed file outputs, and research documentation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
