## Description:

Select processing profiles and register queued job entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations users and agents use this skill to select a processing profile for a workload request and register the selected profile as a queued job entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for workload operations requests involving processing profiles.

Mitigation: Review the requested stage and supplied workload details before relying on the generated processing profile or queue entry.

Risk: Queue records can be misleading if the selected processing profile is based on incomplete workload details.

Mitigation: Confirm record_count, deadline_minutes, and the selected processing profile before using the recorded_profile output operationally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/job-queue-planning-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [String and JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a processing_profile string or a recorded_profile object with queue_entry_id, processing_profile, queue_lane, and chunk_count.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
