## Description:

Mistral AI helps agents operate a user's OOMOL-connected Mistral account for chat, agents, embeddings, OCR, audio transcription, moderation, files, libraries, batch jobs, and fine-tuning workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent inspect the live OOMOL Mistral connector schema and run supported Mistral account actions without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include unverified remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer a signed or version-pinned installer with checksum verification instead of running the installer commands as written.

Risk: The skill can perform write and destructive actions against a connected Mistral account.

Mitigation: Inspect the live connector schema before building payloads and require explicit user confirmation before write or delete actions.

Risk: Mistral account actions are mediated through the OOMOL oo CLI and server-side credentials.

Mitigation: Install and use the skill only when the user trusts OOMOL to mediate these account actions.

## Reference(s):

- [Mistral AI homepage](https://mistral.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mistral-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before each action; connector runs return JSON responses.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
