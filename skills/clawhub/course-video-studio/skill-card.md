## Description:

Turns finished lecture scripts and an authorized teacher portrait into narrated, presenter-led course videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators and training teams use the skill to turn approved teacher portraits and finished lecture scripts into ordered, narrated lesson videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent Beatra Device Token is shared across Beatra skills and can spend generation credits.

Mitigation: Review token access and credit exposure before installing; confirm each paid generation request.

Risk: Automatic updates can change installed skill files without separate approval.

Mitigation: If changes require explicit approval, disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: Using a teacher's likeness or cloning their voice without permission can misuse their identity.

Mitigation: Confirm likeness and voice rights before generation, and obtain consent before cloning a voice.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/course-video-studio)
- [Course Video Studio homepage](https://beatra.ai/skills/course-video-studio)
- [Course video workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with lesson video artifact links and review details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos are delivered in lesson and segment order with duration, dimensions, usage, and charged credits.]

## Skill Version(s):

0.1.9 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
