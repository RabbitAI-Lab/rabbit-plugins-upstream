## Description: <br>
Retrieves current web content through Huawei Cloud's AI networking web search API, with search guidance optimized for Chinese-language queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flp516](https://clawhub.ai/user/flp516) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a user asks for current web information, recent news, source lookup, or verification beyond local knowledge. It executes web searches through Huawei Cloud and returns concise search results for the agent to summarize or cite. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Install metadata includes an unnecessary external fs dependency and unpinned packages. <br>
Mitigation: Remove the external fs dependency, pin or update axios, and install from a reviewed lockfile before deployment. <br>
Risk: The Huawei token is configured directly in source code. <br>
Mitigation: Use an environment variable or local secret mechanism instead of committing, sharing, or backing up a token-filled source file. <br>
Risk: Search results come from live web content and may be incomplete, outdated, or unsuitable without review. <br>
Mitigation: Have the agent verify important results against source pages and filter returned content for the user's context before relying on it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/flp516/skills/xiaoyi-web-search-v2) <br>
- [Huawei AI Networking Service Setup Guide](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-ainetworking-serviceopen-0000002370503878) <br>
- [Huawei AI Networking Web Search API Endpoint](https://connect-api.cloud.huawei.com/api/aiNetworking/v1/webSearch) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell and JavaScript examples; command output is formatted search-result text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Huawei Cloud AI networking token configured before use; search result count is user-configurable with a documented default of 10.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
