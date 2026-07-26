## Description: <br>
Seerfar-Ozon关键词反查 helps agents use LinkFox's Seerfar Ozon keyword back-search API to reverse-look up organic and ad search terms for up to 20 Ozon product SKUs and return market metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External e-commerce operators, marketplace analysts, and agents use this skill to investigate which Ozon and available Wildberries search terms a product SKU appears under, then review search volume, rank, exposure, conversion, seller, and competition metrics for listing and advertising analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that SKU lookup requests, session metadata, and full API responses may be shared with LinkFox services or stored locally by default. <br>
Mitigation: Use the skill only for data appropriate to share with LinkFox, configure credentials deliberately, and review or remove saved response files according to local data-handling policy. <br>
Risk: The security scan flags remote onboarding package download behavior and automatic feedback reporting as reasons for review before installation. <br>
Mitigation: Review the feedback workflow and any onboarding package source before enabling those paths, and install only when the publisher and downloaded materials are trusted. <br>
Risk: The skill consumes LinkFox credits for API calls and can incur extra cost when queries are repeated or paginated. <br>
Mitigation: Confirm expected cost before additional calls and reuse cached or saved responses when they are sufficient. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-keyword-back-search) <br>
- [Seerfar Ozon keyword back-search API reference](references/api.md) <br>
- [LinkFox tool gateway endpoint](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance] <br>
**Output Format:** [Markdown tables and summaries with saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials; full responses are written to local JSON files, with small responses also printed inline.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
