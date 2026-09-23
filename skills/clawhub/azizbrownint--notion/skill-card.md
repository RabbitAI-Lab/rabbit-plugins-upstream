## Description:

Notion CLI/API for pages, Markdown content, data sources, files, comments, search, Workers, and raw API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect, create, update, query, and manage Notion workspace content through the official Notion CLI or direct API calls when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Notion token can grant access to workspace content beyond the immediate task.

Mitigation: Use a least-privileged Notion integration token and limit workspace/database access before running generated commands.

Risk: Commands may trash pages, patch raw API endpoints, upload files, or deploy Workers.

Mitigation: Review generated commands and target IDs before execution, especially destructive operations and Worker deployment.

Risk: The recommended npm install does not pin an exact ntn package version.

Mitigation: Install only from a trusted npm source and consider pinning or reviewing the package version before use.

## Reference(s):

- [Notion CLI overview](https://developers.notion.com/cli/get-started/overview)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/notion)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that read, create, update, trash, upload, deploy, or query Notion resources depending on user intent.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
