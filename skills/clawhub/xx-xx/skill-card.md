## Description:

查询特定时间段内监察部及各调查组的挽损金额数据；该 SOP 仅用于查询挽损金额，不包括案件具体情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuoxiangpang](https://clawhub.ai/user/zhuoxiangpang)

### License/Terms of Use:

MIT-0

## Use Case:

业务用户或授权代理使用该技能查询指定年月内监察部及各调查组的聚合挽损金额。它适用于需要按部门和调查组汇总挽损金额、且不需要案件明细的场景。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill references an internal table for loss-recovery data, so use by an unauthorized agent could expose business data.

Mitigation: Install only where the agent is authorized to query that table and restrict database permissions to the aggregate loss-recovery fields needed for this SOP.

Risk: The workflow is intended for aggregate amounts only and could be misused to request case-specific details outside its scope.

Mitigation: Keep prompts, queries, and returned results limited to supervisory department and investigation-group loss-recovery amounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhuoxiangpang/skills/xx-xx)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown or plain text query guidance and aggregate monetary results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only aggregate loss-recovery lookup; excludes case-specific details.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
