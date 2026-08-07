## Description: <br>
Demandex provides e-commerce demand intelligence for AI agents by mining public Reddit complaint and intent posts into scored opportunity cards and ad-hoc physical-product demand verdicts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent builders use this skill to query Demandex API and MCP endpoints for product demand signals, opportunity cards, and market briefs before deciding where to spend on paid calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Enabling paid MCP tools requires an EVM private key and can spend USDC on Base. <br>
Mitigation: Use free endpoints first, fund only a dedicated low-balance wallet for expected Demandex usage, store the private key securely, never commit or log it, and rotate it immediately if exposed. <br>
Risk: Demand intelligence is aggregated from public Reddit posts and may be incomplete or unsuitable as a sole business decision source. <br>
Mitigation: Treat results as informational signals, review linked evidence and provenance, and validate findings with independent market research before acting. <br>


## Reference(s): <br>
- [Demandex homepage](https://demandex.dev) <br>
- [Demandex API](https://api.demandex.dev) <br>
- [Categories endpoint](https://api.demandex.dev/v1/categories) <br>
- [Sample opportunity endpoint](https://api.demandex.dev/v1/sample/opportunity) <br>
- [Gauge endpoint](https://api.demandex.dev/v1/gauge) <br>
- [Live gauge endpoint](https://api.demandex.dev/v1/gauge/live) <br>
- [Trending opportunities endpoint](https://api.demandex.dev/v1/opportunities/trending) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include endpoint response shapes, MCP server configuration, demand verdicts, opportunity cards, and market brief data.] <br>

## Skill Version(s): <br>
0.3.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
