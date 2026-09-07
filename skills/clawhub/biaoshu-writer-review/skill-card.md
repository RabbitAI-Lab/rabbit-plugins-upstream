## Description:

Helps agents process tender and bid documents with AI-assisted interpretation, bid document generation, compliance review, and similarity checking through the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement-support users use this skill to review tender requirements, generate editable bid documents, check bid compliance risks, and compare bid files for similarity before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercially sensitive information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm the user understands and agrees to cloud processing before upload, and limit inputs to files the user explicitly provides.

Risk: The API key grants account access and could be exposed if pasted into chat or logs.

Mitigation: Have the user store the key locally in the skill configuration and do not request, echo, or transmit the key in conversation.

Risk: Generated bid documents may consume the account's available word balance.

Mitigation: Tell users about word-balance use before bid generation and rely on the service precheck before submitting generation jobs.

Risk: Uploaded files and generated results are retained under the user's 百炼®标书 account according to the service terms.

Mitigation: Ask users to review retention terms and manage historical data through their service account when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review)
- [Usage guide](references/usage.md)
- [Open API contract reference](references/api.md)
- [Knowledge field reference](references/knowledge-fields.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated report and document file paths, JSON status/results, and downloadable .docx outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided local tender or bid files and a locally stored API key; processing sends those files to the 百炼®标书 cloud service.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
