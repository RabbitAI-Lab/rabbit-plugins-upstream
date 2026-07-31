## Description: <br>
Combines facial blood flow and emotional characteristics to analyze stress index, anxiety tendency, and depression tendency, suitable for mental health monitoring scenarios. | 心理压力评估技能，结合面部血流与情绪特征，分析压力指数、焦虑倾向、抑郁倾向，适用于心理健康监测场景 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to assess psychological stress, anxiety tendency, and depression tendency from face images or videos and to retrieve prior assessment reports. The outputs are mental-health reference information and should not be treated as clinical diagnosis or a substitute for professional care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face media and inferred mental-health results may be sent to an external service. <br>
Mitigation: Use the skill only with explicit user consent, limit inputs to necessary media, and review retention and deletion terms before deployment. <br>
Risk: The skill may create or reuse an internal identity and retrieve prior cloud reports without clear confirmation. <br>
Mitigation: Require clear confirmation before uploads or history queries, and document identity handling without exposing internal identifiers. <br>
Risk: Session tokens or identity state may be stored in a local workspace database. <br>
Mitigation: Restrict workspace access and clear local state after use in shared or temporary environments. <br>


## Reference(s): <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, files] <br>
**Output Format:** [Markdown-formatted status text, structured JSON analysis, report links, and optional saved result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include stress index, anxiety tendency, depression tendency, report history entries, and export links returned by the external service.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter states 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
