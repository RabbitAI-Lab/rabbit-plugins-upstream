## Description:

通过官方 getnote CLI 连接得到大脑，完成浏览器授权、连接诊断、CLI 升级，以及保存、查询、搜索和管理真实笔记。用户要按录音台或录音卡来源找笔记、保存链接/图片、上传文件到知识库、查询文件限制、读取标记/发芽报告/时间线、整理知识库/文件夹、订阅博主、管理标签，或明确要求登录、诊断或升级时使用；不会自行安装或更新 Skill。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT-0

## Use Case:

得到大脑用户可用自然语言请求连接诊断、搜索和管理笔记、保存内容或整理知识库；Agent 通过官方 CLI 完成获授权的读取与修改，并返回真实操作结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection and update steps can change five additional agent skills without clearly scoped approval.

Mitigation: Review those skills, their destination files, and recovery options before setup or updates; use a verified login-only workflow when only account access is needed.

Risk: Browser authorization enables access to the user's notes and requested changes.

Mitigation: Authorize only through the browser after reviewing the requested access, and use the login-only workflow when no note operation is needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iswalle/skills/getnote)
- [Connection, diagnosis, and updates](artifact/references/auth.md)
- [Notes and note operations](artifact/references/note.md)
- [Knowledge bases and files](artifact/references/kb.md)
- [Search](artifact/references/search.md)
- [Tags](artifact/references/tag.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports real titles, identifiers, links, and operation status returned by the authorized CLI.]

## Skill Version(s):

2.4.0 (source: frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
