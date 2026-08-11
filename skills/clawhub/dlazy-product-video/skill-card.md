## Description:

Turns product photos, specs, manuals, catalogs, or e-commerce listing links into polished product demo, showcase, or ad videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, e-commerce sellers, and marketing teams use this skill to generate conversion-oriented product videos from product assets or marketplace listings through dLazy CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy API credentials that may be stored in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where appropriate, check local config file permissions, and rotate or revoke keys when access is no longer needed.

Risk: Files attached to CLI runs are uploaded to dLazy media storage.

Mitigation: Upload only files intended for dLazy processing and avoid sensitive project reuse unless deliberate.

Risk: Installing or running the CLI on shared machines may expose credentials or session state.

Mitigation: Review before installing on shared machines and prefer scoped or on-demand execution when persistent global installation is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated product-video outputs returned by the dLazy CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
