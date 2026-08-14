## Description:

Turns changing goals and legacy CMS project records into a compact, conflict-checked delivery state with aligned scope, bounded autonomy, evidence-aware delivery claims, and independent QA control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project owners, and delivery leads use this skill to convert vague goals or legacy CMS records into a current authorization, right-sized governance profile, clear evidence requirements, and QA-ready delivery state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose project-local governance document updates or Node commands, including commands with --write.

Mitigation: Review proposed commands before execution, confirm the workspace boundary, and use write mode only when the target project state is trusted and intended.

Risk: Incorrect or incomplete evidence could lead to overstated delivery or acceptance claims.

Mitigation: Keep delivery class, runtime evidence, stage review, and independent QA decisions separate, and require independent final QA for Standard or Full governance.

Risk: The skill references the separate agent-loop-engineering skill for execution and validation commands.

Mitigation: Confirm that the referenced agent-loop-engineering installation is present and trusted before relying on its scripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/englandtong/skills/coding-management-system)
- [Goal Discovery 2.1](artifact/references/en/goal-discovery.md)
- [Planning And Sizing 2.1](artifact/references/en/planning-and-sizing.md)
- [Legacy Bootstrap 2.1](artifact/references/en/legacy-bootstrap.md)
- [Governance Profiles And Files 2.1](artifact/references/en/governance-profiles.md)
- [Controller, Stage Reviewer, And Independent QA 2.1](artifact/references/en/controller-qa.md)
- [Alignment, Rebaseline, Audit, And Finish Line 2.1](artifact/references/en/alignment-and-rebaseline.md)
- [Execution Contract 2.1](artifact/references/en/execution-contract.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown guidance with structured state fields, templates, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May draft or update project governance artifacts only within an authorized workspace boundary.]

## Skill Version(s):

2.1.0 (source: artifact/SKILL.md and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
