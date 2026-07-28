## Description: <br>
Data-driven pricing strategy engine for Amazon sellers that uses ZooData API endpoints to analyze ASIN pricing landscapes and produce RAISE, HOLD, or LOWER signals with profit simulation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and commerce operators use this skill to analyze one or more ASINs, compare category and competitor pricing, simulate margin scenarios, and decide whether to raise, hold, or lower prices. It requires a ZooData API key and should be used with cost confirmation because API calls consume account credits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/apiclaw/skills/amazon-pricing-command-center) <br>
- [Skill metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [API Field Reference](references/reference.md) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables, pricing signals, confidence labels, data provenance, and API usage details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. Uses ZooData API calls that may consume account credits; broad or batch analyses should estimate cost and confirm before execution. Avoid untrusted ZOODATA_BASE_URL hosts.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
