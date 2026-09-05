## Description:

Uploads tender and bid documents to the 百炼®标书 cloud service to interpret tender requirements, generate editable bid documents, review bid compliance, and compare 2-3 bid files for similarity risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams, procurement consultants, and proposal writers use this skill to analyze tender files, draft technical bid documents, produce compliance review reports, and identify similarity-risk signals before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive tender and bid files are uploaded to a third-party cloud service and may include commercial, pricing, or personal information.

Mitigation: Use only with user consent, lawful possession of the files, and acceptance that processing occurs under the user's 百炼®标书 API key.

Risk: Long-running progress monitoring can make excessive authenticated API requests.

Mitigation: Use a slower polling interval for long jobs or require the publisher to raise the default before deployment.

Risk: Local config.json stores credentials, and the local ZCM cache may contain project-name or job metadata.

Mitigation: Protect config.json with restrictive permissions, exclude it from published packages, and clear local cache data when project metadata is sensitive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-tech)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell-command plans, JSON summaries, HTML or Word reports, and generated .docx bid files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents consume account quota; uploaded files and task outputs are processed and retained by the 百炼®标书 cloud service under the user's API key.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
