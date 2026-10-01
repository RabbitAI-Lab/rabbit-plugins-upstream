## Description:

Guides agents in using dLazy's Qwen3-TTS voice-cloning service to create a reusable voice from an audio sample.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can guide an agent to clone an authorized voice sample for subsequent text-to-speech requests through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning may be used without permission from the speaker.

Mitigation: Only clone voice samples you have the right to use.

Risk: Voice samples may be uploaded to dLazy-hosted services.

Mitigation: Review the service's data handling and obtain appropriate consent before uploading sensitive audio.

Risk: Installing the CLI globally or storing an API key locally creates persistent software and credential exposure.

Mitigation: Review the pinned CLI package before installation and prefer per-run API keys when appropriate.

Risk: The documented output schema and example command contain image-oriented or incorrect parameters.

Mitigation: Check the current CLI help and actual response before relying on the examples.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes voice-sample inputs and subsequent use of the cloned voice; documented response examples need confirmation.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
