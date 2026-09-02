## Description:

Read and manage a Skylight Calendar family hub, including calendar events, chores and reward stars, shared lists, meal plans, frames, messages, photo albums, uploads, and frame settings through an authenticated Skylight account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect and update their own Skylight Calendar family hub, including events, chores, grocery and to-do lists, meal plans, frame membership, and connector diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector receives broad authenticated access to Skylight family data and account-changing tools.

Mitigation: Install only when that access is acceptable, protect MCP configuration files like password files, prefer a refresh token if available, and scope usage to a specific frame with SKYLIGHT_FRAME_ID when possible.

Risk: Some tools can create, update, or delete family calendar, chore, shared list, meal, recipe, frame, message, photo, video, or settings data.

Mitigation: Review write and delete requests carefully before approval, especially operations that affect recurring meals or chores.

Risk: The skill uses Skylight email and password credentials and does not support Google, Apple, or SSO-only accounts.

Mitigation: Use a supported Skylight account credential, store it only in the MCP environment configuration, and restrict access to that configuration.

Risk: Dry-run responses for recurrence-scoped writes do not mean the requested change has happened.

Mitigation: Treat dry-run results as confirmation prompts and re-issue the same request with explicit confirmation only after checking the affected scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [npm package: skylight-mcp](https://www.npmjs.com/package/skylight-mcp)
- [Source repository](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown and structured MCP tool results, including JSON-like dry-run and diagnostic responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may contain Skylight account, family hub, calendar, chore, list, meal, frame, member, message, photo, video, and diagnostic data.]

## Skill Version(s):

0.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
