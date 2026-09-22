## Description:

Writes, rewrites, continues, and polishes WeChat Official Account long-form articles from a topic card, outline, or existing draft, using a configurable writing model or prompt-only agent workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content operators, and brand copywriters use this skill to generate article drafts, rewrite or continue existing copy, and tune WeChat Official Account prose for audience, tone, structure, references, and image placeholders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive drafts, topic cards, article configuration, referenced Markdown, and the writing API key may be sent to a configured model endpoint.

Mitigation: Use a dedicated low-quota WRITING_MODEL_API_KEY, configure only trusted HTTPS model endpoints, and avoid confidential reference documents unless their full text is approved for that provider.

Risk: The security summary notes a preset path bug that can read Markdown files outside the intended preset folders.

Mitigation: Review article.yaml and any draft package before running the skill, especially default_structure and default_closing_block.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-writing)
- [Writing script usage](references/usage.md)
- [WeChat long-form structure template](references/structure-template.md)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown articles, JSON prompt payloads, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates draft.md in an article directory; prompt mode returns system_prompt and user_prompt JSON without calling an LLM.]

## Skill Version(s):

1.0.26 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
