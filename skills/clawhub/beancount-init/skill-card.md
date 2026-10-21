## Description:

Scaffold a new local Beancount ledger with bea init and validation, with optional Fava browser setup when requested. Use for setting up a new ledger or initializing a bookkeeping repository. Skip importing history (beancount-migrate), bank exports, edits to a populated ledger, or ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and people maintaining personal or organizational books use this skill to initialize and validate a fresh local Beancount ledger, with optional browser access through Fava. It is not intended for importing transaction history or modifying an already populated ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting routing guidance could redirect a local setup toward a connected hosted financial account without clear limits.

Mitigation: Use a fresh local directory, explicitly exclude cloud-account operations, and clarify hosted-ledger routing before using a connected Beancount.io account.

Risk: The setup can add persistent ledger instructions and optional Fava dependencies.

Mitigation: Review generated ledger instructions before relying on them, and configure Fava only when requested.

## Reference(s):

- [bea command recipes](references/bea-cli.md)
- [Compatibility paths](references/compatibility.md)
- [Ledger instructions template](references/agents-template.md)
- [CSV import guidance](references/bea-import.md)
- [Deduplication guidance](references/dedup.md)
- [Project homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance, shell commands, and Beancount ledger configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-confirmed currency, opening date, and optional opening balance and account details; Fava setup is optional and only performed when requested.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
