## Description: <br>
Read Workday HR data from a shell with the fpx CLI through the user's already signed-in myworkday.com browser session, without running the workday-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, developers, and operators use this skill to fetch their own Workday tasks, pay, benefits, compensation, and app menu data from an authenticated browser session. It provides setup, endpoint selection, jq projection, and troubleshooting guidance for read-only Workday data access through fpx. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using fpx with a signed-in Workday browser session can expose sensitive HR data or session tokens if raw responses are printed or logged. <br>
Mitigation: Treat all outputs as sensitive, keep the documented jq field projections, and avoid dumping raw Workday response envelopes. <br>
Risk: An expired SSO session can return a login or SAML page instead of JSON while still appearing as a successful fetch. <br>
Mitigation: Check that responses are JSON from the expected Workday tenant host, then reauthenticate in the browser before retrying when a login page is returned. <br>


## Reference(s): <br>
- [Workday htmld endpoint recipes](references/endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only guidance for fetching and projecting Workday JSON responses; outputs may contain sensitive HR data.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
