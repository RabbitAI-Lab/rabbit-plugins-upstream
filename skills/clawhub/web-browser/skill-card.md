## Description:

Environment-aware browser operations for UI verification, CDP trace diagnostics, and browser-login-assisted credential issuance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to inspect visible browser UI, run interaction checks, diagnose closed shadow DOM styling issues, and coordinate login-assisted credential issuance or refresh workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate logged-in browser sessions and handle credentials, including token extraction, storage, reuse, revocation, and browser-profile file operations.

Mitigation: Require explicit per-action approval before reading existing secrets, extracting token values from pages, choosing a persistence destination, revoking credentials, or deleting browser profile files.

Risk: Credential values may be exposed or retained insecurely if they are copied through chat or stored in plaintext locations.

Mitigation: Use a dedicated secret store such as Vault, a provider secret store, or an OS keyring for long-lived credentials, and avoid plaintext ~/.env storage for long-lived secrets.

Risk: Automation in an authenticated browser can issue, expand, or revoke credentials for the wrong account if session identity is not checked.

Mitigation: Verify the logged-in account before sensitive browser actions and ask the user before account creation, revocation, destructive deletion, or ambiguous credential targeting.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI Test Guide](ui-test.md)
- [CDP Trace Guide](cdp-trace.md)
- [Credential Issue Guide](credential-issue.md)
- [Chrome DevTools Protocol DOM Domain](https://chromedevtools.github.io/devtools-protocol/tot/DOM/)
- [Chrome DevTools Protocol CSS.getMatchedStylesForNode](https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getMatchedStylesForNode)
- [Playwright BrowserContext.newCDPSession](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser-action plans, UI verification summaries, credential handoff commands, and CDP trace diagnostics.]

## Skill Version(s):

0.2.7 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
