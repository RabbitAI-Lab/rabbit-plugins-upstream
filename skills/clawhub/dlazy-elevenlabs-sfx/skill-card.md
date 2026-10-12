## Description:

Generates short sound effects from text descriptions for foley, ambience, alerts, and games using dLazy's ElevenLabs SFX integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short audio effects from prompts for video, games, alerts, and ambient sound.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI executes software outside the skill artifact.

Mitigation: Review the publisher's CLI and use the pinned package version before installation.

Risk: Prompts and explicitly supplied files may be sent to dLazy services, and generated audio is hosted there.

Mitigation: Avoid submitting sensitive prompts or files and review the service's handling of generated assets.

Risk: A stored dLazy API key may be exposed if the local account or configuration is compromised.

Mitigation: Protect local credentials and rotate or revoke the key when it is no longer needed.

Risk: The documented response example describes image output despite the skill generating audio.

Mitigation: Check the actual response type and audio URL rather than relying on the example image fields.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI repository (publisher-provided link; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio can be accessed by a hosted URL or saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
