## Description:

Refines one realism issue in an existing AI-generated short video while aiming to preserve its subject, framing, timing, and mood.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to polish lighting, material texture, saturation, or repeated details in an existing AI-generated product, advertising, or social video. It prepares one source-led paid retouch and returns the resulting video and task details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Beatra receives a shared device credential with broad media and wallet authority.

Mitigation: Review the requested access before connecting and keep the credential private.

Risk: Automatic package updates are enabled by default and may install without separate confirmation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you require explicit approval for package changes.

Risk: Uploaded videos are sent to Beatra's remote service.

Mitigation: Upload only videos you are comfortable sharing with Beatra.

Risk: A paid retouch can change details the user intended to keep.

Mitigation: Confirm the scope and estimate before submitting, then review the result against the source and report any visible drift.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/video-realism-retoucher)
- [Beatra skill page](https://beatra.ai/skills/video-realism-retoucher)
- [Focused retouch workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Video links]

**Output Format:** [Markdown with video artifact links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid edit may return video artifacts, task ID, model, dimensions, duration, and billing details.]

## Skill Version(s):

0.1.8 (source: server-resolved release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
