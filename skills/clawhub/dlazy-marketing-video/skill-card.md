## Description:

Creates marketing, promotional, advertising, or brand videos from a product, brand, or brief for social campaigns and product ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to create conversion-focused ecommerce and promotional videos from product details, listings, brands, briefs, or attached reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketing prompts, product details, and explicitly attached files are sent to dLazy hosted services.

Mitigation: Use the skill only with information appropriate for dLazy processing, review files before attaching them, and avoid sending confidential material unless permitted.

Risk: The dLazy API key is stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Keep the key private, prefer on-demand npx usage when a persistent global CLI is not needed, and rotate or revoke the key if the machine is shared or compromised.

Risk: Project sessions preserve context across follow-up turns.

Mitigation: Use session clearing for unrelated work so prior project context is not reused unintentionally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project sessions and uploaded user-supplied files when the user attaches files.]

## Skill Version(s):

1.0.9 (source: release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
