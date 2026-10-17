## Description:

Analyzes plant leaf images or videos for disease features and returns a likely diagnosis, confidence score, and general care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, gardeners, and agricultural teams use the skill to assess visible leaf symptoms from images or videos and review previous plant-disease reports. Its diagnoses are guidance, not a substitute for professional plant pathology advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or private media URLs may be sent to the publisher's cloud service.

Mitigation: Submit only media and URLs approved for cloud processing; seek the publisher's retention and privacy terms before sharing sensitive material.

Risk: The skill creates or reuses an internal identity and stores authentication tokens in a local workspace database.

Mitigation: Use a protected workspace and review identity and token handling before installation.

Risk: Report-history requests retrieve records from the publisher's cloud service.

Mitigation: Confirm user consent and the expected account scope before retrieving prior reports.

## Reference(s):

- [Plant leaf disease identification API reference](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured diagnosis report or report-history list, optionally written to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include disease likelihood, confidence, general care guidance, and report links.]

## Skill Version(s):

1.0.14 (source: server release; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
