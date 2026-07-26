## Description: <br>
Amazon Analysis is a ZooData-powered agent skill for broad or composite Amazon market, product, competitor, pricing, listing, and seller research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and Amazon sellers use this skill to run multi-endpoint Amazon research workflows, including market analysis, product selection, ASIN evaluation, pricing research, competitor comparison, listing guidance, and operational monitoring. The skill requires a ZooData API key and should be used as decision support rather than as the sole basis for business decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon research queries, ASINs, keywords, and related business-analysis parameters are sent to ZooData. <br>
Mitigation: Use only with data that may be shared with ZooData, avoid sensitive inputs, and make external API use clear to the user before running research workflows. <br>
Risk: Reports can rely on sampled data, lower-bound estimates, fallback methods, or incomplete endpoint coverage. <br>
Mitigation: Keep confidence labels, data provenance, API usage notes, missing-data limits, and fallback disclosures visible, and validate important business decisions with additional sources. <br>
Risk: The bundled seller-origin case-study workflow includes nationality-focused profiling heuristics. <br>
Mitigation: Avoid that workflow unless it is rewritten to use only explicit, relevant seller-location fields and to exclude speculative origin inference. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-analysis) <br>
- [ZooData-Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API reference](https://api.zoodata.ai/openapi/v2) <br>
- [API field reference](references/reference.md) <br>
- [Execution guide](references/execution-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands, API-derived tables, confidence labels, data provenance, and API usage notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; outputs may include sampled metrics, lower-bound estimates, and directional recommendations.] <br>

## Skill Version(s): <br>
1.1.8 (source: server evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
