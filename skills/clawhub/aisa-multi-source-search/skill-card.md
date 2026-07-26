## Description: <br>
AIsa Multi Source Search gives agents a unified way to run web, academic, smart, full-text, and Tavily-backed searches with confidence scoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisapay](https://clawhub.ai/user/aisapay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to retrieve and synthesize web, academic, full-text, and Tavily search results through AIsa's API. It supports research assistance, market research, competitive analysis, news aggregation, and multi-source confidence-scored search workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, target URLs, retrieved content, and result bundles are sent to AIsa's API. <br>
Mitigation: Use the skill only for data that may be shared with AIsa, and avoid secrets, sensitive internal content, and private URLs in queries or crawl targets. <br>
Risk: The skill requires an AISA_API_KEY for API access. <br>
Mitigation: Use a scoped key, store it in the environment, rotate it regularly, and do not paste it into prompts, command history, or shared logs. <br>
Risk: Crawl and map features can access third-party sites on behalf of the user. <br>
Mitigation: Run crawl or map operations only on sites where you have authorization and keep crawl depth and target scope constrained. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aisapay/skills/aisa-multi-source-search) <br>
- [OpenClaw Homepage](https://openclaw.ai) <br>
- [AIsa Documentation](https://aisa.mintlify.app) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa Verity Reference Implementation](https://github.com/AIsa-team/verity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl examples, Python client commands, and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and network access to AIsa API endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
