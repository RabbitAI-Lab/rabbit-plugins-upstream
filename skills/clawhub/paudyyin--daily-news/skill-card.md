## Description: <br>
Fetch top news from Baidu, Google, and other sources daily. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to fetch current top headlines and search trends from Baidu, Google Trends, and similar sources, then return the resulting daily news list to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs Python dependencies that are not pinned to exact versions. <br>
Mitigation: Review and pin dependency versions before controlled or repeatable deployments. <br>
Risk: Running the skill contacts Baidu and Google Trends and exposes normal request metadata such as IP address and user agent to those services. <br>
Mitigation: Run only in environments where those outbound requests are permitted and users understand the external network contact. <br>
Risk: Live news and trend scraping can return incomplete or stale results when upstream pages or feeds change. <br>
Mitigation: Check the returned headlines before relying on them in user-facing summaries or downstream workflows. <br>


## Reference(s): <br>
- [Daily News ClawHub listing](https://clawhub.ai/paudyyin/daily-news) <br>
- [Baidu realtime hot search](https://top.baidu.com/board?tab=realtime) <br>
- [Google Trends daily RSS feed](https://trends.google.com/trends/trendingsearches/daily/rss?geo=US) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown] <br>
**Output Format:** [Plain text or Markdown news summary generated from script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live results depend on network access and availability of upstream news and trend services.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
