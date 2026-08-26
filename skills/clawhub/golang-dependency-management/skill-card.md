## Description:

Dependency management strategies for Golang projects — go.mod management, installing/upgrading packages, Minimal Version Selection, vulnerability scanning, outdated dependency tracking, binary size analysis, Dependabot/Renovate setup, conflict resolution, and go.work workspaces. Use when adding, removing, or upgrading Go dependencies, auditing vulnerabilities, resolving version conflicts, or setting up automated dependency updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Go module dependencies, evaluate additions and upgrades, audit vulnerabilities, resolve version conflicts, and configure automated dependency update workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to modify Go project files and run Go tooling that may download modules.

Mitigation: Review proposed changes to go.mod, go.sum, go.work, and update configuration before committing, and run project tests plus vulnerability scanning after dependency changes.

Risk: A newly added dependency may be unnecessary, poorly maintained, or incompatible with project licensing or security expectations.

Mitigation: Require user confirmation before adding dependencies and evaluate standard-library alternatives, maintenance status, license compatibility, and known alternatives before running go get.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-dependency-management)
- [ClawHub publisher profile](https://clawhub.ai/user/samber)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Versioning & Minimal Version Selection](references/versioning.md)
- [Auditing Dependencies](references/auditing.md)
- [Dependency Conflicts & Resolution](references/conflicts.md)
- [Go Workspaces](references/workspaces.md)
- [Automated Dependency Updates](references/automated-updates.md)
- [Visualizing the Dependency Graph](references/visualization.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and Go module configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to go.mod, go.sum, go.work, and dependency update configuration, with user confirmation required before adding a new dependency.]

## Skill Version(s):

1.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
