## Description:

Plans a translation setting from a supplied localization request, normalizing its locale and glossary identifier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization teams and developers use this skill to turn a supplied locale, glossary name, and register into a consistent translation-job setting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect localization request can produce an unsuitable translation setting.

Mitigation: Review the input JSON and verify the locale, glossary ID, and register before using the result.

## Reference(s):

- [Localization Setting Planner release](https://clawhub.ai/wxt-ai/skills/translation-job-setting-identifier)
- [Publisher profile (wxt-ai)](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Configuration]

**Output Format:** [JSON object with translation_setting containing locale, glossary_id, and register]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local computation; no network service or persisted artifact in the configured path.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
