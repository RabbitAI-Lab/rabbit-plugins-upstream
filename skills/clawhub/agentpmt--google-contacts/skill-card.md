## Description:

Google Contacts connector to list, search, create, update, and delete a user's contacts through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent find Google Contacts, retrieve contact details, and create, update, or delete contacts for outreach, scheduling, support, and address book maintenance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Google contact data to an agent.

Mitigation: Use only an AgentPMT and Google account intended for the requested contact workflow, and keep prompts scoped to the minimum contact fields needed.

Risk: The delete_contact action permanently removes contacts.

Mitigation: Require explicit user confirmation of the exact contact resource name before deletion and verify search results before acting.

Risk: Live schema or instruction text may change after the local skill was reviewed.

Mitigation: Treat live schema lookups as clarifying references only and do not expand beyond the six documented actions or the user's explicit request.

Risk: Unpinned setup commands can install changing dependencies.

Mitigation: Review setup commands before running them and avoid letting an agent execute unpinned npx commands automatically.

## Reference(s):

- [Google Contacts Schema](artifact/schema.md)
- [AgentPMT Google Contacts Marketplace Page](https://www.agentpmt.com/marketplace/google-contacts)
- [ClawHub Google Contacts Skill Page](https://clawhub.ai/agentpmt/skills/google-contacts)
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration, Shell commands]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines six Google Contacts actions and their parameter schemas for AgentPMT MCP or REST invocation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
