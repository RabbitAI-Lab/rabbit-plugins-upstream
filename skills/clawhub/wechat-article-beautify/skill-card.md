## Description:

Formats finished Markdown, plain text, or HTML articles with one or more of seven WeChat Official Account templates and produces paste-ready, inline-styled HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

Apache 2.0

## Use Case:

Writers and editors use this skill to reformat finished articles for the WeChat Official Account editor, choosing a matching template or comparing several layouts. It preserves the article's meaning while changing its presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser preview does not sanitize article HTML.

Mitigation: Preview only trusted article HTML.

Risk: Generated files can replace earlier versions in the output location.

Mitigation: Use a dedicated output directory for generated files.

Risk: Formatted content could be published with unintended changes or unsuitable material.

Mitigation: Review the generated article before manually publishing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/weikion/skills/wechat-article-beautify)
- [Server-resolved source repository](https://github.com/weikion/wechat-article-beautify)
- [Template guide](references/template-guide.md)

## Skill Output:

**Output Type(s):** [HTML, Files]

**Output Format:** [Inline-styled HTML article files and an optional HTML comparison page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses seven layout templates and preserves article meaning while changing presentation.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
