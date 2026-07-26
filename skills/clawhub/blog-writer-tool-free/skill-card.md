## Description: <br>
Blog Writer Tool Free helps agents create, list, update, delete, draft, and publish Markdown blog posts through API-key-protected REST endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, independent developers, and agent developers use this skill to manage a personal or local blog workflow, including Markdown authoring, tag organization, draft review, publishing, and post deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish or delete real blog content when used with a capable API key. <br>
Mitigation: Prefer a limited API key, create drafts by default, confirm exact slugs before deletion, and keep backups or soft-delete recovery available. <br>
Risk: API key exposure could allow unauthorized changes to blog content. <br>
Mitigation: Store API keys outside public code, pass them through protected configuration, and rotate any leaked key promptly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/blog-writer-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, REST API examples, and optional JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, modify, publish, or delete blog content through API-key-authenticated endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
