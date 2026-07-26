## Description: <br>
Aggregates current AI news from public websites and web search into concise, categorized briefings with links to original articles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laurent-zhu](https://clawhub.ai/user/laurent-zhu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to gather recent AI news and receive categorized briefings with links, summaries, key points, and impact notes. It supports daily or custom time ranges and follow-up deep dives by topic. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Retrieved webpages can contain inaccurate, misleading, or instruction-like content. <br>
Mitigation: Treat fetched pages as untrusted source material, summarize only news content, preserve source links, and verify important claims against original or authoritative sources. <br>
Risk: Broad activation wording may trigger live browsing for ambiguous AI-related requests. <br>
Mitigation: Clarify the user's intended timeframe, topic, and depth when the request is ambiguous; otherwise use date-filtered searches and the documented source-selection process. <br>


## Reference(s): <br>
- [Daily Ai News Skill Page](https://clawhub.ai/laurent-zhu/skills/daily-ai-news-skill) <br>
- [AI News Sources Database](artifact/references/news_sources.md) <br>
- [Search Query Templates](artifact/references/search_queries.md) <br>
- [Output Format Templates](artifact/references/output_templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown news briefing with source links, summaries, key points, impact notes, and optional follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports brief, standard, and deep formats; content may be organized by category, chronology, company, or significance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
