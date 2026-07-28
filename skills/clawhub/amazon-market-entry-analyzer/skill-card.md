## Description: <br>
One-click market viability assessment for Amazon sellers that analyzes market size, competition intensity, brand landscape, pricing structure, and consumer pain points to deliver a GO/CAUTION/AVOID recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and market researchers use this skill to evaluate a named Amazon niche or product category before entering it. It produces a data-backed market entry report with sub-market discovery, competitor analysis, consumer insight, scoring, and a GO/CAUTION/AVOID recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon product/category research inputs, ASINs, marketplace settings, date ranges, and numeric filters are sent to ZooData. <br>
Mitigation: Do not submit sensitive research context unless sharing it with ZooData is acceptable; keep budget, experience, and risk-tolerance details client-side as the skill describes. <br>
Risk: The skill requires a ZooData API key and spends account credits during analysis. <br>
Mitigation: Load ZOODATA_API_KEY from the environment or a secret manager, avoid pasting credentials into prompts, and confirm expected credit usage before broad or multi-call scans. <br>
Risk: Changing ZOODATA_BASE_URL can send the API key to a non-default endpoint. <br>
Mitigation: Use the default ZooData endpoint unless you control and trust the replacement endpoint. <br>
Risk: Temporary review-analysis files may contain sensitive market research context. <br>
Mitigation: Delete temporary review-analysis working directories after use when they contain sensitive inputs or findings. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-market-entry-analyzer) <br>
- [Publisher Profile](https://clawhub.ai/user/apiclaw) <br>
- [Metadata Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [Market Entry Analyzer API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API-backed analysis, guidance] <br>
**Output Format:** [Markdown reports with inline tables, confidence labels, data provenance, API usage, and shell commands when setup or diagnostic steps are needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may consume ZooData API credits for market, product, competitor, price-band, brand, history, and review-analysis calls.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
