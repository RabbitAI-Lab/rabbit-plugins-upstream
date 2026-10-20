## Description:

Helps an agent review Splitwise balances, expenses, groups, and friends, and manage shared expenses through a connected Splitwise service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing shared expenses use this skill to ask an agent about Splitwise balances and groups, record or correct expenses, and manage friends, comments, and receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a Splitwise API key and sensitive expense, account, and receipt data.

Mitigation: Install only if you trust the package and are comfortable giving it your Splitwise API key.

Risk: Expense, group, friend, profile, comment, and receipt actions can change shared financial records.

Mitigation: Review write previews and duplicate warnings before approving changes; keep confirmation enabled.

Risk: Batch changes may partially succeed before a later step fails.

Mitigation: Check the results before retrying to avoid duplicate or unintended changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise API key registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions]

**Output Format:** [Markdown responses with structured Splitwise results and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report balances, expense details, and receipt information; changes require user approval.]

## Skill Version(s):

3.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
