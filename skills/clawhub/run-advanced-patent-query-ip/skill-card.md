## Description:

Executes explicit PatSnap advanced patent queries and produces evidence-backed competitor patent reports with portfolio counts, company summaries, patent details, optional literature context, and Markdown plus HTML outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent analysts, and IP teams use this skill when they have verified PatSnap access and need to run advanced patent queries, normalize results, and generate evidence-backed competitor patent reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The REST image downloader can fetch API-supplied image URLs without host validation.

Mitigation: Prefer the MCP workflow; if REST scripts are used, restrict outbound network access and add image URL allowlisting plus private-network blocking before downloading images.

Risk: REST execution depends on verified PatSnap endpoints and credentials supplied outside the conversation.

Mitigation: Keep credentials in the execution environment or MCP credential mechanism, require explicitly configured endpoints, and fail closed when settings are absent.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yuanzhian-patsnap/skills/run-advanced-patent-query-ip)
- [PatSnap Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and HTML reports with concise conversation summaries and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write timestamped reports under reports/; requires verified PatSnap MCP access or explicitly configured REST endpoints and environment credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
