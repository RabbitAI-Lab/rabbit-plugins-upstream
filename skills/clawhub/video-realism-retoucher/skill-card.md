## Description:

Retouches one realism issue in an existing AI-generated short video while preserving the intended subject, framing, timing, and mood.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to refine lighting, material texture, color, or repeated details in an existing AI-generated product clip, advertisement, or social video without intentionally changing the shot's composition or timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token grants broad account access and is stored locally.

Mitigation: Install only if this access is acceptable; protect local credentials and revoke the device connection in the Beatra Console when no longer needed.

Risk: The package may silently update its installed files by default.

Mitigation: Disable automatic updates with the documented `update --auto off` command if you prefer to review changes first.

Risk: Installation and runtime registration share coarse device and environment facts with Beatra.

Mitigation: Review the documented registration and authentication behavior before installing.

Risk: Video edits can incur credit charges, and repeating an uncertain submission may duplicate paid work.

Mitigation: Confirm the live estimate and account balance before submitting; check the original task status before retrying with the same request ID.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/video-realism-retoucher)
- [Beatra skill page](https://beatra.ai/skills/video-realism-retoucher)
- [Focused retouch workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Video artifact links]

**Output Format:** [Markdown with retouch instructions, task status, and links to the edited video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task ID, actual model and video properties, billing facts, and any observed visual drift; video rendering is performed by Beatra.]

## Skill Version(s):

0.1.9 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
