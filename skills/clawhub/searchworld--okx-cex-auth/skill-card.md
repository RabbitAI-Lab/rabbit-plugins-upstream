## Description:

Guides an agent through OKX CLI authentication, including site selection, OAuth device-flow login, API-key detection, session status checks, logout, and okx-auth binary management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when connecting an OKX account to the OKX CLI, recovering from authentication failures, checking login status, or managing the auth helper binary. It helps agents avoid silent regional defaults and handle OAuth and API-key paths separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation triggers can start a financial-account authentication flow when the user's intent is ambiguous.

Mitigation: Use the skill only when the user intends to authenticate the OKX CLI, and require explicit confirmation before installing, updating, removing the auth binary, or starting login.

Risk: A language-fixed site-selection prompt and silent regional defaults can cause the user to authorize the wrong OKX site.

Mitigation: Confirm the selected OKX site or region before login and verify that the authorization URL matches the expected OKX site.

Risk: OAuth scopes may include live trading access for a financial account.

Mitigation: Review requested scopes before authorization and do not provide API key, secret key, or passphrase unless deliberately choosing API-key setup.

## Reference(s):

- [OKX](https://www.okx.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface OAuth verification URLs, user codes, selected site, and scopes; users should verify the site and permissions before authorizing.]

## Skill Version(s):

1.4.8 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
