## Description:

Turn an article title, topic, summary, or reference image into a WeChat Official Account cover, WeChat article cover, article hero image, post cover, headline image, or supporting article visual.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand teams, and agents use this skill to turn article topics, titles, summaries, or visual references into publish-ready WeChat cover images with a focused visual hook and headline-safe composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad media and spending scopes.

Mitigation: Install only in an environment where the local ~/.beatra credential and Beatra spending authority are acceptable, and avoid exposing the token in chat, logs, command arguments, or files.

Risk: The package can silently update its installed files by default.

Mitigation: Consider disabling automatic updates immediately with the bundled update control before using the skill in a sensitive environment.

Risk: Image generation consumes Beatra credits and creates asynchronous paid tasks.

Mitigation: Confirm the final prompt, references, canvas, model, controls, and output count before the paid call, then preserve the request identity for recovery to avoid duplicate charges.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/wechat-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-cover-maker)
- [WeChat cover workflow](references/workflow.md)
- [Intent and routing](references/intent-and-routing.md)
- [Canvas and cover craft](references/canvas-and-cover-craft.md)
- [MCP connection](references/mcp-connection.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Review and recovery](references/review-and-recovery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated image artifact links after execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one cover-image workflow at a time and reports task IDs, dimensions, artifact links, and net charged credits when available.]

## Skill Version(s):

0.1.9 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
