## Description:

Scaffold a new local Beancount ledger with bea init and validation, with optional Fava browser setup when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

For users setting up a new local Beancount ledger, this skill scaffolds an initial ledger and validates it, with optional Fava browser setup. It excludes importing history, bank exports, edits to populated ledgers, and hosted Beancount.io ledgers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local-only description conflicts with instructions to access existing online financial ledgers.

Mitigation: Resolve the hosted-ledger scope before use; use a fresh directory and explicitly exclude online-ledger access and cloning.

Risk: Setup can leave persistent local agent instructions and optional Fava dependencies.

Mitigation: Review generated instruction files and add Fava only when it is requested.

## Reference(s):

- [Bea CLI workflow](references/bea-cli.md)
- [Compatibility paths](references/compatibility.md)
- [Ledger instructions template](references/agents-template.md)

## Skill Output:

**Output Type(s):** [Configuration, Files, Shell commands, Guidance]

**Output Format:** [Beancount ledger configuration, Markdown instructions, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-confirmed setup; optional Fava files and dependencies when requested]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
