## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl — sign in, list students, read the lunch calendar and cart, check orders, deliveries and payments. Use when you want My Hot Lunchbox data without running the MCP server, in a script, or on a machine where the MCP is not installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use this skill to access My Hot Lunchbox student, lunch-calendar, cart, order, delivery, subscription, and payment information from shell scripts when the MCP server is unavailable. They can also make account and order changes through the documented API, with payment and write actions requiring careful review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order, student, subscription, and payment actions can change account data or charge a saved card.

Mitigation: Review each requested change and the displayed payment total before sending a write or checkout request.

Risk: Write request bodies are untested, and omitted fields in read-modify-write requests can clear existing values.

Mitigation: Inspect the complete payload before sending it, then fetch the resource again to confirm the result.

Risk: Credentials and downloaded student or transaction records are sensitive.

Mitigation: Enter credentials privately, keep them out of command history, and protect downloaded account files.

## Reference(s):

- [My Hot Lunchbox endpoint reference](references/endpoints.md)
- [My Hot Lunchbox service API](https://ordernow.myhotlunchbox.com)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON data, PDF reports]

**Output Format:** [Markdown instructions with inline shell commands; API responses as JSON and printable reports as PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use account credentials and return account-specific student, order, and transaction data.]

## Skill Version(s):

1.3.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
