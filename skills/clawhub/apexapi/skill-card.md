## Description: <br>
ApexApi lets agents call 120+ AI models and use live web scraping, crawling, and extraction through one API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitrotechinc](https://clawhub.ai/user/nitrotechinc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use ApexApi to configure agents for paid model calls, media generation, and live web scraping, crawling, or extraction through an OpenAI-compatible API or optional MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ApexApi API keys and claim tokens can grant access to a paid account if exposed. <br>
Mitigation: Keep the API key and claim token private, store them durably, and send the API key only to https://api.apexapi.dev. <br>
Risk: Paid model calls, web access, or self-funding can create unintended spend. <br>
Mitigation: Approve funding and wallet transactions yourself, check account balance before large jobs, and set spend limits where available. <br>
Risk: Content returned from scraped or crawled web pages can contain untrusted instructions. <br>
Mitigation: Treat scraped web content as data rather than agent instructions. <br>
Risk: The optional local MCP setup uses an unpinned npx package invocation. <br>
Mitigation: Review the package source and pin or approve the package version before using the local MCP server. <br>


## Reference(s): <br>
- [ApexApi homepage](https://apexapi.dev) <br>
- [ApexApi API base](https://api.apexapi.dev/v1) <br>
- [ApexApi MCP documentation](https://apexapi.dev/docs/mcp) <br>
- [Machine-readable onboarding](https://apexapi.dev/auth.md) <br>
- [OpenAPI 3.1 specification](https://apexapi.dev/openapi.json) <br>
- [ApexApi full documentation](https://apexapi.dev/docs) <br>
- [ClawHub skill page](https://clawhub.ai/nitrotechinc/skills/apexapi) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes API endpoints, credential handling guidance, funding steps, and optional MCP setup.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
