## Description:

Close an accounting period in a local Beancount ledger by reconciling each active account through beancount-reconcile, checking assertions and recurring gaps, reviewing flags, then proposing a commit with the period reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to close a month in a local Beancount ledger by reconciling active accounts, checking assertions and recurring gaps, reviewing flags, and preparing a report-backed commit for explicit approval. It does not push commits or handle single-account close directives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger and statement data can be sensitive, and some ledger workflows may use a hosted-server handoff.

Mitigation: If processing must remain local, explicitly disallow the hosted-server handoff.

Risk: Proposed entries, staged files, or the financial report in the commit message may be incorrect or misleading.

Mitigation: Review proposed entries, staged files, and the financial report; commit only after a passing ledger check and explicit approval.

Risk: Some accounts may remain unreconciled or otherwise unverified at close.

Mitigation: Review the reported status of every active account and keep incomplete work explicit rather than presenting the close as fully verified.

## Reference(s):

- [Close checklist](references/close-checklist.md)
- [bea CLI recipes](references/bea-cli.md)
- [Compatibility paths](references/compatibility.md)
- [BQL recipes](references/bql-recipes.md)
- [Project homepage listed in skill metadata](https://github.com/bex-co/beancount-io/tree/main/skills)
- [Installation guide](https://github.com/bex-co/beancount-io/blob/main/docs/skills/installation.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown close report and proposed git commit message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports tied and unresolved account states; proposes a commit only after a passing ledger check and explicit approval; never pushes.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
