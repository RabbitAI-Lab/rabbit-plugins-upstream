## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from shell scripts using curl with an authenticated Artsonia session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and technically capable Artsonia account holders use this skill to work with authorized Artsonia account data from a shell without running the MCP server. It provides curl-based recipes for reading portfolios and related account pages, downloading artwork images, and performing account-changing form posts with verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive student artwork and account data.

Mitigation: Use it only with Artsonia accounts and student records the operator is authorized to access, and avoid bulk-saving artwork unless there is a clear right and retention plan.

Risk: The cookie jar grants access to an authenticated Artsonia session.

Mitigation: Store the cookie jar in a protected location, do not share it, and delete it when finished.

Risk: Write and invite-email recipes can change account state or send real invitations.

Mitigation: Require deliberate confirmation before running write actions, use only authorized recipient addresses, and verify results by re-reading the affected page.

Risk: The skill documents unauthenticated downloads of private artwork from a public CDN path.

Mitigation: Treat the private-artwork CDN behavior as a responsible-disclosure issue or remove it from normal usage guidance.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [Artsonia](https://www.artsonia.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell command blocks and parser recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read/write curl recipes, cookie-jar handling guidance, endpoint selectors, parser commands, and post-action verification steps.]

## Skill Version(s):

0.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
