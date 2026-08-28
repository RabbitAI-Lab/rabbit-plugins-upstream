## Description:

e2e-verify helps agents verify web application changes in a real browser, choosing between one-off browser walks and durable Playwright tests while reporting only observed paths and findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to verify web UI changes against local or staging targets, then create durable E2E tests for critical flows such as auth, checkout, deletion, or data-loss paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-use runs can send page context to the selected LLM provider.

Mitigation: Run only against local or staging targets with throwaway accounts and non-production data.

Risk: The browser-use activation flow loads .env files and installs local browser tooling.

Mitigation: Review or patch the activation helper before use and avoid sourcing it from untrusted project directories.

Risk: AI-walked browser checks can be mistaken for complete E2E test coverage.

Mitigation: Report the exact flows walked, quote observations, and list paths that were not tested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/e2e-verify)
- [browser-use reference](references/browser-use.md)
- [browser-use repository](https://github.com/browser-use/browser-use)
- [browser-use documentation](https://docs.browser-use.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance and reports with inline code or shell command snippets, plus optional Playwright or browser-use test files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a local or staging URL, throwaway credentials, browser tooling, and LLM API credentials for browser-use runs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
