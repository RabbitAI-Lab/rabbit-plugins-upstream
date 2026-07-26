## Description: <br>
搜索淘宝商品并返回价格、销量、店铺、发货地和商品链接。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiongweixp](https://clawhub.ai/user/xiongweixp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping assistants use this skill to search Taobao by keyword, compare product prices and sales signals, and return concise product result summaries with links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for Bana Skill Center AppID and SecureKey credentials and may save them locally for reuse. <br>
Mitigation: Review before installing, prefer one-time credential use when appropriate, remove saved credentials when no longer needed, and avoid sharing SecureKey values in later responses. <br>
Risk: Credentials are sent to wxpub.aibana.art for Taobao searches, and the endpoint can be overridden with BANA_TAOBAO_BASE_URL. <br>
Mitigation: Use the default service endpoint unless the user explicitly provides a trusted test endpoint, and only proceed when the user is comfortable sending those credentials to the service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiongweixp/skills/bana-taobao-search) <br>
- [Publisher profile](https://clawhub.ai/user/xiongweixp) <br>
- [Bana Skill Center](https://wxpub.aibana.art) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown summaries with optional shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results may include product title, price, sales, shop, shipping location, and detail link; fields can be incomplete if the upstream Taobao page or session fails.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
