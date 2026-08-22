## Description:

Group operational updates into a scheduled digest, remove duplicates, and report delivery timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and agents use this skill to consolidate current operational updates into a scheduled digest with stable grouping, deduplication counts, and delivery timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Digest outputs can include sensitive operational details supplied in the input guidance or updates.

Mitigation: Review source updates and intended recipients before sharing generated digests.

Risk: Incorrect cadence, timezone, cutoff, or deduplication guidance can produce misleading delivery timing or counts.

Mitigation: Validate notification_guidance values and review scheduled_for, item_count, groups, and deduplicated_count before use.

## Reference(s):

- [Operations Digest Composer on ClawHub](https://clawhub.ai/wxt-ai/skills/notification-cadence-guidance-workbench)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns digest_summary with scheduled_for, item_count, groups, and deduplicated_count.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
