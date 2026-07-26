## Description: <br>
RSS新闻订阅免费版 helps an agent fetch international RSS news headlines, summaries, publication times, and links from sources such as BBC, Reuters, AP, and The Guardian, with filtering by source, topic, and result count. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, students, and independent developers use this skill to browse lightweight international news updates through public RSS feeds. Agents can list available sources, fetch current entries, filter by media source or topic, and return concise news summaries with links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package references a script-based RSS workflow, but the release artifact only contains SKILL.md and may be incomplete. <br>
Mitigation: Verify that the runnable script exists and matches the documented commands before installing or deploying the skill. <br>
Risk: A callback_url parameter can send processed results to an external endpoint. <br>
Mitigation: Only provide callback URLs that are explicitly intended to receive the results, and omit callback_url for normal local use. <br>
Risk: RSS content depends on public third-party feeds and can be unavailable, delayed, or incomplete. <br>
Mitigation: Treat returned headlines and summaries as pointers to source articles, and review linked source pages for important decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/news-feed-tool-free) <br>
- [BBC News RSS feed](http://feeds.bbci.co.uk/news/rss.xml) <br>
- [Reuters top news RSS feed](https://www.reuters.com/rssFeed/topNews) <br>
- [AP top news RSS feed](https://apnews.com/rss/apf-topnews.xml) <br>
- [NPR top stories RSS feed](https://feeds.npr.org/1001/rss.xml) <br>
- [Deutsche Welle RSS feed](https://rss.dw.com/rdf/rss-en-all) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text summaries with source-grouped news entries and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include title, summary, publication time, source, and link; content freshness depends on upstream RSS feeds and network access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
