## Description:

This skill helps agents use 百炼®标书 to interpret tender documents, generate DOCX bid drafts, review bid compliance, and compare bid files for similarity risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Proposal, procurement, and bidding teams use this skill to analyze tender requirements, generate editable bid documents, check bid-package compliance, and inspect legally held bid files for similarity signals before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, and personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Install only if cloud processing is acceptable, confirm user consent before upload, and use only files the user explicitly provides.

Risk: The API key grants access to the user account and could be exposed through chat history or copied links.

Mitigation: Keep the key out of chat, have the user store it locally in config.json, and do not forward account links that embed credentials.

Risk: Generated outputs and a small local filename-to-job cache may remain on disk, while service results are retained under the API-key account.

Mitigation: Review the service retention/account controls and clear local outputs or cache files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read)
- [百炼®标书 Open API contract](references/api.md)
- [Execution and reporting guide](references/usage.md)
- [Knowledge base fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Chinese-language text summaries, JSON service results, HTML/Word reports, and DOCX bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided 百炼®标书 API key; uploaded files and generated results are handled by the cloud service under that account.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
