## Description:

A lightweight Git workflow assistant that syncs a managed README workflow block, creates local feature branches after confirmation, and reports Git workflow status without performing commits, merges, pushes, tags, releases, branch deletion, or history rewrites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to keep a repository README aligned with a defined Git workflow, safely create local feature branches from an approved baseline, and run read-only Git workflow status and feature-completion checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes release and hotfix guides and scripts that conflict with the restrictive main skill and could lead to high-impact Git actions such as merge, push, tag, branch deletion, or release operations if followed or run.

Mitigation: For normal installation, rely on SKILL.md and templates/readme-git-workflow.md, and remove or ignore the bundled release and hotfix materials unless a reviewer explicitly wants a broader release-management tool.

Risk: README synchronization can modify repository documentation when the user explicitly requests it.

Mitigation: Preview the exact managed-block change, require a second explicit confirmation, and edit only the GIT_WORKFLOW_START to GIT_WORKFLOW_END block or append the full managed block when no block exists.

Risk: Feature branch creation changes local Git branch state after confirmation.

Mitigation: Require a clean workspace, validate branch name and baseline, check for in-progress Git operations and existing local or remote branch names, and show the resolved baseline commit before running git switch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlykan/skills/git-workflow)
- [README Git workflow template](templates/readme-git-workflow.md)
- [Branch strategy reference](references/branch-strategy.md)
- [Workflow guide](references/workflow-guide.md)
- [Troubleshooting reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with PowerShell or Git command blocks, structured status summaries, and managed README content when explicitly confirmed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update only the README managed workflow block or create a local feature branch after explicit user confirmation; normal checks are read-only.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
