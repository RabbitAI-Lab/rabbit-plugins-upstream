## Description:

Voicemaker helps agents use the Voicemaker text-to-speech service through an OOMOL-connected account to generate speech and list available voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Voicemaker through an OOMOL-connected account, including generating text-to-speech audio and listing voices before choosing a voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute scripts fetched from the network.

Mitigation: Review setup before installing, prefer a trusted versioned package or documented release with checksum or signature verification, and do not let an agent run installer commands automatically.

Risk: Text submitted for speech generation is sent to the connected Voicemaker service.

Mitigation: Confirm the generated speech payload before execution and avoid sending sensitive text unless the account and service handling are approved for that data.

## Reference(s):

- [Voicemaker homepage](https://voicemaker.in/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON responses containing generated audio URLs, voice listings, metadata, and execution IDs.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
