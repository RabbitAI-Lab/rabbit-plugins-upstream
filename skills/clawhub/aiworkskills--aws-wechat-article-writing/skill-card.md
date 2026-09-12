## Description:

从话题、提纲或已有稿件生成、改写、续写和润色微信公众号长文，并可通过配置的写作模型或提示词 JSON 支持 Agent 代写。

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, WeChat operators, and brand copywriters use this skill to draft, rewrite, continue, and polish long-form WeChat public-account articles from topic cards, outlines, existing drafts, and selected business reference Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article drafts, selected reference Markdown, and WRITING_MODEL_API_KEY may be sent to the configured model endpoint.

Mitigation: Use a dedicated low-privilege provider key, verify config.yaml writing_model.base_url before each run, and avoid sensitive reference documents.

Risk: The security summary reports a preset-loading path traversal risk.

Mitigation: Do not run the skill on draft directories or preset selections from untrusted sources until preset path handling is fixed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-writing)
- [Writing script usage](artifact/references/usage.md)
- [WeChat long-form structure template](artifact/references/structure-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown article drafts, prompt JSON, and concise setup or execution guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write draft.md, emit prompt JSON without calling an LLM, and strip source-path citations for downstream review.]

## Skill Version(s):

1.0.26 (source: ClawHub server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
