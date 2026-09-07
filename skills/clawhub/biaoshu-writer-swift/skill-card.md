## Description:

标书自动撰写工具 helps agents use the 百炼®标书 cloud service to interpret tender files, generate .docx bid documents, review bid compliance, and compare bid documents for similarity risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to process authorized tender and bid documents through 百炼®标书 for tender interpretation, bid-document generation, compliance review, and similarity checks. It supports an agent workflow where users provide local files and the agent returns summaries, reports, generated bid documents, or similarity findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Use the skill only with documents the user is authorized to process, and confirm the user is comfortable with the cloud upload before submitting files.

Risk: The API key grants access to the provider account if exposed in chat or copied into shared logs.

Mitigation: Keep the API key in the local config file and do not ask the user to paste, repeat, or disclose it in conversation.

Risk: Generated results and task history may remain available in the provider account for a limited time.

Mitigation: Tell users that outputs may persist with the provider account and direct them to manage history through the provider service when needed.

Risk: Similarity checks provide risk signals and should not be treated as a legal finding of collusion or bid validity.

Mitigation: Present duplicate-check results as internal review signals and recommend human or legal review for submission decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-swift)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)
- [知识库字段说明](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON results, HTML or Word reports, .docx bid documents, and short-lived download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include absolute local report paths, generated .docx bid files, cloud task status, similarity findings, and account word-balance notices.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
