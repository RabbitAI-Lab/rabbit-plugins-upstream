## Description:

Turns product photos, documents, catalogs, or ecommerce listing links into product demo, showcase, or advertising videos through the dLazy CLI and hosted product-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, ecommerce teams, and developers use this skill to generate conversion-focused shopping videos from product assets or marketplace links, with support for multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, manuals, listings, and other attached files may be sent to dLazy as an external service for product-video generation.

Mitigation: Use the skill only for data approved for dLazy processing, and review files and prompts before submission.

Risk: Authentication requires a dLazy API key, which the CLI can save in local configuration.

Mitigation: Prefer a revocable API key or per-invocation DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned dLazy CLI skill template product-to-ecommerce-video and may continue project-scoped chat sessions by project id.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
