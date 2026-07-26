## Description: <br>
YouTube Discovery helps agents search and inspect public YouTube videos, channels, playlists, comments, categories, languages, and regions through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and content teams use this skill to discover public YouTube content, inspect channel and video metadata, analyze public comment threads, and build content research, competitive analysis, SEO, monitoring, or trend discovery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Related AgentPMT setup flows may involve accounts, wallets, payment headers, or other secrets. <br>
Mitigation: Review the related setup skills separately and do not paste private keys, mnemonics, signatures, payment headers, account secrets, or other credentials into prompts or logs. <br>
Risk: The skill is limited to public YouTube metadata and cannot access private analytics, download media, or modify YouTube content. <br>
Mitigation: Use it only for public metadata discovery and fetch live schema or instructions before new production integrations when parameters or response shapes are unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/youtube-discovery) <br>
- [AgentPMT marketplace page](https://www.agentpmt.com/marketplace/youtube-discovery) <br>
- [YouTube Discovery action schema](artifact/schema.md) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [No-account AgentAddress/x402 setup](https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API Calls] <br>
**Output Format:** [Markdown instructions with JSON request examples and remote tool call schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote calls return JSON collections of public YouTube metadata with pagination tokens when more results are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
