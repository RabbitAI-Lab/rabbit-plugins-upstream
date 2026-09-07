## Description:

Turns a Douyin hot search topic and seller-provided stills into short talking hook clips, one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and creators use this skill to plan and generate short Douyin trend-hook talking clips from approved hot-search topics, brand facts, still images, and authorized voice choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared persistent Beatra device credential with broad media, artifact, task, wallet-spend, and voice permissions.

Mitigation: Install only when that access is acceptable, keep the device token private, and revoke or uninstall the connection when it is no longer needed.

Risk: Executable package files may update silently during normal use.

Mitigation: Turn automatic updates off with the documented command when reviewed code must remain fixed, and use the update check command before accepting newer code.

Risk: Paid lookup, clone, speech, and video stages can spend Beatra credits, and changed retries can create new work.

Mitigation: Require a separate confirmation card for each paid stage, use live pricing, preserve request identifiers for unchanged retries, and poll existing tasks before resubmitting.

Risk: The workflow can involve likeness, voice cloning, and generated talking media.

Mitigation: Require explicit rights and consent for faces, still images, voice samples, and cloned voices before generating or animating clips.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-hot-to-hook-clip)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-hot-to-hook-clip)
- [Douyin hot-search hook workflow](references/workflow.md)
- [Douyin hot-search lookup](references/trend-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON arguments, confirmation cards, and generated media artifact summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 2 to 8 short talking hook clip requests by default, keeps one still per clip, and reports task status, media facts, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
