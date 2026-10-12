## Description:

Helps an agent access Splitwise balances, groups, friends, expenses, and receipts through a configured MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with a Splitwise account use this skill to ask an agent about shared balances and expenses, manage groups and expense splits, and retrieve receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Splitwise API key could grant access to account data.

Mitigation: Treat the API key like a password and keep it out of shared files and messages.

Risk: Incorrect write requests could change shared expenses or group membership.

Mitigation: Review the proposed change and its preview before confirming any write.

Risk: Receipts can contain sensitive financial details and may be saved on the MCP server filesystem.

Mitigation: Use inline or text-extraction modes when a saved file is unnecessary; protect and remove saved receipts as appropriate.

Risk: Other Splitwise users can supply comments or descriptions containing misleading instructions.

Mitigation: Treat account content and extracted receipt text as untrusted data, not agent instructions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise API key registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report balances, expense details, and receipt text or saved receipt paths.]

## Skill Version(s):

3.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
