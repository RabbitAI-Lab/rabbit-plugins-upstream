## Description:

Analyzes submitted window or balcony footage for potentially dangerous child climbing or leaning behavior and returns alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and safety-system developers use this skill to analyze images or videos of window and balcony areas for child climbing hazards, review alerts, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's home-monitoring footage or video URLs may be uploaded to an external cloud service.

Mitigation: Obtain guardian consent before use and confirm the provider's retention, access, and deletion controls.

Risk: The skill may silently create or reuse an internal user identity and store authentication tokens locally.

Mitigation: Use a trusted environment, protect local credentials, and review how identities and tokens are managed.

Risk: Historical report links may expose sensitive footage or household monitoring records.

Mitigation: Restrict access to reports and avoid publicly sharing report links.

Risk: An alert may be missed or inaccurate in a child-safety setting.

Mitigation: Treat detection as an aid, not a replacement for adult supervision, and respond promptly to suspected hazards.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or JSON; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior alerts, risk information, and report links; can save a result file.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
