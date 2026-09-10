## Description:

自动视频工作流：抓新闻、生成口播文案、华声生成MG视频、导出并发布到B站，含Fabric封面文字注入与B站投稿表单填写。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lcz5221-svg](https://clawhub.ai/user/lcz5221-svg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to automate a Bilibili news video workflow: fetching news, generating narration copy, creating Huasheng MG video, injecting cover text, and filling the Bilibili submission form.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a logged-in Huasheng or Bilibili browser workflow and submit public content.

Mitigation: Use a dedicated browser profile or account and require explicit human confirmation before any Bilibili submission.

Risk: Generated narration and cover text may be inaccurate or unsuitable for publication.

Mitigation: Manually review generated copy, cover text, title, tags, and description before publishing.

Risk: Recurring browser automation or cron scheduling may run without clear rollback controls.

Mitigation: Scope scheduled runs carefully, log outputs, and disable automation until the operator has reviewed the planned workflow.

Risk: The fetch script writes local files under the skill directory for deduplication and output.

Mitigation: Run in a controlled workspace and review created database and output files before reusing or sharing them.

Risk: The news fetch script disables TLS certificate verification for external news requests.

Mitigation: Review fetched source data before use and restore certificate verification where operationally possible.

## Reference(s):

- [B站投稿表单填写明细](artifact/references/bilibili-form.md)
- [Fabric.js 封面文字注入方法](artifact/references/fabric-cover-text.md)
- [ClawHub skill page](https://clawhub.ai/lcz5221-svg/skills/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands, JavaScript snippets, and generated local text or JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create SQLite news records and output files under the skill directory when its scripts are run.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
