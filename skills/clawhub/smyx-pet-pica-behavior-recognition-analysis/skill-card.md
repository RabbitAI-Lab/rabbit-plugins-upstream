## Description:

Analyzes indoor pet camera videos or video URLs through server-side APIs to detect sustained mouth contact with hazardous non-food items and return pica-behavior warnings, structured reports, recommendations, and report links without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, smart-home operators, and developers use this skill to analyze indoor camera footage for pet contact with wires, plastic, socks, tissues, or toy fragments, triggering warnings when sustained contact suggests a safety risk. It supports local video uploads, network video URLs, and cloud history/report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive indoor pet-camera videos or supplied video URLs may be sent to LifeEmergence cloud services and linked to cloud report history.

Mitigation: Use the skill only where cloud processing, account linkage, and report retention are acceptable; avoid highly private footage unless retention, deletion, and authorization controls are clear.

Risk: The skill may silently create or reuse an account identity and store or transmit identity tokens.

Mitigation: Deploy only in environments where local token storage and automatic identity association have been reviewed and approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Error Reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Structured analysis text, JSON details, Markdown tables for history results, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include warning levels, detected object categories, recommendations, and cloud report export URLs.]

## Skill Version(s):

1.0.7 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
