## Description:

Available Domain Search helps agents generate brandable domain ideas and check live domain availability through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to brainstorm domain names, check availability for one domain or a shortlist, and return registration links for available names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names and business-description queries are sent to AgentPMT for live search.

Mitigation: Avoid including sensitive launch plans or confidential naming strategy unless sharing that information with AgentPMT is acceptable.

Risk: Each remote action costs 3 credits.

Mitigation: Confirm the user intends to run a paid availability or suggestion search before invoking the remote action.

Risk: A broad activation keyword can trigger the skill when a generic domain discussion does not need live search.

Mitigation: Use the skill only when the user asks for live domain availability, suggestions, or AgentPMT-specific domain search behavior.

## Reference(s):

- [Available Domain Search ClawHub Skill](https://clawhub.ai/agentpmt/skills/available-domain-search)
- [Available Domain Search Marketplace Page](https://www.agentpmt.com/marketplace/available-domain-search)
- [Available Domain Search Schema](artifact/schema.md)
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What AgentPMT Is](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown guidance with JSON request examples and remote tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote actions cost 3 credits and may return domain availability status, registration links, or HTML widgets with text fallback.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
