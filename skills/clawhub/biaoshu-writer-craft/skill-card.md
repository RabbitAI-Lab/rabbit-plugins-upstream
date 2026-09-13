## Description:

Uploads tender and bid documents to the 百炼标书 cloud service to interpret tender requirements, generate bid-document .docx drafts, review compliance risks, and compare bid files for similarity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers preparing bid submissions use this skill to analyze tender files, create draft bid documents, check compliance risks, and identify similarity or duplicate-risk signals before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain sensitive business, pricing, and personal data and are uploaded to the 百炼标书 cloud service for processing.

Mitigation: Use the skill only after confirming the user understands and accepts cloud processing for the provided files.

Risk: The linked account's word balance may be spent when generating bid documents, reviewing compliance, or checking duplicate-risk signals.

Mitigation: Confirm paid operations and communicate that final usage is governed by the platform's settlement.

Risk: API keys, phone numbers, SMS codes, and account links could expose credentials if shared in chat.

Mitigation: Keep credentials out of conversation history and have the user configure the API key locally.

Risk: Generated output paths and persisted project metadata may reveal procurement activity on the local machine.

Mitigation: Review output locations and remove local project metadata when the user does not want it retained.

Risk: Security evidence reports privacy, credential, file-writing, and assistant-control concerns that need review before installation.

Mitigation: Review the skill instructions and security guidance before deployment, and run it only within the declared file, network, and credential boundaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-craft)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API overview](references/api.md)
- [Authentication, tasks, and word balance API](references/api-auth.md)
- [Tender interpretation and bid-document generation API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid duplicate-check API](references/api-duplicate.md)
- [Knowledge-base fields](references/knowledge-fields.md)
- [Agent usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Agent-facing guidance, status updates, JSON summaries, local HTML or Word reports, generated .docx bid files, and short-lived download links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-managed API key, uploads user-provided tender or bid files to the 百炼标书 cloud service, and may spend the linked account's word balance for paid operations.]

## Skill Version(s):

3.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
