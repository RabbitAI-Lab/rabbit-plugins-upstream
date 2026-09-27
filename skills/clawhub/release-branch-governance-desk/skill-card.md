## Description:

Select release branches and assess branch policy state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release managers and governance reviewers use this skill to select a release source branch from release request details and assess branch policy state for a selected source branch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous release branch requests can lead to incorrect branch selection or assessment context.

Mitigation: Provide explicit branch_request values with quarter and release_name, or provide an explicit source_branch for assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-branch-governance-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, structured data, guidance]

**Output Format:** [String for source_branch or structured object for branch_policy_assessment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected stage determines whether the agent returns source_branch or branch_policy_assessment.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
