## Description: <br>
Search the web using Baidu AI Search Engine (BDSE). Use for live information, documentation, or research topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cindypapa](https://clawhub.ai/user/cindypapa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve current web search references from Baidu AI Search for live information, documentation lookups, and research topics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Baidu's AI Search API with a BAIDU_API_KEY. <br>
Mitigation: Avoid confidential prompts, credentials, private project names, or regulated data unless Baidu API use is acceptable for the environment. <br>
Risk: The skill depends on an external API key and third-party search provider availability. <br>
Mitigation: Configure BAIDU_API_KEY only in approved environments and handle provider errors before relying on the returned results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cindypapa/skills/baidu-search) <br>
- [Baidu AI Search API endpoint](https://qianfan.baidubce.com/v2/ai_search/web_search) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON search reference results printed to stdout, with command-line status and error text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BAIDU_API_KEY and accepts query, count from 1 to 50, and optional freshness filters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
