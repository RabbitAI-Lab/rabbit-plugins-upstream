## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl instead of running the artsonia-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Artsonia account holders use this skill to fetch account-authorized student artwork, profile, activity, feedback, fan, award, and image data from shell workflows. It also provides curl recipes for selected account write operations that should be used only with appropriate authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Artsonia account and student content.

Mitigation: Use it only with authorization for the relevant account and store cookies, downloaded pages, and images in private temporary locations with restrictive file permissions.

Risk: Some image download guidance reaches a public CDN without using the authenticated session.

Mitigation: Avoid unauthenticated private-image download workflows unless the account holder has explicitly authorized the download and retention of those images.

Risk: Write operations and fan invitations can change account state or notify other people.

Mitigation: Treat POST examples as real account actions, re-read the affected page to verify outcomes, and send fan invitations only to addresses you are authorized to contact.

Risk: The parser workflow may run external npm code from a local artsonia-mcp checkout.

Mitigation: Run the parser only after independently verifying the source and exact revision, or use the simpler curl and grep paths when structured parsing is not required.

## Reference(s):

- [Artsonia endpoint recipes](artifact/references/endpoints.md)
- [Artsonia member site](https://www.artsonia.com/members/)
- [Artsonia login](https://www.artsonia.com/members/login.asp)
- [Artsonia artwork image CDN pattern](https://images.artsonia.com/art/full/$artwork_id.jpg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes curl commands, parser one-liners, jq projections, and verification steps for read and write operations.]

## Skill Version(s):

0.12.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
