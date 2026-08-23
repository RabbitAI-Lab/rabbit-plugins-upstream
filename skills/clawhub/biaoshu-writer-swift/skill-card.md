## Description:

This skill helps agents analyze Chinese tender documents, generate editable bid documents, and run compliance reviews through the 百炼®标书 cloud service after the user supplies local files and an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams, procurement-support staff, and their agents use this skill to process mainland-China tender documents, create draft bid packages, and check bid documents for compliance risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential business, pricing, or personal data and are uploaded to the 百炼®标书 cloud service.

Mitigation: Use the skill only after the user understands and accepts cloud processing, and avoid uploading documents outside the intended tender workflow.

Risk: The App Key is stored locally and can authorize account activity and point consumption if exposed.

Mitigation: Have the user create the local config file themselves, never request or echo the App Key in chat, keep file permissions restrictive, and reset the key if exposure is suspected.

Risk: API traffic can be redirected away from the disclosed service endpoint if an alternate base URL is intentionally configured.

Mitigation: Use the official 百炼®标书 endpoint by default and configure an alternate endpoint only when it is explicitly trusted with both documents and credentials.

Risk: Generated bid drafts and compliance findings can be incomplete, stale, or unsuitable for a specific procurement submission.

Mitigation: Require human review before submission, especially for eligibility, pricing, signatures, legal terms, and all marked placeholders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-swift)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [Usage guide](artifact/references/usage.md)
- [Open API contract reference](artifact/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses plus generated HTML, Word, and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents may take more than 10 minutes and can contain placeholders that require user review and completion.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
