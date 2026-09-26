## Description:

Creates marketing, promotional, advertising, and ecommerce product videos from a product, brand, brief, or product listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to ask an agent to start or continue a dLazy product-to-ecommerce-video project, attach product references, and generate marketing or shopping-video assets for social and campaign use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files are sent to dLazy's hosted service.

Mitigation: Avoid sending unrelated or sensitive material unless dLazy is approved for that data; start a new project for unrelated work.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use OS user permissions, rotate or revoke keys from the dLazy dashboard when needed, or provide the key per invocation with DLAZY_API_KEY.

Risk: Continuing an existing project reuses prior session context.

Mitigation: Use a new project or run the documented clear command before work that should not share earlier context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to dLazy CLI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded files, API-key configuration, and project IDs when continuing hosted dLazy sessions.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
