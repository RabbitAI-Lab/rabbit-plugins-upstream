## Description:

A workflow skill for planning marketing brochures, generating layout-first artwork, and producing folded or lifestyle mock-ups after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and agents use this skill to align brochure requirements, choose fold formats, create brochure layouts, and generate mock-ups through a confirmation-gated workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or run third-party npm code through the dLazy CLI.

Mitigation: Review the @dlazy/cli package before installation and use npx or a pinned install command when appropriate.

Risk: Prompts and uploaded media may be sent to dLazy cloud services for generation.

Mitigation: Use the skill only for brochure or image generation content suitable for dLazy processing, and avoid uploading sensitive local media.

Risk: A long-lived local API credential may remain in the dLazy CLI configuration.

Mitigation: Prefer environment-scoped DLAZY_API_KEY usage when suitable, and rotate or revoke keys when persistent credentials are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands, prompt drafts, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI/API access; brochure image generation is performed one step at a time after user confirmation.]

## Skill Version(s):

1.3.13 (source: release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
