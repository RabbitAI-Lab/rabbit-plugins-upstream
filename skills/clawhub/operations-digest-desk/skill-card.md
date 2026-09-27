## Description:

Choose notification cadence and compose scheduled operations digests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and communications coordinators use this skill to choose a digest cadence, deduplication key, delivery timing, and then assemble scheduled operations updates into a concise grouped digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger wording may cause the skill to be considered for broad operations-communications requests beyond its documented behavior.

Mitigation: Use it only for cadence-rule preparation and digest-summary assembly; route message sending, system access, or incident actioning to separately reviewed tools.

Risk: Incorrect cadence, timezone, grouping, or deduplication choices could make an operations digest misleading.

Mitigation: Review the selected delivery window, timezone, grouping field, deduplication key, and cutoff before using the digest operationally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/operations-digest-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Short string cadence guidance or JSON-compatible digest summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credentials, private files, persistence, or automatic notification sending are required by the documented skill.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
