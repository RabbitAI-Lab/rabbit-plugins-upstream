## Description:

Draft, update, and publish SEO blog posts to Blogizi from a local repo using the Blogizi CLI, hosted MCP as a sandbox backup, or the public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blogizi](https://clawhub.ai/user/blogizi)

### License/Terms of Use:

AGPL-3.0-only

## Use Case:

Developers and AI coding agents use this skill to write markdown blog posts with Blogizi frontmatter, save drafts, update existing posts, and publish to Blogizi when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a Blogizi account API key in ~/.blogizi/config.json.

Mitigation: Have the user authenticate locally, never paste API keys into chat, and protect ~/.blogizi/config.json like a password file.

Risk: The publish workflow can make a post live on Blogizi.

Mitigation: Default to draft/update workflows and require an explicit user request before running publish.

Risk: Using stale dependencies in a shared or high-trust environment may increase operational risk.

Mitigation: Update dependencies and rebuild before deploying the CLI in shared or high-trust environments.

## Reference(s):

- [Blogizi CLI publishing docs](https://blogizi.com/docs/cli-publishing)
- [Blogizi MCP docs](https://blogizi.com/docs/mcp)
- [Blogizi markdown frontmatter docs](https://blogizi.com/docs/markdown-frontmatter)
- [Blogizi public API docs](https://blogizi.com/docs/public-api)
- [Blogizi LLM brief](https://blogizi.com/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local markdown post files and may call Blogizi CLI, MCP, or HTTP API endpoints when configured by the user.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
