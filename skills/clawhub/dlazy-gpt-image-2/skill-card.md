## Description:

GPT Image 2 supports text-to-image generation and image editing or synthesis using reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts and edit or synthesize images with up to five reference inputs through the dLazy GPT Image 2 CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images are sent to dLazy-hosted services for generation.

Mitigation: Avoid submitting sensitive prompts or local files unless that disclosure is intended.

Risk: The skill requires a third-party dLazy API key that may be stored in local CLI configuration.

Mitigation: Use a revocable API key, rotate or revoke it from the dLazy dashboard when needed, and prefer DLAZY_API_KEY for per-invocation authentication if persistent local configuration is not desired.

Risk: Installing or running the skill depends on the third-party dLazy CLI package.

Mitigation: Review the dLazy CLI source or npm package before installation and use the pinned package version declared by the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [CLI commands and JSON responses containing generated image URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted file URLs; asynchronous runs may require polling with a generation ID.]

## Skill Version(s):

1.3.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
