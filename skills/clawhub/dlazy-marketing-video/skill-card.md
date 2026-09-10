## Description:

Creates marketing, promotional, advertising, and ecommerce product videos from product details, brand briefs, or storefront listings for social media and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and ecommerce teams use this skill to invoke dLazy's hosted video-generation agent for conversion-focused product ads, brand promos, shopping videos, and cross-border selling content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party npm CLI and dLazy SaaS services.

Mitigation: Install only if you trust dLazy and @dlazy/cli; prefer npx or a local install when a persistent global binary is not desired.

Risk: Prompts and attached files may be sent to dLazy API and media-storage endpoints.

Mitigation: Review prompts and files before use, and avoid attaching sensitive material unless sharing it with dLazy is acceptable.

Risk: The dLazy API key can be stored in local CLI configuration.

Mitigation: Use OS user file permissions, rotate or revoke keys if exposure is suspected, and consider per-invocation use of DLAZY_API_KEY where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI-generated responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped dLazy chat sessions and uploaded file URLs handled by the dLazy CLI.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
