## Description:

Guides an agent through reading a user's own SimplePractice Client Portal data from a shell with curl against the portal JSON:API, including appointment, billing, document, announcement, practice, and clinician information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to access their authorized SimplePractice Client Portal records without running the SimplePractice MCP server. It is intended for scripted or shell-based retrieval of portal data while preserving the user's control over credentials and session cookies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive health, billing, and live portal session credentials.

Mitigation: Use it only for an authorized portal, keep the cookie jar out of shared folders and git, and remove the fpx profile or cookie jar when access is no longer needed.

Risk: Browser cookie capture can grant broad portal access from an existing signed-in session.

Mitigation: Prefer the email magic-link flow when possible and use fpx capture only when the user is already signed in and accepts the credential exposure.

## Reference(s):

- [SimplePractice Client Portal request reference](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON:API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance only; users provide their own portal host, email, token, and cookie jar path.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
