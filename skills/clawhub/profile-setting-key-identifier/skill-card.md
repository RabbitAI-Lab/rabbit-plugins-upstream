## Description:

Choose a profile setting key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace governance users and agents use this skill to map a request category to the concise profile setting key that should be returned as `setting_key`.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A returned profile setting key could be used to make an unintended profile change if the surrounding workflow accepts it without validation.

Mitigation: Validate the returned `setting_key` against the allowed profile settings before applying any profile changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/profile-setting-key-identifier)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a concise `setting_key` string.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
