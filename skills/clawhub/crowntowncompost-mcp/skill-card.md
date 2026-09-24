## Description:

Access the Crown Town Compost customer portal from a shell with curl to retrieve pickup history, invoices, upcoming service days, skips, and account details without running the crowntowncompost-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an existing Crown Town Compost portal account use this skill to retrieve service, billing, and account information from a shell. The skill also documents account-changing POST workflows that should be used only with deliberate user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes live account-changing workflows for service, profile, support, and cancellation state.

Mitigation: Require explicit user approval before any POST that changes account state, and re-read the portal after each write to verify the result.

Risk: The cookie jar and billing exports may expose account access or sensitive billing information if left unsecured.

Mitigation: Protect or delete the cookie jar after use, and store downloaded billing files only in a secure location.

Risk: Portal credentials are needed to create a session.

Mitigation: Read passwords from stdin or a credential manager rather than placing secrets directly in shell command arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)
- [Crown Town Compost endpoint reference](references/endpoints.md)
- [Crown Town Compost portal](https://portal.crowntowncompost.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl request patterns, CSRF handling notes, jq examples, and verification steps for account writes.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
