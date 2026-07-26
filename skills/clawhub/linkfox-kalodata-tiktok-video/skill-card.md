## Description: <br>
Searches Kalodata-backed TikTok Shop video leaderboards and retrieves a selected video's engagement, GMV, advertising, creator, and product metrics by videoId. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External commerce analysts, marketplace operators, and agent users use this skill to find high-performing TikTok shoppable videos and inspect a selected video's engagement, sales, advertising, and creator metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses credentials and external network calls. <br>
Mitigation: Use only a trusted gateway configuration and a scoped Kalodata or LinkFox API key. <br>
Risk: API responses and metadata may be written locally by default. <br>
Mitigation: Run the skill in an appropriate workspace and review stored response files before sharing or committing project contents. <br>
Risk: Each lookup consumes paid credits. <br>
Mitigation: Confirm the requested region, date range, page, and videoId before making additional calls. <br>


## Reference(s): <br>
- [Kalodata-TikTok视频搜索与详情 API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-video) <br>
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses saved to local files, with stdout JSON or concise summaries depending on response size.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses authenticated external requests, 24-hour parameter caching, and session-organized local response files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
