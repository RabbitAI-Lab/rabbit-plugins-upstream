## Description:

OKX CEX Authentication guides agents through OKX CLI OAuth device-flow login, re-authentication, logout, and auth binary management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an OKX account to the OKX CLI, recover from authentication failures, and manage the auth helper binary before using trading, portfolio, earn, or bot workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive exchange authentication and can lead users into authorizing account access.

Mitigation: Confirm the selected OKX regional site and review the OAuth scopes shown in the browser before authorizing.

Risk: Users may confuse API-key setup with OAuth login and provide API-key credentials unintentionally.

Mitigation: Provide API-key credentials only when specifically choosing API-key setup instead of OAuth.

Risk: The required site-selection prompt has a localization caveat.

Mitigation: Ensure the user understands and explicitly selects the OKX site before any login attempt.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-auth)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and user-facing authentication status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface OAuth verification URLs, user codes, selected site identifiers, and scopes as plain text for user action.]

## Skill Version(s):

1.4.5 (source: server release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
