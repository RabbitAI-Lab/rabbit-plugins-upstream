## Description: <br>
Star Search helps agents search the web, retrieve Chinese and English news, finance, academic, and technical information, and return LLM-assisted answers through MCP, JSON-RPC, SSE, API, and command-line workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[muchenhengxin](https://clawhub.ai/user/muchenhengxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use Star Search to add real-time web, news, finance, academic, and code-search retrieval to agent workflows. It is suited to self-hosted search services that need multi-engine retrieval, LLM answer synthesis, source verification, monitoring, and MCP/API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is a broad self-hosted search service with account, payment, credential, upload, scraping, and persistence behavior. <br>
Mitigation: Install only when operating a full self-hosted search service, review the deployment before use, isolate the service network, secure secrets, and harden account, payment, upload, and persistence paths. <br>
Risk: Untrusted LLM endpoints or local credential fallbacks could expose secrets or route sensitive queries to unintended services. <br>
Mitigation: Pin trusted LLM endpoints, remove the ~/.hermes auth fallback, and manage API keys through secured deployment secrets. <br>
Risk: Automatic content fetching and scraping can reach internal/private URLs or violate service expectations. <br>
Mitigation: Block internal and private URL ranges, restrict outbound network access, and review the Cloudflare and scraping guidance for compliance and abuse risk. <br>
Risk: Mock payment or callback paths can create confusing or unsafe production behavior if left enabled. <br>
Mitigation: Disable or harden mock payment and callback paths before deployment. <br>


## Reference(s): <br>
- [ClawHub Star Search release page](https://clawhub.ai/muchenhengxin/skills/star-search) <br>
- [Search Engine Research](references/search-engine-research.md) <br>
- [VS Baidu Search Comparison](references/vs-baidu-search-comparison.md) <br>
- [Camofox API](references/camofox-api.md) <br>
- [V15 Site Bing Probe Results](references/v15-site-bing-probe-results.md) <br>
- [V16 Engine Addition Checklist](references/v16-engine-addition-checklist.md) <br>
- [V16 RSS Probe Results](references/v16-rss-probe-results.md) <br>
- [End-to-End Pipeline Fix Notes](references/实战102-end-to-end-pipeline-fix.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON, streamed text/API responses, and command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include citations, fetched snippets, entity cards, source credibility signals, structured output formats, and monitoring data.] <br>

## Skill Version(s): <br>
20.41.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
