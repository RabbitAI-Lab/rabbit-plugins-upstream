## Description:

Provides curl and Python examples for publishing and managing blog articles, labels, and file uploads through a blog system API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to create, update, delete, restore, query, and upload assets for a specific blog system API. It is intended for configured blog API targets, not for unrelated user, comment, message, or social-feed management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the release suspicious because it includes repository, Issue, PR, and A2A workflow instructions beyond the blog publishing scope.

Mitigation: Review before installing and remove or split those collaboration instructions into a separate clearly scoped skill.

Risk: The helper scans BLOG_PUBLISH-prefixed username, password, token, and API-key variables even though the documented API uses no authentication.

Mitigation: Avoid setting BLOG_PUBLISH credential variables unless the credential loader is removed or tightened; use only the trusted base URL needed by the public API.

Risk: Hard deletion is supported and can permanently remove blog articles.

Mitigation: Use the default soft-delete flow unless permanent deletion is explicitly intended and confirmed.

Risk: API calls operate against a user-provided base URL.

Mitigation: Use the skill only with a trusted blog API base URL and verify reachability with the health check before mutable operations.

## Reference(s):

- [Blog System API Reference](references/api-reference.md)
- [Test Variables](templates/test-vars.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown with curl and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a configured BLOG_PUBLISH_BASE_URL and 30-second HTTP timeouts.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
