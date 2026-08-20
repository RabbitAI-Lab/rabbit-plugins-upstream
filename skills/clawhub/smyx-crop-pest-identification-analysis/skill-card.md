## Description:

Triggers when a user provides images or videos of crop leaves, buds or fruits for pest identification, calls server-side APIs to detect common agricultural pests such as aphids, red spider mites, cotton bollworms and corn borers, and outputs pest types with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural users, crop advisors, and developers use this skill to analyze crop leaf, bud, or fruit images and videos for common pest types, estimated counts, confidence scores, and report links. It supports early pest discovery for crops such as tomato, corn, peanut, and cotton, while leaving treatment decisions to local plant-protection guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends crop media or URLs to a remote service and uses that service to retrieve report history.

Mitigation: Use it only with media that can be shared with the remote service, and avoid sensitive farm, location, or business data unless retention, deletion, and account controls are documented by the publisher.

Risk: The security evidence says the skill silently creates or reuses internal account identities and stores authentication tokens or profile data locally.

Mitigation: Review local workspace data handling and token storage before use, and run the skill in an environment where the generated identity and stored credentials can be inspected and removed.

Risk: The pest analysis is for agricultural reference and does not provide pesticide or treatment recommendations.

Mitigation: Treat outputs as observational support only and confirm pest-management actions with local plant-protection or agronomy guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Crop Pest Identification API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis reports with pest labels, counts, confidence scores, history tables, and optional output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local media paths or media URLs, supports crop-type and detail-level options, and can query cloud-hosted report history for the current internal identity.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
