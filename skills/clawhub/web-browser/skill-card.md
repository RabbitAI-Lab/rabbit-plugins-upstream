## Description:

Environment-aware browser operations skill that routes UI testing, CDP trace diagnosis, and browser-login-assisted credential issuance through the appropriate visible or automated browser workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to verify browser UI behavior, diagnose page state and closed shadow DOM styling issues, and coordinate credential issuance workflows that require user login before follow-up automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use logged-in browser sessions and credential-issuance flows to access or generate sensitive account material.

Mitigation: Require explicit approval before browser session reuse, secret lookup, token generation, credential persistence, file deletion, or follow-up CLI actions.

Risk: Credential values may be read from pages, stored for reuse, or handed to automation with broad downstream authority.

Mitigation: Use least-privilege scopes, persist credentials only in an approved secret store, and review each generated token or key before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI Test guide](ui-test.md)
- [Credential Issue guide](credential-issue.md)
- [CDP Trace guide](cdp-trace.md)
- [Chrome DevTools Protocol DOM domain](https://chromedevtools.github.io/devtools-protocol/tot/DOM/)
- [CDP CSS.getMatchedStylesForNode](https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getMatchedStylesForNode)
- [Playwright browserContext.newCDPSession](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve browser automation, user login coordination, credential handling, and follow-up CLI handoffs.]

## Skill Version(s):

0.2.5 (source: server release metadata and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
