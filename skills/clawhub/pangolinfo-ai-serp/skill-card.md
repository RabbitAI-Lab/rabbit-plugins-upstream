## Description:

Helps agents query Google SERP, AI Overviews, AI Mode, and keyword trends through Pangolinfo tools, producing grounded search summaries, citations, SERP rows, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need current Google search results, AI Overview or AI Mode output with citations, off-site demand or sentiment signals, and Google Trends-style keyword comparisons. It is intended to help agents ground responses in retrieved search and trend evidence rather than relying on memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, follow-up prompts, and trend keywords are sent to Pangolinfo-backed external search services.

Mitigation: Use the skill only for queries that are appropriate to share with the external service, and avoid submitting sensitive or confidential prompts.

Risk: Shared Amazon-related rules in the artifact may be broader than this skill's Google SERP and trends purpose.

Mitigation: Use this skill for Google SERP, AI Overview or AI Mode, and keyword trend workflows; route Amazon-specific workflows to the intended Pangolinfo Amazon skills or tools.

Risk: AI Overview output is not guaranteed for every query, and trend values are relative rather than absolute search volume.

Mitigation: Fall back to organic SERP results when AI Overview is absent, preserve citations when available, and label keyword trend numbers as relative interest values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pangolinfo/skills/pangolinfo-ai-serp)
- [Pangolinfo publisher profile](https://clawhub.ai/user/pangolinfo)
- [Pangolinfo website](https://www.pangolinfo.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, citation links, concise summaries, setup snippets, and optional structured result excerpts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SERP result tables, AI Overview citation lists, keyword trend summaries, fallback guidance for missing AI Overviews, and authentication setup guidance.]

## Skill Version(s):

4.0.0 (source: server release evidence; artifact frontmatter reports 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
