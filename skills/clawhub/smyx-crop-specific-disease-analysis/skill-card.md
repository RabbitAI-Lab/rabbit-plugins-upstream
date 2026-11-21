## Description:

Expands the disease identification library to cover economic-crop-specific diseases (corn northern/southern leaf blight, potato late blight, peanut leaf spot, tomato viral disease, etc.) for precise leaf-disease recognition. | 扩充病害识别库至经济作物专属病害（玉米大斑病/小斑病、土豆晚疫病、花生叶斑病、番茄病毒病等），实现叶片病害的精准识别。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and crop advisers use this skill to identify visible leaf diseases in crops such as corn, potatoes, peanuts, and tomatoes from images or short videos, and to review structured reports. Results are for preliminary visual identification; the skill does not provide treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because reported account, history, and credential-handling capabilities go beyond the stated crop-disease purpose; scan coverage is partial.

Mitigation: Review the missing local reference and clarify credential and identity handling, history access, and unexpected analysis behavior before installing.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured disease analysis reports in JSON; historical report lists in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include disease type, confidence, symptom description, and a report link.]

## Skill Version(s):

1.0.18 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
