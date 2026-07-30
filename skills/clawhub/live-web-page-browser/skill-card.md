## Description: <br>
Live Web Page Browser fetches live webpages through AgentPMT-hosted remote tool calls and can return HTML, Markdown, structured JSON, links, screenshots, PDFs, snapshots, and crawl results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access live webpages for real-time research, content verification, competitive monitoring, visual capture, link extraction, crawling, and data extraction for downstream workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote browsing can send requested URLs and retrieved page content to AgentPMT-hosted infrastructure. <br>
Mitigation: Use only approved public or otherwise permitted URLs, and do not submit internal URLs, token-bearing URLs, authenticated pages, personal data, or confidential business content without approval. <br>
Risk: Account-level browser session and crawl controls may affect other AgentPMT browser runs. <br>
Mitigation: Confirm job IDs, session IDs, crawl scope, depth, and limit before canceling crawls, killing sessions, or starting broad crawls. <br>
Risk: The generated artifact summary may be less specific than the live AgentPMT schema. <br>
Mitigation: Fetch the live schema or instructions before a production integration and whenever parameters, enum values, nested objects, outputs, or examples are unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/live-web-page-browser) <br>
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/live-web-page-browser) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>
- [Action schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, HTML, images, PDF] <br>
**Output Format:** [Markdown guidance with JSON, REST, MCP, and shell examples; remote tool responses may include HTML, Markdown, structured JSON, links, screenshots, PDFs, snapshots, and crawl records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses AgentPMT-hosted remote browser calls; live schema lookup is recommended before production integrations or when parameters are unclear.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
