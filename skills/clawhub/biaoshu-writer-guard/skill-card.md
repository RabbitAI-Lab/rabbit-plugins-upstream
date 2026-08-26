## Description:

A Chinese bidding-document assistant that uses an App Key to call the 百炼标书 API for tender interpretation, bid-document generation, compliance review, report export, and multi-file similarity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze user-provided tender files, generate editable bid documents, review bid compliance, and produce reports for procurement submissions. It is intended for workflows where the user has supplied local tender or bid files and has confirmed use of the 百炼标书 cloud service under their App Key account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before uploading files and use the skill only with user-selected local tender or bid files.

Risk: Generated bid documents may be incomplete, inaccurate, or unsuitable for direct submission.

Mitigation: Review generated bid documents and compliance reports before submission, especially retained placeholders, eligibility requirements, red-line failures, pricing, signatures, and dates.

Risk: The App Key is a full account credential and can be exposed through chat, logs, screenshots, or credential-bearing links.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and do not forward links that include credential or bind_key parameters.

Risk: Uploaded files and generated results may remain available on the service for the documented retention period.

Mitigation: Tell users that results may be retained under the App Key account and can be reviewed or managed through the service.

Risk: Bid-document generation consumes account credits, while some other actions still require a positive balance before submission.

Mitigation: Check account balance before running tasks and explain that generation is the operation documented as consuming credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-guard)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage and operating guide](references/usage.md)
- [Knowledge-base field guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Chinese-language assistant guidance plus generated HTML, Word, DOCX, and JSON-backed report artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include tender interpretation summaries, compliance risk lists, editable bid documents, absolute local output paths, progress updates, and account-balance notices.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
