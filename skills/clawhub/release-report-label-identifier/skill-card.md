## Description:

Prepare a configuration entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operators and developers use this skill to turn a supplied configuration note into a concise configuration entry for routine release work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated configuration entries may be used before confirming business correctness.

Mitigation: Review the generated config_key, config_value, and config_label before applying them to production systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-report-label-identifier)

## Skill Output:

**Output Type(s):** [configuration, text]

**Output Format:** [Object with config_key, config_value, and config_label fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated from the current request's config_note; review before applying to production systems.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
