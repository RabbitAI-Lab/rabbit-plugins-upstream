## Description:

Selects dLazy audio models to generate speech, music, and sound effects from user prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run dLazy models for text-to-speech, music, and sound-effect generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy-hosted services.

Mitigation: Share only content approved for third-party processing.

Risk: CLI authentication stores a dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Running the CLI can consume account credits.

Mitigation: Review expected usage and available credits before generating audio.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [CLI commands and JSON responses containing generated audio URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is hosted by dLazy; generation requires an API key and may consume account credits.]

## Skill Version(s):

1.3.26 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
