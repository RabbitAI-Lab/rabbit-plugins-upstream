## Description:

Uploads user-selected tender and bid documents to the 百炼®标书 cloud service to interpret tender requirements, generate editable .docx bid drafts, review bid risks, and compare bid-document similarity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams, proposal writers, and procurement reviewers use this skill to analyze tender files, create bid-document drafts, run compliance checks, and review similarity risks before submission. It is intended for workflows where users can lawfully upload the selected documents to the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm the user is comfortable with that upload before installing or using the skill for sensitive documents.

Risk: The Api Key grants access to the service account if exposed in chat or shared links.

Mitigation: Keep the Api Key out of chat and have the user manage it only in the local credential file.

Risk: Generated bid content or review findings may be incomplete, incorrect, or unsuitable for final submission.

Mitigation: Review generated documents and reports before relying on them in a procurement process.

Risk: Uploaded files and generated results may remain available in the service account for a limited period.

Mitigation: Use the service account controls to review and manage retained history for sensitive projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-check-assistant)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract](artifact/references/api.md)
- [Usage guide](artifact/references/usage.md)
- [Knowledge fields reference](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown summaries plus generated local files or service results such as HTML reports, Word documents, JSON similarity results, and absolute output paths or download links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-managed Api Key; selected files are processed by the stated cloud service and generated results should be reviewed before use.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
