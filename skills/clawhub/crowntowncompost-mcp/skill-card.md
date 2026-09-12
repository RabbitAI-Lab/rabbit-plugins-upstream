## Description:

Provides curl-based guidance for signing in to the Crown Town Compost portal and retrieving or managing pickup history, invoices, upcoming service days, skips, and account details without running the crowntowncompost-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with Crown Town Compost portal credentials use this skill to script account lookups, service history review, invoice checks, and carefully approved account or service changes from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to read account, service, and billing-related data from a signed-in Crown Town Compost portal session.

Mitigation: Use only with the account holder's explicit consent and limit commands to the specific lookup requested.

Risk: The skill describes actions that can change service or account state, including skips, profile updates, support messages, missed-pickup reports, and cancellation-related requests.

Mitigation: Require explicit approval before any write action and re-read the portal page or endpoint afterward to verify the result.

Risk: A reusable session cookie jar may expose portal access if stored insecurely.

Mitigation: Use a private temporary cookie jar with 0600 permissions on a trusted machine and delete it after use.

Risk: Billing responses may expose payment-related links.

Mitigation: Do not script payment flows or card entry; open payment actions in a browser only when the user deliberately requests them.

## Reference(s):

- [Endpoint reference](artifact/references/endpoints.md)
- [Crown Town Compost portal](https://portal.crowntowncompost.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command blocks and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied Crown Town Compost portal credentials and a local private cookie jar.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
