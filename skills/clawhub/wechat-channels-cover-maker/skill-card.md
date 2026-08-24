## Description:

Create a WeChat Channels video cover, WeChat Video Account cover, or WeChat Channels thumbnail from a video topic, title, script, key frame, portrait, product photo, or reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, local businesses, and brand teams use this skill to plan, generate, refine, and review one WeChat Channels video cover or thumbnail from a topic, script, key frame, portrait, product photo, or reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization with broad media and spending scopes.

Mitigation: Install only when those scopes are acceptable, keep the credential private, and disconnect or uninstall the package when access is no longer needed.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates before use when explicit change control or pre-approval of package changes is required.

Risk: Image generation and editing requests can spend Beatra credits.

Mitigation: Freeze the route, prompt, canvas, inputs, model, controls, cost limit, and client_request_id before one user-approved paid submission.

Risk: Package and platform registration metadata is sent to Beatra.

Mitigation: Review this metadata behavior before use in environments with sensitive deployment or platform-identification requirements.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/wechat-channels-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-channels-cover-maker)
- [WeChat Channels cover workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image artifacts]

**Output Format:** [Markdown guidance with shell commands, tool payload details, and generated artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task ID, observed dimensions, resolved model, and returned billing.net_charged_credits after a task completes.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
