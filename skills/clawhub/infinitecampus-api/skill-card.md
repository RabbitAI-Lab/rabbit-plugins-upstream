## Description: <br>
Guides an agent through direct, read-oriented curl and jq access to an authorized Infinite Campus Campus Parent portal for grades, attendance, assignments, schedules, messages, documents, and fees. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technically capable authorized portal users use this skill to query district-specific Infinite Campus parent portal data without running the MCP server. It is intended for scripted, read-oriented access where credentials, cookies, tokens, and student records can be handled privately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles private student records, credentials, live session cookies, XSRF tokens, terminal output, and downloaded portal files. <br>
Mitigation: Use only with authorization, keep credentials and session files out of shared or synced folders, avoid committing outputs, and delete temporary cookie jars and downloads when no longer needed. <br>
Risk: Some portal reads can expose grades, attendance, fees, messages, documents, and other sensitive education records in shell history or logs. <br>
Mitigation: Run commands in a controlled local environment, avoid logging command output, and review generated files before sharing or storing them. <br>
Risk: A message-body fetch may mark a portal message as read in some district configurations. <br>
Mitigation: Treat message retrieval as potentially state-changing and warn users before fetching individual message bodies. <br>


## Reference(s): <br>
- [Infinite Campus endpoint recipes](references/endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files] <br>
**Output Format:** [Markdown with shell command examples and endpoint reference guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of temporary cookie jars and downloaded portal documents; outputs can contain sensitive student records.] <br>

## Skill Version(s): <br>
2.4.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
