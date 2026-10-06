## Description:

Selects a release branch name from a supplied quarter and release name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release managers use this skill to derive a consistent source branch name from a release quarter and name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation mentions writable output directories and SQLite even though the configured branch-selection operation does not use them.

Mitigation: Clarify the documentation and confirm the configured operation before running the local helper.

## Reference(s):

- [Release Branch Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/release-branch-policy-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with a source_branch string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Branch names use the release/qN-name pattern.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
