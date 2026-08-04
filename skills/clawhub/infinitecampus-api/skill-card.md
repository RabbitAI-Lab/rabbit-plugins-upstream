## Description: <br>
Query an authorized Infinite Campus Campus Parent portal directly with curl, using district-specific settings and user-supplied credentials to retrieve grades, attendance, assignments, schedules, messages, documents, fees, and related student records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, guardians, and developers with authorized Infinite Campus access use this skill to build curl-based workflows for reading student portal data without running the MCP server. It is intended for district-specific scripting and troubleshooting where the operator provides the portal URL, district app name, and credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles portal credentials, session cookies, XSRF tokens, and student records. <br>
Mitigation: Use only with authorized accounts, keep credentials in a trusted secret store or environment variables, avoid hardcoding passwords, and delete the temporary cookie jar after use. <br>
Risk: Document download URLs can be relative or absolute, which could expose session headers if an absolute URL is not checked. <br>
Mitigation: Validate any absolute document-download URL before sending the XSRF header or session cookie. <br>
Risk: Some district modules or endpoints may be disabled or unconfirmed, producing expected 404 responses rather than usable data. <br>
Mitigation: Check district display options before assuming a 404 is an error, and treat behavior and food service endpoints as module-dependent. <br>
Risk: Fetching a message body may mark the message as read on some district configurations. <br>
Mitigation: Warn users before retrieving message bodies and avoid doing so automatically when read state matters. <br>


## Reference(s): <br>
- [Infinite Campus endpoints for curl](references/endpoints.md) <br>
- [ClawHub skill release page](https://clawhub.ai/chrischall/skills/infinitecampus-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and jq command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a district portal URL, district app name, authorized portal credentials, and temporary cookie plus XSRF token handling.] <br>

## Skill Version(s): <br>
2.4.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
