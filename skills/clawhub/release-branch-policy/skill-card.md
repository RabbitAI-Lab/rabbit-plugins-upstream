## Description:

Combines select a branch for a release with assess a release branch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill for routine release governance: selecting normalized release branch names and assessing selected branches against catalog, version-line, and release-state expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents release branch operations but does not include executable validation logic or embedded policy data.

Mitigation: Confirm that the branch catalog and release-state rules used by the workflow are supplied and maintained elsewhere before relying on the assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-branch-policy)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Text or Markdown with release branch names and branch policy assessment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces source_branch and branch_policy_assessment outputs from user-supplied branch release inputs.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
