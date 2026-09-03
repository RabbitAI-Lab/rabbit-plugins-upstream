## Description:

Uploads tender and bid documents to 百炼®标书 to interpret tender requirements, generate editable .docx bid documents, review bid risks, and compare 2-3 bid files for duplicate or similarity signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to analyze tender files, draft bid documents, review compliance risks, and check authorized bid files for similarity before submission. It supports Chinese tender/bid workflows that require structured reports, editable documents, and careful handling of commercial or personal information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user awareness and authorization before upload, process only user-selected files, and avoid uploading documents the user is not allowed to share.

Risk: The Api Key grants access to the user's service account if exposed.

Mitigation: Keep the Api Key out of chat, store it only in the local config file, and do not echo credential-bearing links or values.

Risk: Duplicate-check results can be misread as legal determinations about collusion or bid validity.

Mitigation: Use duplicate checking only as an internal pre-submission signal, require authorization to process all files, and have qualified reviewers make final legal or procurement judgments.

Risk: Generated bid documents and review findings may be incomplete or inaccurate for a specific procurement.

Mitigation: Review generated documents, risk findings, source evidence, and required fill-in items before submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-gov)
- [百炼®标书 Open API Contract](references/api.md)
- [Execution Details](references/usage.md)
- [Knowledge Base Field Reference](references/knowledge-fields.md)
- [百炼®标书 Service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance, JSON summaries, HTML/Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a 百炼®标书 Api Key; user-selected tender and bid files are uploaded to biaoshu.zhiliaobiaoxun.com, and generated .docx files may be delivered through short-lived download links.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
