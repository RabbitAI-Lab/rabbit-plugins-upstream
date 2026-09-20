## Description:

This skill operates ElevenLabs through the OOMOL-connected connector for reading, creating, updating, and deleting ElevenLabs data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate an ElevenLabs account through OOMOL's oo CLI, including voice discovery, model lookup, text-to-speech generation, sound-effect generation, and generation-history access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create speech or sound-effect generations and may affect the connected ElevenLabs account.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: The destructive delete_history_item action can remove ElevenLabs generation-history data.

Mitigation: Confirm the target history item ID and obtain explicit approval before deletion.

Risk: First-time setup includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Use official installation instructions and inspect installer commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elevenlabs)
- [ElevenLabs homepage](https://elevenlabs.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector actions return JSON and may produce audio files in transit storage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require confirmation before running.]

## Skill Version(s):

1.0.5 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
