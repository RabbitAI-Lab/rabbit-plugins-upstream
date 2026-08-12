## Description:

A ClawHub agent skill for mainland-China technical bid workflows that uploads user-provided tender and bid documents to the 百炼®标书 API to interpret tenders, generate technical bid .docx files, and run compliance reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users, bid teams, and agents use this skill to analyze Chinese tender files, draft technical bid documents, and review submitted bid documents for compliance risks. It is intended for workflows where users knowingly provide local tender or bid files and configure their own 百炼®标书 App Key.

### Deployment Geography for Use:

Mainland China bidding workflows; reviewers should confirm any broader deployment geography before publication.

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm user consent before upload and disclose that files and results are processed and retained under the user's App Key account.

Risk: The App Key is a credential tied to the user's account and billing balance.

Mitigation: Keep the App Key out of chat, store it only in the local skill config file, and never forward links or messages that expose the key.

Risk: The skill can spend account credits when generating bid documents.

Mitigation: Check balance before submission and make clear that bid generation consumes credits while interpretation and compliance review have a balance gate.

Risk: Changing the API base through ZCM_BASE could send documents to an unexpected endpoint.

Mitigation: Review any ZCM_BASE override before use and prefer the documented 百炼®标书 domain.

Risk: Platform terms, risk labels, generated reports, and report artifacts are documented as Simplified Chinese outputs.

Mitigation: Tell multilingual users that operational labels and generated reports remain zh-CN even when surrounding explanations are translated.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-tech)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书 Open API base](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and status text with generated HTML, Word, and .docx file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and bid documents are written locally; cloud task results and generated .docx files are documented as expiring after about 7 days.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
