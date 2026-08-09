## Description:

Guides agents through Git branch creation, testing, release, hotfix, and rollback workflows while requiring explicit confirmation for destructive operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to standardize Git workflow decisions, branch naming, feature testing, release preparation, hotfix handling, and rollback guidance. It is intended for agent-assisted repository operations where potentially destructive Git commands must be reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release and branch-management flows can push, tag, merge to main or release branches, delete branches, or rewrite history.

Mitigation: Require the agent to show the exact command, target branch, expected impact, and irreversible effects, then obtain fresh explicit approval before any such operation.

Risk: The skill promises explicit confirmation for destructive operations, but the authoritative security summary says this is not enforced consistently across executable and documented release flows.

Mitigation: Review the skill before installation, prefer protected branches and pull requests, and restrict direct execution of push, tag, merge, branch deletion, reset --hard, and force-push commands.

Risk: Shared-branch rollback or history rewriting can disrupt collaborators or CI/CD state.

Mitigation: Use revert-based rollback for shared branches and reserve force-with-lease or reset workflows for personal feature branches after confirming no other collaborators depend on them.

## Reference(s):

- [Workflow Guide](references/workflow-guide.md)
- [Branch Strategy](references/branch-strategy.md)
- [Troubleshooting](references/troubleshooting.md)
- [Release Script Usage](docs/RELEASE_SCRIPT_USAGE.md)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Git commands that require user review and explicit approval before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
