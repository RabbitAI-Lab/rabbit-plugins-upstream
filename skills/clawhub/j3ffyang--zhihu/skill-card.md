## Description:

Zhihu uses the Zhihu Open Platform CLI to search Zhihu and web content, retrieve hot lists, request Zhihu Direct Answer responses, and read the current user's own Zhihu creations, follows, and favorites with minimal data access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Zhihu community content and wider web sources, review trending topics, request retrieval-backed answers, and access their own account-linked Zhihu data through a CLI-backed workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes a user-local Zhihu CLI helper binary.

Mitigation: Install only when a Zhihu CLI integration is intended; the artifact requires user consent and verifies HTTPS release metadata, artifact size, SHA-256, archive structure, and binary version before installing.

Risk: The skill uses a user-provided Zhihu Access Secret for API calls and account-linked read-only features.

Mitigation: Prefer secure secret input or a host secret store, avoid pasting the Access Secret into ordinary chat, and rotate the Access Secret if it is exposed.

Risk: Zhihu API calls can consume quota and may return account-linked content.

Mitigation: Use only the minimum commands needed for the task, stop on quota or frequency-limit errors, and avoid writing full account-linked results to files or long-term memory unless the user explicitly asks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/zhihu)
- [CLI usage reference](artifact/references/cli.md)
- [Zhihu Open Platform guide](artifact/references/open-platform.md)
- [HTTP API reference](artifact/references/http-api.md)
- [User data API reference](artifact/references/user-api.md)
- [OAuth integration reference](artifact/references/oauth.md)
- [MCP integration reference](artifact/references/mcp.md)
- [Zhihu Developer Docs](https://developer.zhihu.com/docs)
- [Zhihu Developer Profile](https://developer.zhihu.com/profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, source links, and status JSON when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zhihu or web search result titles, excerpts, authors, URLs, initialization status, and credential setup guidance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact manifest version 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
