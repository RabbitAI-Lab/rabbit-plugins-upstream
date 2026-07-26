## Description: <br>
Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition to support home risk monitoring for patients with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, and healthcare-support teams use this skill to submit local or URL-based monitoring media for abnormal movement analysis and to retrieve cloud-hosted report history. Results are for auxiliary monitoring and should not replace clinical diagnosis or physician judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive health-related monitoring videos may be sent to the lifeemergence cloud service and associated with report history. <br>
Mitigation: Use only with explicit consent from recorded individuals, review the provider's privacy and retention terms, and avoid sensitive household footage unless those terms are acceptable. <br>
Risk: The skill silently creates or reuses an identity and can persist service tokens locally. <br>
Mitigation: Limit workspace access and review or clear the workspace data database when persisted service tokens or identity-linked history should not remain. <br>
Risk: Behavior-recognition results could be mistaken for medical diagnosis. <br>
Mitigation: Present results as auxiliary monitoring only and defer diagnosis, treatment changes, and urgent care decisions to qualified medical professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis) <br>
- [API 接口文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Structured text, Markdown tables, and JSON-style analysis output with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include abnormal-behavior analysis, monitoring suggestions, cloud report history, and exported report links.] <br>

## Skill Version(s): <br>
1.0.7 (source: server-resolved release metadata; SKILL.md frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
