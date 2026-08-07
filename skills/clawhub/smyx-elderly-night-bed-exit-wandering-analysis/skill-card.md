## Description:

Using fixed cameras with infrared night vision in nursing-home or home bedrooms, this skill monitors elderly bed-exit status and night activity trajectories and produces abnormal alerts for prolonged bed exit or wandering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams, home-care users, and developers use this skill to analyze night camera video or video URLs for elderly bed-exit duration, wandering behavior, alert level, and report links. Outputs are care-reference behavior statistics and alerts, not medical diagnosis or specific care instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive elder-care bedroom or hallway video and may send private files or URLs to configured cloud services.

Mitigation: Use only with appropriate consent from monitored residents or authorized caregivers, and verify the configured service's security, retention, export, and access controls before deployment.

Risk: The skill may create or reuse an identity and store session tokens in a local workspace database.

Mitigation: Review local storage handling before installation, restrict workspace access, and clear stored tokens or reports according to the care organization's retention policy.

Risk: Behavior alerts are care-reference signals and can be incomplete or incorrect.

Mitigation: Require human review of suspected bed-exit, wandering, fall, or missing-person situations before taking care actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis)
- [Elderly night bed-exit and wandering API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports with alert text, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted historical reports and return Markdown tables for report lists.]

## Skill Version(s):

1.0.8 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
