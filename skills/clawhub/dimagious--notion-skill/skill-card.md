## Description:

Safe Notion API access for pages, databases, and blocks: schema diffs before structural changes, append-first writes, and personal/work profile switching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dimagious](https://clawhub.ai/user/dimagious)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, read, create, and update Notion pages, databases, and blocks while preserving workspace data through read-before-write checks, append-first writes, and confirmation before destructive or structural changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Notion integration token can access every page or database shared with it.

Mitigation: Create a dedicated low-scope integration, share only the needed Notion resources, and protect profile key files with restrictive permissions.

Risk: Writes to the wrong workspace or target can alter real notes, pages, or databases.

Mitigation: Use explicit profile selection, resolve pages and databases before acting, and require confirmation for destructive writes or schema changes.

## Reference(s):

- [Notion API documentation](https://developers.notion.com)
- [Notion integrations](https://www.notion.so/my-integrations)
- [ClawHub skill page](https://clawhub.ai/dimagious/skills/notion-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Notion integration token and curl; jq is documented as a local helper dependency.]

## Skill Version(s):

2.0.0 (source: server release metadata and artifact README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
