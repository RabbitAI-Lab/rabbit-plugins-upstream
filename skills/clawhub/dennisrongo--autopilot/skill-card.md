## Description:

Autopilot runs one well-defined coding task end to end without mid-run questions, producing a verified working tree and evidence-backed report while stopping before commits, pushes, or pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill for headless or hands-off execution of a single scoped work item when they want implementation, verification, review, and a final evidence report without interactive plan approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hands-off execution can edit the working tree without interactive review during the run.

Mitigation: Use it only for a well-defined task and review the final diff and report before shipping.

Risk: Dangerous permission bypasses reduce the harness safety net.

Mitigation: Keep dangerous permission bypasses limited to disposable or sandboxed environments.

Risk: The workflow may read and invoke installed local skills selected by its routing table.

Mitigation: Review the skills available in the environment and the final Skills used report.

## Reference(s):

- [Runtime notes](artifact/references/runtime.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with code, command, configuration, and working-tree change guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a task-scoped report with requirements evidence, assumptions, review outcome, skills used, and next human action.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
