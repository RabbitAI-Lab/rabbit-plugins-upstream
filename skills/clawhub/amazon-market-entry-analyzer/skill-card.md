## Description: <br>
Evaluates Amazon product categories with ZooData market, competitor, price, brand, review, and trend data to produce a GO/CAUTION/AVOID market-entry recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, ecommerce operators, and market researchers use this skill to evaluate a named product niche or category before entering the market. It produces a viability score, GO/CAUTION/AVOID verdict, competitor and price analysis, consumer insight summary, and data provenance based on ZooData API results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package exposes a broad ZooData command-line tool beyond the market-entry workflow. <br>
Mitigation: Use the documented market-entry workflow for this skill and review proposed commands before execution. <br>
Risk: The skill requires a ZooData API key and can redirect API traffic if ZOODATA_BASE_URL is set. <br>
Mitigation: Provide only the intended ZooData key, avoid setting ZOODATA_BASE_URL unless redirection is intentional, and remove credentials from the environment after use. <br>
Risk: The workflow can consume API credits across many endpoints. <br>
Mitigation: Monitor the API usage table, stop on credit-exhaustion responses, and avoid repeated deep dives without user confirmation. <br>
Risk: Market-entry recommendations are based on sampled API data and should not be treated as the sole basis for business decisions. <br>
Mitigation: Validate recommendations with additional sources, supplier economics, compliance review, and seller-specific constraints before acting. <br>
Risk: Fallback review analysis may create temporary work directories containing review data. <br>
Mitigation: Delete temporary review work directories after fallback analysis is complete. <br>


## Reference(s): <br>
- [Market Entry Analyzer API Field Reference](references/reference.md) <br>
- [ZooData Skills GitHub Repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [ClawHub Skill Listing](https://clawhub.ai/apiclaw/skills/amazon-market-entry-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with tables, confidence labels, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; API-backed findings include data provenance and API usage tables.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
