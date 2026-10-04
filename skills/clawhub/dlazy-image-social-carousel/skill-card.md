## Description:

Guides agents through planning, confirming, and creating social-media carousel images with a cover-first workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan platform-specific social carousels, approve a visual direction and cover, then generate coordinated remaining slides through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced CLI package and version may differ from descriptions in the skill.

Mitigation: Verify the @dlazy/cli package and pinned version before installation.

Risk: Prompts and referenced local media are sent to dLazy's cloud service.

Mitigation: Obtain approval before uploading sensitive prompts or media and review what is shared.

Risk: The CLI may store an API key locally, and responses may include Chinese prompts.

Mitigation: Use DLAZY_API_KEY if local key storage is unsuitable, and review output language before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with planning tables, commands, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Presents a direction plan and cover for approval before proceeding with remaining slides.]

## Skill Version(s):

1.3.26 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
