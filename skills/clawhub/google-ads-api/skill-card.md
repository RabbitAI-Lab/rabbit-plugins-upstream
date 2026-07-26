## Description: <br>
Google Ads API integration with managed OAuth for querying campaigns, ad groups, keywords, and performance metrics with GAQL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, analysts, and developers use this skill to access Google Ads account data, run GAQL queries, inspect campaign performance, and manage Google Ads resources through Maton-managed authentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Ads account data and OAuth access flow through Maton's service. <br>
Mitigation: Use the intended Maton and Google Ads accounts, protect MATON_API_KEY, and review organizational requirements for third-party access before use. <br>
Risk: Requests can target the wrong Google Ads connection or manager/client account when multiple accounts are available. <br>
Mitigation: Specify the connection ID and the correct customer or login customer ID before querying or changing data. <br>
Risk: Create, update, or delete calls can alter Google Ads resources. <br>
Mitigation: Require clear confirmation of the target resource and intended effect before any write or delete action. <br>


## Reference(s): <br>
- [ClawHub Google Ads skill](https://clawhub.ai/byungkyu/skills/google-ads-api) <br>
- [Google Ads API overview](https://developers.google.com/google-ads/api/docs/start) <br>
- [GAQL query guide](https://developers.google.com/google-ads/api/docs/query/overview) <br>
- [GAQL fields reference](https://developers.google.com/google-ads/api/fields/v24/overview) <br>
- [Maton CLI manual](https://cli.maton.ai/manual) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI, HTTP, Python, JavaScript, and GAQL examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and a connected Google Ads OAuth account; write and delete actions require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
