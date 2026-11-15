## Description:

Generates images with Alibaba Bailian's Qwen Image 2.0 Pro, with support for detailed text rendering, multilingual layouts, photorealistic detail, and strong prompt adherence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can ask an agent to generate images from text prompts, optionally providing reference images. The skill is suited to mixed text-and-image designs, including multilingual layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI login and credential handling were not fully assessed by the security scan.

Mitigation: Review the CLI before installing and use a revocable API key; rotate or revoke it if needed.

Risk: Prompts and supplied reference images may be sent to dLazy-hosted services for generation.

Mitigation: Avoid sending confidential material unless its use is permitted by your organization and the service terms.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files (PNG) returned as hosted URLs or saved locally, with JSON result or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image size can be selected from the documented presets; up to three reference images may be supplied. Generation can return asynchronously.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
