## Description:

Uses an App Key to call the 百炼®标书 cloud API for tender interpretation, package extraction, editable .docx bid document generation, and optional compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and bid teams use this skill to interpret local tender files, create draft bid documents, and review generated bid files for compliance risks. It is intended for users who can provide an App Key and are authorized to upload tender or bid materials to the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use only when the user and organization permit cloud processing of those files, and confirm consent before the first upload.

Risk: The App Key is a full account credential stored locally for API access.

Mitigation: Have the user write the key locally, do not request or echo it in chat, keep the credential file restricted, and reset the key if exposure is suspected.

Risk: Bid document generation consumes account credits and long-running generation can continue after a local client interruption.

Mitigation: Check account balance and user intent before generation, use idempotent or resumable job handling, and avoid duplicate submissions.

Risk: Uploaded files and generated results are retained by the service account for a limited period, and local reports or a small filename cache may remain on disk.

Mitigation: Avoid highly sensitive materials unless retention is acceptable, and remove local outputs or cache files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)
- [Knowledge field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown responses plus generated local files such as HTML reports, Word reports, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include absolute local file paths, structured interpretation summaries, compliance findings, and billing or credential guidance.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
