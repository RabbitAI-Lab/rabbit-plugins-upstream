## Description:

标书智能制作 helps agents analyze tender documents, generate editable bid documents, draft bid responses, and review bid files for rejection and compliance risks through the 百炼®标书 cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to process local tender and bid files: interpret solicitation requirements, generate editable .docx bid documents, and review submissions for rejection, compliance, similarity, and manual-check risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain business, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use the skill only after the user understands and accepts that upload; process only user-selected tender and bid files.

Risk: The App Key is a full account credential and could be exposed through chat logs or forwarded links.

Mitigation: Keep the App Key out of chat, store it only in local config.json, and do not forward service links that include credential-bearing parameters.

Risk: Bid generation uses account points, and uploaded files and generated outputs remain available under the App Key account for a limited retention period.

Mitigation: Review billing and retention expectations before generating bid documents, and use the account portal to manage retained results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-spark)
- [百炼®标书 Open API contract](artifact/references/api.md)
- [Execution and usage guide](artifact/references/usage.md)
- [Knowledge-base field guide](artifact/references/knowledge-fields.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown/text guidance plus generated .docx bid documents, HTML or Word reports, and JSON API results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-supplied App Key stored in local config.json; uploads selected tender and bid files to biaoshu.zhiliaobiaoxun.com; generated task results and .docx outputs are retained by the service for about 7 days.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
