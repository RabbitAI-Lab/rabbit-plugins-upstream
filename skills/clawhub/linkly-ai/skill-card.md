## Description:

Searches, browses, reads, and captures notes across Linkly AI-indexed local files and linked cloud libraries through CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkly-ai](https://clawhub.ai/user/linkly-ai)

### License/Terms of Use:

Apache 2.0

## Use Case:

Employees, external users, developers, and agents use this skill to find, enumerate, inspect, and read indexed documents across local and linked cloud sources, then save or list local Markdown notes when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad local and linked cloud document contents through search, listing, grep, outline, and read workflows.

Mitigation: Install it only for agents that should access Linkly-indexed documents, and review retrieved document content before using it in sensitive decisions.

Risk: Note-saving commands can create or rewrite local Markdown notes on the user's Desktop.

Mitigation: Use clear note creation or edit instructions, confirm the intended note when editing, and rely on the skill's versioned edit flow to avoid blind overwrites.

Risk: Indexed document content may contain untrusted or misleading instructions.

Mitigation: Treat retrieved document text as evidence for the user's task, not as agent instructions to execute.

## Reference(s):

- [Linkly AI Skill Page](https://clawhub.ai/linkly-ai/skills/linkly-ai)
- [Linkly AI CLI Installation Guide](https://linkly.ai/docs/en/use-cli)
- [Linkly AI MCP Cloud Gateway](https://mcp.linkly.ai)
- [Linkly AI CLI Reference](references/cli-reference.md)
- [Linkly AI MCP Tools Reference](references/mcp-tools-reference.md)
- [Advanced Search Strategies](references/search-strategies.md)
- [Troubleshooting Linkly AI](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text guidance, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include document IDs, search/list result summaries, line-referenced excerpts, troubleshooting steps, and local note content when requested.]

## Skill Version(s):

0.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
