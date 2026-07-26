## Description: <br>
Extract web data, capture screenshots, scrape content, and generate AI images via OpenGraph.io. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[primeobsession](https://clawhub.ai/user/primeobsession) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI assistant users use this skill to retrieve URL metadata, capture webpage screenshots, scrape or extract public web content, ask questions about webpages, and generate images such as diagrams, icons, social cards, and QR codes through OpenGraph.io APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad web scraping and webpage query workflows can send internal links, signed URLs, secrets, private documents, authenticated pages, personal data, or confidential prompts to OpenGraph.io. <br>
Mitigation: Use the skill only with public or clearly authorized URLs and avoid submitting secrets, private documents, personal data, authenticated content, internal links, signed URLs, or confidential prompts. <br>
Risk: Proxy and auto-proxy options can be misused to bypass site controls, bot protections, paywalls, rate limits, or geo-restrictions. <br>
Mitigation: Use proxy features only for authorized access patterns and do not use them to evade site controls, paywalls, rate limits, or geographic restrictions. <br>
Risk: The optional MCP setup installs and runs an npm package. <br>
Mitigation: Verify the opengraph-io-mcp package source before installation and consider pinning a trusted version. <br>


## Reference(s): <br>
- [OpenGraph.io Skill on ClawHub](https://clawhub.ai/primeobsession/skills/opengraph-io-skill) <br>
- [OpenGraph.io Website](https://www.opengraph.io) <br>
- [OpenGraph.io Documentation](https://www.opengraph.io/documentation) <br>
- [AI Agent Reference](references/for-ai-agents.md) <br>
- [API Reference](references/api-reference.md) <br>
- [Platform Support](references/platform-support.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Image Generation Reference](references/image-generation.md) <br>
- [MCP Client Setup](references/mcp-clients.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and an OPENGRAPH_APP_ID credential; optional MCP setup uses the opengraph-io-mcp npm package.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
