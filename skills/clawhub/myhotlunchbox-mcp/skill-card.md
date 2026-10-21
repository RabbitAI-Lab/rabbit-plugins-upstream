## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl — sign in, list students, read the lunch calendar and cart, check orders, deliveries and payments. Use when you want My Hot Lunchbox data without running the MCP server, in a script, or on a machine where the MCP is not installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents can use curl-based shell guidance to access My Hot Lunchbox student, calendar, cart, order, delivery, and payment information without the MCP server. The skill also describes account-changing operations for use in scripts or a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified account-changing commands may overwrite or delete data without consistently requiring confirmation.

Mitigation: Start with read-only operations; prefer the website for changes until write payloads are verified; require explicit preview and approval before deletions, order changes, or subscription changes; confirm the exact total before payment; protect credentials and exported records.

## Reference(s):

- [My Hot Lunchbox endpoints reference](artifact/references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [My Hot Lunchbox service](https://ordernow.myhotlunchbox.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Printable report commands return PDF files; account-changing commands require careful review.]

## Skill Version(s):

1.2.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
