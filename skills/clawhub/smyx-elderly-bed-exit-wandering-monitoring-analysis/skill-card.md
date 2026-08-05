## Description: <br>
Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods. It is suitable for night-time safety monitoring in nursing homes and for elderly people living alone. | 老人离床徘徊监测技能，识别夜间起床离床、长时间徘徊、长时间静止不动异常行为，适用于养老院、独居老人夜间安全监测 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Care teams, families, and developers can use this skill to analyze nighttime elder-care videos or video URLs for bed-exit, wandering, and prolonged immobility events, then review structured reports or report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elder-care footage may be uploaded to a cloud service for analysis. <br>
Mitigation: Use only authorized footage, minimize identifying content where possible, and confirm cloud data handling is acceptable before deployment. <br>
Risk: The skill may create or reuse a local identity and store service tokens in the workspace. <br>
Mitigation: Run it in a dedicated workspace with restricted access, and remove or rotate stored identity and token data when it is no longer needed. <br>
Risk: Automatic history report lookup can expose identity-linked elder-care reports. <br>
Mitigation: Limit who can trigger report-list queries and verify that report access is appropriate for the care setting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown or JSON analysis reports, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video files or public video URLs; documented formats are mp4, avi, and mov with a 10 MB maximum input size.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release evidence; artifact frontmatter is 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
