## Description:

Access Artsonia (artsonia.com) student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl instead of running the artsonia-mcp server — log in with a username/password form POST to get a session cookie, then curl the server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or guardians with an Artsonia account can use this skill to retrieve student portfolio details, comments, fans, teacher feedback, awards, profile information, and artwork downloads. It also provides commands for submitting comments, inviting fans, marking feedback read, and updating notification preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded pages and reusable login cookies may contain sensitive student information or account access.

Mitigation: Store cookies and downloaded pages in a private directory with owner-only permissions, then remove them after use.

Risk: Comments, invitations, and account changes can affect an Artsonia account; marking feedback read applies to all feedback for that student.

Mitigation: Explicitly request these actions and state their effects before submitting them; re-fetch the affected page to confirm changes.

Risk: The documented parser build relies on a separate repository.

Mitigation: Inspect that parser repository before running its install or build commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia endpoint recipes](artifact/references/endpoints.md)
- [Artsonia member site](https://www.artsonia.com/members/)
- [Artsonia artwork image CDN](https://images.artsonia.com/art/full/$artwork_id.jpg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use an Artsonia session cookie and can access student portfolio information or submit account changes.]

## Skill Version(s):

1.3.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
