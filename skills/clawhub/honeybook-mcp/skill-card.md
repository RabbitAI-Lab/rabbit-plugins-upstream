## Description:

This skill helps agents work with HoneyBook client-portal data for wedding-vendor contracts, invoices, brochures, proposals, payments, and portal sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users managing HoneyBook wedding-vendor portals use this skill to inspect shared files, workspace status, invoices, contracts, saved payment methods, and portal deep links. It supports user-directed session capture from vendor magic links and confirmation-gated signing or payment flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted HoneyBook magic links can grant portal access.

Mitigation: Use the skill only with intended vendor portal links and treat shared magic links as account-access material.

Risk: The skill handles sensitive portal data, including invoice, contract, workspace, session, and saved-payment-method details.

Mitigation: Install only for HoneyBook portal workflows where this data access is expected, and review agent outputs before acting on payment or contract information.

Risk: Signing and payment flows can affect real vendor relationships and obligations.

Mitigation: Require explicit user confirmation before returning signing or payment deep links, consistent with the artifact behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with portal status summaries and deep-link guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided HoneyBook magic links, locally cached sessions, invoice details, contract status, workspace details, and saved-payment-method details.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
