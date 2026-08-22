## Description:

Act helps agents search Shenzhen activities, view details and schedules, and create single or batch public activity listings through the Fore.vip MCP service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[onsoul](https://clawhub.ai/user/onsoul)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find Shenzhen-area activities, inspect activity details and schedules, and publish public activity listings after collecting required event information and user confirmation.

### Deployment Geography for Use:

Shenzhen, China (CN-SZ)

## Known Risks and Mitigations:

Risk: The skill can publish public activity listings in bulk using a chat-provided API key.

Mitigation: Install only if the publisher is trusted, use a limited API key where possible, and review each proposed activity before publication.

Risk: Batch creation may rely on web-sourced event and image information.

Mitigation: Create only events with clear source information, skip entries without usable cover images or coordinates, and keep the user confirmation step before publishing.

Risk: API keys may be exposed if shared directly in ordinary chat.

Mitigation: Use a safer secret-entry method when available and avoid retaining or reusing the key across creation sessions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/onsoul/skills/act)
- [Fore.vip MCP Service](https://mcp.fore.vip)
- [Fore.vip Project Site](https://fore.vip)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Structured data, Guidance]

**Output Format:** [Markdown summaries with MCP tool calls and structured activity objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Activity creation requires an X-API-Key and can publish public listings; activity detail lookup increments view count.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
