## Description:

Turns a supplied localization note into a translation setting with a normalized locale, glossary ID, and register.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization and content-operations teams use this skill to turn a supplied locale, glossary name, and register into a consistent translation setting for a handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled zh-CN example may be mistaken for the current request and produce the wrong locale or glossary setting.

Mitigation: Supply a request JSON with the actual localization note; treat the included example only as an input-shape guide.

## Reference(s):

- [Localization Setting Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/translation-job-setting-identifier)

## Skill Output:

**Output Type(s):** [Configuration]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a translation_setting object containing locale, glossary_id, and register; does not persist a business artifact.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
