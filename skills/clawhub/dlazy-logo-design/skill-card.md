## Description:

Creates, upgrades, and evaluates logos and brand marks through the dLazy hosted logo-design agent, producing transparent-background logos with multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue project-scoped dLazy logo-design sessions for brand identity work, including concept generation, refinement, evaluation, and preview-oriented delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI stores a service API key in local user configuration, and the security evidence flags that the pinned CLI package does not clearly enforce the stated credential-permission claim.

Mitigation: Review before installing on shared or sensitive machines; prefer per-invocation DLAZY_API_KEY use or verify local permissions on ~/.dlazy/config.json.

Risk: Files attached with --files are uploaded to dLazy media storage before use by the hosted agent.

Mitigation: Attach only design assets and reference files that are intended to be uploaded to dLazy.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown-oriented chat responses with inline shell commands and generated logo or preview assets from the hosted dLazy agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped multi-turn sessions; attached local files are uploaded to dLazy media storage before being referenced by the hosted agent.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
