## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform that helps agents plan and generate main images, secondary product images, and A+ content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents use this skill to plan and generate Amazon product-detail visuals, including compliant main images, secondary images, infographics, lifestyle shots, detail images, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI that handles dLazy API keys, prompts, and user-selected media paths.

Mitigation: Review the @dlazy/cli package for the exact pinned release before use, avoid elevated global installs where possible, and provide only media files intended for upload.

Risk: Security evidence flags inconsistent version documentation around the CLI and release.

Mitigation: Verify the release version and CLI package version before installation or execution, and prefer pinned commands from server-resolved metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with task plans, image checklists, prompt drafts, CLI command snippets, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to authenticate with the dLazy CLI and generate one image at a time after user confirmation.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
