## Description:

上传招标或投标文件后，辅助完成招标文件解读、投标文件生成、标书合规审查和 2-3 份投标文件相似风险检查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to process tender and bid documents through the 百炼®标书 cloud service, produce editable bid documents, and review compliance or similarity risks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Use the skill only after confirming the document owner consents to cloud processing and account-level retention.

Risk: The skill can query account knowledge-base data under the configured API-key account.

Mitigation: Use an API key scoped to the intended account and review which company profile, qualification, performance, and financial categories are available before deployment.

Risk: Local credential and project metadata may remain in the skill-local config file and ~/.zcm/projects.json.

Mitigation: Protect the local workspace, avoid sharing config files, and remove local caches when the skill is no longer needed.

Risk: The security verdict is suspicious because declared write paths do not fully describe the local project cache behavior.

Mitigation: Review the permission boundary and local cache behavior before enabling the skill in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-spark)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown or text summaries, JSON result summaries, HTML/Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts may include local report files and short-lived cloud download links for bid documents.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
