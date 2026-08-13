## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and finance teams use this skill to make FreshBooks API calls from a shell when they need scripted access or do not have the freshbooks-mcp server installed. It supports both read workflows and write examples for FreshBooks business records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables shell-mediated FreshBooks access that can create or change accounting records.

Mitigation: Use a least-privilege FreshBooks app or account, require explicit review before POST or soft-delete examples, and re-read records after writes to confirm persistence.

Risk: FreshBooks refresh tokens are single-use and rotate, so shared or mishandled token state can lock out access.

Mitigation: Keep tokens out of shared shells and logs, protect the state file, and avoid pointing multiple tools at the same rotating-token state file.

## Reference(s):

- [FreshBooks Developer Portal](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks token helper](references/fb-token.sh)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, curl examples, jq filters, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, Node.js for OAuth bootstrap, and FreshBooks OAuth client credentials.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
