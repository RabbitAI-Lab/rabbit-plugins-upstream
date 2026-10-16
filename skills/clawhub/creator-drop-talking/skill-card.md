## Description:

Turns a confirmed new-drop script and authorized stills into short talking launch teasers, one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and listing teams use the skill to plan and generate short spoken product-drop announcements from confirmed launch facts and authorized images and voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared Beatra device authorization can spend credits across generation tools and be reused by other Beatra skills.

Mitigation: Review the full approval scopes before connecting, approve each paid stage and its live price, and disconnect the shared authorization when no longer needed.

Risk: A broad remote tool connection and locally shared bearer credential may expose more account authority than this clip workflow needs.

Mitigation: Install only where shared Beatra credentials and broad account access are acceptable; restrict access to the local credential and review connected tools.

Risk: The installed client silently checks for and installs verified updates by default.

Mitigation: Turn off automatic updates with the documented update command if changes must be reviewed before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/creator-drop-talking)
- [Beatra skill homepage](https://beatra.ai/skills/creator-drop-talking)
- [Workflow](artifact/references/workflow.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Video files]

**Output Format:** [Labeled clip plan and generated talking teaser clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One 2–15 second clip per still; clips are not stitched. Paid generation requires separate approval.]

## Skill Version(s):

0.1.9 (source: server-resolved ClawHub release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
