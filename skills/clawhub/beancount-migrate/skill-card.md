## Description:

Migrates finance-app transaction exports into a fresh Beancount ledger, confirming mappings and reconciling source counts and balances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and personal-finance users can convert exported transaction histories from Mint, Monarch, QuickBooks Online, or similar apps into a new Beancount ledger. The workflow confirms account and category mappings, checks transfers, and reconciles counts and balances without merging into an existing populated ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The stated local-only migration scope conflicts with directions to use connected hosted financial-ledger tools.

Mitigation: Use a fresh local ledger and explicitly prohibit hosted-tool access until the conflicting routing instructions are corrected. Keep original exports, approve mappings and the write destination, and check the migration report.

## Reference(s):

- [Project homepage](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Markdown]

**Output Format:** [Beancount ledger entries and a Markdown migration report, with shell commands for verification.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mapping proposals require user confirmation; migration results include source counts, balances, and skipped or unmapped rows.]

## Skill Version(s):

1.0.1 (source: evidence.json release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
