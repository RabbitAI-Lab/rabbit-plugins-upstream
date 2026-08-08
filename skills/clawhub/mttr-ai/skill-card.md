## Description:

查询安全水位的指标：mttr、事件量、ai提效。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuoxiangpang](https://clawhub.ai/user/zhuoxiangpang)

### License/Terms of Use:

MIT-0

## Use Case:

Security operations and management users can use this skill to query security waterline metrics such as MTTR, event volume, and AI efficiency. It applies default scope and time rules for ambiguous questions and explains unsupported monthly, quarterly, or yearly MTTR requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous metric questions default to 信息安全部 and the current week, which may produce an unexpected scope for the requester.

Mitigation: Ask users to specify department and time range explicitly, and state the applied defaults when answering ambiguous requests.

Risk: Security metric responses may expose data beyond the requester's intended authorization if surrounding access controls are too broad.

Mitigation: Configure data-access controls so the skill can only return metrics the requester is allowed to view.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text responses describing metric query results and scope assumptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults ambiguous queries to 信息安全部 and the current week unless the user specifies a department or time range.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
