## Description:

Work with Notion pages and databases via the official Notion API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiiang0529](https://clawhub.ai/user/xiiang0529)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide an agent in reading, creating, updating, and querying Notion pages and databases through a local Notion CLI and the official Notion API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Notion integration token can expose workspace content if it is leaked or logged.

Mitigation: Treat NOTION_API_KEY as a secret and avoid placing it in prompts, shared logs, or committed configuration.

Risk: Overbroad integration sharing can give the agent access to more Notion pages or databases than needed.

Mitigation: Share the Notion integration only with the pages and databases required for the task.

Risk: Schema changes can disrupt databases if applied without review.

Mitigation: Inspect schema diffs and require explicit confirmation before applying database schema changes.

Risk: The skill depends on a local Notion CLI that is outside the artifact.

Mitigation: Install any required Notion CLI from a trusted source before use.

## Reference(s):

- [Notion API documentation](https://developers.notion.com)
- [Notion integrations](https://www.notion.so/my-integrations)
- [ClawHub skill page](https://clawhub.ai/xiiang0529/skills/notion-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NOTION_API_KEY and a trusted local Notion CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
