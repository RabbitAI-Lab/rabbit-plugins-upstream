## Description:

Dependency checkup for owner-operators that identifies who can unilaterally change business rules, prices, access, supply, premises, licenses, key-person availability, or payment rails, and requires switching cost and time estimates for every high-risk dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Owner-operators and non-technical business leaders use this skill to map production-side dependencies across channels, premises, licenses, key people, supply, and payment rails. It helps them classify dependency risk, identify unassessed switching costs or timelines, and choose concrete next steps for Plan B preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist sensitive business dependency details, including suppliers, platforms, leases, key staff, payment channels, switching costs, and past incidents.

Mitigation: Confirm the configured memory path and anonymization settings before use, and avoid storing identifying details unless they are needed for the assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-dependency)
- [理论底座 · 依赖](references/理论底座.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown business dependency assessment with tables, prioritized findings, and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write configured memory notes for calibration when available; does not contact external parties.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
