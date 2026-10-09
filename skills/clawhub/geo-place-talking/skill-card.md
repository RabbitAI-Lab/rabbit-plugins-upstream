## Description:

Turns a teacher's geography place table and authorized still images into short, individual talking clips that speak only facts supplied in the table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to create short geography place talking clips from their own place tables and authorized images, with separate approval before paid voice, speech, or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests a shared Beatra device credential with broad account access and authority to make paid generation calls.

Mitigation: Install only if you trust the publisher with this account scope; confirm each paid stage and revoke the device through the Beatra Console when access is no longer needed.

Risk: Package files can update automatically without a separate confirmation.

Mitigation: Review updates before using them or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/geo-place-talking)
- [Geography place talking-clip workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio files, Video files]

**Output Format:** [Labeled clip plan and separate generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One 2–15-second talking clip per still; clips are not stitched together.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
