## Description:

标事通标书智能写作 helps users process tender and bid documents with the 百炼®标书 cloud service for tender interpretation, .docx bid drafting, compliance review, and two-to-three-file bid similarity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bidding, and proposal teams use this skill to analyze tender requirements, draft bid documents, review bid compliance risks, and compare a small set of bid files for similarity before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bid, pricing, company, or personal information is uploaded to and retained by a third-party cloud service.

Mitigation: Confirm the user understands and consents before upload, process only files the user is authorized to provide, and avoid using the skill for documents that cannot leave the local environment.

Risk: The bundled progress monitor can poll the cloud API excessively during long-running background workflows.

Mitigation: Use a much slower polling interval or require an upstream fix before relying on progress-stream monitoring for long jobs.

Risk: The skill uses a local Api Key and paid word-balance account behavior.

Mitigation: Keep the Api Key in the local config file only, do not paste or echo it in chat, and confirm available balance and user intent before generating billable bid documents.

Risk: Similarity and compliance outputs can be mistaken for legal determinations.

Mitigation: Present results as internal review signals and require qualified human review for procurement, anti-collusion, or legal conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-guard)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge base fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, terminal progress text, JSON results, HTML or Word reports, and generated .docx bid files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided 百炼®标书 Api Key; uploads user-selected tender and bid files to the service; generated task results and .docx files are retained by the service for about 7 days.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
