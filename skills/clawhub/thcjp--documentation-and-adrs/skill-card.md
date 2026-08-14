## Description:

Helps agents record architectural decisions and generate or manage documentation and ADR outputs from supplied content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to draft, update, and structure documentation or architecture decision records when making architectural decisions, changing public APIs, or shipping features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local command execution and file-reading authority may exceed what is expected for a documentation-branded skill.

Mitigation: Use it only for explicit ADR or documentation tasks, keep command execution in a sandbox where possible, and require user confirmation before commands or file-changing actions.

Risk: Credential and API-key setup guidance could expose sensitive values if prompts or outputs are not constrained.

Mitigation: Avoid providing API keys unless clearly necessary, use least-privilege credentials, and redact secrets from prompts, generated documents, logs, and command output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/documentation-and-adrs)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON snippets, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured status or result metadata when the agent formats documentation workflow outputs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
