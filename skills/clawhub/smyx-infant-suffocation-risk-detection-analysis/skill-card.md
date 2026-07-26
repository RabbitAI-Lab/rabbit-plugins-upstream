## Description: <br>
Analyzes infant crib video or image inputs to classify sleep posture, detect mouth/nose occlusion, and return structured suffocation-risk alerts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, childcare operators, and developers use this skill to process crib-monitor media, identify prone sleeping or face occlusion, and produce risk-level alerts for infant sleep monitoring. Outputs are visual risk assessments and should not be treated as medical diagnosis or a replacement for adult supervision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive infant bedroom videos or video URLs may be uploaded to a cloud service and associated with a silently managed local identity. <br>
Mitigation: Use only with guardian consent and after confirming backend account ownership, token storage, report storage, retention, deletion, and access controls. <br>
Risk: History and export links may expose child-monitoring reports if link access, expiration, or sharing controls are unclear. <br>
Mitigation: Confirm report link expiration and access policy before deployment, and restrict use to environments where exported reports can be protected. <br>
Risk: Visual risk alerts can be incorrect or delayed and are not medical diagnosis. <br>
Mitigation: Use the skill as an auxiliary monitoring signal only, keep adult supervision in place, and verify high-risk alerts directly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-suffocation-risk-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown tables and narrative text, with JSON available through the detail option.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk levels, sleep posture, face occlusion status, event timing, snapshots, alert text, recommendations, and report or export links.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
