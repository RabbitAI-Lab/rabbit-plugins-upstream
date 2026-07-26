## Description: <br>
Helps frontline manufacturing and quality teams create a QRQC response board for same-day issue capture, ownership, escalation, and closure tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Frontline team leads, manufacturing supervisors, and quality engineers use this skill during shift quality meetings to record anomalies, assign owners, track containment actions, and decide whether issues are closed, tracked across shifts, or escalated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may provide sensitive production, customer, or quality data while building QRQC boards. <br>
Mitigation: Confirm the data is appropriate to share with the agent before use and follow site confidentiality rules. <br>
Risk: The submitted artifact references a report-building script that is not included. <br>
Mitigation: Treat script-based report generation as unavailable unless an installer separately supplies and reviews that script. <br>
Risk: Prematurely marking an issue closed could hide unresolved quality problems. <br>
Mitigation: Require explicit owner and closure-time confirmation, and keep incomplete fields marked as "待补充". <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-qrqc-quick-response) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-qrqc-quick-response) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Plain text and Markdown QRQC war room boards] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Marks missing fields as "待补充" and does not generate web output.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
