## Description:

Helps contest organizers assess identity and environment consistency using submission signals and returns a JSON risk recommendation for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and reviewers use this tool to flag unusual submission patterns for investigation, not to make final eligibility or cheating determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identity and device information can expose participant data.

Mitigation: Use hashed environment identifiers and keep raw identity information outside the tool where possible.

Risk: Risk flags or a recommendation to freeze submissions may be mistaken for a final finding.

Mitigation: Check results against current contest rules and require human review before restricting submissions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/anti-cheat-identity)
- [LGD theory reference](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk level, warning flags, recommended action, and return code; recommendations require human review.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; packaged files state 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
