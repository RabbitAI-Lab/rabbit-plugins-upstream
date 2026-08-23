## Description:

Create a profile-setting review item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and governance reviewers use this skill to turn an approved profile setting key into a concise review item for workspace governance handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated review item could be used with the wrong profile setting key or governance queue.

Mitigation: Use only an approved setting_key and review the produced review_item before including it in a governance workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/profile-setting-key-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Structured review item object with review_item_id, setting_key, value_type, and review_queue fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the supplied setting_key and should be reviewed before governance handoff.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
