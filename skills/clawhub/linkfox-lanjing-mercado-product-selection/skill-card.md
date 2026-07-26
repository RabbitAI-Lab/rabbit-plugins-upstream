## Description: <br>
Mercado Libre（美客多）选品数据查询与分析，通过 LinkFox 网关统一调用蓝鲸商品、官链、关键词、类目、趋势、店铺、评论、汇率与套餐用量工具。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce analysts, marketplace operators, and agents use this skill to query Mercado Libre product, catalog, keyword, category, trend, seller, review, exchange-rate, and plan-usage data through the LinkFox gateway. It supports research and operational product-selection workflows across Mexico, Brazil, Argentina, Chile, and supported Colombia tools. <br>

### Deployment Geography for Use: <br>
Global use; data tools target Mercado Libre sites in Mexico, Brazil, Argentina, Chile, and supported Colombia workflows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a LinkFox API key for paid Mercado Libre data calls. <br>
Mitigation: Use a scoped LinkFox API key, confirm credit cost before repeated paid calls, and keep the gateway pointed at the official LinkFox endpoint unless an alternate endpoint is fully trusted. <br>
Risk: Complete API responses are saved locally and may include sensitive business research data. <br>
Mitigation: Review saved response files before sharing the workspace, delete sensitive local outputs when no longer needed, and avoid printing raw responses unless required for diagnostics. <br>
Risk: A configurable gateway can receive authorization headers and request payloads. <br>
Mitigation: Keep LINKFOX_TOOL_GATEWAY at the official LinkFox gateway for normal use and only override it in trusted environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-lanjing-mercado-product-selection) <br>
- [LinkFox gateway API reference](references/api.md) <br>
- [Lanjing Mercado Libre tool reference](references/lanjing-mercado-tool-reference.md) <br>
- [LinkFox API key and credits guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox tool gateway](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples, shell command examples, and saved JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Calls may use a 24-hour local cache, paid tools may consume LinkFox credits, and full API responses are saved locally while large responses are summarized in stdout.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
