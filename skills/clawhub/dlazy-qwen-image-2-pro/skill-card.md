## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layout, photorealistic detail, strong semantic adherence, and mixed Chinese/English image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to invoke dLazy's hosted Qwen Image 2 Pro image-generation workflow from an agent, producing generated image outputs from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local input files may be sent to the third-party dLazy cloud service.

Mitigation: Use only data approved for third-party cloud processing and avoid sending secrets, regulated data, or confidential files unless policy permits it.

Risk: Generated files may be hosted by dLazy and returned as remote URLs.

Mitigation: Review generated output handling requirements before sharing sensitive or customer-specific content, and download or store outputs according to local policy.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Prefer per-invocation environment variables when persistence is not desired, protect local configuration files, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions]

**Output Format:** [JSON result containing generated image URLs, with optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, optional local save paths, and image sizes declared by the CLI.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
