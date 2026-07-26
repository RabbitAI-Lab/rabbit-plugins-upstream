## Description: <br>
Analyzes pet or home camera media to detect pet entry into an active UV disinfection area, assess UV lamp status, produce risk alerts, recommend shutdown actions, and retrieve historical reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to analyze pet safety risks in UV disinfection spaces from uploaded or URL-based media. It supports structured monitoring reports, high-risk alerts, UV lamp shutdown recommendations, and historical report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive pet and home camera media through the publisher's cloud services. <br>
Mitigation: Use only with media that may be sent to the publisher's service, and review cloud-processing expectations before deployment. <br>
Risk: The security evidence reports automatic identity creation or reuse, login to an external service, and local token storage. <br>
Mitigation: Review the code and clear local workspace data, databases, or tokens if the skill is no longer used. <br>
Risk: UV lamp state recognition can be affected by lighting conditions when visual glow detection is used. <br>
Mitigation: Prefer supported smart-home API linkage or device state signals where available, and treat visual-only detections as safety-supporting alerts rather than medical advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet UV safety monitor API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports with command-line usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk level, detected pet type, UV lamp status, recommended actions, event logs, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
