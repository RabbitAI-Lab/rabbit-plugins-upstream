## Description:

Turn YouTube insurance captions into one talking insurance clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External advisors and agent operators use this skill to turn public YouTube insurance captions and advisor-supplied clause wording into separate short talking clips. It supports staged approval for caption lookup, voice cloning, speech synthesis, and image-to-video generation without inventing coverage terms or payout claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device credential that can spend Beatra credits and access media and task tools.

Mitigation: Review the Beatra approval screen before installation, provide only intended stills or voice samples, and use the bundled client so credentials are not exposed in command arguments.

Risk: Silent package updates are enabled by default for this Beatra package.

Mitigation: Accept this only if automatic verified updates are appropriate for the installation, or disable them after installation with `scripts/mcp_client.py update --auto off`.

Risk: Caption lookup, voice cloning, speech synthesis, and video generation are billable stages that can consume credits.

Mitigation: Use the skill's staged approval cards, live price checks, unique request identities, and task polling before submitting or retrying paid work.

Risk: Insurance caption outputs could mislead users if the agent invents coverage terms, deductibles, waiting periods, claim outcomes, or payout statements.

Mitigation: Restrict spoken lines to advisor-supplied clause wording or labeled caption text and review each clip before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/youtube-insure-caption-talking)
- [Beatra skill homepage](https://beatra.ai/skills/youtube-insure-caption-talking)
- [Insurance caption talking-clip workflow](artifact/references/workflow.md)
- [YouTube insurance caption lookup](artifact/references/caption-lookup.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [MCP connection](artifact/references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and generated media task instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled caption-to-talking slot list and staged execution guidance for separate speech and video tasks; generated clips remain separate files.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
