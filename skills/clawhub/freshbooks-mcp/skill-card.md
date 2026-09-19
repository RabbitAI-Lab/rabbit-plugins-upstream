## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to generate shell-based FreshBooks API setup steps, authenticated curl calls, and jq recipes for accounting and time-tracking workflows without running the freshbooks-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce commands that make live FreshBooks accounting changes or email clients.

Mitigation: Prefer read-only queries unless a write is explicitly intended; review generated write commands before running them and re-read records after writes to confirm the result.

Risk: OAuth client secrets, refresh tokens, and the session file can expose FreshBooks account access if logged or shared.

Mitigation: Keep secrets out of logs, shared shells, and CI output; protect the session file and related secret files with user-only permissions.

Risk: FreshBooks refresh tokens rotate and are single-use, so multiple writers against one token state can lock out access.

Mitigation: Use a single token state writer for this helper, keep it separate from other FreshBooks tools, and re-run the browser authorization flow if the refresh token is spent.

Risk: Some recipe paths and write examples are marked unverified in the artifact.

Mitigation: Validate unverified requests in a low-risk FreshBooks account or against current FreshBooks documentation before using them on production records.

## Reference(s):

- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token helper](references/fb-token.sh)
- [FreshBooks developer app registration](https://my.freshbooks.com/#/developer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell, jq, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include FreshBooks API write examples that should be reviewed before execution.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
