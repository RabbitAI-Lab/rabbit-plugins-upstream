## Description:

Analyzes pet grooming videos for stress signals such as struggling, panting, and tail tucking, and provides stress-level reports to help groomers respond.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Groomers and pet-care or veterinary staff use the skill to assess stress behavior in grooming videos, review graded reports, and decide when to pause or adjust care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grooming videos or video URLs are sent to external Lifeemergence/Open API services, potentially exposing sensitive customer, shop, or clinic footage.

Mitigation: Obtain appropriate consent and confirm the publisher's data retention and deletion terms before submitting sensitive footage.

Risk: The skill can silently create or reuse an identity, store service tokens locally, and retrieve identity-linked historical reports.

Mitigation: Review identity and token handling before installation, restrict access to the workspace, and confirm account and report-access terms with the publisher.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Pet grooming stress analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown reports or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stress grades, behavior observations, recommendations, and report links; historical reports can be listed.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
