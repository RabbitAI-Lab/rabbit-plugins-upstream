## Description: <br>
Bi-directional sync and management for Notion pages and databases. Use when working with Notion workspaces for collaborative editing, research tracking, project management, or when you need to sync markdown files to/from Notion pages or monitor Notion pages for changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robansuini](https://clawhub.ai/user/robansuini) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and workspace operators use this skill to search, query, update, monitor, and synchronize Notion pages or databases with local Markdown workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A batch update can modify many Notion records if the selected database, filter, or stdin page list is broader than intended. <br>
Mitigation: Run batch updates with --dry-run first, set a narrow --filter or explicit stdin page list, and keep --limit scoped to the intended pages. <br>
Risk: The Notion integration token can access important shared or business data if it is over-permissioned or exposed. <br>
Mitigation: Use a least-privilege Notion integration shared only with needed pages and databases, and protect token files or stdin/env handling. <br>
Risk: File sync commands can read from or write to local paths outside the current workspace when --allow-unsafe-paths is used. <br>
Mitigation: Keep the default workspace path guard enabled and use --allow-unsafe-paths only for deliberate, reviewed paths. <br>


## Reference(s): <br>
- [Notion Sync API Reference](references/API-REFERENCE.md) <br>
- [Notion Integrations](https://www.notion.so/my-integrations) <br>
- [ClawHub Skill Page](https://clawhub.ai/robansuini/skills/notion-sync) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts can emit JSON results or Markdown content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a Notion integration token supplied through NOTION_API_KEY, a token file, or stdin.] <br>

## Skill Version(s): <br>
2.5.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
