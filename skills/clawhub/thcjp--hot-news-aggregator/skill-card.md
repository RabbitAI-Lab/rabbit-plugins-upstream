## Description: <br>
Hot News Aggregator helps agents search, filter, summarize, deduplicate, and structure Chinese and international news across social, technology, military, finance, sports, and current-events topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to produce news briefs, topic timelines, industry updates, sentiment summaries, and structured JSON or Markdown digests from user-specified topics, categories, date ranges, and languages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill advertises broad shell execution, local file access, and external API use that are not tightly scoped to news aggregation. <br>
Mitigation: Run it in a constrained environment, avoid broad credentials, and review proposed commands or file-writing actions before allowing them. <br>
Risk: Generated news summaries, scores, sentiment labels, and trend analyses may be incomplete, stale, or misleading if source coverage is weak. <br>
Mitigation: Cross-check important items against multiple cited sources and treat summaries as decision support rather than final factual authority. <br>
Risk: Some news sources or APIs may require credentials and may impose rate limits or availability constraints. <br>
Mitigation: Use minimally scoped API keys, keep credentials out of version control, and configure retries or fallback sources for operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/hot-news-aggregator) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefs or structured JSON with article summaries, categories, importance scores, entities, sources, trends, and troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include source URLs, timestamps, sentiment labels, trend topics, API key setup guidance, and command or file-handling instructions when the agent environment supports them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
