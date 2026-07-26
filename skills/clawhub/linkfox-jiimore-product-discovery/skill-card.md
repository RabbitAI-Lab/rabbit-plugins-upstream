## Description: <br>
Jiimore-商品发现 helps agents discover Amazon products by querying Jiimore product-discovery data with keyword, marketplace, conversion, click-growth, review, price, and profitability filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and e-commerce analysts use this skill to find potential products by keyword and filter results by market, conversion rate, click growth, review count, price, seller country, listing age, and gross margin. It is suited to product discovery, opportunity screening, and competitive benchmarking, not broader advertising, inventory, or listing-optimization workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends product-search parameters and session metadata to an external paid Jiimore/LinkFox API. <br>
Mitigation: Use it only with data appropriate for the external service, confirm API-key and credit expectations with the user, and avoid unnecessary repeated queries. <br>
Risk: Full API responses are saved locally, and fallback output paths may place saved results outside the current workspace when preferred paths are not writable. <br>
Mitigation: Review where result files are written, avoid sensitive query content, and clean up saved JSON outputs when they are no longer needed. <br>
Risk: Automatic feedback reporting can send user satisfaction or issue details to a separate LinkFox endpoint. <br>
Mitigation: Disable or avoid feedback reporting unless users explicitly consent to sending that information. <br>


## Reference(s): <br>
- [Jiimore product discovery API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-product-discovery) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>
- [LinkFox tool gateway](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON, markdown] <br>
**Output Format:** [Markdown guidance with JSON request examples, shell commands, API responses, saved JSON files, and tabular result summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full API responses to local JSON files, uses a 24-hour local cache by default, and may summarize large responses unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
