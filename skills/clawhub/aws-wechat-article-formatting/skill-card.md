## Description:

Converts Markdown articles into WeChat-compatible HTML with inline styles, selectable themes, typography controls, and reusable layout components for public-account publishing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, editors, independent authors, and publishing teams use this skill to format Markdown drafts as WeChat public-account HTML. Agents use it to choose a theme, run the local formatter, and produce article.html for review or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML can preserve attacker-controlled markup or unsafe attributes when the input article is untrusted.

Mitigation: Run the skill only on trusted Markdown and trusted theme/component files; sanitize generated HTML before previewing, publishing, or hosting content from untrusted sources.

Risk: The formatter has local filesystem and shell permissions and writes article.html.

Mitigation: Review the target article path and output path before execution, and run the formatter in a controlled workspace with only the necessary project files available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-formatting)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [Theme preset documentation](artifact/references/presets/README.md)
- [WeChat HTML constraints](artifact/references/wechat-html-constraints.md)
- [Component presets](artifact/references/components/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated inline-style HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with python3, reads article and theme/component configuration files, and writes article.html.]

## Skill Version(s):

1.0.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
