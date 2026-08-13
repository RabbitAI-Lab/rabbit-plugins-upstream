## Description:

GroqCloud lets agents work with GroqCloud through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect GroqCloud models and run chat, transcription, and translation actions through an OOMOL-connected GroqCloud account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat, transcription, and translation actions may send prompts, audio, URLs, or files to the connector service and GroqCloud.

Mitigation: Review the action schema and exact payload with the user before running write actions.

Risk: The skill operates through the user's OOMOL-connected GroqCloud account.

Mitigation: Install it only when agents should use that connected account, and rely on the documented confirmation flow for actions that send or change data.

## Reference(s):

- [ClawHub GroqCloud Skill](https://clawhub.ai/oomol/skills/oo-groqcloud)
- [GroqCloud Homepage](https://groq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
