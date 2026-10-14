## Description:

Guides the planning and cover-first generation of coordinated social-media carousel images using visual references and the dLazy image-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to plan platform-specific social carousels, confirm a visual direction, generate a cover, and produce matching slides after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a global CLI and running image-generation commands executes third-party software.

Mitigation: Review the @dlazy/cli package before installation and use the documented on-demand npx option if a global installation is undesirable.

Risk: The CLI stores an API key locally and sends prompts and supplied media to dLazy cloud services.

Mitigation: Protect the local key, use only media approved for upload, and rotate or revoke the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source and documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown planning tables and status updates with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cover-first review before subsequent slides; default platform aspect ratio at 1K resolution.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
