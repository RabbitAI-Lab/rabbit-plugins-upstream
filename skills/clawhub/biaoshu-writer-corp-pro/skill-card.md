## Description:

A ClawHub agent skill for mainland-China bidding workflows that uses the 百炼®标书 API to interpret tender documents, generate editable bid documents, format bid responses, and review submissions for disqualification and compliance risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and their agents use this skill to analyze Chinese tender documents, prepare .docx bid submissions, and review draft bid files for high-risk, review-needed, and informational compliance issues before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential pricing, personal information, or trade secrets and are uploaded to the third-party 百炼®标书 service for processing.

Mitigation: Use the skill only after the user confirms they are comfortable uploading those files to 百炼®标书, and avoid documents that the user is not authorized to share with that service.

Risk: The skill stores an App Key in a local config file, and credential-bearing recharge or binding links could expose account access if pasted into chat.

Mitigation: Have the user create the local config file themselves, never ask them to paste the App Key in conversation, and do not forward links that contain App Key or bind_key parameters.

Risk: Server security evidence notes that code permits API base URL overrides beyond the declared single service domain.

Mitigation: Review ZCM_BASE and any saved base URL before use, and keep requests pointed at the official https://biaoshu.zhiliaobiaoxun.com/api/open/v1 service unless an authorized reviewer approves otherwise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-corp-pro)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Text guidance plus generated .docx bid documents and HTML or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local App Key and user-provided local document paths; generated bid documents and reports are returned as local files.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
