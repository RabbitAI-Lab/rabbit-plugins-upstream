## Description:

This skill helps agents use the 百炼®标书 service to interpret tender documents, generate editable bid documents, and review bid-file compliance from user-approved local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and agents use this skill to analyze tender requirements, draft editable bid documents, and check bid files for disqualification or compliance risks after the user provides local tender or bid files and a user-managed App Key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Use only user-approved local files, confirm the user understands the upload before first use, and avoid sending unrelated files.

Risk: The App Key grants access to the user's service account and credits.

Mitigation: Keep the App Key in local config only, do not ask for it in chat, do not echo it, and do not share key-bearing recharge or binding links.

Risk: Bid generation consumes account credits and long-running jobs may continue after the local agent command stops waiting.

Mitigation: Confirm credit-consuming generation before submission, track the returned job id, and resume status/result retrieval instead of resubmitting the same generation request.

Risk: Generated bid content and compliance findings may be incomplete when source documents, enterprise knowledge, or service responses are incomplete.

Mitigation: Keep uncertain fields as placeholders, present partial-result status clearly, and require human review before procurement submission.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [API contract reference](artifact/references/api.md)
- [Usage guide](artifact/references/usage.md)
- [Knowledge fields reference](artifact/references/knowledge-fields.md)
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-insight)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with generated .docx, HTML, Word, and JSON task outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and bid documents are written locally; bid generation can consume credits from the user's App Key account.]

## Skill Version(s):

1.0.13 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
