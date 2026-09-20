## Description:

Environment-aware browser operations for UI testing, CDP shadow DOM tracing, and browser-login-assisted credential issuance using the appropriate visible or automatable backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to verify browser UI behavior, diagnose page state and closed shadow DOM styling issues, and assist credential issuance or refresh flows that require a visible browser session. It helps route work across wmux, cmux, Playwright MCP, and Chrome DevTools based on the user's environment and task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents through real browser sessions and credential issuance, refresh, extraction, storage, revocation, or publishing handoffs.

Mitigation: Require explicit confirmation for each credential source searched, token issued or revoked, storage destination, and cloud upload or publishing handoff.

Risk: Credential values could be exposed through chat, shell history, local files, or an unsuitable storage destination.

Mitigation: Prefer reusable secret stores such as Vault, OS keychains, GitHub secrets, or a password manager; avoid command-line passwords and do not leave issued credentials only in chat.

Risk: The bundled CDP trace script supports a login option and creates a browser context that ignores HTTPS certificate errors.

Mitigation: Do not use the login option against non-local HTTPS sites unless certificate validation is fixed, and keep credential entry in an interactive user-controlled browser session.

Risk: Browser automation can act in the wrong account or against an unintended visible session.

Mitigation: Verify the logged-in identity before creating, refreshing, revoking, or storing credentials, and confirm the target backend is visible and connected before continuing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI testing topic](artifact/ui-test.md)
- [CDP trace topic](artifact/cdp-trace.md)
- [Credential issuance topic](artifact/credential-issue.md)
- [Chrome DevTools Protocol DOM domain](https://chromedevtools.github.io/devtools-protocol/tot/DOM/)
- [CDP CSS.getMatchedStylesForNode](https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getMatchedStylesForNode)
- [Playwright browserContext.newCDPSession](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell, JavaScript, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes browser findings rather than returning raw snapshots; credential workflows may hand off commands for secret storage, revocation, or downstream automation.]

## Skill Version(s):

0.2.9 (source: server release and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
