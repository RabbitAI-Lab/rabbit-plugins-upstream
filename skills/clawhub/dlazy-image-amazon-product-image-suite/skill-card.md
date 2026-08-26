## Description:

A professional product image generation skill for Amazon product detail pages, covering main images, secondary images, and A+ modules while aligning outputs with Amazon image guidelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and creative teams use this skill to plan and generate Amazon-ready product image sets, including main listing images, secondary visual assets, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media files may leave the local machine for dLazy cloud image generation.

Mitigation: Use the skill only with content that can be processed by dLazy's cloud API, and avoid submitting sensitive product assets unless that transfer is acceptable.

Risk: API keys can be stored in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for one-off runs when local persistence is undesirable, rotate or revoke keys from the dLazy dashboard when needed, and review permissions on ~/.dlazy/config.json.

Risk: The workflow depends on a third-party npm CLI and external API endpoints.

Mitigation: Review the dLazy CLI source or npm package before installation and install only when the dependency and network behavior fit the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with task status, image checklists, prompt drafts, shell commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use the dLazy CLI to send prompts and supplied media files to dLazy cloud endpoints for image generation.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
