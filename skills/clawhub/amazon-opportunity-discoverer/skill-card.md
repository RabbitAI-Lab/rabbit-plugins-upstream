## Description: <br>
Automated product opportunity scanner for Amazon sellers that scans categories with ZooData, validates candidates with real-time market data, and ranks opportunities by composite score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and ecommerce researchers use this skill to discover Amazon product opportunities from a budget, seller profile, category, or keyword. It produces ranked candidates, risk alerts, next steps, data provenance, and API usage details from ZooData API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ZooData API key and can consume paid credits during broad product research scans. <br>
Mitigation: Confirm broad scans before execution, monitor API usage in the report, and use a scoped environment variable for the key. <br>
Risk: Business-sensitive product research may be sent to the configured ZooData API host. <br>
Mitigation: Avoid setting ZOODATA_BASE_URL unless the target host is intentionally trusted and appropriate for the research data. <br>


## Reference(s): <br>
- [Reference API Field Guide](references/reference.md) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Keys](https://zoodata.ai/en/api-keys) <br>
- [Skill Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with tables, confidence labels, data provenance, API usage, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. Review broad API-consuming scans before execution, prefer environment variables for credentials, and avoid setting ZOODATA_BASE_URL unless the target host is trusted.] <br>

## Skill Version(s): <br>
1.0.4 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
