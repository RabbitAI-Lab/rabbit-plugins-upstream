## Description: <br>
Generates high-signal capital market anomaly and delta reports for Chinese and global markets using local news collection, market-data helper skills, source-diversity rules, and temporal verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangzhe1991](https://clawhub.ai/user/yangzhe1991) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to gather recent market news, compare it against the prior 24 hours of saved reports, and produce concise markdown briefings about market-moving events, affected tickers, and leading signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches live financial and news data and the evidence says some advertised 24-hour and anti-hallucination safeguards may be overstated. <br>
Mitigation: Treat generated reports as analyst drafts, verify source URLs, publication times, and market data before acting on them, and keep the final verification checklist mandatory. <br>
Risk: The skill runs local helper scripts by path, including cross-skill finance and crypto helpers. <br>
Mitigation: Install and run it only in a trusted OpenClaw workspace, review the referenced helper scripts, and pin or vendor dependencies before routine use. <br>
Risk: The skill stores report/cache files and includes behavior that may delete prior report history. <br>
Mitigation: Review or modify retention commands before deployment and keep backups if saved market-report history is operationally important. <br>
Risk: The evidence guidance calls out shell=True subprocess usage in local scripts. <br>
Mitigation: Review command construction before execution and prefer argument-list subprocess calls when adapting or maintaining the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangzhe1991/skills/capital-market-report) <br>
- [Publisher profile](https://clawhub.ai/user/yangzhe1991) <br>
- [Sina Finance roll API](https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50) <br>
- [BBC Business RSS](https://feeds.bbci.co.uk/news/business/rss.xml) <br>
- [Yahoo Finance RSS](https://finance.yahoo.com/news/rssindex) <br>
- [WSJ Markets RSS](https://feeds.a.dj.com/rss/RSSMarketsMain.xml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with source links, event sections, delta summary, calendar items, and verification checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live source URLs for reported articles and saves report/cache files under the user's OpenClaw workspace.] <br>

## Skill Version(s): <br>
6.1.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
