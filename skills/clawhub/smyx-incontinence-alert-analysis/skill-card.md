## Description:

Analyzes care images and videos for wet clothing or excretion and provides alerts, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and care teams use the skill to review images or videos of elderly, bedridden, or infant care recipients for possible incontinence and to retrieve past care reports. Results support, but do not replace, direct checks and professional care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive care images or videos and identity-linked reports may be processed by lifeemergence.com cloud services.

Mitigation: Obtain consent before uploading, and confirm the provider's retention, access controls, and report-sharing practices.

Risk: Account and token management and report-history lookup happen automatically.

Mitigation: Review local token storage and the identity associated with cloud reports before using the skill.

Risk: Visual alerts may be inaccurate due to lighting, angle, or clothing thickness.

Mitigation: Have a caregiver check alerts directly; do not substitute the results for professional care.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Incontinence analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown report list with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis results to a file; supports basic, standard, and JSON detail levels.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release metadata; bundled SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
