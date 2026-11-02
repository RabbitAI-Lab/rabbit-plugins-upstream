## Description:

Replicates a source video by analyzing its first frame and audio and returning a Seedance 2.0 bundle with a prompt, frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can use this skill to analyze a reference video and request a corresponding Seedance 2.0 prompt and media bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, audio, image, and prompt data supplied to the skill are sent to dLazy's hosted service; local media paths are uploaded for processing.

Mitigation: Use only media you are comfortable uploading and review the service terms before sending it.

Risk: The skill depends on an external CLI and requires a dLazy API key, which may be stored in the user's CLI configuration.

Mitigation: Review the CLI before installation, protect the saved key or provide it through the documented environment variable, and rotate or revoke it if exposed.

Risk: Video generation may incur usage costs.

Mitigation: Use --dry-run to inspect the payload and cost estimate before submitting a generation request.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image, Audio, Video]

**Output Format:** [JSON response with hosted media asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return media outputs asynchronously when requested.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
