## Description:

Turn a product lineup into a live shopping script your host can actually read on air.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, live-commerce operators, creator teams, and agents use this skill to turn a product lineup into a minute-by-minute selling schedule, product talk tracks, ready-to-read host lines, a compliance pass, talking-point cards, countdown cards, and short spoken delivery takes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token stored under ~/.beatra.

Mitigation: Install only in trusted local environments, do not expose the token in prompts or logs, and use the bundled uninstall flow when disconnecting the device.

Risk: The skill can spend Beatra credits after its approval step.

Mitigation: Review the frozen production plan, current estimate, selected cards, spoken takes, and stable request IDs before approving any paid generation.

Risk: The package silently checks for and installs verified updates by default.

Mitigation: Disable automatic checks with `python3 scripts/mcp_client.py update --auto off` when change control requires manual review.

Risk: Rendered image cards can contain wrong or illegible prices or quantities.

Mitigation: Read every generated card figure back against the approved schedule before using it in a live selling room.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/live-commerce-script-studio)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/live-commerce-script-studio)
- [Planning the session](references/session-plan.md)
- [Writing the talk track](references/talk-track.md)
- [Live session workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured schedules, talk tracks, line libraries, compliance notes, command examples, task IDs, artifact links, and media metadata when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger paid Beatra image and speech generation after an explicit approval step; reports only returned task, usage, billing, and artifact facts.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
