## Description:

Access the Crown Town Compost customer portal from a shell with curl to retrieve pickup and service history, invoices, upcoming service days, skips, and account details without running the crowntowncompost-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to script authenticated Crown Town Compost portal access for account, pickup, service, and billing information. It can also guide deliberate account actions such as skipping service, reporting issues, updating account details, contacting support, or entering cancellation flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through authenticated Crown Town Compost portal sessions and account-changing POST requests.

Mitigation: Require clear user confirmation before POST requests that skip service, update account details, report issues, contact support, or enter cancellation flow.

Risk: The skill handles sensitive account credentials and session cookies.

Mitigation: Protect the password and cookie jar, avoid exposing secrets in process arguments, and prefer read-only use unless an account change is intentional.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Crown Town Compost portal](https://portal.crowntowncompost.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that read portal data, handle an authenticated cookie jar, or perform account-changing POST requests when the user deliberately asks for them.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
