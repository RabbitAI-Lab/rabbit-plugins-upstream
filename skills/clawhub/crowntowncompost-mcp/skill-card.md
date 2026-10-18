## Description:

Guides agents in accessing Crown Town Compost customer-portal service history, invoices, schedules, and account details through authenticated shell requests without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Crown Town Compost customers and their authorized agents can retrieve pickup history, billing information, and upcoming service details from the customer portal, or prepare carefully reviewed account requests, without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials and a saved login session could expose customer and billing information if disclosed.

Mitigation: Grant access only to a trusted agent, protect credentials and the cookie jar with restrictive permissions, and delete the cookie jar after use.

Risk: Skipping service, changing account details, submitting support requests, reporting missed pickups, or requesting cancellation can alter the customer's account.

Mitigation: Require explicit customer confirmation before each account-changing request, review submitted fields, and re-read the portal to verify the result.

Risk: A partial account-details update can unintentionally turn off notification preferences.

Mitigation: Read current values first and submit all account fields and intended preference settings together.

## Reference(s):

- [Crown Town Compost portal endpoint reference](references/endpoints.md)
- [Crown Town Compost customer portal](https://portal.crowntowncompost.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover authenticated portal requests and interpretation of service and billing responses.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
