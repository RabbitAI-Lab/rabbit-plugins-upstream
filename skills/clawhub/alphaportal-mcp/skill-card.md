## Description:

Access AlphaPortal (AlphaRoute) school-bus data, including students, stops, live bus GPS, and arrival notifications, from a shell with curl by capturing a signed-in web app refresh token and minting API access tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and authorized AlphaPortal users use this skill to retrieve student transportation records, bus location, notifications, and related account data from shell scripts without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refresh tokens provide sensitive account access for several days if exposed.

Mitigation: Use only with accounts the user is authorized to access, avoid storing tokens in shell history, logs, scripts, or shared terminals, and rotate or recapture tokens when needed.

Risk: The optional browser-bridge path reads signed-in browser local storage.

Mitigation: Use the browser-bridge option only after reviewing and trusting the bridge and extension involved.

Risk: Write examples can change transportation records without a dry run.

Mitigation: Independently confirm the student ID, request body, and intended change before running any write command.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and jq command examples for authenticated AlphaPortal API calls.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
