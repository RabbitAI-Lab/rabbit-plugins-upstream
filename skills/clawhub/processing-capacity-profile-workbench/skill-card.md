## Description:

Registers a queued processing profile and records the resulting job entry locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to register a processing profile for a queued job and receive its queue entry, lane, and chunk count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local job-queue SQLite receipt is written to the selected output directory, which may be sensitive or shared.

Mitigation: Choose a dedicated writable output directory and avoid sensitive or shared locations.

## Reference(s):

- [Job Queue Register on ClawHub](https://clawhub.ai/wxt-ai/skills/processing-capacity-profile-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response with a recorded profile and local effect receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a local SQLite receipt in the chosen output directory; does not submit an external job.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
