## Description:

Choose a profile setting key for a supported workspace request category.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace users and agents use this skill to choose the appropriate profile setting key for notification digest, sharing visibility, or default language requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect request category could yield the wrong profile setting key.

Mitigation: Use a supported request category and confirm the returned key matches the intended setting.

Risk: Running an unreviewed local helper may produce unexpected results.

Mitigation: Review the installed skill and request JSON before executing its Python helper.

## Reference(s):

- [Profile Setting Directory on ClawHub](https://clawhub.ai/wxt-ai/skills/profile-setting-key-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing a setting_key string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns one of three supported profile setting keys; does not persist a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
