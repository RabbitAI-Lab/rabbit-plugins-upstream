## Description:

Creates short, spoken welcome and amenity clips from authorized host or room photos and confirmed stay details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Hosts and property managers use this skill to turn authorized stills and confirmed check-in or amenity details into one short talking clip per photo, delivered in stay order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra Device Token grants broad media, task, and spending-related authority across Beatra skills.

Mitigation: Connect only if comfortable with that scope; keep the token private and revoke the device connection if it is no longer trusted.

Risk: The package silently installs verified updates by default, changing local skill files without separate approval.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when package changes must be reviewed first.

Risk: Speech and video generation are separately billable and can consume Beatra credits.

Mitigation: Check the current price and request explicit approval for each paid speech or video call before submission.

Risk: Generated speech or likeness could misrepresent a host or introduce incorrect stay details.

Mitigation: Confirm likeness and voice rights, use only verified stay facts, and review each resulting clip before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/airbnb-welcome-avatar)
- [Publisher skill homepage](https://beatra.ai/skills/airbnb-welcome-avatar)
- [Homestay welcome talking-clip workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Video clips]

**Output Format:** [Markdown storyboard and results with links to individual video clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One 2–15-second clip per approved still or speech segment; results include actual duration, dimensions, usage, and net charged credits.]

## Skill Version(s):

0.1.8 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
