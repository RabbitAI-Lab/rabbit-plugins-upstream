## Description:

Access AlphaPortal (AlphaRoute) school-bus data from a shell by capturing a signed-in browser refresh token, minting access tokens, and calling the REST API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized AlphaPortal users use this skill to retrieve school-bus data, live vehicle locations, notifications, and related account information without running the MCP server. It is also used to build scripts around AlphaPortal API calls after a valid browser refresh token has been obtained.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The refresh token acts like a portable login credential and can be misused if copied, logged, or stored on an untrusted machine.

Mitigation: Use the skill only with authorized AlphaPortal accounts, keep the token out of logs and scripts, avoid shared machines, and recapture or rotate the token if exposure is suspected.

Risk: Write endpoints can change sensitive student transportation settings without a dry-run confirmation in the shell workflow.

Mitigation: Prefer the MCP path for write operations, review every payload before execution, and treat curl write commands as immediately effective.

Risk: API responses can expose student, stop, notification, and live vehicle-location data.

Mitigation: Limit command output and saved files to the minimum needed, avoid pasting responses into public or shared systems, and run commands only in trusted environments.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API endpoint paths, curl commands, token environment variable setup, jq filters, and cautions for write operations.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
