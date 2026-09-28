## Description:

Plan translation settings and build translation job entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization operations teams use this skill to plan translation settings from a localization note and record concise translation job entries from approved settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls named localization tools whose behavior depends on the target environment.

Mitigation: Before installing, confirm that suggest_translation_setting and build_translation_job_entry are the expected localization tools.

Risk: Incorrect localization inputs could produce unsuitable translation settings or job entry fields.

Mitigation: Review generated locale, glossary_id, register, job_code, and segment_limit values before recording or dispatching a localization job.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/localization-job-desk)
- [Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Structured object fields for translation_setting and recorded_translation_setting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns concise localization fields such as locale, glossary_id, register, job_code, and segment_limit.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
