## Description:

覆盖理赔报案受理、材料处理、医疗审核、责任认定、理算调度、欺诈检测、核赔决策、结案通知全链路。从报案到结案的一站式智能理赔处理能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

理赔人员可将此技能用于整理报案、材料审核、责任分析和结案沟通等环节的参考草稿与核对清单。所有业务结论须由具备资质的人员复核，并由授权人员在机构系统中执行。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because some local references were unavailable.

Mitigation: Review the referenced materials before relying on the assessment, and treat the benign verdict as an assessment rather than a guarantee of safety.

Risk: Claim drafts may be mistaken for final coverage or payment decisions, and inputs may contain sensitive personal or medical information.

Mitigation: Mask sensitive data before use and have qualified claims staff verify drafts; authorized personnel should make decisions and carry out any system actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/gechengling/skills/claim-expert-digital-employee)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown and text drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference drafts and checklists with source labels; require qualified human review and do not perform claim-system actions.]

## Skill Version(s):

2.1.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
