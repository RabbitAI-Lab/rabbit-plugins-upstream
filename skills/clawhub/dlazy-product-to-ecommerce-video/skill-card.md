## Description:

Turns product specs, manuals, catalogs, or marketplace listings into conversion-focused ecommerce videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and developers use this skill to start or continue dLazy hosted projects that generate shopping-video content from product information and attached media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, ecommerce product details, and explicitly attached files are sent to dLazy's hosted service.

Mitigation: Install and use the skill only when that data sharing is acceptable, and attach only files intended for dLazy processing.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect local credentials and rotate or revoke the dLazy API key from the dLazy dashboard when access should change.

Risk: Using a persistent global CLI install leaves a third-party binary on the system.

Mitigation: Prefer the pinned npx invocation, npx @dlazy/cli@1.2.3, when a persistent global binary is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or terminal text with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated hosted project state and uploaded file URLs managed by the dLazy service.]

## Skill Version(s):

1.3.11 (source: server release metadata, released 2026-09-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
