## Description:

Generates images from text prompts with Qwen Image 2 Pro through dLazy, including designs with detailed text and mixed Chinese-English layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to generate images from prompts, including layouts with complex text and photorealistic detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy's hosted service, which also hosts generated outputs.

Mitigation: Avoid submitting confidential prompts or files without approval for external processing and hosting.

Risk: Login can save a dLazy API key on the user's device.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: Running the third-party CLI installs or executes its package in the user's environment.

Mitigation: Review the package source before use; prefer the pinned on-demand npx command when a global install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown guidance and commands; JSON image-result links from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated images locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
