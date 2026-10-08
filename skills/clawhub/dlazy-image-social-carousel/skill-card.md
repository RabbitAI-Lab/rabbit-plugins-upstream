## Description:

Guides agents through planning and generating social-media carousel slides using a confirmed design direction and an approved cover image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to plan platform-specific social carousels, approve a cover design, and generate visually consistent remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an external CLI package requires installing or running third-party software.

Mitigation: Review the @dlazy/cli package before use; choose the npx alternative if a global installation is undesirable.

Risk: Prompts and referenced media are sent to dLazy's hosted service, and use requires an API key.

Mitigation: Avoid submitting sensitive content without approval and rotate or revoke the API key through the service dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown planning tables, status updates, generation commands, and generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slide plans and image generation proceed after user confirmation; the cover is approved before remaining slides.]

## Skill Version(s):

1.3.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
