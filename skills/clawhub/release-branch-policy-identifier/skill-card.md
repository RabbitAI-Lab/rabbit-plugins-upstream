## Description:

Select a branch for a release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release managers and developers use this skill to derive a concise source branch from a supplied release quarter and release name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could provide more release information than the branch-selection task requires.

Mitigation: Provide only the release quarter and release name needed to derive the source branch.

Risk: Branch selection guidance can be wrong if the supplied release quarter or release name is incorrect.

Mitigation: Review the returned source_branch against the release plan before using it in release operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-branch-policy-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the source_branch field as a concise branch name string.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
