## Description:

通过官方 getnote CLI 连接得到大脑，完成浏览器授权、连接诊断、CLI 升级，以及保存、查询、搜索和管理真实笔记。用户要按录音台或录音卡来源找笔记、保存链接/图片、上传文件到知识库、查询文件限制、读取标记/发芽报告/时间线、整理知识库/文件夹、订阅博主、管理标签，或明确要求登录、诊断或升级时使用；不会自行安装或更新 Skill。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT-0

## Use Case:

面向使用得到大脑的用户，帮助代理通过官方 getnote CLI 完成授权连接和诊断，并按用户请求保存、查找、阅读和管理笔记、知识库及标签。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious because connection setup is reported to synchronize other Skills; the scan is incomplete because three local references could not be resolved.

Mitigation: Before installing, review the reported synchronization and decide whether to accept the persistent changes; treat the scan as incomplete.

Risk: Requested commands can modify, share, or delete remote notes and knowledge-base content.

Mitigation: Follow the skill's confirmation rules for deletion, replacement, public sharing, and bulk removal, and verify write results by reading them back where specified.

## Reference(s):

- [连接、诊断与升级](artifact/references/auth.md)
- [笔记操作](artifact/references/note.md)
- [搜索](artifact/references/search.md)
- [知识库与文件](artifact/references/kb.md)
- [标签](artifact/references/tag.md)
- [官方 getnote CLI（npm）](https://www.npmjs.com/package/@getnote/cli)
- [ClawHub 技能发布页](https://clawhub.ai/iswalle/skills/getnote)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown responses with confirmed note titles, summaries, links, and troubleshooting steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Request-dependent; reports confirmed results and actual identifiers, links, errors, and next steps.]

## Skill Version(s):

2.5.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
