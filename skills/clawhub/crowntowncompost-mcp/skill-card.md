## Description:

Access the Crown Town Compost customer portal from a shell with curl to retrieve pickup and service history, invoices, upcoming service days, skips, and account details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers or developers with valid Crown Town Compost portal credentials use this skill to query account data from scripts and shell sessions, and to prepare carefully reviewed curl commands for supported account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes live account-changing POST examples for service skips, missed-pickup reports, account updates, support messages, and cancellation workflows.

Mitigation: Require explicit user confirmation before executing any POST that changes service or account state, and re-read the portal after each write to verify the result.

Risk: The workflow stores authenticated portal session cookies in a local cookie jar.

Mitigation: Protect the cookie jar with appropriate filesystem permissions, delete it after use when persistence is not needed, and avoid sharing logs or files that contain session data.

## Reference(s):

- [Crown Town Compost portal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that may read account data or change account state when executed with valid credentials.]

## Skill Version(s):

0.5.2 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
