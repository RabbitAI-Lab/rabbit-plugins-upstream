## Description:

Happy Horse 1.0 generates videos from text, a first frame, or reference media, and supports video editing with mode-specific routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate or edit short videos with Happy Horse 1.0, using text prompts and optional image or video references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image, video, and audio inputs may be uploaded to dLazy for processing.

Mitigation: Only submit media you are comfortable uploading, and review dLazy's service terms.

Risk: Video generation can incur usage costs.

Mitigation: Use --dry-run to review the request and estimated cost before generation.

Risk: The login flow stores an organization API key in the local CLI configuration.

Mitigation: Protect access to the local account, or provide DLAZY_API_KEY per invocation; rotate or revoke keys through the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Guidance]

**Output Format:** [JSON task and result metadata with generated video URLs, or a downloaded video file when saving is requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous task IDs are available when --no-wait is used.]

## Skill Version(s):

1.3.35 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
