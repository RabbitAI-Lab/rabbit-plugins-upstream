## Description:

Use folkctl to inspect and update folk.app CRM data through its REST API. Covers people, companies, groups, members, custom fields, deals, custom objects, users, notes, tasks, interactions, legacy reminders, webhooks, and official MCP setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-edel](https://clawhub.ai/user/j-edel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and CRM administrators use this skill to inspect, create, update, and manage folk.app CRM records through folkctl while preserving dry-run and confirmation workflows for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a pinned third-party CLI that can access Folk CRM data through FOLK_API_KEY.

Mitigation: Install only after verifying trust in the pinned source, keep FOLK_API_KEY narrowly scoped where possible, and rotate the key if exposure is suspected.

Risk: Create, update, delete, and option-removal commands can change or remove CRM records and associated contact data.

Mitigation: Use --dry-run --json before mutations, summarize the exact resource and request, and require explicit user confirmation before destructive actions.

Risk: Changing FOLK_API_BASE_URL can route requests away from the default Folk API endpoint.

Mitigation: Set FOLK_API_BASE_URL only when the user intentionally needs a non-default Folk API endpoint.

## Reference(s):

- [folkctl project homepage](https://github.com/j-edel/folkctl)
- [folkctl v0.2.0 release](https://github.com/j-edel/folkctl/releases/tag/v0.2.0)
- [folkctl reviewed PR](https://github.com/j-edel/folkctl/pull/1)
- [Folk reminders-to-tasks migration guide](https://developer.folk.app/migrations/reminders-to-tasks)
- [Folk MCP tools reference](https://developer.folk.app/mcp/tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON-oriented CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses folkctl --json for machine-readable responses and --dry-run before mutations.]

## Skill Version(s):

0.2.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
