## Description:

Helps agents generate images with Qwen Image 2 Pro through the dLazy CLI, including text-heavy designs and reference-image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to instruct an agent to generate images from prompts, optionally supplying reference images and saving generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media may be sent to the dLazy hosted service.

Mitigation: Review prompts and selected media for sensitive content before submission.

Risk: The dLazy CLI is a third-party dependency, and login stores an API key locally.

Mitigation: Review the pinned CLI before installation and use a per-invocation API key if local storage is unsuitable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions for a CLI that returns JSON with image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated images locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.25 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
