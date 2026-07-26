## Description: <br>
Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods, for night-time safety monitoring in nursing homes and for elderly people living alone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Care teams, family caregivers, and developers use this skill to analyze night-time elderly monitoring video for bed-exit, wandering, prolonged immobility, risk indicators, recommendations, and cloud report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends elderly monitoring videos, URLs, identity-linked requests, and report history to an external cloud service. <br>
Mitigation: Use only with appropriate consent and data handling approval, avoid unnecessary identifying content, and review the configured service endpoints before deployment. <br>
Risk: The skill can silently create local user records and store authentication tokens in the workspace data area. <br>
Mitigation: Run it in an isolated workspace, restrict access to the workspace data directory, and remove local identity or token state when it is no longer needed. <br>
Risk: Monitoring results are safety-support information and may be incorrect or incomplete. <br>
Mitigation: Require caregiver review and on-site confirmation before acting on abnormal-behavior alerts or health-related conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Elderly monitoring API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content, analysis status, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local mp4, avi, or mov files up to 10 MB, or public video URLs that are processed by the cloud analysis service.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
