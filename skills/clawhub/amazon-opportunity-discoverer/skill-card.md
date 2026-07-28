## Description: <br>
Amazon Opportunity Discoverer helps Amazon sellers scan categories, validate product candidates with ZooData signals, and rank product opportunities by a composite score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and ecommerce researchers use this skill to discover what products to sell when they do not already have a specific niche in mind. It maps seller profile inputs to scanning strategies, calls ZooData for market and product signals, and returns a ranked opportunity report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ZooData requests with a ZooData API key, and a non-default API host could receive that credential. <br>
Mitigation: Prefer ZOODATA_API_KEY, keep the default ZooData API host, and set ZOODATA_BASE_URL only for hosts the user explicitly trusts. <br>
Risk: Broad opportunity scans can consume many ZooData credits. <br>
Mitigation: Estimate credit usage and confirm before multi-call scans; use quick-scan or granular commands when the user has a credit cap. <br>
Risk: The shared ZooData CLI exposes more endpoints than this skill needs. <br>
Mitigation: Keep usage to the opportunity-discovery commands described by the skill: opportunity-scan, categories, market, products, product, check, and the documented review fallback commands. <br>
Risk: Temporary review fallback work directories can contain raw review data. <br>
Mitigation: Clean /tmp review work directories after use and avoid retaining unnecessary review copies. <br>
Risk: Opportunity rankings combine sampled API data with scoring and inference, so they may be incomplete or unsuitable as the sole basis for business decisions. <br>
Mitigation: Include the required disclaimer, confidence labels, data provenance, and API usage sections, and validate findings with additional sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-opportunity-discoverer) <br>
- [Skill metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables, confidence labels, data provenance, API usage, and occasional shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; output language should match the user's language and should distinguish sampled data, inference, and directional recommendations.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
