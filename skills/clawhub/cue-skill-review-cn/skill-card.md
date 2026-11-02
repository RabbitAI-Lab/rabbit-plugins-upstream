## Description:

帮助用户在安装前审阅 skill 的声明、前置条件、面文承诺、样例、许可与出处，并生成逐条关联原文的体检报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和其他 skill 使用者可在安装前审阅本地 skill，或经解析通道取回的远端正文，并生成带原文锚点与检索日期的体检报告。报告用于初筛和同题对照；是否安装由用户决定。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A report may contain incorrect or misleading guidance; passing automated checks does not verify its claims.

Mitigation: Treat the report as a draft, verify each finding against its cited source, and make the installation decision yourself.

Risk: Choosing an existing report path may overwrite important files.

Mitigation: Choose and confirm a report path that will not overwrite important files.

Risk: Remote retrieval may involve additional data handling and service costs.

Mitigation: Review the separate parser's data handling and confirm costs before enabling remote retrieval.

Risk: An unpinned install command may not install the reviewed fixed copy.

Mitigation: Prefer installing a reviewed fixed copy over using an unpinned command.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-skill-review-cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review report with source-anchored findings and a source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only review; reports are drafts and leave installation decisions to the user.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
