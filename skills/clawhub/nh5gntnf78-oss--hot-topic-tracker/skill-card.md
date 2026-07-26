## Description: <br>
Tracks hot-topic lists across Douyin, Xiaohongshu, Zhihu, Bilibili, Weibo, and WeChat, analyzes trends with the current platform model, generates content ideas, and can save the results to Tencent Docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nh5gntnf78-oss](https://clawhub.ai/user/nh5gntnf78-oss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, social media operators, marketing teams, and content strategists use this skill to collect current platform trends, rank and cluster topics, forecast topic momentum, compare competitor content, and generate platform-specific content ideas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Logged-in browser sessions may expose account-specific social or content-platform data during trend collection. <br>
Mitigation: Require explicit confirmation before using profile="user" and avoid running the skill against sensitive accounts or private content. <br>
Risk: Broad trigger phrases plus automatic Tencent Docs saving can write generated reports to an unintended destination. <br>
Mitigation: Confirm the Tencent Docs destination, sharing settings, and report title before saving or scheduling recurring runs. <br>
Risk: Scheduled hourly monitoring can repeatedly collect and publish low-confidence trend predictions. <br>
Mitigation: Limit recurring jobs to defined time windows and review generated alerts or reports before distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nh5gntnf78-oss/skills/hot-topic-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/nh5gntnf78-oss) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with tables, structured topic recommendations, optional code snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include trend summaries, title variants, platform-specific content outlines, competitor analysis, scheduling guidance, and Tencent Docs destination details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
