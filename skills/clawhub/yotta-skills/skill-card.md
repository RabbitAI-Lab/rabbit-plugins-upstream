## Description:

YuanGe helps developers choose, install, update, and manage YottaMeta skills across agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use YuanGe to plan which YottaMeta skills fit a task, install or update them across supported agents, and inspect local skill directories and Hub links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted imports may escape the selected folder, and the health check may execute untrusted skill code.

Mitigation: Wait for import-containment and trusted-script checks before adopting unfamiliar skills or running doctor; review install targets before proceeding.

Risk: Registry fallback may be unsuitable when a fixed source is required.

Mitigation: Pin the installer version and disable registry fallback when the source must remain fixed.

Risk: Downloaded skills and live installation behavior were not evaluated in this review.

Mitigation: Review and scan the skills and installation behavior in the intended environment before adoption.

## Reference(s):

- [YottaMeta yotta-skills repository](https://github.com/YottaMeta/yotta-skills)
- [yotta-skills on npm](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Install flow](references/install-flow.md)
- [Hub guide](references/hub.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and guidance vary by task and target agent.]

## Skill Version(s):

0.30.7 (source: frontmatter, package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
