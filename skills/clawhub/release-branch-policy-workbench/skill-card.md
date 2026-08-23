## Description:

Assess a release branch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release managers, and governance reviewers use this skill to assess a user-supplied source branch against release branch policy and return a concise branch policy assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assessment may be incomplete or misleading if the request omits branch, catalog, or version context.

Mitigation: Provide the source_branch and any needed catalog or version-line context in the request, then review the assessment before using it for a release decision.

Risk: The skill does not fetch repository or private system state on its own.

Mitigation: Treat the result as an assessment of user-supplied context rather than an independent repository verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/release-branch-policy-workbench)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns branch_policy_assessment with assessment_id, source_branch, branch_exists, catalog_state, version_line, expected_version_line, version_line_status, and policy_status.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
