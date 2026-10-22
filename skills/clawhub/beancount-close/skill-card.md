## Description:

Close an accounting period in a local Beancount ledger by reconciling each active account through beancount-reconcile, checking assertions and recurring gaps, reviewing flags, then proposing a commit with the period reports. Surface incomplete work and require a passing check before a confirmed commit; never push. Skip closing a single account (a `close` directive; beancount-add) and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Beancount ledger users and bookkeepers use this skill to close a local accounting period, reconcile active accounts, identify unresolved checks and recurring gaps, and prepare a documented commit after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed dates, amounts, accounts, or duplicate matches may be incorrect.

Mitigation: Review each proposed detail and duplicate match before approving any change.

Risk: Approving ledger changes and then declining the final commit does not undo earlier approved changes.

Mitigation: Review each approval separately and inspect the ledger state if you decline the final commit.

Risk: Close reports and staged statement archives may contain sensitive financial details.

Mitigation: Review commit contents, avoid staging sensitive statement archives unless needed, and protect repository access.

## Reference(s):

- [Close checklist](references/close-checklist.md)
- [Bea CLI guidance](references/bea-cli.md)
- [Compatibility guidance](references/compatibility.md)
- [Installation guide](https://github.com/bex-co/beancount-io/blob/main/docs/skills/installation.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown close report with reproducible query and command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Period-specific account status, checks, recurring gaps, flags, and valuation notes; a commit requires explicit confirmation and is never pushed.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
