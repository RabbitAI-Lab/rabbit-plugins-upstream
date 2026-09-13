## Description:

上传招标/投标文件，AI 一站式完成智能解读（废标红线/评分标准/控标洞察）、成品投标文件(.docx)生成、标书审查（分级风险+雷同检测）和标书查重（2-3份投标文件相似/雷同风险检查）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to interpret tender files, generate finished bid documents, review bid compliance, and compare bid files for similarity or duplicate-risk signals. It supports Chinese tender and bid workflows that require uploaded local documents, user confirmation before sensitive actions, and paid account word balance for non-free operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential commercial, pricing, or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use the skill only with documents the user is willing and authorized to upload, confirm consent before upload, and review the skill before installing.

Risk: API keys, phone numbers, SMS codes, or parameterized account links could expose account access.

Mitigation: Do not send credentials or SMS codes in chat; have the user store the API key locally in the skill config file and avoid forwarding links that contain keys or bind parameters.

Risk: The skill may write or upload beyond stated boundaries, may overwrite arbitrary output paths, and may create local project metadata containing tender filenames and job or project IDs.

Mitigation: Prefer the default generated-output directory or a vetted path, avoid overwriting existing files, and inform users that local project metadata may be created.

Risk: Paid operations can consume the account word balance, while generation estimates may differ from final billing.

Mitigation: Require user confirmation before paid generation, review, or duplicate-check operations and present estimated consumption as approximate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-ace)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API dispatcher](references/api.md)
- [Authentication, jobs, and word balance API](references/api-auth.md)
- [Tender interpretation and bid document generation API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid duplicate check API](references/api-duplicate.md)
- [Knowledge base fields](references/knowledge-fields.md)
- [Execution and usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Natural-language guidance and summaries, JSON results, HTML or Word reports, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses short-lived download links for generated bid documents by default; local reports and optional local downloads are written under configured output paths.]

## Skill Version(s):

3.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
