## Description: <br>
RSS Reader helps agents fetch and parse public RSS or Atom feeds into structured feed metadata and entries through AgentPMT-hosted tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to public feed ingestion for content aggregation, monitoring, market intelligence, podcast listings, and content pipeline workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AgentPMT-hosted feed reads may incur credit charges or expose submitted feed URLs to the service. <br>
Mitigation: Use the skill only with public RSS or Atom feed URLs and confirm expected credit usage before routine automation. <br>
Risk: Prompts or logs could expose credentials, wallet secrets, payment headers, or private feed URLs if users include them in tool inputs. <br>
Mitigation: Do not provide secrets or private feed URLs in prompts or logs; use the referenced setup skill for account connection handling. <br>
Risk: Malformed feeds can return partial parsed results. <br>
Mitigation: Use include_raw when feed health matters and check parsing diagnostics before relying on returned entries. <br>


## Reference(s): <br>
- [RSS Reader schema](./schema.md) <br>
- [AgentPMT RSS Reader marketplace page](https://www.agentpmt.com/marketplace/rss-reader) <br>
- [ClawHub RSS Reader page](https://clawhub.ai/agentpmt/skills/rss-reader) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance] <br>
**Output Format:** [Markdown instructions with JSON request and response examples; runtime tool responses are JSON objects.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports one read action for public RSS/Atom feed URLs with max_items from 1 to 200 and timeout_seconds from 1 to 120.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
