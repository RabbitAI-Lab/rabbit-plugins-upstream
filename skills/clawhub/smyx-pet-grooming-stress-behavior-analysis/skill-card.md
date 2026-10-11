## Description:

Analyzes pet grooming videos or video URLs for stress-related behaviors and returns a graded report to help groomers respond.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet groomers, veterinary staff, and pet care providers use this skill to review grooming footage for signs of stress and view graded behavior reports or cloud report history. It is an observational aid, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grooming videos or video URLs are sent to a cloud service and may contain sensitive customer or clinic footage.

Mitigation: Use only with appropriate consent and after checking the provider's access controls and retention policy.

Risk: The skill may silently create or reuse a cloud-linked identity and store tokens locally.

Mitigation: Review the identity and local token behavior before installation, and limit use to trusted environments.

Risk: Cloud report history can be retrieved with limited user control.

Mitigation: Confirm the intended account and permissions before requesting history, and avoid sharing report links beyond authorized recipients.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown behavior report or history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a report to a local file and link to cloud reports.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
