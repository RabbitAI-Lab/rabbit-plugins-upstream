## Description: <br>
视频平台公域流量精准获客工具。基于评论区数据挖掘，支持竞品截流、意向客户筛选、舆情转化及私域引流，适用于短视频营销、销售线索挖掘、精准获客与流量变现，助力企业低成本获取高意向客户。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[um-why](https://clawhub.ai/user/um-why) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and sales teams use this skill to search public Douyin content, retrieve creator posts and comments, monitor hot topics, and export structured lead signals for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk collection of public Douyin user and comment data may create privacy, platform-terms, or anti-spam compliance issues. <br>
Mitigation: Use only when authorized to collect and process the targeted data, and review platform terms, privacy obligations, and anti-spam rules before deployment. <br>
Risk: The API token and search, video, or account inputs are sent to guaikei.com. <br>
Mitigation: Limit token access to approved operators, avoid sending sensitive inputs, and rotate the token if exposure is suspected. <br>
Risk: Result logs can contain user IDs, nicknames, comment text, and related metadata on disk. <br>
Mitigation: Store logs in an access-controlled location and delete or secure them after operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/um-why/skills/douyin-public-customer-acquisition) <br>
- [Publisher profile](https://clawhub.ai/user/um-why) <br>
- [Guaikei service website](https://www.guaikei.com) <br>
- [Options reference](references/options.md) <br>
- [Changelog](references/changelog.md) <br>
- [Search input schema](assets/search_cli_req.schema.json) <br>
- [Search output schema](assets/search_cli_resp.schema.json) <br>
- [Post input schema](assets/post_cli_req.schema.json) <br>
- [Post output schema](assets/post_cli_resp.schema.json) <br>
- [Comment input schema](assets/comment_cli_req.schema.json) <br>
- [Comment output schema](assets/comment_cli_resp.schema.json) <br>
- [Hot list output schema](assets/hot_cli_resp.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, configuration] <br>
**Output Format:** [CLI console output and JSON log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, and comment commands can write JSON logs under the skill logs directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
