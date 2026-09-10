## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run FreshBooks REST API queries and guided shell workflows without installing the FreshBooks MCP server. It is also useful for scripted accounting, project, payment, and time-tracking checks where OAuth token rotation must be handled carefully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is described as querying FreshBooks but includes examples that can create, update, email, or hide live accounting records.

Mitigation: Review every non-GET command before execution, use credentials for only the intended FreshBooks account, and re-read affected records to confirm the result.

Risk: FreshBooks OAuth refresh tokens are single-use and rotating; sharing state files or running multiple writers against the same state can invalidate access.

Mitigation: Use the provided token helper with a dedicated state file, avoid concurrent writers, and keep terminal logs and token files private.

## Reference(s):

- [FreshBooks developer app registration](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, curl examples, jq recipes, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate live FreshBooks API calls that read, create, update, email, or hide accounting records depending on the selected example.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
