## Description:

Build and run grounded business agents on agent4.io over MCP - agents, knowledge bases, load-on-demand skills, stateful Storylines and page playbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hellojixian](https://clawhub.ai/user/hellojixian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to configure, publish, and operate agent4.io agents through a remote MCP server. It guides creation of grounded agents, knowledge bases, load-on-demand skills, page playbooks, Storylines, shares, usage checks, and related platform administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected agent configuration, knowledge-base material, and queries to the hosted agent4.io service.

Mitigation: Confirm the user intends to use agent4.io and only transmit documents, prompts, and business data they are allowed to process there.

Risk: The required AGENT4_API_KEY grants tenant access and is sensitive.

Mitigation: Store the key as a secret, avoid exposing it in logs or shared transcripts, and verify the connected tenant with tenant_info before making changes.

Risk: Broad REST API actions, privacy or BYOK changes, channel bot-token actions, public shares, and follow-ups can affect deployed agents or external users.

Mitigation: Use explicit user confirmation before these actions and return concrete console links or generated URLs so the user can review the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hellojixian/skills/agent4-io)
- [Publisher profile](https://clawhub.ai/user/hellojixian)
- [agent4.io cookbook](https://agent4.io/cookbook)
- [agent4.io API reference](https://agent4.io/api.md)
- [agent4.io MCP endpoint](https://api.agent4.io/v1/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands, MCP tool-call recipes, configuration snippets, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT4_API_KEY and a configured agent4.io remote MCP connection; outputs may direct the agent to send user-selected configuration, prompts, and knowledge-base content to agent4.io.]

## Skill Version(s):

1.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
