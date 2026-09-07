## Description:

Powerful video generation with Kling v3 for high-quality text-to-video and image-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos from text prompts or reference images through the dLazy Kling v3 cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a cloud generation service that requires a dLazy API key and may store credentials in local CLI configuration.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Local media paths supplied to the CLI may be uploaded to dLazy media storage for model processing.

Mitigation: Confirm that media is appropriate to upload before invoking the skill, especially for private, regulated, or customer-provided files.

Risk: Generation requests can consume account credits or fail when credits are insufficient.

Mitigation: Use dry-run or review the request before execution when cost matters, and check account credit status before long or repeated generations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Shell commands and JSON responses with generated media URLs or saved video assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
