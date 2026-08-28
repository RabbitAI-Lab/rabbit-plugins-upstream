## Description:

Environment-aware browser operations for UI verification, closed shadow DOM CDP tracing, and login-assisted credential issuance across wmux, cmux, Playwright, and chrome-devtools backends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect browser UI state, run visible browser interaction checks, diagnose closed shadow DOM styling issues, and assist credential issuance through authenticated browser sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential workflows can direct an agent to find, extract, store, reuse, reset, or revoke secrets with too little per-action user control.

Mitigation: Use test accounts or tightly scoped tokens, require explicit approval before token issuance, reset, or revoke actions, reject temp-file token handoffs unless necessary, and decide the exact secret-store destination before persistence.

Risk: Authenticated browser automation can expose real accounts, raw credentials, or sensitive post-login pages.

Mitigation: Keep sign-in interactive and visible to the user, avoid invisible browser backends for fresh login flows, and persist credentials only to an approved reusable secret store.

## Reference(s):

- [Web Browser Skill](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI Test Topic](ui-test.md)
- [CDP Trace Topic](cdp-trace.md)
- [Credential Issue Topic](credential-issue.md)
- [Chrome DevTools Protocol DOM Domain](https://chromedevtools.github.io/devtools-protocol/tot/DOM/)
- [Chrome DevTools Protocol CSS.getMatchedStylesForNode](https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getMatchedStylesForNode)
- [Playwright browserContext.newCDPSession](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JavaScript snippets, and browser-operation steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include UI verification findings, CDP trace interpretation, credential handoff steps, and secret-store persistence guidance.]

## Skill Version(s):

0.2.8 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
