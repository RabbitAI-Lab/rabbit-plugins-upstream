## Description: <br>
Aggregate and deliver daily news digests from multiple public sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and scheduled agents use this skill to retrieve a concise daily digest of current hot topics from Baidu Hot Search and Google Trends. It is suited for quick news briefings, trend monitoring, and daily report generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill parses external web and RSS content, so dependency or parser behavior could affect reliability. <br>
Mitigation: Pin and review the Python dependencies before installation, then periodically retest the configured sources. <br>
Risk: Public trend sources can be unavailable, rate-limited, region-specific, or incomplete. <br>
Mitigation: Treat the digest as a current-trends summary and verify important items against primary news sources before acting on them. <br>


## Reference(s): <br>
- [ClawHub daily-news skill page](https://clawhub.ai/paudyyin/skills/daily-news) <br>
- [Baidu Hot Search board](https://top.baidu.com/board?tab=realtime) <br>
- [Google Trends Daily Search Trends RSS](https://trends.google.com/trends/trendingsearches/daily/rss?geo=US) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [UTF-8 text digest with a timestamp and numbered news items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches public web and RSS sources at runtime; output length depends on available unique results.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, package.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
