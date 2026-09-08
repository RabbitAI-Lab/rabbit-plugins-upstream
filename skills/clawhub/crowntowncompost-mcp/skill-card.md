## Description:

Access the Crown Town Compost customer portal for pickup history, invoices, upcoming service days, skips, and account details from a shell with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and shell-oriented users use this skill to authenticate to the Crown Town Compost customer portal and retrieve service, billing, calendar, and account information without running the MCP server. It also provides guarded examples for account-changing portal actions such as skips, profile updates, support messages, and cancellation requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through live account-changing portal actions, including service skips, profile changes, support messages, and cancellation-related requests.

Mitigation: Require explicit user confirmation before running write-capable commands, and re-read the portal state after each write to verify the intended change.

Risk: The workflow stores authenticated session cookies in a local cookie jar.

Mitigation: Delete the cookie jar after use or store it with restrictive filesystem permissions.

Risk: Portal credentials and session access expose personal service, billing, and account information.

Mitigation: Install and run the skill only for workflows that need access to the user's Crown Town Compost account, and avoid scripting payments.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Crown Town Compost customer portal](https://portal.crowntowncompost.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local cookie jar and authenticated portal requests; users should review write-capable commands before execution.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
