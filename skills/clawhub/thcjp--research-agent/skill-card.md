## Description:

This skill supports open-ended topic research, living Markdown document creation, file processing, API-assisted workflows, and interactive automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and teams use this skill to research topics, process documents, extract content, and produce structured Markdown or JSON results within an agent workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, command execution, and API-related authority.

Mitigation: Run it in a constrained workspace and review proposed commands, file writes, and external API actions before allowing them.

Risk: Sensitive files or API keys could be exposed through broad file access or generated research outputs.

Mitigation: Avoid exposing sensitive directories or credentials to the workspace and review generated documents before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/research-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and command/configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution logs, status fields, intermediate document artifacts, and retry or skip-step parameters.]

## Skill Version(s):

1.0.1 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
