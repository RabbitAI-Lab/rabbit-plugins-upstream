## Description:

Operates LinkedIn through an OOMOL-connected account by using the linkedin connector and oo CLI for profile retrieval, post creation, reshares, and post deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting users with an OOMOL-connected LinkedIn account can inspect live connector schemas, retrieve the authenticated member profile, create text, article, link, or reshare posts, and delete posts after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute remote installer scripts directly in a shell without verification.

Mitigation: Review the OOMOL CLI installer first and prefer a versioned, signed, or checksum-verified install method.

Risk: The skill can publish LinkedIn content or delete posts from the connected account.

Mitigation: Confirm the account, exact payload, expected effect, and raw post URN before running write or destructive actions.

Risk: Connector input and output contracts may change over time.

Mitigation: Inspect the live action schema immediately before constructing each connector payload.

## Reference(s):

- [ClawHub LinkedIn Skill](https://clawhub.ai/oomol/skills/oo-linkedin)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [LinkedIn](https://www.linkedin.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in OOMOL account with a connected LinkedIn OAuth2 credential; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
