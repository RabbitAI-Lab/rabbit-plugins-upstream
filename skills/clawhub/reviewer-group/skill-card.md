## Description:

Combines select a reviewer group with register a request reviewer group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to select reviewer groups for procurement, access, policy, and workspace governance requests, then register the chosen group for request ownership and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The request-review registration operation could write to an unintended register if it is bound to the wrong destination.

Mitigation: Before installation or use, confirm that record_reviewer_group writes only to the intended request-review register.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/reviewer-group)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Text fields for reviewer_group and recorded_group]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
