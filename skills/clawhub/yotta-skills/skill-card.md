## Description:

YuanGe helps developers route tasks to combinations of YottaMeta skills and manage their installation, updates, and local inventory across AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users of supported AI agents use YuanGe to choose a suggested skill combination for a task, install or update those skills, and inspect or manage a local skill inventory and Hub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates this release suspicious and is incomplete, with reported concerns around handling untrusted packages.

Mitigation: Review the verdict and inspection coverage before installing; do not treat disputed alerts as confirmed or missing coverage as evidence of safety.

Risk: The security guidance reports a risk of executing untrusted code during inspection.

Mitigation: Do not inspect untrusted packages in an uncontrolled environment; review and scan them before installation.

Risk: The security guidance flags repeatedly recommending an unpinned installer as a concern.

Mitigation: Pin the package version and verify the intended release before running installer commands.

## Reference(s):

- [Orchestration guide](references/orchestration.md)
- [Install flow guide](references/install-flow.md)
- [Local Hub guide](references/hub.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [CLI text, Markdown guidance, shell commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-dependent; may install, update, link, or inventory skill files.]

## Skill Version(s):

0.30.15 (source: server-resolved release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
