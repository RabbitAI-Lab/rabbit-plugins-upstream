## Description: <br>
Query an Infinite Campus Campus Parent portal district directly with curl by logging in with a real username and password, capturing the session cookie and XSRF token, and fetching grades, attendance, assignments, schedule, messages, documents, and fees. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch their own Infinite Campus portal data from a district-specific Campus Parent instance without running the Infinite Campus MCP server. It is useful for shell scripts or machines where the MCP is not installed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles an Infinite Campus password, session cookie jar, XSRF token, downloaded PDFs, and command output that may contain sensitive school records. <br>
Mitigation: Use a private working directory or secret store, avoid logging or sharing these values, and delete cookie jars and downloaded documents when they are no longer needed. <br>
Risk: The skill uses curl commands against a user's own Infinite Campus account and district portal. <br>
Mitigation: Install and run it only when comfortable authenticating directly with curl and only against the user's authorized district account. <br>


## Reference(s): <br>
- [Infinite Campus endpoints for curl](references/endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and curl/jq recipes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-oriented API call guidance; downloaded documents and command output may contain sensitive school records.] <br>

## Skill Version(s): <br>
2.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
