## Description:

Turns product photos, documents, catalogs, or product listing links into polished product demo, showcase, or advertising videos through the dLazy hosted product-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and ecommerce teams use this skill to ask an agent to produce product demo, showcase, or advertising videos from product images, files, catalogs, or listing URLs. The workflow is useful for product ads and cross-border selling videos that may need multilingual voiceover or an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product files attached with the CLI are uploaded to dLazy media storage before the hosted agent can use them.

Mitigation: Only attach product files that are approved for upload to dLazy, and review data-sharing expectations before use.

Risk: The dLazy API key can be saved in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when local persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the third-party dLazy CLI and hosted APIs.

Mitigation: Review the pinned dLazy CLI source and package before installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped chat sessions, uploaded product files, and dLazy CLI authentication state.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
