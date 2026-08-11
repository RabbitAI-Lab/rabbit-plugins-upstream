## Description:

Turns product specs, manuals, catalogs, or ecommerce listings into conversion-focused shopping video workflows with multi-language voiceover and an optional virtual host through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and marketing teams use this skill to drive the dLazy product-to-ecommerce-video template from an agent session. It is intended for creating product ads and cross-border selling videos from product materials or marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product details, and attached files can be sent to dLazy's hosted API and media storage.

Mitigation: Review product materials for sensitive content before use, and attach only files that are appropriate for dLazy's hosted service.

Risk: The dLazy API key may be stored in the local CLI configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when local persistence is not desired, and rotate or revoke organization keys from the dLazy dashboard when needed.

Risk: The skill depends on the pinned third-party dLazy CLI and hosted service availability.

Mitigation: Install the pinned CLI version declared by the skill and review dLazy service responses for authentication, balance, or generation failures before treating output as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown or plain text streamed through the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids, uploaded file URLs, task status, error messages, and generated ecommerce video workflow results from dLazy's hosted service.]

## Skill Version(s):

1.3.6 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
