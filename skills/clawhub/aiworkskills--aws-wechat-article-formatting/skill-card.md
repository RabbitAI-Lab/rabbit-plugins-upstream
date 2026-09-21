## Description:

Formats WeChat public-account articles by converting local Markdown drafts into WeChat-compatible inline-styled HTML with selectable templates, color schemes, components, previews, and font options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and publishing teams use this skill to turn trusted local Markdown article drafts into WeChat-ready HTML and preview or choose formatting themes before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted Markdown, article configuration, themes, or component presets can produce active HTML in generated output.

Mitigation: Use the skill only with trusted local drafts and trusted presets, and review generated HTML before pasting or opening previews.

Risk: Theme paths are not tightly contained.

Mitigation: Keep custom presets in controlled project or user preset directories and avoid presets from untrusted contributors until path containment is added.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-formatting)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [Project homepage](https://aiworkskills.cn)
- [WeChat HTML constraints](references/wechat-html-constraints.md)
- [Formatting presets README](references/presets/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and shell commands that produce local HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python 3; reads article Markdown, article configuration, optional closing text, and trusted formatting presets; writes article.html or preview HTML.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
