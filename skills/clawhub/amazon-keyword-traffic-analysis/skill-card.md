## Description: <br>
Amazon keyword research and traffic analysis for keyword expansion, ad keyword filtering, single-keyword deep dives, reverse-ASIN traffic review, ASIN keyword health, and traffic-change diagnosis using ZooData. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, ecommerce operators, and marketing analysts use this skill to run ZooData-backed Amazon keyword workflows for ad keyword discovery, keyword viability checks, reverse-ASIN traffic review, and ASIN-keyword traffic diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends keyword, ASIN, marketplace, date, and filter inputs to the ZooData API. <br>
Mitigation: Use it only when ZooData is an approved data processor for the query data and avoid including unrelated sensitive user-profile text. <br>
Risk: The skill requires a ZooData API key and can read the optional local ZooData credential store. <br>
Mitigation: Prefer ZOODATA_API_KEY in the environment, avoid plaintext config files when possible, and rotate or revoke credentials if exposed. <br>
Risk: Changing ZOODATA_BASE_URL can direct requests to an untrusted host. <br>
Mitigation: Keep the default ZooData API host unless a trusted deployment explicitly requires another endpoint. <br>
Risk: Broad or ambiguous multi-call scans can consume ZooData account credits. <br>
Mitigation: Estimate credit use and confirm with the user before running broad scans. <br>
Risk: ZooData keyword and ASIN observations are directional and do not prove seller-specific conversion, profitability, bids, or budget decisions. <br>
Mitigation: Request seller-provided ABA-SQP or Amazon Ads evidence before making calibrated commercial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-keyword-traffic-analysis) <br>
- [ZooData Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [Execution Guide - Amazon Keyword Intelligence](references/execution-guide.md) <br>
- [ZooData Keyword API Reference](references/reference.md) <br>
- [Keyword Expansion](references/scenarios-expand.md) <br>
- [Single Keyword Analysis](references/scenarios-keyword-analysis.md) <br>
- [Reverse ASIN Keyword Analysis](references/scenarios-reverse-asin.md) <br>
- [Keyword Traffic Diagnosis](references/scenarios-keyword-traffic-diagnosis.md) <br>
- [Amazon Brand Analytics metric glossary](https://sellercentral.amazon.com/brand-analytics/metric-glossary?linkedFrom=query-performance-brand-report-table-qp-impressions-group) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with data notes, evidence summaries, recommendations, and inline ZooData CLI command usage when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; ZooData API calls may consume account credits and use keyword, ASIN, marketplace, date, and filter inputs.] <br>

## Skill Version(s): <br>
0.1.3 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
