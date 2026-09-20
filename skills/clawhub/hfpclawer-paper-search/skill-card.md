## Description:

Discover, download, and organize academic papers from arXiv, HuggingFace Papers, and OpenReview with multi-source search, deduplication, PDF download, Markdown conversion, and optional wiki sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to monitor research topics, discover new papers across multiple sources, download PDFs, convert papers to Markdown, and optionally sync results into a wiki or local paper workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access research configs, local paper stores, optional Zotero data, and external paper APIs.

Mitigation: Install only when those accesses are intended, review config paths before wiki sync or profile-based recommendations, and keep private identifiers in local ignored configuration.

Risk: Unpinned uvx or pip installs can change package contents over time.

Mitigation: Prefer pinned package versions or trusted lockfiles before relying on the skill in repeatable workflows.

Risk: MCP and monitor modes expose tool functions to an agent when started.

Mitigation: Start MCP or monitor modes only for sessions where those capabilities are expected and appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/hfpclawer-paper-search)
- [Project homepage](https://github.com/diamond2nv/hfpapers-crawler)
- [PyPI package](https://pypi.org/project/hfpclawer/)
- [Publisher profile](https://clawhub.ai/user/diamond2nv)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or organize local paper metadata, PDFs, Markdown conversions, wiki-ready files, audit records, and optional MCP tool guidance.]

## Skill Version(s):

0.19.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
