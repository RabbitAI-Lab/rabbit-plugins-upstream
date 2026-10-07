## Description:

Group operational updates into a scheduled digest, remove duplicates, and report delivery timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams consolidate updates into deduplicated, grouped digests and determine the next delivery time from their notification guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can submit digest contents to an external endpoint using environment-provided credentials without strong scoping or confirmation.

Mitigation: Leave delivery configuration unset unless intended, use a trusted endpoint, and exclude sensitive updates unless external submission is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/notification-cadence-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON digest summary and a local digest file, with an optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the scheduled delivery time, retained item count, grouped updates, and deduplication count.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
