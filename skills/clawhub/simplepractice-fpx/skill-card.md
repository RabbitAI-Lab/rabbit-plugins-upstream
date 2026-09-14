## Description:

Helps an agent guide users through reading their own SimplePractice Client Portal data from a shell with curl, including appointments, billing records, documents, announcements, practice details, and optional session-cookie capture with fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to provide shell commands for querying their own authorized SimplePractice Client Portal data without running an MCP server. The skill focuses on read-only portal access for appointments, billing information, documents, announcements, and practice or clinician details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles medical portal session cookies and protected health information.

Mitigation: Use it only with your own account or an authorized dependent account, keep the cookie jar private with restrictive permissions, keep it out of source control, and avoid shared machines.

Risk: The optional browser-cookie capture flow grants local tooling broader access than the normal curl workflow needs.

Mitigation: Prefer the magic-link curl flow when possible, use browser capture only for an already signed-in authorized session, and remove the fpx profile after seeding the cookie jar.

Risk: The global CLI and browser extension setup introduces package and extension trust decisions.

Mitigation: Use the unpinned global CLI path only after independently verifying the package and extension are acceptable for the environment.

## Reference(s):

- [SimplePractice Client Portal request reference](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
