## Description: <br>
Determines nine TCM constitution types including Yin deficiency, Yang deficiency, Qi deficiency, phlegm-dampness, and blood stasis through facial features and physical signs, and provides personalized health preservation and conditioning suggestions. | 中医体质识别分析技能，通过面部特征与体征判别阴虚、阳虚、气虚、痰湿、血瘀等九种中医体质类型，给出个性化养生调理建议 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to submit a face image, video, or media URL to a publisher cloud API for TCM constitution analysis and report-history retrieval. It returns structured wellness-oriented reports with constitution types, tendencies, scores, health-risk notes, and personalized diet, routine, exercise, and acupoint-care guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face, video, and health-analysis data may be sent to the publisher's cloud service. <br>
Mitigation: Review the publisher service and obtain appropriate user consent before sending sensitive media or health-related data. <br>
Risk: The skill may silently create or reuse an internal identity and store authentication tokens and user fields in a local workspace database. <br>
Mitigation: Run the skill in an isolated workspace, restrict local file access, and clear local identity or token storage when the session ends. <br>
Risk: Historical report requests may retrieve prior reports without a separate confirmation step. <br>
Mitigation: Require explicit user confirmation before report-history queries in production workflows and limit access to authorized users. <br>
Risk: TCM constitution outputs are wellness guidance and may be mistaken for medical diagnosis. <br>
Mitigation: Present reports as reference information only and direct users to qualified medical professionals for diagnosis or treatment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export URLs and report-history lists.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
