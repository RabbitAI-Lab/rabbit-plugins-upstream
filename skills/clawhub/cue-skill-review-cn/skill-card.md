## Description:

为待安装的 skill 起草一份五面体检报告，逐条附上带检索日期的原文来源，并把安装判断留给人。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

适合在安装他人的 skill 前，供开发者或使用者整理声明、前置条件、面文承诺、样例运行情况以及许可和出处方面的证据。报告用于初筛和对照，不替用户决定是否安装。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unreviewed or moving installed copy may differ from the version assessed.

Mitigation: Install a reviewed copy or pin the installer and repository revision.

Risk: Writing a report to an existing path can overwrite that file.

Mitigation: Choose a separate report output path.

Risk: The optional parsing service may receive material submitted for review.

Mitigation: Enable the parser only for material you are comfortable sharing with that service.

Risk: A passing report check can be mistaken for confirmation that the reviewed skill is secure.

Mitigation: Treat the check as a structural check; it does not establish the reviewed skill's security.

## Reference(s):

- [Omni Reader parsing configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Markdown, Source index]

**Output Format:** [Five-section Markdown review report with source anchors and retrieval dates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft review; installation decisions remain with the user.]

## Skill Version(s):

0.1.3 (source: SKILL.md frontmatter, CHANGELOG.md 2026-10-29, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
