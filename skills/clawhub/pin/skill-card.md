## Description:

查询京东账号（京东pin）绑定手机号及关联员工公司信息流程；入参为：pin（京东账号（京东pin））

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuoxiangpang](https://clawhub.ai/user/zhuoxiangpang)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized analysts or support operators use this workflow to trace a JD account pin to phone binding history and related employee or company records when they have a verified business need.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can correlate a JD account with phone, employee, and company records without stating authorization or privacy controls.

Mitigation: Deploy only where users are authorized for these datasets and where approvals, logging, masking, and purpose limits are enforced outside the skill.

Risk: The workflow could be used for general account lookup without a verified business need.

Mitigation: Require a documented business purpose before use and restrict access to approved support or investigation workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhuoxiangpang/skills/pin)
- [ClawHub Publisher Profile](https://clawhub.ai/user/zhuoxiangpang)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent through dependent lookup steps for one JD pin input; it does not include code or executable tooling.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
