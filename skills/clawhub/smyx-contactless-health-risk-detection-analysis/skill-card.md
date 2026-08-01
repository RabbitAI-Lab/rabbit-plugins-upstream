## Description: <br>
Combines frontal facial image capture with multimodal physiological feature analysis to provide early risk screening and alerts for chronic and acute conditions such as heart attack, stroke, hypertension, and hyperlipidemia. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit frontal facial images or videos for contactless early health-risk screening and to retrieve prior cloud reports. Results are screening references and do not replace professional medical diagnosis or examination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive facial image or video inputs and health-risk outputs may be sent to Life Emergence cloud APIs. <br>
Mitigation: Use the skill only with appropriate consent and data-handling approval for cloud processing of facial and health-risk data. <br>
Risk: The skill may create or reuse a local identity, persist account tokens in a workspace database, and query prior cloud reports automatically. <br>
Mitigation: Review local workspace data retention, token storage, and history-query behavior before installation or deployment. <br>
Risk: Screening outputs may be mistaken for medical diagnosis. <br>
Mitigation: Present outputs as early risk-screening references and direct high-risk users to professional medical diagnosis and examination. <br>


## Reference(s): <br>
- [API 接口文档](artifact/references/api_doc.md) <br>
- [SMYX Analysis API 文档](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-health-risk-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown or JSON structured health-risk screening report with optional report links and historical report lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the rendered result to a requested output file.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
