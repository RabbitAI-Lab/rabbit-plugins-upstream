## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layout, photorealistic detail, semantic adherence, and mixed Chinese-English image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images through the dLazy CLI using Alibaba Bailian qwen-image-2.0-pro, including designs that need detailed prompt adherence, realistic texture, and mixed Chinese-English text rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected media files to the dLazy hosted service for image generation.

Mitigation: Use it only with content appropriate for the dLazy service and avoid submitting sensitive prompts or media unless approved for that workflow.

Risk: Use requires a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Prefer per-user credentials, avoid elevated execution, and rotate or revoke the API key if exposure is suspected or the skill is no longer used.

Risk: The skill depends on the dLazy npm CLI and hosted API availability.

Mitigation: Prefer the pinned on-demand npx invocation when possible and review the CLI/package source and service trust boundary before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides invocation of a cloud image-generation CLI that can return image output URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
