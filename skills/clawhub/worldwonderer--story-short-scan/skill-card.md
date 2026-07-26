## Description: <br>
Scans short-form Chinese web-fiction ranking samples from platforms such as Zhihu Yanyan, Qimao, Black Rock, and Dianzhong to identify current genre, emotion, and topic signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, editors, and developers use this skill to collect or review short-story ranking samples, compare platform trends, and turn those observations into topic candidates, risk thresholds, and follow-up validation actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Black Rock collector can use a logged-in admin browser token to query protected backend APIs. <br>
Mitigation: Install only when this collection behavior is intended, use a dedicated browser profile or account where possible, and confirm the account is allowed to access the backend API. <br>
Risk: Ranking-based market signals can become stale quickly and may mislead writing decisions if treated as durable trends. <br>
Mitigation: Require each report to state the sample date, confidence level, saturation risk, and next rescan time before using it for planning. <br>
Risk: Browser scraping in a profile with unrelated active sessions can expose sensitive session context to collection scripts. <br>
Mitigation: Run browser-based collection in a dedicated profile that does not contain unrelated sensitive logins. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-short-scan) <br>
- [OpenClaw Metadata Source](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Real Market Data Reference](references/real-market-data.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with tables, ranked recommendations, and optional command guidance for browser-based data collection] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should include sample date, trend confidence, saturation risk, and the next recommended rescan time.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
