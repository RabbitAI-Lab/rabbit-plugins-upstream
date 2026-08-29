## Description:

百炼标书智能写作工具 calls the 百炼®标书 cloud API with a user-provided App Key to interpret tender files, extract packages, generate bid documents in .docx format, and optionally review bids for compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid-writing teams use this skill to send local tender and bid documents to 百炼®标书 for tender interpretation, package selection, bid-document generation, and compliance review. The workflow is intended for mainland-China bidding scenarios and returns editable documents, reports, summaries, and operational guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender, bid, company, and pricing documents are uploaded to the 百炼®标书 cloud service under the user's App Key.

Mitigation: Install and use only when users are comfortable with that upload path, and confirm user consent before sending sensitive files.

Risk: The App Key is an account credential and could expose account access if shared in chat or copied into logs.

Mitigation: Keep the App Key out of conversation history and store it only in the local config file controlled by the user.

Risk: Generated bid documents and compliance findings may contain errors or incomplete judgments.

Mitigation: Review generated bid documents, compliance reports, and unresolved placeholders before submission.

Risk: Bid generation can consume account credits and task results remain available in the service account for a limited period.

Mitigation: Check account balance before generation and make users aware of credit use and limited service-side result retention.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-bailian)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API contract reference](references/api.md)
- [Execution and usage guide](references/usage.md)
- [Knowledge field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and plain text guidance, JSON API results, HTML or Word reports, and generated .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include absolute local file paths for generated reports and bid documents; bid generation can consume account credits.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
