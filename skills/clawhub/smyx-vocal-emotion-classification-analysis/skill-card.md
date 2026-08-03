## Description: <br>
Classifies pet vocalization audio or video into emotion categories with acoustic features, confidence scores, structured reports, and report links while avoiding medical or behavior-modification advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze dog or cat vocalization media for emotion categories, confidence scores, and historical report lookup. It is intended for companionship, boarding, veterinary calming assessment, and behavior-training support, not for medical diagnosis or behavior-modification advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media files or media URLs are sent to the LifeEmergence cloud service for analysis. <br>
Mitigation: Use only media that is appropriate to share with that service, and avoid sensitive recordings unless the publisher documents authorization, retention, and handling terms. <br>
Risk: The skill can silently create or reuse a local account identity and store authentication tokens in a workspace SQLite database. <br>
Mitigation: Review workspace data storage and token handling before installation, and run the skill in a workspace where that local identity behavior is acceptable. <br>
Risk: Historical report lookup retrieves account-scoped cloud records. <br>
Mitigation: Confirm that cloud history access is expected for the workspace identity before using report-list features. <br>
Risk: Emotion classifications can be low-confidence or affected by noisy, mixed, too-short, or too-long vocalizations. <br>
Mitigation: Treat results as informational emotion classification only, and do not use them as medical, training, or behavior-correction advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocal-emotion-classification-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API 接口文档](references/api_doc.md) <br>
- [smyx_analysis API接口文档](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files] <br>
**Output Format:** [Structured text or JSON with optional Markdown tables and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the analysis result to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
