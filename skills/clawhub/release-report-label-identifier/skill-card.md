## Description:

Extracts a RETENTION label from a supplied release configuration note and returns a structured configuration entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations staff and developers use this skill to turn a supplied configuration note into a configuration entry containing its RETENTION label.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The extracted label may be wrong if the supplied configuration note is incorrect, and the result does not confirm that a release action occurred.

Mitigation: Review the supplied config_note and verify the returned label against the intended release configuration; do not treat the JSON result as proof of a completed action.

## Reference(s):

- [Release Configuration Brief on ClawHub](https://clawhub.ai/wxt-ai/skills/release-report-label-identifier)

## Skill Output:

**Output Type(s):** [Configuration data]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The configuration_entry object contains config_key, config_value, and config_label.]

## Skill Version(s):

1.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
