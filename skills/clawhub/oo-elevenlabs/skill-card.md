## Description:

ElevenLabs (elevenlabs.io). Use this skill for ANY ElevenLabs request: reading, creating, updating, and deleting data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ElevenLabs through the OOMOL oo CLI, including voice/model inspection, text-to-speech generation, sound-effect generation, account details, subscriptions, and generation history management. It supports read actions as well as confirmed write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup directs users to run internet-hosted installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a verified, pinned, or package-manager method when possible, and review installer commands before execution.

Risk: The skill operates ElevenLabs through OOMOL as an intermediary for the user's account.

Mitigation: Install only when use of OOMOL with the ElevenLabs account is acceptable for the user's security and compliance posture.

Risk: Some actions can write data or delete ElevenLabs history items.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ElevenLabs Homepage](https://elevenlabs.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-elevenlabs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI action schemas before execution and returns connector JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
