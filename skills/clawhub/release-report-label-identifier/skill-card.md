## Description:

Extracts a RETENTION label from a supplied release configuration note and returns a normalized configuration entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams use this skill to identify a RETENTION label in a supplied configuration note and prepare a normalized configuration entry for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vague configuration requests can leave the intended retention label unclear.

Mitigation: Confirm the returned label matches the intended release configuration before using the entry.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/release-report-label-identifier)

## Skill Output:

**Output Type(s):** [Configuration]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns config_key, config_value, and config_label; no persistent artifact.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
