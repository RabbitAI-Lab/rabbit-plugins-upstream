## Description: <br>
Comprehensive news aggregator that fetches, filters, and deeply analyzes real-time content from 8 major sources: Hacker News, GitHub Trending, Product Hunt, 36Kr, Tencent News, WallStreetCN, V2EX, and Weibo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[administratorfung](https://clawhub.ai/user/administratorfung) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and knowledge workers use this skill to fetch current public news from multiple technology, finance, product, and social sources, then turn the results into concise Simplified Chinese briefings and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts multiple public news sites and can follow article links in deep mode. <br>
Mitigation: Run it in a normal project sandbox and use it only when this public web fetching behavior is expected. <br>
Risk: The skill depends on Python packages for HTTP fetching and HTML parsing. <br>
Mitigation: Pin or review the Python dependencies before deployment. <br>
Risk: The skill writes Markdown reports to the local reports/ directory. <br>
Mitigation: Review generated reports before sharing or publishing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/administratorfung/skills/news-aggregator-skill-3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [JSON news items from the fetch script and Markdown news reports for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes timestamped reports under reports/ and may include fetched article text when deep mode is enabled.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
