## Description:

帮助用户上传招标/投标文件到百炼®标书云端，完成招标解读、投标文件生成、标书审查和投标文件相似/雷同风险检查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to interpret tender requirements, generate draft bid documents, review bid compliance, and compare 2-3 bid files for similarity risks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential business, pricing, or personal information and are uploaded to a third-party service.

Mitigation: Install and use only after confirming the user is comfortable sending those files to the stated service under their API-key account.

Risk: The workflow involves API keys, phone registration, and SMS codes.

Mitigation: Do not ask users to share API keys, SMS codes, phone numbers, or registration details in chat; users should manage credentials locally.

Risk: Local output paths are not sufficiently bounded in the security evidence.

Mitigation: Use the default output directory or explicitly approved paths until the publisher constrains writes to an approved directory.

Risk: The release includes overreaching response rules and was marked suspicious by the authoritative ClawHub security scan.

Mitigation: Review the skill and scan result before deployment, and treat generated bid guidance or reports as materials requiring human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-guard)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API overview](references/api.md)
- [Authentication, jobs, and entitlement API](references/api-auth.md)
- [Bid generation workflow API](references/api-bid-workflow.md)
- [Bid compliance API](references/api-compliance.md)
- [Bid duplicate checking API](references/api-duplicate.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON summaries, HTML or Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided API key; tender and bid files are processed by the third-party service, and some operations consume account word balance.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
