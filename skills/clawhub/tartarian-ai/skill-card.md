## Description:

World-aware MCP field doctrine for Tartarian.Ai agents that teaches authenticated Automa how to observe, move, gather, craft, barter, fight, use Guild systems, and act lawfully inside Tartarian's persistent world.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tartarian-admin](https://clawhub.ai/user/tartarian-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to connect to Tartarian through OAuth-protected MCP and control an authenticated shared vessel in the game world. It guides routine play, inventory and equipment handling, combat, storage, crafting, barter, Guild workflows, and concise operator collaboration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent in-game changes through the authenticated Tartarian account and shared vessel, including movement, inventory, storage, barter, Guild actions, chat moderation, structure removal, and reclaim or reset operations.

Mitigation: Install only for intended Tartarian game control and require operator review before permission-sensitive, economic, destructive, or reset-style actions.

Risk: OAuth tokens, session cookies, authorization codes, PKCE verifiers, and service secrets could be exposed if handled in chat.

Mitigation: Use the browser or client authorization flow for authentication and do not paste credentials or secrets into conversation.

Risk: The human operator and agent share control of the same vessel, so stale position, inventory, equipment, Guild, or target state can lead to incorrect actions.

Mitigation: Re-read the smallest relevant state before revision-sensitive or state-changing actions, especially after manual operator movement or UI changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tartarian-admin/skills/tartarian-ai)
- [Publisher profile](https://clawhub.ai/user/tartarian-admin)
- [Tartarian MCP endpoint](https://mcp.tartarian.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with MCP endpoint, authentication posture, tool categories, and operating protocols]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Tartarian OAuth/MCP session; agent actions can affect the authenticated user's shared vessel and persistent game state.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
