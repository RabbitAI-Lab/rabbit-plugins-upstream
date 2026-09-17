## Description:

ChatBotKit (chatbotkit.com) lets an agent read, create, and update ChatBotKit data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage ChatBotKit bots, conversations, messages, datasets, records, files, and usage through a connected OOMOL account. It is intended for ChatBotKit workflows that need schema inspection, validated JSON action payloads, and confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup uses remote installer commands that execute downloaded scripts.

Mitigation: Inspect or verify installer artifacts before execution and use a safer oo CLI installation path when available.

Risk: Some ChatBotKit actions can change account state without being clearly tagged as write actions.

Mitigation: Require explicit user confirmation for every state-changing action, including dataset attach and detach operations.

## Reference(s):

- [ChatBotKit homepage](https://chatbotkit.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns ChatBotKit action results as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
