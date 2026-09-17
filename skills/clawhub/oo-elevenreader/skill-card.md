## Description:

ElevenReader (elevenlabs.io). Use this skill for ANY ElevenReader request — searching and reading data. Whenever a task involves ElevenReader, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ElevenReader through an OOMOL-connected account, including listing text-to-speech models, searching voices, reading text aloud, and checking user or subscription information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts directly in a shell.

Mitigation: Before installing the oo CLI, prefer an official package manager or downloaded installer with a pinned version and verified checksum or signature.

Risk: ElevenReader access is mediated through OOMOL-connected credentials.

Mitigation: Use the skill only when OOMOL-mediated access is acceptable for the account and data involved.

## Reference(s):

- [ElevenReader homepage](https://elevenlabs.io/text-reader)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elevenreader)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
