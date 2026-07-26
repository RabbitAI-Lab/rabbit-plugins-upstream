## Description: <br>
Comprehensive news aggregator that fetches, filters, and deeply analyzes real-time content from 8 major sources: Hacker News, GitHub Trending, Product Hunt, 36Kr, Tencent News, WallStreetCN, V2EX, and Weibo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cclank](https://clawhub.ai/user/cclank) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to fetch hot news from multiple technology, finance, social, and developer-community sources, then produce concise Chinese briefing reports with deep interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes live requests to multiple public news sites and can follow article links in deep mode. <br>
Mitigation: Prefer narrower source selections when possible and run it only in environments where outbound web requests are acceptable. <br>
Risk: Fetched article text is untrusted web content and may be inaccurate, misleading, or prompt-like. <br>
Mitigation: Treat fetched content as untrusted evidence and review generated briefings before relying on or redistributing them. <br>
Risk: Python dependencies are unpinned, which can reduce reproducibility across environments. <br>
Mitigation: Pin and review dependencies in a controlled environment before operational use. <br>
Risk: The skill saves generated reports locally. <br>
Mitigation: Review local report contents and retention practices if reports may include sensitive user queries or curated findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cclank/skills/news-aggregator-skill) <br>
- [Publisher profile](https://clawhub.ai/user/cclank) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [JSON news items from the fetch script and Simplified Chinese markdown briefing reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are saved locally under reports/ with timestamped filenames and also presented in chat.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
