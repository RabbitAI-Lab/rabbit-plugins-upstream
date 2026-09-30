## Description:

Build a translation job entry from a supplied locale, glossary, and register.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization teams use this skill to validate translation settings and record a local translation-job entry for a requested locale, glossary, and writing register.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operation writes a translation-job manifest beneath the chosen output directory.

Mitigation: Use a dedicated writable output directory and review the local artifact before relying on it.

Risk: Request data may be included in the local translation-job record.

Mitigation: Only provide sensitive information when it is necessary for the job setting.

## Reference(s):

- [Translation Job Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/translation-job-setting-workbench)

## Skill Output:

**Output Type(s):** [Configuration, Files]

**Output Format:** [JSON response and local JSON manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the recorded translation setting and a local artifact receipt; does not confirm an external business action.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
