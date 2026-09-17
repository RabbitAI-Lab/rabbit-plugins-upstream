## Description:

Operates SiteSpeakAI through the OOMOL oo CLI to inspect action schemas, read account and chatbot data, query chatbots, and manage updated answers with confirmation for write or destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected SiteSpeakAI account from an agent, including retrieving chatbot settings, conversations, leads, sources, suggested messages, and updated answers. It also supports querying chatbots and creating, updating, or deleting chatbot updated answers after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve sensitive SiteSpeakAI account data, including conversations, leads, account details, and broad chatbot data.

Mitigation: Confirm scope before broad reads and request only the minimum account or chatbot data needed.

Risk: The first-time setup guidance includes one-line remote installer commands for the oo CLI.

Mitigation: Use safer manual installation, verify the installer or package source, and install the CLI only from an expected OOMOL source.

Risk: Write or destructive actions can change or delete SiteSpeakAI updated answers.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and effect before running write or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sitespeakai)
- [SiteSpeakAI Homepage](https://sitespeak.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON payloads, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
