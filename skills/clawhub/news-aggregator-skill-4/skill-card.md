## Description: <br>
Comprehensive news aggregator that fetches, filters, and analyzes real-time content from Hacker News, GitHub Trending, Product Hunt, 36Kr, Tencent News, WallStreetCN, V2EX, and Weibo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanjolnoring](https://clawhub.ai/user/nanjolnoring) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to request current news scans, focused keyword briefings, finance updates, and deeper interpretations of trending technical topics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed artifact references separately supplied fetch_news.py and templates.md files that are not included in the artifact. <br>
Mitigation: Before installing, confirm that any separately supplied fetch script and template file come from a trusted source. <br>
Risk: The skill fetches public web pages and can broaden searches unless strict filters are requested. <br>
Mitigation: Use explicit source, keyword, and time-window requests when precision matters, and review generated summaries before relying on them. <br>
Risk: Saved Markdown reports may contain sensitive topics or research interests in a local reports/ folder. <br>
Mitigation: Delete local reports when topics are sensitive or when retained copies are not needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nanjolnoring/skills/news-aggregator-skill-4) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports and JSON fetch results when the companion fetch script is available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Saves timestamped Markdown reports under reports/ and presents the report content in chat.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
