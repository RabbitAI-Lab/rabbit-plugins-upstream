## Description:

This skill orchestrates industry research, keyword research, search demand analysis, intent mapping, audience research, content gap analysis, competitor keyword review, and SERP analysis using Ahrefs, Firecrawl, and Exa to produce a comprehensive intelligence brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mariokarras](https://clawhub.ai/user/mariokarras)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, SEO, and growth teams use this skill to research search intent, keyword clusters, audience questions, pain points, content gaps, and competitor positioning before campaign or content planning. Agents can use the resulting brief as structured market intelligence for downstream strategy work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, seed keywords, competitor URLs, and derived client context may be sent to third-party research services when those services are configured.

Mitigation: Review planned inputs before execution and avoid sending confidential, regulated, or unnecessary client information to external services.

Risk: The generated research brief may contain stale, incomplete, or misleading market signals if source data is unavailable or weak.

Mitigation: Review the generated `.agents/industry-research-{client}.md` file, check section timestamps, and verify important claims before downstream workflows rely on it.

## Reference(s):

- [Industry Research Skill Page](https://clawhub.ai/mariokarras/skills/industry-research)
- [Ahrefs API v3 Endpoint](https://api.ahrefs.com/v3)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance, configuration]

**Output Format:** [Markdown research brief with tables, bullet lists, timestamps, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local .agents/industry-research-{client}.md brief; target size is 3,000-5,000 words.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
