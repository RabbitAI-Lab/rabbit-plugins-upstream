## Description:

This skill lets an OpenCode agent use the Zhihu Open Platform to search Zhihu and the web, retrieve hot topics, invoke Zhihu Direct Answer, and read the current user's own Zhihu content, follows, and favorites with minimal necessary access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenCode users and developers use this skill to gather Zhihu community sources, broader web search results, current hot-list context, Zhihu Direct Answer responses, and their own Zhihu account context through the Zhihu CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access Secret exposure could allow unwanted use of the user's Zhihu Open Platform account and quota.

Mitigation: Use stdin, a host secret store, or an environment variable for the Access Secret; do not repeat full secrets in answers, logs, files, or shared transcripts; revoke or regenerate the Access Secret if exposure is suspected.

Risk: The skill installs and runs an external Zhihu CLI binary when the user authorizes setup.

Mitigation: Install only when the user trusts the Zhihu CLI distribution path; rely on the documented HTTPS manifest, same-host download, size, SHA-256, archive-structure, and version checks before running the binary.

Risk: Personal Zhihu content, follows, favorites, and quota-consuming verification calls may be accessed during authorized account tasks.

Mitigation: Use only the minimal CLI commands needed for the user's request, request consent before initialization or verification calls, avoid storing full account data in files or memory, and stop on quota or rate-limit errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/zhihu-for-opencode)
- [Zhihu Open Platform](https://developer.zhihu.com/)
- [Zhihu Open Platform documentation](https://developer.zhihu.com/docs)
- [Zhihu Open Platform profile and Access Secret](https://developer.zhihu.com/profile)
- [CLI usage documentation](artifact/references/cli.md)
- [Open Platform guide](artifact/references/open-platform.md)
- [HTTP API documentation](artifact/references/http-api.md)
- [User data API documentation](artifact/references/user-api.md)
- [OAuth application integration](artifact/references/oauth.md)
- [MCP integration documentation](artifact/references/mcp.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI/API response excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links plus JSON, SSE, or XML snippets returned by Zhihu CLI, HTTP API, or MCP calls.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact manifest reports 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
