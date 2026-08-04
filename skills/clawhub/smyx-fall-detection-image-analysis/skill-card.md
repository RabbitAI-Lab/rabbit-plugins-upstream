## Description: <br>
Detects whether someone has fallen in a target area from images or short videos for elder-care and nursing-home safety monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, family members, and elder-care operators use this skill to submit images or short clips for fall-detection analysis and to view structured current or historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elder-care images, videos, and report-history queries may be sent to configured Life Emergence/SMYX cloud services. <br>
Mitigation: Use the skill only with appropriate consent and data-sharing permission, and prefer a dedicated workspace or account for sensitive elder-care media. <br>
Risk: The skill may silently create or reuse cloud identity and store account tokens in a local workspace database. <br>
Mitigation: Restrict access to the workspace, review or clear local workspace data after use, and avoid sharing the workspace with unrelated users. <br>
Risk: Fall-detection results are safety references and may be wrong or incomplete. <br>
Mitigation: Treat the report as screening support, confirm suspected falls directly, and follow the applicable emergency-response process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text reports, with optional JSON/detail output from command-line execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured fall-detection findings, risk feedback, recommendations, report links, or a Markdown table of historical reports.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
