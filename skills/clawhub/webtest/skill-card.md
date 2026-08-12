## Description:

webtest helps agents plan, run, and report browser-based web regression tests from natural-language requests in Chinese or English.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kastol](https://clawhub.ai/user/kastol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, test engineers, and acceptance reviewers use this skill to turn a URL and natural-language test scope into browser test steps, assertions, and a Markdown regression report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may operate a browser against websites and flows that can expose private site data or perform real business actions.

Mitigation: Use the skill only on authorized targets, prefer disposable test accounts and test environments, and avoid production payments or real orders unless they are explicitly intended.

Risk: Generated reports and screenshots may include sensitive page contents, account details, or site-specific operational information.

Mitigation: Keep reports and screenshots local, review them before sharing, and exclude run artifacts from release packages.

Risk: Checkout, account, or form flows can have side effects when run against production systems.

Mitigation: Confirm the target environment and test data before execution, and treat automated results as needing human review for key paths.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kastol/skills/webtest)
- [Assertion Catalog](references/assertion-catalog.md)
- [Run Guide](references/run-guide.md)
- [Report Template](references/report-template.md)
- [Admin Console Flow](references/admin-console-flow.md)
- [Windows Edge Fallback](references/windows-edge-fallback.md)
- [Example Run](references/example-run.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports with test plans, assertion results, screenshots or paths when available, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual output follows the user's input language.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
