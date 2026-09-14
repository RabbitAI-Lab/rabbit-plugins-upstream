## Description:

Turns product photos, product information, or ecommerce listings into conversion-focused shopping ad videos through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy projects that create ecommerce, product, TikTok Shop, store, or ad videos from product references and prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill wraps a third-party pinned CLI and hosted SaaS service.

Mitigation: Install or run it only after confirming trust in dLazy and the @dlazy/cli package; prefer npx or another isolated environment when a persistent global binary is not desired.

Risk: Prompts, options, API credentials, and attached files may be sent to dLazy API and file storage endpoints.

Mitigation: Attach only files suitable for upload to dLazy, avoid elevated-privilege npm installs, and rotate or revoke the dLazy API key if the installation or service is later distrusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and terminal-oriented guidance with dLazy CLI commands and streamed service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and the pinned @dlazy/cli 1.2.3 package declared by the artifact metadata.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
