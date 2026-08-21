## Description:

Research what a person or company posts about on LinkedIn, including topics, tone, and how recently they have posted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to understand a LinkedIn profile or company's recent posting themes, tone, cadence, and representative posts before writing outreach or comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn identifiers and fetched post data are sent through Veezee.

Mitigation: Use the skill only when sharing the target identifier and returned post data with Veezee is acceptable.

Risk: Multiple pages or realtime freshness can consume free or paid credits.

Mitigation: Check usage before fetching additional pages, set max_credits on calls, and use realtime freshness only when recent posts are necessary.

Risk: A Veezee API key can be reused to spend available credits.

Mitigation: Keep the API key private and avoid exposing it in prompts, logs, shared files, or public configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/veezee-build/skills/veezee-post-voice-research)
- [Veezee LinkedIn MCP server](https://mcp.veezee.io/linkedin)
- [Veezee all-tools MCP server](https://mcp.veezee.io/all)
- [Veezee API key mint endpoint](https://api.veezee.io/v1/keys/mint)
- [Veezee upgrade page](https://veezee.io/upgrade)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown summary with topics, tone, posting cadence, representative excerpts, post URLs, and credits spent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [LinkedIn only; output depends on fetched cached or realtime post data and available credits.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
