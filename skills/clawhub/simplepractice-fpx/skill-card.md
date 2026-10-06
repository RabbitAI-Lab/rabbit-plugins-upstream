## Description:

Guides users through signing in to their own SimplePractice Client Portal and reading appointments, billing records, documents, announcements, and practice information with shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Portal users and their authorized assistants can retrieve their own appointments, billing records, documents, and practice details without running an MCP server. The skill offers shell-based sign-in and read-only request examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic links, PINs, session cookies, and browser profiles can grant access to sensitive medical records if exposed.

Mitigation: Keep credentials off shared machines and out of git and logs; restrict the cookie file to the account owner and remove the cookie and browser profile when no longer needed.

## Reference(s):

- [SimplePractice Client Portal request reference](references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and JSON:API response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal guidance; returned records may contain sensitive health information.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
