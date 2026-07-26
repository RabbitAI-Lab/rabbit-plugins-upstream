## Description: <br>
Searches the web using Baidu AI Search Engine (BDSE) for live information, documentation, and research topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ide-rea](https://clawhub.ai/user/ide-rea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to retrieve current Baidu web search results for live information, documentation lookup, and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries may be sent to Baidu or a configured sandbox proxy. <br>
Mitigation: Install only when that data flow is acceptable for the intended use case. <br>
Risk: The Baidu API key is sensitive and may be exposed if local configuration files are shared. <br>
Mitigation: Use a dedicated, revocable API key and keep ~/.openclaw/openclaw.json private and out of source control. <br>
Risk: Baidu API usage can affect account usage limits or billing. <br>
Mitigation: Monitor Baidu usage and billing for the key used by this skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ide-rea/skills/baidu-search) <br>
- [Baidu API Key Setup Guide](references/apikey-fetch.md) <br>
- [Baidu AI Search API Key Console](https://console.bce.baidu.com/ai-search/qianfan/ais/console/apiKey) <br>
- [Baidu AI Search Web Search Endpoint](https://qianfan.baidubce.com/v2/ai_search/web_search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API Calls] <br>
**Output Format:** [JSON search results printed to stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BAIDU_API_KEY; supports result count from 1 to 50 and optional freshness filters.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
