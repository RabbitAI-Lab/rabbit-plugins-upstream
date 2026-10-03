## Description:

Helps an agent retrieve Splitwise balances, expenses, groups, and friends and manage shared expenses through a configured Splitwise connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Splitwise users can ask an agent to review balances and shared expenses, manage groups, and create, edit, or delete expenses after confirming account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Splitwise API key grants access to account data.

Mitigation: Keep the key out of shared files and chats, and install only if comfortable granting account access.

Risk: Installing and running the external package executes software outside the skill instructions.

Mitigation: Review the package before installing or running it.

Risk: Expense and group changes may affect other people or shared balances.

Mitigation: Review confirmation previews before creating, editing, or deleting records; use explicit Splitwise wording for ambiguous requests.

Risk: Receipt downloads can leave sensitive files in the server's working directory.

Mitigation: Configure the receipt output location or use inline results when local files are not wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Text or structured expense data; optional receipt files or inline receipt content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Receipts may be written to the server's working directory by default.]

## Skill Version(s):

3.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
