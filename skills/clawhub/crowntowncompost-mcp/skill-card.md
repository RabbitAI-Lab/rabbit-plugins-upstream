## Description:

Guides an agent through using curl to log in to the Crown Town Compost customer portal and retrieve or update service, billing, account, and support information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers or operators with Crown Town Compost portal credentials use this skill to guide agents in querying service history, invoices, upcoming pickup days, environmental impact figures, and account pages from a shell. Account-changing actions should be treated as deliberate operations that are reviewed before execution and verified afterward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents POST requests that can change account state, including skip or unskip service, account updates, support messages, missed-pickup reports, and cancellation-related actions.

Mitigation: Review each command before running it, avoid delegating write actions blindly, and re-read the relevant portal page after every write to verify the intended result.

Risk: The workflow uses a persistent session cookie jar and Crown Town Compost portal credentials.

Mitigation: Store credentials securely, avoid exposing passwords in process arguments, protect the cookie jar, remove it after use, and avoid running the workflow on shared machines.

Risk: Billing responses may include Stripe invoice, receipt, or hosted payment links.

Mitigation: Use browser-based review for payment flows and do not script payment submission or card entry.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)
- [Crown Town Compost portal](https://portal.crowntowncompost.com)
- [Endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command snippets and endpoint reference examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided portal credentials and a local cookie jar; some documented commands can perform account-changing POST requests.]

## Skill Version(s):

0.6.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
