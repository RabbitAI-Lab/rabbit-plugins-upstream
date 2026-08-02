## Description: <br>
Data-driven pricing strategy engine for Amazon sellers that auto-detects product categories from ASINs, analyzes pricing landscapes, and returns RAISE/HOLD/LOWER signals with profit simulation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and their agents use this skill to analyze one or more ASINs, compare category pricing signals, simulate margin outcomes, and decide whether to raise, hold, or lower prices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled ZooData CLI exposes broader research endpoints than this pricing workflow needs, which can increase credit use or collect unrelated market data if used outside the documented scope. <br>
Mitigation: Keep runs limited to documented pricing-analysis endpoints and confirm estimated credit usage before batch or broad analyses. <br>
Risk: Pricing signals depend on sampled ZooData API responses and lower-bound monthly sales estimates, so recommendations may be incomplete or stale. <br>
Mitigation: Treat RAISE/HOLD/LOWER signals as decision support, include the report disclaimer and confidence labels, and validate against additional business data before changing prices. <br>
Risk: The skill requires a ZooData API key and makes network calls that consume account credits. <br>
Mitigation: Use trusted ZooData endpoints, protect ZOODATA_API_KEY, stop on missing or invalid keys, and report API usage and credits consumed. <br>


## Reference(s): <br>
- [ZooData API Field Reference](artifact/references/reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-pricing-command-center) <br>
- [ZooData Skills Repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Keys](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown reports with tables and concise pricing recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include data provenance, API usage, confidence labels, and credit estimates.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
