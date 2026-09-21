## Description:

Turns a product, product image, or product listing link into a conversion-focused ecommerce advertising video through the dLazy hosted ecommerce-video CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, marketers, and developers use this skill to start or continue dLazy projects that generate shopping, store, TikTok Shop, and product-ad videos from product material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and selected attachments may be sent to the dLazy SaaS service.

Mitigation: Confirm the user is comfortable with dLazy service processing before use, and avoid attaching sensitive files unless they are intended for that service.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when local persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm installation changes the local environment.

Mitigation: Use the pinned npx invocation, npx @dlazy/cli@1.2.3, when a persistent global binary is not required.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted dLazy agent responses and may reference uploaded files or project IDs.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence; artifact frontmatter is 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
