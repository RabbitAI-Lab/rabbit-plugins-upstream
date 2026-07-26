## Description: <br>
Generates, rewrites, and polishes long-form WeChat public account article drafts from a topic card or spoken topic using configured article style constraints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content teams, creators, and developers use this skill to produce an initial WeChat long-form article draft, then rewrite or polish that draft according to account-level and article-level style settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Article topics, drafts, article.yaml, topic-card.md, and merged writing configuration may be sent to the user-configured LLM endpoint. <br>
Mitigation: Configure only trusted endpoints and review article inputs before use, especially when they contain confidential or unpublished material. <br>
Risk: The API key setup example is inconsistent with the documented WRITING_MODEL_API_KEY setting. <br>
Mitigation: Use a dedicated API key stored as WRITING_MODEL_API_KEY in aws.env and correct any API_KEY example before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-wechat-article-writing-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown draft files with concise status and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces draft.md for a selected article directory and may provide rewrite or polish output using the same writing constraints.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
