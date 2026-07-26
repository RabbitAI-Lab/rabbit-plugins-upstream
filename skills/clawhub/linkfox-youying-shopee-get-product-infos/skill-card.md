## Description: <br>
友鹰Shopee商品选品工具，支持Shopee全站点的商品查询与筛选，覆盖马来西亚、中国台湾、印尼、泰国、菲律宾、新加坡、越南、巴西、墨西哥、智利、哥伦比亚等11个站点。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace analysts, and agents use this skill to build paid LinkFox/YouYing API queries for Shopee product search, filtering, and market data review across 11 marketplaces. It helps return product metrics such as price, sales, rating, category, shop attributes, and source links without extending into advertising, logistics, or store-operation advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls third-party LinkFox/YouYing API endpoints using API keys from environment variables. <br>
Mitigation: Install only in environments where the LinkFox/YouYing gateway is trusted, scope API-key access carefully, and avoid exposing credentials in logs or shared shells. <br>
Risk: The script persists full API responses and cached results locally, which may include product, shop, query, or session data. <br>
Mitigation: Review the generated linkfox data and cache directories, apply local retention controls, and avoid running the skill in workspaces where persisted marketplace data is not acceptable. <br>
Risk: The artifact includes automatic feedback reporting behavior and remote onboarding or dependency-install guidance. <br>
Mitigation: Review or disable feedback reporting and remote installation steps before deployment, especially in managed or restricted agent environments. <br>
Risk: The API consumes paid credits and can incur cost through repeated queries. <br>
Mitigation: Keep the default cache enabled, ask before broad pagination or repeated searches, and disclose additional credit use before issuing follow-up API calls. <br>


## Reference(s): <br>
- [友鹰-Shopee 商品选品 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-youying-shopee-get-product-infos) <br>
- [LinkFox tool gateway](https://tool-gateway.linkfox.com) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and tables, JSON API responses saved to files, and inline shell/Python command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script always writes full API responses to a local linkfox session data path, uses a 24-hour local cache by default, and summarizes responses larger than 8 KB unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
