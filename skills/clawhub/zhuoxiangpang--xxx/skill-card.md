## Description:

查询员工作为被处理人｜被举报人的案件详情，注意该SOP不适用于 查询员工作为负责人的案件查询

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuoxiangpang](https://clawhub.ai/user/zhuoxiangpang)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized reviewers use this SOP to query case details for a named employee when the employee is the processed or reported person. It explicitly excludes queries where the employee is the responsible person.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can expose sensitive employee case records beyond its stated role-based scope.

Mitigation: Install only for users authorized to access employee case records, tighten the workflow to approved structured role fields or require separate approval for broader text search, and mask responsible-person details unless needed for authorized review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhuoxiangpang/skills/xxx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown SOP with structured query steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a personnel name and authorized access to employee case records.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
