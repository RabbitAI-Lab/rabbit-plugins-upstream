## Description:

Access the Crown Town Compost customer portal from a shell with curl to retrieve pickup history, invoices, upcoming service days, skips, and account details without running the crowntowncompost-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate read access to Crown Town Compost portal data and to prepare shell commands for selected account actions. It is intended for users who have their own portal credentials and want scriptable access to service, billing, and account information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles portal credentials and stores a reusable session cookie.

Mitigation: Provide credentials only for accounts the user controls, avoid logging returned billing or account data, and delete or restrict access to the cookie jar after use.

Risk: The documented POST workflows can change account state, including skips, account updates, support messages, missed-pickup reports, or cancellation-related actions.

Mitigation: Require explicit user confirmation before any account-changing request and re-read the portal after each write to verify the resulting state.

## Reference(s):

- [Crown Town Compost portal endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces curl-based workflows and parsing guidance; does not include executable bundled code.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
