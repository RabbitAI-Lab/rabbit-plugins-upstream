## Description:

Guides OpenClaw users in syncing bank transactions through Plaid or GoCardless, fetching Gmail bills, and exporting local financial records to Beancount or Ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xbinkai](https://clawhub.ai/user/xbinkai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users can connect financial accounts, retrieve bills from Gmail, and organize or export transaction data for personal accounting.

### Deployment Geography for Use:

Global; Plaid supports the US and Canada, while GoCardless supports Europe.

## Known Risks and Mitigations:

Risk: The external plugin can access sensitive banking data, Gmail bills, and stored tokens.

Mitigation: Review the package before connecting real accounts, enable only needed providers, and use least-privilege credentials.

Risk: Local financial records and credentials may expose private information if stored or shared insecurely.

Mitigation: Protect local records, keep tokens in the system keychain, and do not commit credentials to code.

## Reference(s):

- [BillClaw on ClawHub](https://clawhub.ai/xbinkai/skills/billclaw)
- [BillClaw OpenClaw plugin on npm](https://www.npmjs.com/package/@firela/billclaw-openclaw)
- [BillClaw CLI on npm (optional)](https://www.npmjs.com/package/@firela/billclaw-cli)
- [BillClaw Connect on npm (optional)](https://www.npmjs.com/package/@firela/billclaw-connect)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide bank and Gmail syncs and Beancount or Ledger exports through the installed plugin.]

## Skill Version(s):

0.5.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
