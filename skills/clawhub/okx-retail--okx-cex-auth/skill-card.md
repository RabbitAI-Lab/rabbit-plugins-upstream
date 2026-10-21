## Description:

Guides OKX CLI users through site selection, OAuth or API-key authentication, session checks, logout, and authentication troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX users and their agents use this skill to set up or restore CLI authentication, check login status, and resolve authentication errors before accessing account features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication leaves account access available to later CLI commands, potentially including trading actions.

Mitigation: Confirm the selected site and review granted scopes after login before using trading-related skills; log out when access is no longer needed.

## Reference(s):

- [OKX](https://www.okx.com)
- [OKX CEX Authentication on ClawHub](https://clawhub.ai/okx-retail/skills/okx-cex-auth)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and login instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the selected site and granted scopes after successful login.]

## Skill Version(s):

1.4.9 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
