## Description:

PIPL Audit helps users run a Chinese Personal Information Protection Law compliance audit across 9 domains and 32 checks, with offline preview and optional cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and compliance teams use this skill to preview or run a structured PIPL compliance audit for organizations processing personal information of natural persons in China. It guides the user through 32 checks and can produce a scored local report after cloud evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scored audit sends manually entered answers that may reveal business, security, or legal exposure details to compliancehub.cn.

Mitigation: Confirm the user accepts that cloud transfer before scoring, or use the non-interactive preview to inspect the checklist offline.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/pipl-audit)
- [ComplianceHub cloud service](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands; audit reports can be text, JSON, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored runs send the 32 audit answers to compliancehub.cn for evaluation; non-interactive preview mode remains offline.]

## Skill Version(s):

2.0.2 (source: package.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
