## Description:

Group operational updates into a scheduled digest, remove duplicates, and report delivery timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to consolidate updates into a deduplicated digest and determine its next scheduled delivery time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates or updates a local digest under the supplied output directory.

Mitigation: Use a dedicated writable output folder and review the generated digest before relying on it.

Risk: Free-form guidance can contain unrelated instructions.

Mitigation: Treat guidance as operational input only; exclude unrelated instructions.

## Reference(s):

- [Operations Digest Composer on ClawHub](https://clawhub.ai/wxt-ai/skills/notification-cadence-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [JSON digest summary and local Markdown digest file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scheduled delivery time, retained item count, groups, deduplicated count, and a local-file receipt.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
