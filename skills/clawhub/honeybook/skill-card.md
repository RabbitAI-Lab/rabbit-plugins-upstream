## Description:

Supports HoneyBook client-portal work by helping an agent view vendor contracts, invoices, workspace files, payment methods, and deep links for signing or paying.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect HoneyBook client-portal status across wedding vendors, including unsigned contracts, open or overdue invoices, shared files, saved payment methods, and portal links for signing or payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic-link sessions can grant HoneyBook portal access if shared or stored carelessly.

Mitigation: Paste HoneyBook magic links only when portal access is intended, treat those links like secrets, and remove cached sessions when the environment supports it.

Risk: Contract, invoice, workspace, and payment-method details may expose sensitive business or payment information.

Mitigation: Review retrieved portal data before sharing it and confirm user intent before returning signing or payment deep links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Text or Markdown summaries with HoneyBook portal deep links when requested and confirmed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include contract, invoice, workspace, session, and payment-method details returned from the HoneyBook portal.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
