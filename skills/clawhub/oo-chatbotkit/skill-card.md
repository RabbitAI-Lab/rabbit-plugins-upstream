## Description:

ChatBotKit lets an agent operate ChatBotKit through an OOMOL-connected CLI for reading, creating, and updating bots, conversations, messages, datasets, files, and account usage data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage ChatBotKit resources through an OOMOL-connected account, including bots, conversations, messages, datasets, records, files, and usage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands pipe downloaded scripts directly into a shell.

Mitigation: Review installation steps before use and prefer an official, verifiable installation method for the OOMOL CLI.

Risk: Dataset attachment and detachment actions can change ChatBotKit state even though the artifact does not mark them as write actions.

Mitigation: Require explicit user confirmation before attaching or detaching files from ChatBotKit datasets.

Risk: The authoritative security verdict is suspicious.

Mitigation: Review and scan the skill before deployment, with particular attention to installation commands and state-changing dataset actions.

## Reference(s):

- [ChatBotKit skill page](https://clawhub.ai/oomol/skills/oo-chatbotkit)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [ChatBotKit homepage](https://chatbotkit.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live action schemas before running ChatBotKit connector actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
