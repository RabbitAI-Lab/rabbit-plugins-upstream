## Description:

Product video, product demo video, product ad video, product showcase - turn a product's photos or link into a polished demo or ad video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create product ads and ecommerce shopping videos from product images, specifications, catalogs, or listing links through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service for product-video generation.

Mitigation: Use approved product materials, avoid uploading sensitive assets unless permitted, and review dLazy's service terms and data-handling expectations before deployment.

Risk: Authentication stores a revocable dLazy API key in the user's local CLI configuration.

Mitigation: Use organization-scoped keys, protect the local config file, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: A global CLI install persists the pinned package on the user's system.

Mitigation: Use the pinned npx invocation when a persistent global install is not desired, and review the pinned package or source before use in sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a project-scoped dLazy CLI workflow; attached local files are uploaded to dLazy media storage before use.]

## Skill Version(s):

1.0.16 (source: server release evidence; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
