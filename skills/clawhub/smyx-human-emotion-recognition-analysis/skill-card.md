## Description: <br>
Analyzes frontal face images or videos with a cloud visual AI service to produce emotion recognition results, abnormal emotion flags, report links, and history lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to analyze user-provided face media for structured emotion recognition reports and report-history retrieval. Results are for reference only and should not be treated as psychological counseling or clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images or videos and inferred emotion or mental-state data are sent to the publisher's cloud service. <br>
Mitigation: Use only with appropriate consent and authorization, and avoid uploading sensitive media unless cloud processing is acceptable. <br>
Risk: Report history is account-linked and may retrieve prior cloud analysis results for the resolved identity. <br>
Mitigation: Review history output before sharing it, and segregate or clear workspace identity data when reports should not be reused across sessions. <br>
Risk: The skill may store account tokens in a local workspace SQLite database. <br>
Mitigation: Restrict workspace access and remove local token/database files when decommissioning or transferring the workspace. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API reference](references/api_doc.md) <br>
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with optional report links and saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video files or public media URLs, supports basic/standard/json detail levels, and can query cloud report history.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
