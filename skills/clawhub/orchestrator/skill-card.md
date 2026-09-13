## Description:

Use when starting or running an agent-driven software project with the afonsoft harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate agent-driven software projects, including project setup, planning, SPEC-driven execution, GitHub issue flow, QA gates, and release preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate commits, issue creation or closure, PR creation, pushes, and merges with broad repository authority.

Mitigation: Require explicit approval before those actions and preview all GitHub payloads before submission.

Risk: Automated T1/T2 execution may change repository state beyond the user's intent.

Mitigation: Disable or narrow T1/T2 auto-execution and require approval for protected branches, public exposure, credentials, deployment changes, and repository-mutating commands.

Risk: The suggested unpinned npx reinstall command may fetch unexpected skill revisions.

Mitigation: Pin the catalog or revision and verify provenance before reinstalling.

Risk: Target repository visibility or GitHub operations may expose private work.

Mitigation: Verify repository visibility, remotes, and authentication scope before running the workflow.

## Reference(s):

- [Orchestrator delegation protocol](references/orchestrator-delegation-protocol.md)
- [Orchestrator state template](references/orchestrator_stats.md)
- [Legacy Orchestrator state template](references/ESTADO_ORQUESTRATOR.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/orchestrator)
- [Publisher metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, checklists, project state templates, and configuration-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates other specialized skills and writes or updates project governance state when used by an agent.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; artifact metadata version 2.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
