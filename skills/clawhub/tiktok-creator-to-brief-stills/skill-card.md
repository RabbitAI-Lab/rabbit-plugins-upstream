## Description:

Turn a TikTok creator homepage and recent posts into a collaboration brief still set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Media buyers use this skill to turn a chosen TikTok creator profile, recent works, and already-written collaboration terms into a reviewed set of brief stills for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that installation grants a shared Beatra token with capabilities beyond still-image generation.

Mitigation: Install only if the shared credential model is acceptable, keep the token private, and use the bundled authorization and uninstall flows for connection management.

Risk: The security evidence reports that silent package updates are enabled by default.

Mitigation: Turn automatic updates off before use in environments that require reviewed code only.

Risk: The workflow can create paid lookup, image generation, transform, and edit tasks.

Mitigation: Require separate user confirmation for each paid stage, quote live prices, use one opaque request identity per task, and avoid duplicate retries after uncertain delivery.

Risk: Generated brief stills may contain small text or inaccurate printed details.

Mitigation: Inspect every returned still and treat generated text as a review item rather than a certified offer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/tiktok-creator-to-brief-stills)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-creator-to-brief-stills)
- [Collaboration brief still workflow](references/workflow.md)
- [TikTok creator lookup](references/creator-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces lookup memos, still lists, confirmation cards, task status summaries, billing details, and generated image artifact descriptions.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
