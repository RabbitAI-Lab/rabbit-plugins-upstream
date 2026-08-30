## Description:

Notion API integration with managed OAuth for querying databases, searching pages, reading workspace content, and performing confirmed writes through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with Notion workspaces, databases, pages, blocks, and users through Maton-managed OAuth. It supports read/list workflows by default and requires explicit confirmation for connection creation, writes, deletion, bulk changes, and shared-workspace modifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may connect to or act on the wrong Notion workspace when multiple Maton accounts or Notion connections exist.

Mitigation: Verify the active Maton profile and specify the intended connection before acting, especially before any write or shared-workspace change.

Risk: Writes, deletion, bulk updates, or shared-workspace modifications can alter visible Notion content or disrupt workflows.

Mitigation: Default to read/list calls, confirm the exact target resource and intended effect with the user, and require explicit approval for each high-impact operation or batch.

Risk: Long-lived API keys can leak through logs, shell history, child processes, or persisted files when the CLI cannot be used.

Mitigation: Prefer OAuth and the Maton CLI credential store; when raw HTTP is unavoidable, do not print or persist the key, feed headers on stdin, and send the key only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-api-skill)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Notion API Introduction](https://developers.notion.com/reference/intro)
- [Notion Search Reference](https://developers.notion.com/reference/post-search.md)
- [Notion Query Database Reference](https://developers.notion.com/reference/post-database-query.md)
- [Notion Get Page Reference](https://developers.notion.com/reference/retrieve-a-page.md)
- [Notion Create Page Reference](https://developers.notion.com/reference/post-page.md)
- [Notion Update Page Reference](https://developers.notion.com/reference/patch-page.md)
- [Notion Append Block Children Reference](https://developers.notion.com/reference/patch-block-children.md)
- [Notion Filter Reference](https://developers.notion.com/reference/post-database-query-filter.md)
- [Notion LLM Reference](https://developers.notion.com/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API Calls]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should keep credentials hidden, default to read/list calls, and require explicit confirmation before writes or connection changes.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter: 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
