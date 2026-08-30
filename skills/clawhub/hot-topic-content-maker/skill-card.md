## Description:

Turns a trending topic, moment, or seasonal peg into same-day social content with angles, cover wording and image, caption, hashtags, and an optional narrated vertical clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social content teams use this skill to turn a topic they provide, or an optional paid trend lookup, into a publishable post for platforms such as Douyin, Xiaohongshu, WeChat Channels, TikTok, Reels, and Shorts. It is intended for trendjacking, newsjacking, seasonal campaigns, moment marketing, and rapid same-day content production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill silently self-updates code, which can make reviewed local code change after installation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when reviewed code must remain fixed, and re-review before enabling updates again.

Risk: The security summary says the skill uses a broad persistent shared Beatra device authorization with credit-spending and artifact/task capabilities.

Mitigation: Install only in environments where shared credential handling is acceptable, keep tokens out of chat and command arguments, and use the provided uninstall or revocation flow when access should end.

Risk: The workflow can make paid Beatra calls for trend lookup, image generation, speech synthesis, and video generation.

Mitigation: Require the documented confirmation gates, stable request IDs, and task polling before each paid stage; do not resubmit uncertain or running tasks with changed arguments.

Risk: Trend-based posts can contain unsupported claims or misleading facts about active public events.

Mitigation: Use only user-supplied facts or attributed lookup results, label shelf-life and momentum as inference, and surface regulated, controversial, loss-related, or short-fuse topics for user choice.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/hot-topic-content-maker)
- [Beatra skill homepage](https://beatra.ai/skills/hot-topic-content-maker)
- [Finding the angle](references/angle-finding.md)
- [Looking up what is trending](references/trend-lookup.md)
- [Building the post](references/post-plan.md)
- [Hot topic workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, structured Beatra task details, and links to generated media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce cover images, beat frames, narration, and video artifacts through paid Beatra tasks after user confirmation.]

## Skill Version(s):

0.1.7 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
