## Description: <br>
Auto Publish provides a multi-platform content publishing scaffold for video posts, batch queues, tag generation, best-time recommendations, and tracking reports. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[nh5gntnf78-oss](https://clawhub.ai/user/nh5gntnf78-oss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, operators, and developers use this skill to prepare publishing commands, batch lists, generated tags, recommended posting windows, and local tracking reports for multi-platform content workflows. Treat live publishing and analytics claims as scaffold behavior unless the platform integrations are reviewed, hardened, and verified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may mislead users by presenting fabricated publish URLs and analytics as real results. <br>
Mitigation: Treat it as a demo scaffold and verify real platform API integrations before relying on any publish or analytics output. <br>
Risk: Platform credentials may be entered into scripts/config.json. <br>
Mitigation: Use safer secret storage, avoid committing real credentials, and review the code before adding any live platform credentials. <br>
Risk: A hardened version could perform live or batch posting without enough user confirmation. <br>
Mitigation: Require dry-run review and explicit confirmation before any live or batch publishing action. <br>


## Reference(s): <br>
- [Auto Publish on ClawHub](https://clawhub.ai/nh5gntnf78-oss/skills/auto-publish) <br>
- [Douyin Open Platform](https://open.douyin.com/) <br>
- [Xiaohongshu Open Platform](https://open.xiaohongshu.com/) <br>
- [Bilibili Open Platform](https://open.bilibili.com/) <br>
- [Google Cloud Console for YouTube Data API](https://console.cloud.google.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and Python/JSON snippets; scripts emit JSON or console text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include local configuration examples, publish-list examples, generated tags, recommended posting times, publish-result records, tracking metrics, and optional .skill package archives.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
