## Description:

Synthesizes text into natural-sounding speech using Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ClawHub users generate Chinese or English spoken audio from text, selecting a voice and speech speed as needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for synthesis is sent to dLazy's hosted API and generated assets are hosted on files.dlazy.com.

Mitigation: Avoid sending sensitive text unless you trust the service and its handling of generated assets.

Risk: Logging in may store an API key in the local dLazy configuration.

Mitigation: Protect local credentials and rotate or revoke keys if needed.

Risk: The documented example shows an image result rather than audio, so the expected output format is uncertain.

Mitigation: Check the returned asset type before using or distributing it.

Risk: Global installation leaves a persistent CLI binary on the system.

Mitigation: Use the pinned npx invocation instead if a persistent installation is unwanted.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Audio asset links]

**Output Format:** [Text guidance and CLI commands; the service returns JSON with a generated asset URL or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio can be downloaded to a local path; the documented example shows an image rather than audio, so confirm the returned asset type.]

## Skill Version(s):

1.3.24 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
