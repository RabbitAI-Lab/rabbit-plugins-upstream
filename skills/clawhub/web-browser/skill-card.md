## Description: <br>
Environment-aware browser operations for UI verification, closed shadow DOM cascade diagnosis, and browser-login-assisted credential issuance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to inspect browser UIs, verify user-visible flows, diagnose closed shadow DOM styling, and help issue or refresh service credentials after user-controlled login. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help create, extract, store, and reuse access tokens or secrets. <br>
Mitigation: Require explicit user confirmation for each credential source, token action, handoff destination, and persistent store, while keeping authentication and MFA entry under user control. <br>
Risk: Browser automation may access third-party or production logged-in pages. <br>
Mitigation: Use the skill only on pages the user is authorized to inspect, and prefer visible browser backends so the user can monitor interactions. <br>
Risk: Persisting credentials in local files can leave reusable secrets outside managed controls. <br>
Mitigation: Prefer a dedicated secret manager or OS keyring over .env files or local CLI files, and store only the minimum credential needed for the requested handoff. <br>


## Reference(s): <br>
- [Web Browser skill page](https://clawhub.ai/drumrobot/skills/web-browser) <br>
- [UI Test guide](./ui-test.md) <br>
- [Credential Issue guide](./credential-issue.md) <br>
- [CDP Trace guide](./cdp-trace.md) <br>
- [Chrome DevTools Protocol DOM domain](https://chromedevtools.github.io/devtools-protocol/tot/DOM/) <br>
- [Chrome DevTools Protocol CSS.getMatchedStylesForNode](https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getMatchedStylesForNode) <br>
- [Playwright BrowserContext.newCDPSession](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces browser-operation plans, verification summaries, credential handoff steps, and CDP trace commands; raw snapshot data should be summarized.] <br>

## Skill Version(s): <br>
0.2.4 (source: server release metadata and CHANGELOG, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
