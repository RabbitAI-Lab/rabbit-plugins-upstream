## Description:

Turn user-supplied policy renewal dates and authorized stills into one insurance renewal reminder talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External insurance advisors and wealth educators use this skill to turn supplied policy renewal schedules and authorized still images into short talking renewal reminder clips. It guides the agent to plan slots, confirm paid voice, speech, and video stages, and avoid inventing policy facts or recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill asks for broad Beatra account authority across media, artifact, wallet, and task permissions.

Mitigation: Install only when that shared credential scope is acceptable, avoid unnecessary personal policy details or unauthorized likeness and voice samples, and revoke the Beatra device authorization after use if continued access is not needed.

Risk: The server security summary says the bundled client can silently replace installed code through automatic updates.

Mitigation: Turn off automatic updates for reviewed-version control and use the bundled update check before accepting a newer package.

Risk: The workflow creates paid speech, clone, and video tasks and may charge based on measured usage rather than the initial estimate.

Mitigation: Confirm each paid stage separately, use one opaque client request ID per slot or segment, poll terminal tasks before retrying, and report actual billed credits from the task result.

Risk: The skill handles insurance renewal dates and can animate faces or voices from supplied assets.

Mitigation: Use only schedule facts supplied by the user, require likeness and voice rights before cloning or animation, and do not invent coverage guarantees, premium amounts, deadlines, or renewal recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/insurance-renew-talking)
- [Renewal reminder talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Bundled MCP client diagnostics](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of 2 to 8 separate 2-15 second talking clips; paid stages use live model cards, per-request IDs, and asynchronous task polling.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
