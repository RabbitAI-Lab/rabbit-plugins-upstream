## Description:

The skill helps bidding teams upload tender and bid files to BaiLian Biaoshu's cloud service for tender interpretation, .docx bid-document generation, compliance review, and similarity checks across two to three bid files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid-writing, procurement, and compliance teams use this skill to interpret tender documents, produce editable bid documents, review bid submissions for risk signals, and compare legally held bid files for similarity before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain business, pricing, and personal information and are uploaded to BaiLian Biaoshu's cloud service for processing.

Mitigation: Confirm the user is comfortable with the upload and retention model before processing, and limit inputs to documents the user explicitly provides for the requested task.

Risk: The API key controls access to the user's BaiLian Biaoshu account.

Mitigation: Have the user create the local config.json themselves and never paste, repeat, or expose the API key in chat.

Risk: Bid document generation consumes the API-key account's available character balance.

Mitigation: Treat generation as the billable workflow and make the cost-bearing step clear before starting a generation job.

Risk: Similarity and duplicate-check results are risk signals, not legal determinations of collusion or bid validity.

Mitigation: Present duplicate-check findings as internal pre-submission review signals and require human or legal review for final determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-radar)
- [BaiLian Biaoshu service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge base field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with JSON results and generated .docx, HTML, or Word report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a BaiLian Biaoshu API key; generated bid documents are billable, while interpretation, compliance review, and duplicate checks require available account balance before submission.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
