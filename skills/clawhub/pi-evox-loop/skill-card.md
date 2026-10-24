## Description:

Adds an experience-inheritance workflow for coding agents to recall prior fixes, record useful repairs, and optionally evaluate whether those fixes transfer across tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use it to help coding agents reuse reviewed fixes from earlier tasks, record new repairs for future recall, and optionally assess the workflow with controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored lessons may bypass advertised safeguards and influence later agent sessions.

Mitigation: Require manual review of each complete lesson and defer persistent hooks and automatic approval of shared lessons until scanning, approval-state, and signature checks are corrected.

Risk: Session logs and optional transcript refinement may contain private task content.

Mitigation: Avoid sharing sensitive transcripts and restrict access to session logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with shell commands, code examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to record and reuse task lessons; review lesson content before use.]

## Skill Version(s):

0.30.0 (source: server-resolved release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
