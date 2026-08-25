## Description:

Guides an agent through real-browser QA of an existing runnable web application, with evidence capture, optional authorized repair, release gating, deployment, and post-deployment regression.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liubai00](https://clawhub.ai/user/liubai00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to smoke-test or regress existing web applications in a real browser, triage functional, interaction, UI, and accessibility defects, and carry out repairs or releases only when those authorities are explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may use browser access and, when separately authorized, repository edits, command execution, deployment credentials, and Git or report delivery authority.

Mitigation: Install and use it only in workspaces where those authorities are acceptable, and grant repair, deployment, Git, and delivery permissions separately for the current task.

Risk: Production targets, real notifications, payments, user or account changes, rollback actions, and secret-bearing evidence can have external side effects.

Mitigation: Keep those actions behind explicit approval with a named target and boundary; treat production and shared environments as read-only unless current-task authorization is complete.

Risk: QA evidence can accidentally expose secrets, tokens, cookies, credentials, or unrelated personal data.

Mitigation: Record sanitized evidence references in the ledger and avoid storing secrets, raw personal data, or credential material.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liubai00/skills/webapp-qa-loop)
- [Project Homepage](https://github.com/liubai00/webapp-qa-loop)
- [README](README.md)
- [Scope and Scenario Selection](references/scope-and-selection.md)
- [Browser Playbook](references/browser-playbook.md)
- [Issue Ledger](references/issue-ledger.md)
- [Repair and Reuse Gate](references/repair-and-reuse.md)
- [Release and Rollback Gate](references/release-and-rollback.md)
- [Automation Promotion](references/automation-promotion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with command snippets, ledger-backed evidence summaries, code changes, and configuration guidance when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a durable QA ledger for nontrivial audit, repair, and release runs; avoids storing secrets or raw personal data.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
