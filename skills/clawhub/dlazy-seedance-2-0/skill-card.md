## Description:

Generates Seedance 2.0 videos from text prompts, multimodal references, or first and last frames through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate videos from text prompts, image, video, or audio references, or selected first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media are sent to dLazy, and local media files are uploaded to its media storage.

Mitigation: Submit only media you are comfortable sending to dLazy.

Risk: Video generation may incur charges.

Mitigation: Review the CLI dry-run cost estimate before starting a generation.

Risk: The security review did not verify the published CLI executable or hosted-service behavior.

Mitigation: Review the pinned CLI before installation and prefer the device-login flow over pasting API keys into chat.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [Generated video assets with a JSON response containing output URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 480p–1080p resolution and 4–15 second durations; outputs can be saved locally.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
