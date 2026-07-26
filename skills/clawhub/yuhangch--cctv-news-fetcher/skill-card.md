## Description: <br>
Fetch and parse news highlights from CCTV News Broadcast (Xinwen Lianbo) for a given date. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuhangch](https://clawhub.ai/user/yuhangch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch CCTV News Broadcast highlights for a requested date and receive a concise summary grouped by topic when possible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to CCTV-related news pages when asked for news. <br>
Mitigation: Install and use it only in environments where that network access is acceptable, and review the documented domains before execution. <br>
Risk: News summaries depend on live public pages that may change, be unavailable, or parse incompletely. <br>
Mitigation: Verify important summaries against the linked CCTV source pages before relying on them. <br>
Risk: Relative date requests such as today or yesterday depend on the agent environment's local time. <br>
Mitigation: Use an explicit YYYYMMDD date when the exact broadcast date matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuhangch/skills/cctv-news-fetcher) <br>
- [Publisher profile](https://clawhub.ai/user/yuhangch) <br>
- [Example Usage](examples/example.md) <br>
- [CCTV News Broadcast recent archive](https://tv.cctv.com/lm/xwlb/day/{YYYYMMDD}.shtml) <br>
- [CCTV News Broadcast older archive](https://cctv.cntv.cn/lm/xinwenlianbo/{YYYYMMDD}.shtml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands] <br>
**Output Format:** [Markdown summary based on JSON crawler output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bun or Node.js, node-html-parser, and outbound access to CCTV-related news pages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
