## Description:

Manages a FastAPI blog system through documented REST API workflows for articles, tags, users, comments, messages, moods, file uploads, admin actions, frontend pages, and health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage a configured FastAPI blog service through its published API, including content publishing, updates, file uploads, and administrative deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, upload, and delete live blog content, including hard deletes and admin bulk deletion.

Mitigation: Require explicit human confirmation before uploads, hard deletes, file deletes, or admin bulk deletion.

Risk: The skill operates against a caller-provided blog API base URL.

Mitigation: Confirm the base URL is trusted before running commands against the target service.

Risk: Admin token use can expand the impact of deletion workflows.

Mitigation: Change default admin credentials and avoid giving admin tokens unless the requested operation requires them.

## Reference(s):

- [API Reference](references/api-reference.md)
- [Test Variables](templates/test-vars.json)
- [ClawHub Skill Page](https://clawhub.ai/yangaiwu/skills/blog-mini-kit-liufei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [JSON by default, with optional Markdown summaries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a trusted BLOG_MINI_KIT_LIUFEI_BASE_URL; some operations can mutate or delete live blog content.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
