## Description:

A lightweight Git workflow assistant that updates a managed README workflow block, creates confirmed local feature branches, and performs read-only workflow status and feature completion checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to keep a repository README aligned with a lightweight Git workflow, create local feature branches after confirmation, and inspect local Git workflow status without performing release or history-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes legacy documentation and scripts that describe release, merge, push, tag, branch deletion, reset, and force-push workflows outside the main skill boundaries.

Mitigation: Review before installing and use the restrictive runtime instructions in SKILL.md and templates/readme-git-workflow.md as the only operational sources; remove or clearly separate legacy files before broad deployment.

Risk: Local feature branch creation and README updates can still modify a repository when explicitly confirmed.

Mitigation: Require a clean working tree, show the branch name, baseline, relevant Git status, or README diff, and wait for explicit confirmation before any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlykan/skills/git-workflow)
- [README workflow template](templates/readme-git-workflow.md)
- [Branch strategy reference](references/branch-strategy.md)
- [Workflow guide reference](references/workflow-guide.md)
- [Troubleshooting reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose README edits or local feature branch creation only after explicit user confirmation; status and completion checks are read-only.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
