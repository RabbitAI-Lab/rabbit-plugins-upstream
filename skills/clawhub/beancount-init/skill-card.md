## Description:

Scaffold a new local Beancount ledger with bea init and validation, with optional Fava browser setup when requested. Use for setting up a new ledger or initializing a bookkeeping repository. Skip importing history (beancount-migrate), bank exports, edits to a populated ledger, or ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and people setting up personal or household bookkeeping use this skill to create and validate a new local Beancount ledger, with optional Fava browser setup. It is not for importing transaction history, modifying a populated ledger, or working on a hosted Beancount.io ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect opening balance, currency, date, or account set could make the new ledger misleading.

Mitigation: Confirm the opening details and proposed accounts with the user before writing, then run the ledger validation step.

Risk: Installing bookkeeping software or the optional Fava browser environment changes the local environment.

Mitigation: Install the required bea tool through the documented option and set up Fava only when requested.

## Reference(s):

- [Shared bea command recipes](references/bea-cli.md)
- [Compatibility paths](references/compatibility.md)
- [Ledger instructions template](references/agents-template.md)
- [Project skill documentation](https://github.com/bex-co/beancount-io/tree/main/skills)
- [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Beancount ledger files with concise Markdown and shell-command setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a new local ledger; Fava-related files and setup are optional.]

## Skill Version(s):

1.0.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
