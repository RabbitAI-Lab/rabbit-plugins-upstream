## Description:

Battle-tested runbook for running long OpenMM molecular dynamics jobs on Kaggle's free GPU tier, with checkpoint/resume operations, Kaggle platform traps, OpenMM 8.3.1 guidance, RECELL debugging, ligand rebuild guidance, equilibration steps, and a static preflight checker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, computational chemistry practitioners, and agent operators use this skill to plan, execute, debug, and hand off long OpenMM molecular dynamics runs on Kaggle GPU sessions while avoiding known platform and API failure modes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runbook includes bootstrap steps that may install third-party packages or tools before running an OpenMM workload.

Mitigation: Review the commands before execution, pin and verify downloads where practical, and run them only in an environment intended for the Kaggle workflow.

Risk: The optional supervisor can relaunch Kaggle kernels and version datasets, which can consume quota or mutate remote resources.

Mitigation: Start the supervisor only on explicit human instruction, run at most one instance, and monitor status, logs, and quota while it operates.

Risk: Kaggle credentials are required for live operations and could be exposed if copied into project files.

Mitigation: Keep credentials in the standard user-controlled location, do not print or embed key contents, and use the included preflight gate to detect accidental secrets in kernel code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/kaggle-openmm-md-runbook)
- [Operations Quick Reference](references/operations.md)
- [Traps & API Matrix](references/traps-and-api-matrix.md)
- [Runbook](RUNBOOK.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a stdlib-only static checker that reports preflight gate results for user-provided kernel and input directories.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
