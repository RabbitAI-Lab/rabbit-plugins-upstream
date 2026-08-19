## Description:

E2e Verify helps agents verify web app changes in a real browser, choosing between one-off AI-driven checks and durable Playwright tests while requiring non-production targets and observation-based reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to verify web application changes through real browser observation. It supports immediate smoke checks, durable Playwright test authoring for high-risk flows, and structured reporting of findings and untested scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser verification can expose page content, test data, and credentials to a configured LLM provider.

Mitigation: Run only against localhost or staging with seeded accounts, avoid real user cookies, and choose an approved provider or local model for sensitive flows.

Risk: The browser-use activation flow may load environment variables from home or project .env files.

Mitigation: Review .env files before sourcing the activation helper and keep production secrets out of browser verification sessions.

Risk: AI-driven browser walks can miss paths or overstate confidence if reported as a full test pass.

Mitigation: Report only the flows walked, quote concrete observations, list untested scope, and use durable Playwright tests for critical regression paths.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dennisrongo/skills/e2e-verify)
- [browser-use Reference](references/browser-use.md)
- [browser-use Repository](https://github.com/browser-use/browser-use)
- [browser-use Documentation](https://docs.browser-use.com)
- [browser-use Examples](https://github.com/browser-use/browser-use/tree/main/examples)
- [browser-harness Real Browser Mode](https://github.com/browser-use/browser-harness)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline commands and optional generated Playwright or browser-use scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should enumerate flows walked, observations, findings, and scope not tested; durable browser tests should include red and green evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
