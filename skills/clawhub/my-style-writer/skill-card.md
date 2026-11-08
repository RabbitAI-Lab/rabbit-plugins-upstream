## Description:

Analyzes selected Markdown articles to build a writing-style profile, drafts articles in that style, and formats them with an HTML template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

Apache License 2.0

## Use Case:

External writers and publishers can use the skill to analyze their Markdown archive, create a reusable style profile, draft new articles in their established voice, and produce WeChat-ready HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis runs can overwrite generated report files.

Mitigation: Use a dedicated folder containing only articles intended for analysis, confirm the configured paths, and keep copies of generated reports you need to retain.

Risk: Confidential writing may be handled by the host AI service when supplied for analysis or drafting.

Mitigation: Check the host AI service's data handling before using confidential articles.

## Reference(s):

- [GitHub source repository](https://github.com/weikion/my-style-writer)
- [ClawHub release page](https://clawhub.ai/weikion/skills/my-style-writer)
- [Writing style profile reference](references/style-profile.md)
- [Default WeChat HTML template](templates/wechat-template.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, Files]

**Output Format:** [Markdown style profiles and article drafts; HTML formatted articles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Style profiles and generated article files are saved locally.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
