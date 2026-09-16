## Description:

Voicemaker lets agents operate Voicemaker text-to-speech through an OOMOL-connected account, including generating speech and listing available voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route Voicemaker tasks through OOMOL, including text-to-speech generation and voice discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TTS generation may create output or consume account credits.

Mitigation: Confirm the intended generation payload and expected effect with the user before running generation actions.

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Only run installer commands when the user intentionally wants setup and independently trusts the installer source.

Risk: The release security verdict is suspicious and calls for review before installation.

Mitigation: Review the skill and its OOMOL connector behavior before installing or deploying it.

## Reference(s):

- [Voicemaker homepage](https://voicemaker.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Voicemaker action responses that include generated audio URLs, voice listings, usage details, and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
