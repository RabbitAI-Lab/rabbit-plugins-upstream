## Description:

Helps an agent guide users through reading their own SimplePractice Client Portal data from a shell with curl, including authentication, appointments, billing items, documents, announcements, and related portal metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation-minded patients use this skill to retrieve their own SimplePractice portal records with shell commands instead of running a separate MCP server. It is focused on read-only portal data workflows such as appointments, invoices, statements, superbills, receipts, documents, announcements, practice details, and clinician information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles protected health information and authenticated portal data.

Mitigation: Use it only for your own SimplePractice portal data and avoid sharing outputs or command history that contain medical, billing, or identity details.

Risk: The cookie jar is a bearer credential for the medical portal.

Mitigation: Keep the cookie jar off shared machines and out of version control, restrict file permissions, and delete it when access is no longer needed.

Risk: The optional fpx path requests browser-cookie and local-storage access.

Mitigation: Use the fpx browser-cookie path only after reviewing and approving the requested Transporter permissions.

## Reference(s):

- [SimplePractice Client Portal request reference](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is read-only by design and centers on authenticated JSON:API requests made with curl.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
