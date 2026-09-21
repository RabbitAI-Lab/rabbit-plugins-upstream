## Description:

Access the Crown Town Compost customer portal (portal.crowntowncompost.com) for pickup and service history, invoices, upcoming service days, skips, and account details from a shell with curl instead of running the crowntowncompost-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide authenticated shell access to a Crown Town Compost customer portal session for reading service, billing, and account information. It also documents account-changing portal actions such as skips, support messages, missed-pickup reports, and profile updates that should be confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent using a saved authenticated portal session to make live changes to a customer compost-service account.

Mitigation: Require explicit confirmation before skip, account update, support submission, missed-pickup report, or cancellation-related actions, and re-read the portal state after any write.

Risk: A session cookie jar can grant account access if exposed.

Mitigation: Treat the cookie jar like a password and delete it after use.

## Reference(s):

- [Crown Town Compost portal endpoint reference](references/endpoints.md)
- [Crown Town Compost customer portal](https://portal.crowntowncompost.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes authenticated curl workflows for JSON endpoints and server-rendered pages.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
