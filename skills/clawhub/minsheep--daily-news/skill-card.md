## Description: <br>
Fetch top news from Baidu, Google, and other sources daily. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[MINSHEEP](https://clawhub.ai/user/MINSHEEP) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to fetch a daily list of current hot search and trend headlines from Baidu and Google Trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill returns remote headlines from Baidu and Google Trends, so results may be incomplete, unavailable, or misleading if upstream pages, feeds, or network access change. <br>
Mitigation: Treat returned headlines as remote content, verify important items against primary sources, and review failures or empty results before relying on the output. <br>
Risk: The skill runs a local Python script with third-party Python dependencies and outbound network requests. <br>
Mitigation: Run it in a virtual environment, review or pin dependency versions before deployment, and allow outbound access only to the expected public news and trend endpoints. <br>


## Reference(s): <br>
- [Baidu Hot Search](https://top.baidu.com/board?tab=realtime) <br>
- [Google Trends Daily Search Trends RSS](https://trends.google.com/trends/trendingsearches/daily/rss?geo=US) <br>
- [ClawHub skill page](https://clawhub.ai/MINSHEEP/daily-news) <br>
- [MINSHEEP publisher profile](https://clawhub.ai/user/MINSHEEP) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text headline list] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs a timestamped Chinese-language list of up to 10 unique headlines gathered from remote public trend sources.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
