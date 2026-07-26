## Description: <br>
Analyzes side-view pet walking videos or URLs with AI pose estimation to report gait metrics, symmetry indicators, and possible lameness or restricted joint mobility without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, veterinary staff, and developers use this skill to submit side-view walking videos for vision-based gait screening, history lookup, and structured reporting on stride, stance and swing phase, left-right symmetry, and mobility indicators. The output is a reference analysis and does not replace veterinary orthopedic assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or video URLs are sent to a remote service for analysis. <br>
Mitigation: Use only media that the user is authorized to share, avoid sensitive footage, and confirm the service endpoint and retention expectations before installation. <br>
Risk: The skill can create or reuse a local identity and store local user or token data. <br>
Mitigation: Review account binding, token storage location, and cleanup or disablement options before deploying the skill in shared or regulated environments. <br>
Risk: History lookup retrieves prior report links from the cloud. <br>
Mitigation: Confirm that cloud report access matches the intended user account and that users understand how prior reports are stored, retrieved, and removed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-gait-analysis-lameness-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON results, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local video files or video URLs, optional pet type and detail level, and can query cloud history for prior reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
