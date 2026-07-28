## Description: <br>
Extracts Amazon review intelligence across pain points, buying factors, user profiles, usage patterns, competitor sentiment, differentiation opportunities, and listing copy suggestions using ZooData. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze Amazon product reviews by ASIN, competitor set, or category. It helps identify customer complaints, purchase drivers, market context, and practical listing or product improvement opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product identifiers, keywords, review queries, marketplace filters, and the ZooData API key are sent to the configured API host. <br>
Mitigation: Use ZOODATA_API_KEY, keep credentials out of shared files, and do not set ZOODATA_BASE_URL to an untrusted host. <br>
Risk: Composite or broad scans can consume ZooData account credits. <br>
Mitigation: Confirm the expected credit cost before multi-call scans and use granular commands when working under a credit cap. <br>
Risk: Sparse review samples can make percentage-based conclusions look stronger than the evidence supports. <br>
Mitigation: Apply the skill's sample-size advisory, report counts alongside percentages, and validate important business decisions with additional sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-review-intelligence-extractor) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API reference](https://api.zoodata.ai/openapi/v2) <br>
- [Local API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with command examples and optional JSON-backed analysis outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. API calls consume ZooData credits and fallback review analysis may create temporary files under /tmp.] <br>

## Skill Version(s): <br>
1.0.5 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
