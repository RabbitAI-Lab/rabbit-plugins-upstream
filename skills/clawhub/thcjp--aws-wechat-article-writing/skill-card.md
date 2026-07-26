## Description: <br>
Helps agents draft, rewrite, continue, and polish long-form WeChat public account articles from topics, outlines, or existing drafts while applying local writing constraints and optional business references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and content operators use this skill to generate and iterate WeChat public account article drafts from a topic card, outline, or existing draft. It is intended for article-writing workflows that need account-level tone, reader, structure, publishing-intent, and reference-document constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Article drafts, topic cards, selected business reference documents, and the writing-model API key may be used with the configured LLM endpoint. <br>
Mitigation: Use a dedicated API key, configure only trusted base_url endpoints or an internal proxy, and choose the prompt-only path when content should not be sent to a third-party model. <br>
Risk: Generated drafts may reflect model errors or omit required account constraints if configuration is incomplete. <br>
Mitigation: Confirm article_category, target_reader, default_author, publish_method, and article-level constraints before writing, then review generated drafts before downstream review or publishing steps. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/aws-wechat-article-writing) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON-like status output, shell commands, and generated article draft files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces draft.md for writing-stage article drafts; review and final publishing outputs are outside this skill's stated boundary.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter lists 1.0.26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
