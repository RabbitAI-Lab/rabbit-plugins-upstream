## Description:

Build a translation job entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization operations users use this skill to turn a supplied translation_setting object into a concise recorded translation job entry for the current request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated job_code or segment_limit values may not match a workflow-specific business rule because the artifact does not define their derivation.

Mitigation: Review job_code and segment_limit before using the recorded translation job entry in a production localization workflow.

## Reference(s):

- [Translation Job Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/translation-job-setting-workbench)
- [wxt-ai Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Concise structured text describing the recorded_translation_setting object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces recorded_translation_setting with job_code, locale, glossary_id, register, and segment_limit fields.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
