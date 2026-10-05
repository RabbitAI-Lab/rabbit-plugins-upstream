## Description:

Creates short talking renewal reminders from an advisor's supplied policy schedule and authorized still images, with one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance advisors and wealth educators use this skill to draft renewal-date narration from their supplied schedule and create short talking clips from stills they are authorized to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device credential grants broad access to billable media operations.

Mitigation: Connect only if comfortable granting full-scope access; approve each paid stage separately and revoke the device in the Beatra Console when no longer trusted.

Risk: Automatic package updates can replace installed files without a separate confirmation.

Mitigation: Consider disabling automatic updates with the documented `update --auto off` command before use.

Risk: Generated reminders could misstate policy deadlines or imply coverage guarantees.

Mitigation: Use only dates and wording from the advisor's supplied schedule, and review each narration and clip before sharing.

Risk: A talking portrait or cloned voice could be used without permission.

Mitigation: Confirm likeness and voice rights before using an image or cloning a voice; file access alone is not consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/insurance-renew-talking)
- [Beatra skill homepage](https://beatra.ai/skills/insurance-renew-talking)
- [Renewal reminder talking-clip workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Markdown, Video clips, Audio]

**Output Format:** [Labeled renewal-reminder plan and individual 2–15-second talking clips with narration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per authorized still; paid voice, speech, and video stages require separate approval.]

## Skill Version(s):

0.1.7 (source: server-resolved ClawHub release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
