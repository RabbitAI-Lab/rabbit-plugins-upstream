## Description:

Guides OpenClaw users in syncing bank transactions, fetching bills from Gmail, and exporting financial data to Beancount or Ledger formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xbinkai](https://clawhub.ai/user/xbinkai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users can configure bank and Gmail connections, sync transactions and bills, and export records for accounting workflows.

### Deployment Geography for Use:

Global (bank connectivity varies by provider: Plaid in the US and Canada; GoCardless in Europe)

## Known Risks and Mitigations:

Risk: The third-party npm plugin requests access to sensitive banking and Gmail credentials and data.

Mitigation: Review the package and requested OAuth scopes; start with sandbox or test credentials before connecting real accounts.

Risk: Background sync behavior and the precise data-access scope are not fully described.

Mitigation: Confirm whether automatic sync or webhook services are enabled before using real financial or email data.

## Reference(s):

- [BillClaw on ClawHub](https://clawhub.ai/xbinkai/skills/billclaw)
- [BillClaw OpenClaw plugin on npm](https://www.npmjs.com/package/@firela/billclaw-openclaw)
- [BillClaw CLI on npm (optional)](https://www.npmjs.com/package/@firela/billclaw-cli)
- [BillClaw Connect on npm (optional)](https://www.npmjs.com/package/@firela/billclaw-connect)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides optional account sync and accounting-format exports through the installed plugin.]

## Skill Version(s):

0.7.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
