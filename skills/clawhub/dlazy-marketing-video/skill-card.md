## Description:

Creates marketing, promotional, advertising, and brand videos from a product, brand, listing, or brief for social media and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce sellers, and agent users use this skill to create conversion-oriented product, promotional, and advertising videos from product specs, listings, brand assets, or briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product materials, and attached files may be sent to dLazy hosted services.

Mitigation: Review data before use, avoid sensitive inputs where inappropriate, and use a fresh project or --clear for sensitive or unrelated work.

Risk: A dLazy API key is required and may be saved locally or supplied per invocation.

Mitigation: Use per-invocation keys when appropriate, restrict local config access, and rotate or revoke saved keys if exposure is suspected.

Risk: The skill depends on a third-party CLI and hosted service.

Mitigation: Review the pinned dLazy CLI package before installation and use the pinned npm or npx invocation from the skill metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or CLI-streamed text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted dLazy projects and uploaded files; requires dLazy API authentication.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
