## Description:

A workflow skill for designing marketing brochures, from requirements gathering and layout planning through confirmed mock-ups and lifestyle renders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and marketing teams use this skill to plan brochure structure, generate layout-first artwork, and produce folded and lifestyle brochure mock-ups after explicit confirmation gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to the third-party dLazy cloud service.

Mitigation: Use the skill only when that data-sharing model is acceptable, and avoid sending sensitive or restricted content unless approved.

Risk: dLazy login may persist an API key under the user's profile.

Mitigation: Use DLAZY_API_KEY or npx for less persistent setup when appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated output URLs are hosted by dLazy.

Mitigation: Review generated URLs and resulting assets before sharing or publishing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces brochure plans, image-generation prompts, layout confirmation requests, and dLazy-generated image URLs.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
