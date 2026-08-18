## Description:

Identifies prone sleeping positions, head covering, and occlusion of the mouth/nose by bedding or clothing; provides real-time high-risk alerts to safeguard infant sleep safety. | 婴儿趴睡窒息预警技能，识别俯卧睡姿、蒙头、口鼻被被褥/衣物遮挡，高风险实时报警，守护婴儿睡眠安全

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant sleep monitoring videos or image/video URLs for prone sleeping, head covering, and mouth or nose occlusion risks, and to return structured safety reports or history results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant sleep media, report metadata, and internally managed identity information may be sent to configured lifeemergence cloud services.

Mitigation: Use only with appropriate consent and data handling approval, and install only where cloud processing of this sensitive media is acceptable.

Risk: The skill may silently create and reuse cloud-linked identities, store tokens locally, and retrieve history through broad automatic triggers.

Mitigation: Review identity, token storage, and history lookup behavior before deployment; use an isolated account or controlled environment when testing.

Risk: The skill is an auxiliary infant sleep monitoring aid and should not be treated as a substitute for adult supervision or medical judgment.

Mitigation: Keep human supervision in place and treat high-risk alerts as prompts for immediate caregiver review and, when needed, professional care.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk level, detected sleep posture, mouth or nose coverage, head covering status, safety suggestions, history rows, and report links.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
