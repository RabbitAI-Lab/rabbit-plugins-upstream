## Description:

Provides manual guidance for saving PikPak links and selectively restoring shares, with an offline checker for task receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and assistants can follow a manual workflow to submit authorized links, check tasks by exact ID, and restore selected files from shares. The local checker examines JSON task receipts without accessing the network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A timed-out submission or restore may have succeeded, so repeating it can create unintended duplicates.

Mitigation: Reconcile the original link or share, destination and exact IDs before any newly authorized attempt.

Risk: Restoring a share without selected file IDs can include files the user did not approve.

Mitigation: Preview all pages and folders, then restore only the explicitly approved file IDs.

Risk: Using the disclosed referral code may reward its sharer.

Mitigation: Give users a choice before registration and explicitly pass an empty affiliate value if they decline.

## Reference(s):

- [PikPak Save release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-save)
- [Upstream design and limitations](artifact/references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions and JSON task-receipt summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual workflow; the offline receipt checker does not provide persistent task tracking.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
