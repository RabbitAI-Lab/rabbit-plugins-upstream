## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to set up FreshBooks OAuth, maintain a rotating token state file, and produce curl and jq commands for reading or modifying FreshBooks accounting, project, and time-tracking data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable shell-assisted access to live FreshBooks accounting data.

Mitigation: Install only when this access is acceptable, use the least-privileged FreshBooks app or scopes available, and start with a test account when possible.

Risk: FreshBooks OAuth client secrets, access tokens, and refresh tokens could be exposed through logs, shell tracing, or shared state files.

Mitigation: Keep credentials out of logs, disable shell tracing around token commands, protect the token state file, and avoid sharing one token state file across tools.

Risk: Generated POST, PUT, DELETE, email, payment, invoice, estimate, or time-entry actions can modify live business records.

Mitigation: Require explicit human confirmation before executing write actions and re-read affected records to confirm the intended result.

## Reference(s):

- [FreshBooks developer app registration](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks token helper](references/fb-token.sh)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell and JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that read or modify live FreshBooks account data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
