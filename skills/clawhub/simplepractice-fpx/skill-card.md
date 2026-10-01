## Description:

Guides users through reading their own SimplePractice Client Portal appointments, billing records, documents, and practice information using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with access to their own SimplePractice Client Portal use this skill to retrieve appointments, billing documents, shared files, announcements, and practice details from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session cookies and retrieved portal data can expose sensitive health and billing information.

Mitigation: Keep the cookie jar private with restrictive permissions, avoid shared machines, and never commit or share credentials or outputs.

Risk: Signing documents, paying invoices, or changing appointments requires deliberate write actions outside this read-only guide.

Mitigation: Use the portal itself for signing, payments, cancellations, and other write actions.

## Reference(s):

- [SimplePractice FPX release](https://clawhub.ai/chrischall/skills/simplepractice-fpx)
- [SimplePractice Client Portal request reference](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for read-only retrieval of portal data; responses may contain sensitive health and billing information.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
