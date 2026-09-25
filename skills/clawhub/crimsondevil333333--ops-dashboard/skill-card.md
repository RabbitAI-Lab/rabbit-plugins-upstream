## Description:

Gather operational signals (disk usage, git status, recent commits, and resources) so you can answer "How is the Clawdy infrastructure doing?" without manually running multiple checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333)

### License/Terms of Use:


## Use Case:

Developers and operations-focused agents use this skill to summarize workspace health before deployments, updates, or support work. It combines disk usage, git status, recent commits, load averages, and top directory sizes into one operational report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose local repository health metadata, including git status, recent commits, disk usage, load averages, and directory sizes.

Mitigation: Run it only against workspaces whose operational metadata is intended to be included in the report, and avoid pointing --workspace at sensitive folders.

## Reference(s):

- [Ops Dashboard reference](references/ops-dashboard.md)
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/ops-dashboard)

## Skill Output:

**Output Type(s):** [text, shell commands, code, guidance]

**Output Format:** [Markdown guidance with inline shell commands and plain-text CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can produce summary or resource-focused workspace health reports.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
