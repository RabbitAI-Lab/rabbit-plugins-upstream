## Description:

Analyzes indoor pet videos for sustained contact with hazardous non-food objects and provides safety alerts and reports without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and home-monitoring developers use indoor camera videos or video URLs to identify possible chewing of wires, plastic, and other non-food items, review alerts, and retrieve past reports. Results are safety guidance, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor camera videos or video URLs are sent to a cloud service.

Mitigation: Start with a non-sensitive test video and verify the publisher's privacy and deletion terms before uploading personal footage.

Risk: The skill may create or reuse a local identity and store authentication tokens and report history.

Mitigation: Review this behavior before installation and avoid shared workspaces unless access to tokens and history is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety alerts, risk levels, recommendations, and report links.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
