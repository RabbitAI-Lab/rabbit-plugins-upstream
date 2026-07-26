## Description: <br>
Detects whether anyone has fallen within a specified target area and supports image and short video analysis for home-care and nursing-home safety monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, and care-facility operators use this skill to analyze existing images or short clips for suspected falls and review structured safety reports. The output is a screening aid and should be confirmed by a human before emergency or care decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private home, elder-care, or medical-adjacent images and videos may be uploaded to remote services for analysis. <br>
Mitigation: Use the skill only with media you are authorized to upload, avoid unnecessary personal or sensitive content, and confirm that remote processing is acceptable for the deployment. <br>
Risk: The skill can create or reuse an identity automatically and associate cloud report history with that identity. <br>
Mitigation: Run it only in workspaces where automatic account association is acceptable, and review report-history access expectations before use. <br>
Risk: Local token persistence in the workspace data directory may expose account-linked access if the workspace is shared. <br>
Mitigation: Restrict workspace access, clear persisted data when rotating users or environments, and avoid using shared workspaces for sensitive deployments. <br>
Risk: Fall-detection output may be incomplete or wrong and is not suitable as the sole basis for emergency decisions. <br>
Mitigation: Treat results as safety screening, require human confirmation, and follow established care or emergency response procedures for suspected falls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown text with structured analysis content, JSON report data, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return current analysis results or cloud report-history listings; results are safety references and not a substitute for human confirmation.] <br>

## Skill Version(s): <br>
1.0.8 (source: evidence.json release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
