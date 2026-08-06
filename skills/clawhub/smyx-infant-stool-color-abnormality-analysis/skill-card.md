## Description: <br>
Analyzes infant diaper or stool images to classify stool color, flag clay-pale or bloody findings, and return risk-oriented guidance and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, caregivers, pediatric clinics, postpartum care centers, and developers use this skill to screen infant stool images for color categories that may require observation, recapture, clinic follow-up, or urgent medical evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant diaper or stool images and report history are sensitive health data and may be uploaded to or retained by cloud services. <br>
Mitigation: Deploy only with explicit guardian consent, documented retention expectations, and an operator review of the cloud service terms before use. <br>
Risk: The skill can create or reuse hidden identity state and automatically query historical reports. <br>
Mitigation: Run it only in environments where automatic identity creation, local identity reuse, and report-history lookup are approved and auditable. <br>
Risk: Color classification is screening support and may be affected by lighting, filters, image quality, and context not visible in the image. <br>
Mitigation: Treat results as directional guidance, require recapture under appropriate lighting when quality is poor, and direct caregivers to qualified medical evaluation for abnormal findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Infant stool color API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured JSON or Markdown report with stool color class, risk level, recommended action, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hosted report export URLs and historical report-list results when the list workflow is used.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
