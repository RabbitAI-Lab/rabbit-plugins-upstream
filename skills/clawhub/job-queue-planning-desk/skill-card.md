## Description:

Selects a processing profile for a workload and, when requested, registers the profile in a local job queue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations staff and developers use this skill to select a processing profile from a workload brief and optionally register that profile as a local queued record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downstream registration creates a local SQLite queue record in the supplied output directory.

Mitigation: Use a dedicated, writable output directory and request registration only when the local record is wanted.

Risk: Request files may contain unnecessary sensitive information.

Mitigation: Provide only the declared workload or processing-profile fields; do not pass sensitive request files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/job-queue-planning-desk)
- [Skill usage and operation documentation](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON with a processing profile or recorded queue entry and an effect receipt when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream registration writes a local SQLite queue record only when an output directory is provided; it does not confirm an external action.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
