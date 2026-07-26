## Description: <br>
Helps quality managers and shop-floor supervisors classify manufacturing quality alerts, map escalation responsibilities and response times, and produce text and Markdown escalation boards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality managers, site supervisors, and operations teams use this skill to standardize L1-L4 quality-alert escalation, calculate response timeliness, and create auditable escalation reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quality-alert inputs may include internal manufacturing incident details or responder names. <br>
Mitigation: Use the skill only in an appropriate workspace and avoid entering sensitive business data unless the environment is approved for it. <br>
Risk: Generic escalation thresholds or responsibilities may not match a site's approved quality process. <br>
Mitigation: Review and adapt escalation levels, response-time limits, and responsible roles against enterprise policy before operational use. <br>
Risk: The skill can recommend escalation actions but does not make stop-line, release, or customer-notification decisions. <br>
Mitigation: Keep final operational decisions with authorized quality or management personnel. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-quality-alert-escalation) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-quality-alert-escalation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Plain text and Markdown reports with escalation workflow, escalation matrix, dashboard, and summary statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires quality-alert event details; organization-specific responsibilities and thresholds should be supplied by the enterprise.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
