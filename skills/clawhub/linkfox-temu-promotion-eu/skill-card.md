## Description: <br>
Temu 欧洲站电商促销 API，经 LinkFox 网关转发 Partner EU Promotion / 促销活动相关 bg/temu 接口（活动创建、报名、查询、优惠券/秒杀等，接口将按 Partner 文档逐条接入）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to query Temu EU promotion activities, inspect candidate or enrolled goods, enroll goods, update promotion goods, and check asynchronous operation results through LinkFox-proxied Temu Partner APIs. <br>

### Deployment Geography for Use: <br>
Europe / Temu EU supported seller workflows <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle Temu seller tokens and LinkFox gateway credentials. <br>
Mitigation: Use a private workspace, prefer temporary or least-privilege tokens, and avoid sharing command arguments or logs that include tokens. <br>
Risk: The skill stores Temu tokens and full API responses locally, which may include sensitive seller or promotion data. <br>
Mitigation: Restrict file permissions and do not commit the generated linkfox/ directory or ~/.linkfox token store. <br>
Risk: Promotion enrollment, update, and deactivate actions can change live seller operations. <br>
Mitigation: Manually confirm activity IDs, goods IDs, prices, quantities, and operateType values before running mutating commands. <br>
Risk: The generic Temu proxy can call broader Temu API types than the promotion-focused workflow. <br>
Mitigation: Limit usage to documented Temu EU promotion types unless the user explicitly authorizes another Temu API call. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-eu) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization](references/access-token.md) <br>
- [Partner EU promotion catalog](references/partner-eu-catalog.md) <br>
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896) <br>
- [Authorization flow](references/authorization-flow.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request or response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full API responses under a local linkfox session data directory and may print summaries for large responses.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
