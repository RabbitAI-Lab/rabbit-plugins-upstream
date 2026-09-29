## Description:

Detects morbid behavioral cues in poultry and pigs from continuous barn videos — such as difficulty standing, ruffled feathers/piloerection, isolation, drowsiness and appetite loss — and outputs behavior type with risk level up to 2-3 days ahead of visible clinical signs. | 识别站立困难、羽毛蓬松、离群、嗜睡等病态行为，比人工观察提前2-3天。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, veterinarians, and developers use this skill to screen fixed-camera barn images or videos for poultry or swine behavioral abnormalities and receive structured reports with behavior types, locations, risk levels, group morbidity ratios, and report links. The output is for early screening support, not formal diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn images, videos, or media URLs are sent to a configured external service for analysis.

Mitigation: Deploy only where users and data owners accept that transfer, and avoid submitting media that contains unrelated sensitive content.

Risk: The skill can create or reuse a local identity cache and access account-linked history reports.

Mitigation: Review identity and token handling before installation, restrict workspace access, and confirm that history lookup behavior matches the deployment policy.

Risk: Behavior screening results could be mistaken for veterinary diagnosis or treatment guidance.

Mitigation: Present results as early screening support and require qualified veterinary or laboratory confirmation before disease diagnosis or medication decisions.

## Reference(s):

- [API 接口文档](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown reports and tables, with optional JSON detail output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links, behavior labels, risk levels, locations, group morbidity ratios, and analysis timestamps.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
