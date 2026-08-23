## Description:

标书智能制作 helps agents support mainland-China bidding workflows by sending user-provided tender and bid files to 百炼®标书 for tender interpretation, bid document generation, and compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users, bidding teams, and procurement-support agents use this skill to interpret Chinese tender documents, generate editable bid documents, and review bid files for compliance risks before submission.

### Deployment Geography for Use:

Global; functional scope is mainland-China bidding workflows and Simplified Chinese tender documents.

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain confidential commercial, pricing, and personal information and are uploaded to a third-party cloud service for processing.

Mitigation: Use the skill only after the user confirms informed consent, and upload only the local files needed for the requested interpretation, generation, or compliance review.

Risk: Uploaded files and generated results are retained under the App Key account for a limited period, and historical data may remain visible in the platform account.

Mitigation: Tell users about server retention before first upload and direct them to manage historical data through the 百炼®标书 platform.

Risk: The App Key authorizes the account and may be exposed if copied into chat, shared in links, or sent to an unintended endpoint.

Mitigation: Keep the App Key in the local config file only, never echo it in user-facing messages, and avoid ZCM_BASE or --base unless the endpoint is intentionally trusted.

Risk: Bid generation consumes account credits and long-running jobs can continue after a local command or UI times out.

Mitigation: Check balance before generation, confirm the user expects credit use, and resume existing jobs by job ID instead of resubmitting work that may duplicate charges.

Risk: Generated bid content and compliance findings may be incomplete, inaccurate, or dependent on the user's account knowledge base.

Mitigation: Require qualified human review before submitting any bid document or acting on compliance findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-spark)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书 API](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)
- [API contract reference](references/api.md)
- [Usage and operation guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown responses plus generated .docx, HTML, Word, and JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and platform labels are primarily Simplified Chinese; bid generation can produce editable .docx files with placeholders for information the service cannot confirm.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
