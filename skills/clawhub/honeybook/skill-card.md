## Description:

Helps users review HoneyBook client-portal projects, vendor files, invoices, payments, questionnaires, meetings, tasks, and messages, and prepare portal actions with confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients can check vendor projects, contracts, invoices, payments, questionnaires, and messages, and request links to sign or pay or approved replies to vendors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cached portal sessions can expose access to client and vendor information on a shared or compromised device.

Mitigation: Use only for explicitly requested HoneyBook access; protect the device and delete cached sessions or rotate access if it is shared or compromised.

Risk: Reading portal records can expose sensitive invoices, payment details, contact information, and private messages.

Mitigation: Limit access and sharing to records needed for the user's request, and avoid exposing sensitive details unnecessarily.

Risk: Sending a portal message can email vendors and other workspace participants.

Mitigation: Show the message preview and obtain the user's explicit approval before sending.

## Reference(s):

- [HoneyBook skill on ClawHub](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown with portal links and message previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can summarize portal records or provide links for signing and payment; sending a message requires explicit confirmation.]

## Skill Version(s):

1.2.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
