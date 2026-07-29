## Description: <br>
Data-driven pricing strategy engine for Amazon sellers that analyzes ASINs, category pricing, competitors, and profit scenarios to recommend RAISE, HOLD, or LOWER signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and ecommerce operators use this skill to evaluate product pricing from one or more ASINs, compare category and competitor signals, estimate profit scenarios, and decide whether to raise, hold, or lower price. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled CLI exposes ZooData research commands beyond the pricing workflow. <br>
Mitigation: Limit agent instructions to the pricing subcommands used by this skill and review endpoint plans before execution. <br>
Risk: API calls send ASINs, category data, marketplace or date values, and numeric filters to ZooData while consuming account credits. <br>
Mitigation: Confirm estimated credit use before broad or batch analysis and avoid sending unnecessary business context. <br>
Risk: Credential handling depends on ZOODATA_API_KEY or an optional local ZooData config file. <br>
Mitigation: Prefer an environment variable or managed secret store, use a scoped key where possible, and keep the API base URL restricted to trusted ZooData or localhost hosts. <br>


## Reference(s): <br>
- [Amazon Pricing Command Center reference](artifact/references/reference.md) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData Skills repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-pricing-command-center) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with tables, API usage details, and concise pricing recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should include data provenance, credit usage, confidence labels, and the required ZooData sampling disclaimer.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
