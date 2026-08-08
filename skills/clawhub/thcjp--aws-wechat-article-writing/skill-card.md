## Description: <br>
Drafts long-form WeChat public-account articles from topic cards, outlines, or spoken topics, supporting rewriting, continuation, polishing, model selection, business-reference injection, image placeholders, and draft publishing intent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and content teams use this skill to guide an agent through generating and revising WeChat public-account article drafts while enforcing account writing constraints, reference handling, and draft publication settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Article content, configuration context, and user-supplied reference documents may be sent to a user-configured LLM endpoint. <br>
Mitigation: Use a dedicated API key, verify the configured model endpoint is trusted, and avoid supplying sensitive business documents unless their contents may be sent to that endpoint. <br>
Risk: Drafting workflows can create publication-ready material before human review. <br>
Mitigation: Keep publication settings on draft unless explicit publication is intended, and review generated drafts before any downstream publishing step. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-wechat-article-writing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces article drafts and related writing workflow guidance; generated drafts may include image placeholders and references to local source materials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
