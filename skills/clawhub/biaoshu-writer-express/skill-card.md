## Description:

投标文件自动生成工具，凭 App Key 调用开放 API 从招标文件到成品标书全自动：解读招标文件抽取评分标准与废标红线、一键生成成品投标文件(.docx)、技术标与商务标撰写排版、生成后合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid and proposal teams use this skill to analyze tender documents, identify scoring criteria and disqualification risks, generate editable bid documents, and review completed bids for compliance after confirming cloud upload, App Key, and billing requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal information and are uploaded to the 百炼标书 cloud service under the user's App Key account.

Mitigation: Install and use only when the user is comfortable with that upload, confirm consent before file processing, and disclose that cloud results may remain available through the account for a limited period.

Risk: The App Key grants access to the user's account and could be exposed if pasted into chat or shared through credential-bearing links.

Mitigation: Keep the App Key in the local config file, never ask the user to paste it into chat, and do not forward links containing App Key or bind_key parameters.

Risk: A custom API base URL can redirect uploads to a different endpoint if ZCM_BASE is set.

Mitigation: Leave ZCM_BASE unset unless the user deliberately trusts the alternate endpoint.

Risk: Bid document generation consumes account points and long-running jobs could be submitted more than once.

Mitigation: Precheck balance, make billing visible before generation, and use idempotency or job continuation for retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-express)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [Usage guide](references/usage.md)
- [API contract](references/api.md)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Agent-facing text and Markdown, plus generated DOCX bid documents and HTML or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local tender or bid file paths and a local App Key configuration; generated files are written under the configured output directory.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
