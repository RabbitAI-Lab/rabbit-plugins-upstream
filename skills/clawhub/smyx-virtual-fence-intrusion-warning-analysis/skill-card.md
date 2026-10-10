## Description:

Analyzes home monitoring video for virtual-fence crossings and provides infant safety alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to analyze monitoring videos for infants leaving designated safe zones or approaching hazardous areas, and to view current and historical alert reports. Alerts support, but do not replace, physical safeguards and adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos of children or home interiors may be sent to a cloud service without clear consent.

Mitigation: Obtain explicit consent before uploading media or sharing media URLs, and review the service's data-handling terms.

Risk: Silent identity selection and local account creation can link sensitive reports to an account without the user's awareness.

Mitigation: Disclose account linking, require explicit authorization, and remove hidden identity overrides.

Risk: Returned authentication tokens are stored in a shared workspace database.

Mitigation: Avoid persistent token storage where possible; otherwise restrict access and protect stored tokens.

Risk: Missed or inaccurate alerts could create a false sense of infant safety.

Mitigation: Treat alerts as supplementary and maintain physical safeguards and adult supervision.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results and Markdown report links or tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk notices and links to current or historical reports.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
