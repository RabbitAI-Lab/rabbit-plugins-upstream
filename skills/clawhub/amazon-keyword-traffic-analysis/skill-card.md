## Description: <br>
Supports Amazon keyword expansion, ad-keyword filtering, single-keyword analysis, ASIN keyword health checks, keyword traffic diagnosis, and ASIN traffic-term workflows using ZooData keyword endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace analysts, and agents use this skill to research Amazon keyword demand, expand candidate keywords, inspect ASIN traffic sources, and diagnose keyword traffic movement with ZooData evidence boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and can make credit-consuming authenticated API calls. <br>
Mitigation: Install only for trusted use, keep the API key private, and confirm broad or multi-call scans before execution. <br>
Risk: The bundled ZooData CLI exposes broader authenticated functionality than the documented keyword workflows. <br>
Mitigation: Restrict use to the documented keyword subcommands and review requested commands before running them. <br>
Risk: Seller ABA-SQP or Ads data may contain sensitive business information. <br>
Mitigation: Share only data the user is authorized to provide and include only the fields needed for the requested keyword decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-keyword-traffic-analysis) <br>
- [ZooData Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [README.md](artifact/README.md) <br>
- [Execution Guide](artifact/references/execution-guide.md) <br>
- [ZooData Keyword API Reference](artifact/references/reference.md) <br>
- [Keyword Expansion](artifact/references/scenarios-expand.md) <br>
- [Single Keyword Analysis](artifact/references/scenarios-keyword-analysis.md) <br>
- [Reverse ASIN Keyword Analysis](artifact/references/scenarios-reverse-asin.md) <br>
- [Keyword Traffic Diagnosis](artifact/references/scenarios-keyword-traffic-diagnosis.md) <br>
- [Amazon Brand Analytics metric glossary](https://sellercentral.amazon.com/brand-analytics/metric-glossary?linkedFrom=query-performance-brand-report-table-qp-impressions-group) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with API usage tables and inline command references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; API calls may consume ZooData account credits; conclusions are bounded by available keyword, ASIN, and seller-provided evidence.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
