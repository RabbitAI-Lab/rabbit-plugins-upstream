## Description: <br>
Email Triage retrieves unread Microsoft mailbox messages, classifies them into T0-T3 priority tiers, generates an HTML daily report, and can send a brief text summary through enterprise WeChat or WeChat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenyang-x](https://clawhub.ai/user/zenyang-x) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees who need a morning mailbox briefing use this skill to prioritize unread work email, inspect high-priority items, and save an HTML dashboard for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads sensitive mailbox content and generates summaries from it. <br>
Mitigation: Grant only Microsoft connector scopes the user is comfortable with, preferably read-only mailbox access, and test with non-sensitive mail before routine use. <br>
Risk: HTML reports are saved to the Desktop mail report folder and summaries may be pushed to chat channels. <br>
Mitigation: Confirm the report folder location, local device access, enabled push channel, and exact recipient account or channel before enabling scheduled runs. <br>
Risk: The artifact includes a read-state repair step that may PATCH messages back to unread despite read-only claims. <br>
Mitigation: Remove or disable the PATCH read-state repair unless the user explicitly accepts that mailbox state may be modified. <br>
Risk: Automated priority classification may mis-rank urgent or low-priority messages. <br>
Mitigation: Treat the HTML dashboard as triage assistance and review original messages, especially T0 and T1 items, before acting. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, HTML, Files, API Calls, Guidance] <br>
**Output Format:** [HTML report file plus plain-text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Microsoft Graph mailbox fields; optional enterprise WeChat or WeChat notification.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
