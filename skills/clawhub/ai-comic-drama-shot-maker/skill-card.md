## Description:

Turns an approved comic panel, character sheet, or story beat into a short animated comic-drama shot using Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other external users animate approved comic or manga panels, interpolate between panels, or create an original first frame and turn it into one motion-comic shot. Each paid stage requires user approval before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants a persistent, broad device token that can spend credits and access Beatra tasks and artifacts.

Mitigation: Review the scope before connecting, keep the token private, and approve each paid stage after reviewing its estimate.

Risk: Local package code silently self-updates by default.

Mitigation: Review the update behavior and run `python3 scripts/mcp_client.py update --auto off` if code changes require approval.

Risk: Paid image and video generation can consume credits, and final charges can differ from the estimate.

Mitigation: Confirm sufficient balance and each stage's price before submission; report the task's actual net charged credits.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ai-comic-drama-shot-maker)
- [Comic-drama shot workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Markdown, Video artifact links, Guidance]

**Output Format:** [Markdown with generated video links, task status, and billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One independently reviewed shot per approved video task; an original first frame is a separate paid stage.]

## Skill Version(s):

0.2.0 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
