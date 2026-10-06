## Description:

Builds a translation job entry from a selected locale, glossary, and register.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization teams use this skill to record translation-job settings and create a local job entry. If delivery is configured, it can also submit the record to an external service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery target can submit translation-job records to an external endpoint using available credentials.

Mitigation: Review the delivery endpoint, SMTP settings, API key, and any delivery config before use; leave delivery unconfigured unless external submission is intended.

## Reference(s):

- [Translation Job Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/translation-job-setting-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a recorded translation setting and creates a local job artifact; includes a delivery receipt when configured.]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
