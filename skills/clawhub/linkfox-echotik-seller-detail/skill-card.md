## Description: <br>
查询TikTok Shop店铺（卖家）详情，通过sellerId获取单个店铺的完整档案，返回总销量、多周期(1天/7天/30天/90天)销量与销售额(GMV)、粉丝数、评分、评价数、好评率、送达率、回复率、在店商品数、带货达人数、带货视频数、直播数、价格区间、商品分类、预估上架时间等指标。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and ecommerce analysts use this skill to retrieve a full performance profile for one TikTok Shop store when they already have a sellerId. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and makes authenticated network calls to retrieve seller details. <br>
Mitigation: Install and run it only when the user is comfortable granting LinkFox API access for this workflow. <br>
Risk: Calls can consume paid LinkFox credits. <br>
Mitigation: Avoid repeated automatic calls for the same request, and tell the user before continuing with extra paid lookups. <br>
Risk: Full seller-detail responses are stored locally after calls. <br>
Mitigation: Review the generated LinkFox session data files and handle them according to the workspace's data-retention expectations. <br>
Risk: A configured LINKFOX_TOOL_GATEWAY value can change the API gateway used by the script. <br>
Mitigation: Verify LINKFOX_TOOL_GATEWAY is unset or points to the official LinkFox gateway before use. <br>
Risk: The artifact documents automatic feedback reporting to a separate LinkFox feedback endpoint. <br>
Mitigation: Review feedback behavior before installation if user comments or task outcomes may be sensitive. <br>


## Reference(s): <br>
- [EchoTik-TikTok店铺详情 API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-seller-detail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell or Python command examples and saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a sellerId; writes complete seller-detail responses to local LinkFox session data, prints small JSON responses inline, and summarizes larger responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
