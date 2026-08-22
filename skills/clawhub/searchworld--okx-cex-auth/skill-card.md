## Description:

Guides agents through OKX CLI authentication, including regional site selection, OAuth device-flow login, API-key detection, login status checks, logout, and auth binary management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to authenticate an OKX CLI session before account, trading, portfolio, earn, or bot workflows, and to recover from expired or missing authentication state.

### Deployment Geography for Use:

Global, with explicit OKX site selection for Global, EEA, US, or TR endpoints.

## Known Risks and Mitigations:

Risk: Installing or using the OKX CLI can affect access to an OKX account if the package or command source is not trusted.

Mitigation: Confirm the OKX CLI package is trusted before installation and use the server-resolved package and homepage references when reviewing the release.

Risk: A wrong regional OKX site choice may persist and affect later CLI commands.

Mitigation: Require the user to explicitly choose the OKX site before login and verify the selected site during authentication status checks.

Risk: OAuth authorization may include trading-related scopes.

Mitigation: Have the user review OAuth scopes during authorization and proceed only with scopes appropriate for the intended workflow.

Risk: Existing or invalid API-key profiles can take precedence over OAuth and cause confusing authentication failures.

Mitigation: Run the documented pre-flight checks, then replace the API key or remove the API-key profile before switching entirely to OAuth.

Risk: OKX authentication state and site choice may persist for future CLI operations.

Mitigation: Use status checks before downstream workflows and logout or update configuration when the session or site should no longer be used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-auth)
- [OKX homepage](https://www.okx.com)
- [OKX CLI npm package](https://www.npmjs.com/package/@okx_ai/okx-trade-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to wait for user site selection and authorization signals before continuing authentication-sensitive workflows.]

## Skill Version(s):

1.4.4 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
