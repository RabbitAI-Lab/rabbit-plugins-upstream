## Description:

Query and manage Mentionkit social monitoring workflows to review brand mentions, find reply opportunities, shortlist lead conversations, inspect source links, and create tracked keywords.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shash7](https://clawhub.ai/user/shash7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect agents to Mentionkit MCP or API workflows for social mention review, lead discovery, source verification, keyword tracking, and simple scripted data access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to access Mentionkit workspace data through MCP or the public API.

Mitigation: Install it only for intended Mentionkit workspaces and use read-only API or MCP access when possible.

Risk: MCP write scope can allow keyword creation, keyword reactivation, or mention review state updates.

Mitigation: Grant write scope only when those actions are intended, and require explicit project choices before mutating a workspace.

Risk: A source URL fetch can fail during mention review, reducing confidence in the underlying mention.

Mitigation: Treat failed fetches as unverified and lower confidence instead of presenting the source as confirmed.

## Reference(s):

- [Source repository](https://github.com/shash7/mentionkit-skill)
- [ClawHub skill page](https://clawhub.ai/shash7/skills/mentionkit-skill)
- [Mentionkit](https://mentionkit.com)
- [Mentionkit OpenAPI JSON](https://api.mentionkit.com/openapi.json)
- [Mentionkit OpenAPI YAML](https://api.mentionkit.com/openapi.yaml)
- [Mentionkit MCP Tools Reference](artifact/references/MCP-TOOLS.md)
- [Mentionkit Public API v1 Reference](artifact/references/API-V1.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with API examples and workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to call Mentionkit MCP tools or the Mentionkit Public API v1 when credentials and access are available.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
