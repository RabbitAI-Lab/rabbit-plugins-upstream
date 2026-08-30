## Description:

Hunts bugs with evidence trails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code for likely defects, document reproducible evidence with file and line references, prepare minimal fixes, and plan verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad development triggers may activate the skill outside a focused bug-review task.

Mitigation: Confirm the review scope before applying findings or suggested fixes.

Risk: Persona wording may make recommendations sound more authoritative than the evidence supports.

Mitigation: Treat expertise framing as review context and verify conclusions with code review and normal project test commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-bug-review)
- [Pensive plugin homepage from clawdis metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with defect findings, proposed code changes, verification commands, and evidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file and line references, severity classifications, root-cause notes, test updates, and remaining-risk guidance.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
