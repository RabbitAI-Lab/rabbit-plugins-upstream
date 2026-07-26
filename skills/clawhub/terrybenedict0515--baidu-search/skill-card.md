## Description: <br>
Search the web using Baidu AI Search Engine (BDSE) for live information, documentation, or research topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrybenedict0515](https://clawhub.ai/user/terrybenedict0515) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to run Baidu web searches from an OpenClaw environment when they need current web results, documentation lookups, or research context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Baidu's service and may reveal sensitive topics or internal context. <br>
Mitigation: Avoid searching for secrets, credentials, private customer data, or confidential internal material. <br>
Risk: The BAIDU_API_KEY credential can be exposed if OpenClaw configuration is shared or committed. <br>
Mitigation: Keep OpenClaw configuration out of version control and rotate the API key if exposure is suspected. <br>


## Reference(s): <br>
- [Baidu Search on ClawHub](https://clawhub.ai/terrybenedict0515/baidu-search) <br>
- [Baidu API Key Setup Guide](references/apikey-fetch.md) <br>
- [Baidu AI Search API Key Console](https://console.bce.baidu.com/ai-search/qianfan/ais/console/apiKey) <br>
- [Baidu AI Search Web Search Endpoint](https://qianfan.baidubce.com/v2/ai_search/web_search) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON search results printed to stdout, with Markdown setup guidance in the skill references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and BAIDU_API_KEY; accepts query, count, and freshness request parameters.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
