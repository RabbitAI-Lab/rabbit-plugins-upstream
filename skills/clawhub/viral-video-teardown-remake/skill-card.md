## Description:

Turns a proven short-form video into a new branded version by analyzing its hook, beats, audience signals, and script pattern, then producing a rewritten shot list, generated frames, narration, and one vertical clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to study a reference short video and remake its structure around their own product, service, or topic. It helps produce a teardown, shot list, generated beat frames, narration, and a vertical remake clip through gated Beatra generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and stores a shared Beatra device token with broad account scope.

Mitigation: Install only if the Beatra account trust model is acceptable; keep the token local, do not expose it in chat or logs, and use the bundled uninstall flow when disconnecting.

Risk: The skill can spend Beatra credits after workflow confirmations.

Mitigation: Require explicit user approval for each priced lookup or generation stage, use stable request IDs, and report returned billing facts for completed tasks.

Risk: The bundled client silently updates package files by default.

Mitigation: Review the package before use and disable silent updates with python3 scripts/mcp_client.py update --auto off when automatic replacement is not desired.

Risk: Installation and platform metadata is sent to Beatra during use.

Mitigation: Use the skill only where that metadata sharing is acceptable for the account and deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/viral-video-teardown-remake)
- [Beatra skill homepage](https://beatra.ai/skills/viral-video-teardown-remake)
- [Reading a reference from a link](references/reference-lookup.md)
- [Reading the reference](references/teardown.md)
- [Rewriting onto your subject](references/remake-plan.md)
- [Remake workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis and tables with shell command snippets and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task IDs, billing facts, artifact links, generated still frames, narration audio, and a vertical video when remote tasks succeed.]

## Skill Version(s):

0.1.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
