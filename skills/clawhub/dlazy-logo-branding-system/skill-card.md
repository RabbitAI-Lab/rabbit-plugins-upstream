## Description:

Guides a phased logo and brand identity workflow from initial concepts through consistent visual applications and deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and brand teams use this skill to plan, generate, review, and refine logo concepts and coordinated brand assets with phased approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted services.

Mitigation: Confirm the content is suitable to share before submitting prompts or reference assets.

Risk: The CLI can store a dLazy API key locally.

Mitigation: Use the DLAZY_API_KEY environment variable if persistent key storage is unwanted, and rotate or revoke keys when needed.

Risk: The published skill version differs from the CLI version documented for installation; the CLI implementation is not included in the skill artifacts.

Mitigation: Review the @dlazy/cli@1.2.3 package before running it and verify the intended CLI version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI project (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with design rationales, phase plans, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation proceeds one approved step at a time.]

## Skill Version(s):

1.2.21 (source: ClawHub release evidence; embedded skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
