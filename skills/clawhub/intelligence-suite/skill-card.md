## Description: <br>
Makima's All-Seeing Intelligence Suite combines real-time AI news tracking and global news monitoring for a comprehensive strategic briefing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xhrisfu](https://clawhub.ai/user/xhrisfu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to fetch public AI and global news signals, scrape short article snippets, and prepare structured briefing material for synthesis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fetched article snippets and public web content may be incomplete, stale, misleading, or adversarial. <br>
Mitigation: Treat all scraped snippets as untrusted source material and verify important claims against primary sources before acting on them. <br>
Risk: The Node dependencies and public network fetches expand the runtime supply-chain and content-ingestion surface. <br>
Mitigation: Review dependency versions before installing and run the skill only in an environment where the listed public network access is acceptable. <br>
Risk: The global monitor includes a hardcoded placeholder entertainment item that is not real news. <br>
Mitigation: Exclude or clearly label the placeholder item during synthesis so it is not presented as factual reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xhrisfu/skills/intelligence-suite) <br>
- [OpenAI RSS feed](https://openai.com/blog/rss.xml) <br>
- [Microsoft AI RSS feed](https://blogs.microsoft.com/ai/feed/) <br>
- [Hacker News API](https://hacker-news.firebaseio.com/v0/topstories.json) <br>
- [Reuters RSS feed](https://www.reutersagency.com/feed/?best-regions=global&post_type=best) <br>
- [SCMP RSS feed](https://www.scmp.com/rss/91/feed) <br>
- [RTHK RSS feed](https://rthk9.rthk.hk/rthk/news/rss/e_expressnews_elocal.xml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Console text with structured intelligence and news packs for agent synthesis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches public RSS/API sources and short linked-article snippets; output should be treated as untrusted web text.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
