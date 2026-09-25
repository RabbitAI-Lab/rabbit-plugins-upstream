## Description:

Choose profile setting keys and open profile-setting review items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and workspace governance operators use this skill to select the appropriate profile-setting key for a profile request and create a profile-setting review item for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selected profile setting key could be inappropriate for the user's governance request.

Mitigation: Review the returned setting_key before using it to create a profile-setting review item.

Risk: Review-item creation changes the governance workflow state.

Mitigation: Install and invoke the skill only in workspaces that expect profile-setting review workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/profile-governance-desk)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Structured text fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a setting_key string or a review_item object with review_item_id, setting_key, value_type, and review_queue.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
