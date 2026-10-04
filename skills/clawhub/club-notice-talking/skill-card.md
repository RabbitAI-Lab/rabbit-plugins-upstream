## Description:

Turns a supplied club-activity script and authorized stills into separate short talking clips, one per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and club advisors use the skill to turn their own activity-script points and authorized stills into individual narrated club notices or signup clips. It plans the clip list, requests approval before paid generation, and returns separate clips rather than a stitched video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device connection grants broad media, task, artifact, and spending authority.

Mitigation: Connect only if comfortable granting that access, and review each paid-stage approval card before allowing generation.

Risk: The bundled client silently installs newer package code by default, so previously reviewed code can change.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if the reviewed installation should remain fixed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/club-notice-talking)
- [Beatra skill homepage](https://beatra.ai/skills/club-notice-talking)

## Skill Output:

**Output Type(s):** [Text, Video clips]

**Output Format:** [Markdown slot list and separate video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each clip targets 2–15 seconds; report available MIME type, duration, file size, and charged credits.]

## Skill Version(s):

0.1.9 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
