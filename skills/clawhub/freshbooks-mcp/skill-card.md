## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with FreshBooks access use this skill to set up OAuth token handling and issue scripted curl and jq requests for FreshBooks accounting, payments, projects, and time tracking data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses FreshBooks OAuth app credentials and can access FreshBooks account data.

Mitigation: Use it only in a trusted shell, keep credentials out of logged commands, and store secrets in an appropriately protected local secret file.

Risk: FreshBooks non-GET requests can create or modify accounting records.

Mitigation: Review every non-GET request before running it, confirm target identifiers, and re-read affected records after writes.

Risk: Raw curl options passed through the helper are sent with the bearer token attached.

Mitigation: Do not allow untrusted text to shape fb_curl paths or arguments.

Risk: Rotating FreshBooks refresh tokens can be invalidated by multiple writers or by failing to persist a replacement token.

Mitigation: Use the dedicated state file, avoid sharing it with other tools, and re-run the browser authorization flow if a refresh token is spent.

## Reference(s):

- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks token helper](references/fb-token.sh)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks developer app registration](https://my.freshbooks.com/#/developer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include FreshBooks API paths, jq filters, curl options, and cautions for reviewing write operations before execution.]

## Skill Version(s):

0.6.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
