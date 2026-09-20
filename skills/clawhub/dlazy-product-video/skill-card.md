## Description:

Turns product photos, specifications, catalogs, or marketplace listings into product demo, showcase, and ad videos through the dLazy hosted product-to-ecommerce-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, ecommerce operators, cross-border sellers, and agents use this skill to create product demo, showcase, and advertising videos from product photos, attached files, or marketplace links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files are sent to the dLazy hosted service, and attached files are uploaded to dLazy storage.

Mitigation: Only submit product information and files that are appropriate to upload to dLazy, and review service terms before use with sensitive material.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Use OS user-restricted config permissions, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The skill depends on the pinned dLazy CLI and hosted API behavior.

Mitigation: Review the pinned CLI package and source links before installation, and monitor authentication, balance, and service errors during use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, media]

**Output Format:** [Markdown and terminal-oriented guidance with shell commands; generated product video artifacts are produced by the dLazy hosted service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to the dLazy API and file storage endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
