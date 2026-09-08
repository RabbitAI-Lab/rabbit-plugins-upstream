## Description:

Formats WeChat public-account articles by converting local Markdown drafts into paste-ready inline-styled HTML with selectable themes, color schemes, font sizes, and layout components.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, WeChat public-account editors, and publishing teams use this skill to select formatting themes and convert article Markdown plus local article configuration into WeChat-compatible HTML for review or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML from untrusted Markdown, themes, or component presets could contain unsafe or misleading content if previewed, hosted, or pasted without review.

Mitigation: Use trusted Markdown and preset sources, review generated article.html before publishing, and sanitize generated HTML before hosting or previewing untrusted input.

Risk: Local custom formatting presets can change the final article layout and embedded HTML output.

Mitigation: Keep project and user-level formatting presets from trusted sources and inspect custom YAML before using it in a publishing workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-formatting)
- [Publisher homepage](https://aiworkskills.cn)
- [WeChat HTML constraints](references/wechat-html-constraints.md)
- [Formatting preset reference](references/presets/README.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated WeChat-compatible HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with python3; writes article.html from trusted Markdown, article metadata, optional closing text, and formatting presets.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
