## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up FreshBooks OAuth credentials, resolve FreshBooks account identifiers, and run curl/jq recipes for reading and intentionally writing accounting, project, and time-tracking data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents as a FreshBooks query workflow while also documenting live accounting write operations.

Mitigation: Review commands before execution, run write examples only when intentional, and re-read affected records to confirm persistence.

Risk: FreshBooks refresh tokens and the local session file are sensitive secrets, and refresh tokens rotate on use.

Mitigation: Use credentials scoped as narrowly as FreshBooks allows, keep printed refresh tokens and session files private, and avoid sharing one token state file across tools.

Risk: Some recipe paths are marked unverified against a live account.

Mitigation: Test unverified recipes with non-production data or read-only operations before relying on them for accounting changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer app registration](https://my.freshbooks.com/#/developer)
- [FreshBooks curl recipes](references/recipes.md)
- [FreshBooks OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [FreshBooks token helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript and shell helper code, jq filters, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform authenticated FreshBooks API calls and writes when the user runs provided commands; token state is stored locally.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
