## Description:

Research and compare news from the Chinng AI-Agent Portal. Use when finding relevant articles, investigating a topic, or preparing a sourced news summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chinng-inta](https://clawhub.ai/user/chinng-inta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search, compare, and summarize news records from the Chinng AI-Agent Portal while preserving portal citations and original source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News-search topics and retrieval requests are sent to the Chinng AI-Agent Portal MCP endpoint.

Mitigation: Use the skill only for topics suitable to share with that endpoint and avoid sensitive queries.

Risk: Portal metadata and summaries may be incomplete, and link-only records do not include article summaries.

Mitigation: Verify important claims against original source links and present link-only records as dated pointers.

Risk: Standalone MCP registration persists in the client configuration until removed.

Mitigation: Remove the portal MCP registration from the client when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chinng-inta/skills/news-triage)
- [Chinng AI-Agent Portal MCP endpoint](https://portal.chinng-lab-srv.dev/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with citations, dated pointers, and inline shell commands when standalone MCP setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite portal records, retain original source links, and respect license_note and omission metadata.]

## Skill Version(s):

0.2.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
