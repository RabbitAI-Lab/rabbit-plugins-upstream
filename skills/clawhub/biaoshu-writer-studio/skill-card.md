## Description:

智能标书编制 helps agents process locally provided tender and bid documents through the 百炼®标书 cloud service to interpret tender requirements, generate editable bid documents, review compliance risks, and compare bid files for similarity signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and business users use this skill to analyze tender files, create draft bid documents, check submitted bid files for compliance issues, and compare 2-3 bid files for similarity risk before submission. It is intended for Simplified Chinese procurement and bidding workflows using the user's 百炼®标书 account.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud under the user's API-key account.

Mitigation: Confirm user consent before upload, use only user-selected local files, and review the vendor's retention and account controls before processing sensitive documents.

Risk: The API key grants access to the user's 百炼®标书 account.

Mitigation: Keep the API key out of chat, store it only in the local config file, and rotate it through the vendor portal if exposure is suspected.

Risk: Generated outputs and limited local metadata may remain on disk after processing.

Mitigation: Store outputs in the intended output directory, restrict access to generated reports and config files, and remove local artifacts when they are no longer needed.

Risk: Bid similarity checks provide internal risk signals and do not establish legal conclusions about collusion, bid validity, or regulatory compliance.

Mitigation: Treat similarity findings as review cues and have qualified procurement or legal reviewers assess any high-risk result before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-studio)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Agent-facing guidance plus JSON results, HTML or Word reports, short-lived download links, and editable .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated report labels and procurement terminology are primarily zh-CN. Bid generation consumes account word balance; interpretation, compliance review, and similarity checks require available balance to submit but do not themselves consume it. Task results and generated .docx files are retained by the service for about 7 days.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
