## Description:

BillClaw helps OpenClaw users sync bank transactions, retrieve bills from Gmail, and export locally stored financial data to Beancount or Ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xbinkai](https://clawhub.ai/user/xbinkai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users manage bank transactions and email bills through optional Plaid, GoCardless, and Gmail connections, then export records for bookkeeping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected bank transactions and Gmail bills contain sensitive financial and personal information.

Mitigation: Grant only the Plaid and Gmail permissions needed, and review who can access locally stored records.

Risk: Credentials stored in plaintext configuration files may be exposed.

Mitigation: Prefer environment variables or system keychain storage over plaintext configuration files.

Risk: Installing third-party npm components introduces software supply-chain exposure.

Mitigation: Review the npm packages and their source before installing or updating them.

## Reference(s):

- [BillClaw on ClawHub](https://clawhub.ai/xbinkai/skills/billclaw)
- [BillClaw project documentation](https://github.com/fire-la/firela-bot)
- [BillClaw OpenClaw plugin](https://www.npmjs.com/package/@firela/billclaw-openclaw)
- [BillClaw CLI (optional)](https://www.npmjs.com/package/@firela/billclaw-cli)
- [BillClaw Connect (optional)](https://www.npmjs.com/package/@firela/billclaw-connect)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Accounting data files]

**Output Format:** [Markdown guidance and Beancount or Ledger exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bank and Gmail features require separately configured accounts and credentials; bank provider availability varies by region.]

## Skill Version(s):

0.7.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
