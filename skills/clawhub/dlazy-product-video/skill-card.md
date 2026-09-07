## Description:

产品视频生成 Product Video turns product photos or links into polished product demo, showcase, or advertising videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce operators use this skill to invoke the dLazy CLI for product demo, advertising, and shopping-video generation from product photos, product documents, or marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill depends on a third-party npm CLI and hosted dLazy service.

Mitigation: Install only if you trust the dLazy package and service; prefer the pinned npx invocation when avoiding a persistent global CLI.

Risk: Requests and selected attachments are sent to dLazy API and media storage endpoints.

Mitigation: Attach only files intended for upload, and avoid sending sensitive product data unless the user accepts the service handling.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied by environment variable.

Mitigation: Keep the API key scoped to the user's organization and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, API key setup, and local files selected for upload.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
