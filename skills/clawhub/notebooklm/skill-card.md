## Description:

This skill helps agents query Google NotebookLM notebooks for citation-backed, source-grounded answers and manage notebooks, sources, and Studio content through NotebookLM MCP tools or the HTTP REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[roomi-fields](https://clawhub.ai/user/roomi-fields)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research users use this skill to obtain grounded NotebookLM answers with citations, manage notebook sources, and generate study or Studio content from uploaded sources. It is also useful for quota-aware research workflows that cache citation-preserved answers for later offline retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent act through a user's NotebookLM-backed Google session, including notebook and source management.

Mitigation: Confirm the intended NotebookLM account and scope before performing account, notebook, source, or authentication actions.

Risk: Public sharing, source import, and batch-to-vault workflows may expose content or write files locally.

Mitigation: Require explicit user confirmation for public sharing, imports, and export directories, and choose safe output paths before writing.

Risk: Multi-account rotation could be used to bypass provider limits.

Mitigation: Use account switching only for legitimate re-authentication or user-approved account selection, not to evade NotebookLM quotas.

## Reference(s):

- [NotebookLM MCP HTTP REST API Reference](references/rest-api.md)
- [Effective Research with NotebookLM](references/research-workflows.md)
- [@roomi-fields/notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp)
- [RTFM](https://github.com/roomi-fields/rtfm)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include NotebookLM answers with source names, citation numbers, and cited excerpts when JSON or expanded citation formats are selected.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
