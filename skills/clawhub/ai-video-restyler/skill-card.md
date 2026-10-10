## Description:

Restyles one short source video in a chosen visual style while aiming to preserve its subject, action, composition, and camera intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video teams use this skill to turn a short source clip into a new visual treatment, such as anime or ink, and review the resulting style, motion, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token can access other Beatra media and account tools beyond video restyling.

Mitigation: Install only if you trust Beatra with that wider access; keep the token private.

Risk: Automatic updates can replace local skill files without a separate prompt.

Mitigation: Review updates or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: Uninstalling the last Beatra skill may revoke the shared device connection and remove shared local state.

Mitigation: Check which other Beatra skills use the connection before uninstalling or disconnecting.

Risk: Video restyling is billable, and the final charge can differ from the initial estimate.

Mitigation: Confirm the live estimate and available credits before submitting; report the settled charge from the completed task.

## Reference(s):

- [AI Video Restyler on ClawHub](https://clawhub.ai/beatra-ai/skills/ai-video-restyler)
- [AI Video Restyler product page](https://beatra.ai/skills/ai-video-restyler)
- [Video restyle workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with returned video artifact links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual task status and charged credits; video artifacts are returned by the external service.]

## Skill Version(s):

0.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
