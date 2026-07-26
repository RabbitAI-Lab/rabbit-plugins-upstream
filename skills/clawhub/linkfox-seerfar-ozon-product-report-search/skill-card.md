## Description: <br>
Searches Seerfar Ozon product-report data so an agent can filter product-level rows by sales, revenue, growth, conversion, price, rating, reviews, brand, seller, fulfillment, listing age, margin, return rate, and related Ozon metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and commerce analysts use this skill to screen Ozon products, inspect competitor product performance, mine best sellers, and build price or conversion-band reports from product-level Seerfar data. It is most relevant when the user needs Ozon product rows rather than keyword, shop, category, or non-Ozon marketplace data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-product-report-search) <br>
- [Seerfar Ozon product report API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown guidance, JSON API parameters, stdout summaries, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API-key configuration and consumes LinkFox credits. Security review verdict is suspicious: install only if LinkFox receiving Ozon report queries, API keys, and session metadata is acceptable; review LINKFOX_TOOL_GATEWAY before use, avoid secrets in feedback text, and clear generated linkfox data and cache files when reports are no longer needed.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
