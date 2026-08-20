## Description:

Bid-document generation skill for mainland-China tender workflows that uploads user-provided tender or bid files to the Bailian Biaoshu API to interpret tenders, generate editable .docx bid documents, and produce compliance review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze Chinese tender documents, create editable bid submissions, and review bid files for compliance risks before submission. It is intended for workflows where the user has explicitly provided local tender or bid files and accepts cloud processing by the Bailian Biaoshu service.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the Bailian Biaoshu cloud service for processing.

Mitigation: Confirm user consent before uploads and avoid processing documents that are not approved for third-party cloud handling.

Risk: Security evidence says the skill can redirect sensitive document uploads and the App Key to a configurable API host despite describing the official domain as the only network target.

Mitigation: Verify the configured API base is the official biaoshu.zhiliaobiaoxun.com endpoint and avoid ZCM_BASE or alternate base overrides unless the operator intentionally trusts that server.

Risk: The App Key is an account credential tied to billing and generated results.

Mitigation: Keep the App Key in the local skill config, never request or paste it in conversation, and reset it through the service if exposure is suspected.

Risk: Generated bid documents and compliance reports can contain placeholders, incomplete checks, or content that needs business review.

Mitigation: Review generated .docx files, reports, risks, and unresolved placeholders before submitting a bid.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-bid-gen)
- [Bailian Biaoshu service](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API contract reference](references/api.md)
- [Usage and operations guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance, configuration]

**Output Format:** [Text summaries with generated .docx bid files, HTML reports, optional Word reports, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local App Key configuration; generated documents and reports should be reviewed before use.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
