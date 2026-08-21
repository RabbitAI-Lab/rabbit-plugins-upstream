## Description:

Turns vague or changing goals and legacy CMS project records into a compact, conflict-checked delivery state with clear outcomes, bounded autonomy, alignment checks, evidence-aware claims, and independent QA control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project owners, and delivery leads use this skill to convert uncertain requirements or legacy CMS project records into one current authorization, choose an appropriate governance profile, and coordinate bounded execution, stage review, alignment, and independent QA.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can organize project governance files and may maintain delivery state in the workspace.

Mitigation: Use it only in workspaces where AI-maintained delivery state is intended, and review generated Active Packets before allowing writes.

Risk: The skill may call a separately installed agent-loop-engineering helper for execution-related validation or bootstrap tasks.

Mitigation: Confirm the helper is installed from a trusted source and review proposed commands before enabling multi-agent delegation.

Risk: Governance or QA decisions can be misleading if accepted without checking the supporting evidence.

Mitigation: Require evidence-backed acceptance, preserve independent QA for Standard and Full governance, and treat conflicting evidence as the weaker result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/englandtong/skills/coding-management-system)
- [Execution Contract 2.1](references/en/execution-contract.md)
- [Goal Discovery 2.1](references/en/goal-discovery.md)
- [Planning And Sizing 2.1](references/en/planning-and-sizing.md)
- [Legacy Bootstrap 2.1](references/en/legacy-bootstrap.md)
- [Governance Profiles And Files 2.1](references/en/governance-profiles.md)
- [Controller, Stage Reviewer, And Independent QA 2.1](references/en/controller-qa.md)
- [Alignment, Rebaseline, Audit, And Finish Line 2.1](references/en/alignment-and-rebaseline.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with structured decision fields, templates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project governance files such as Active Packets, Work Orders, loop records, and QA decisions when explicitly authorized.]

## Skill Version(s):

2.1.1 (source: SKILL.md body and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
