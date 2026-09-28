## Description:

Helps an agent sync and analyze a user's Credit Karma transactions, spending, and account summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with Credit Karma accounts use this skill to sync transactions and ask an agent for spending breakdowns, merchant activity, and account summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit Karma session cookies grant access to sensitive financial information.

Mitigation: Treat copied Cookie headers and CKAT/CKTRKID values like passwords; review the external package and browser extension before granting access.

Risk: Sensitive transaction history remains stored locally after session credentials are removed.

Mitigation: Protect the local database and remove it separately when transaction history is no longer needed; use ck_forget_session to clear stored credentials.

## Reference(s):

- [creditkarma on ClawHub](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp package](https://www.npmjs.com/package/creditkarma-mcp)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transaction and spending answers depend on locally synced data.]

## Skill Version(s):

3.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
