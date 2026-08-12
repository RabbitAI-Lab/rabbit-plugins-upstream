## Description:

Web Browser routes an agent to visible browser backends for UI verification, CDP shadow DOM style diagnosis, and browser-login-assisted credential issuance or refresh.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to verify browser-visible UI behavior, diagnose page state and closed shadow DOM styling, and handle login-assisted credential issuance, refresh, revocation, persistence, and handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can find, create, extract, persist, reuse, and revoke credentials through logged-in browser sessions.

Mitigation: Require explicit approval for each credential source, token issuance, scope expansion, secret-store write, and revoke action before the agent proceeds.

Risk: Credential material could be stored in long-lived locations such as .env files, skill data, or secret stores.

Mitigation: Prefer scoped credentials and approved secret stores; avoid .env or skill-data storage unless the operator accepts the long-term exposure risk.

Risk: Multi-account browser sessions can issue credentials under the wrong account or revoke the wrong credential.

Mitigation: Verify the logged-in identity before issuance, verify the issued credential after handoff, and require an exact key or token identifier match before revocation.

Risk: Interactive login in an invisible or headless browser can block the user from controlling authentication.

Mitigation: Use a user-visible backend for fresh login flows and reserve invisible Playwright-style automation for sessions that are already authenticated.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI Test Guide](ui-test.md)
- [Credential Issue Guide](credential-issue.md)
- [CDP Trace Guide](cdp-trace.md)
- [Chrome DevTools Protocol DOM Domain](https://chromedevtools.github.io/devtools-protocol/tot/DOM/)
- [CDP CSS.getMatchedStylesForNode](https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getMatchedStylesForNode)
- [Playwright BrowserContext.newCDPSession](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes UI findings instead of returning raw browser snapshots; credential workflows may produce commands or configuration for secret storage and downstream automation.]

## Skill Version(s):

0.2.6 (source: server release evidence, changelog released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
