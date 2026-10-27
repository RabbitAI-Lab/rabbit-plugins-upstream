## Description:

A lightweight, project-specific Git workflow assistant that activates only for explicit README workflow sync, local feature branch creation, workflow status checks, and feature completion checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to keep a repository README workflow block synchronized, create local feature branches after confirmation, and inspect Git workflow status without performing commits, pushes, merges, releases, or destructive history changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled release scripts and legacy release documentation can change or publish repository history, which conflicts with the narrow behavior described by the main skill file.

Mitigation: Remove or split out the release scripts and legacy release documentation before installation unless repository publish authority is intended and controlled.

Risk: Running the bundled release scripts could perform repository publishing actions beyond the lightweight workflow assistant's documented boundaries.

Mitigation: Do not run the bundled release scripts without branch protections, backups, and explicit human approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlykan/skills/git-workflow)
- [README](artifact/README.md)
- [Branch strategy](artifact/references/branch-strategy.md)
- [Workflow guide](artifact/references/workflow-guide.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [README workflow template](artifact/templates/readme-git-workflow.md)
- [Release script usage](artifact/docs/RELEASE_SCRIPT_USAGE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain text with inline Git, PowerShell, and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose README edits or local branch-creation commands; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
