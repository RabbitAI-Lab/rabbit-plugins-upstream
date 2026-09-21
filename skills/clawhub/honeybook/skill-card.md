## Description:

Provides HoneyBook client-portal assistance for contracts, invoices, questionnaires, messages, meetings, tasks, payments, and vendor workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to read and manage HoneyBook client-portal data across wedding vendors, including contracts, invoices, questionnaires, messages, meetings, tasks, notes, attachments, and payments. It supports confirmed actions such as generating sign or pay links and sending portal messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive HoneyBook portal, vendor, contract, invoice, payment-related, and message data.

Mitigation: Install and invoke it only for HoneyBook workflows where the user expects the agent to handle that portal data.

Risk: The skill stores HoneyBook session credentials locally.

Mitigation: Use it only on trusted environments and remove stored sessions when access is no longer needed.

Risk: Broad trigger wording around invoices, contracts, planners, vendors, and payments may activate the skill for general requests.

Mitigation: Confirm that the request is intended to use HoneyBook data before reading portal records or preparing actions.

Risk: Sending HoneyBook portal messages can contact vendors and co-clients.

Mitigation: Preview outgoing messages and require explicit confirmation before sending.

## Reference(s):

- [ClawHub honeybook skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Structured data, Deep links, Guidance]

**Output Format:** [Markdown-style agent responses with structured HoneyBook portal data and portal links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions require explicit confirmation before producing sign, pay, or send-message outcomes.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
