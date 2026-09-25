## Description:

magic-api-generate helps agents guide developers through magic-api setup, magic-script syntax, database operations, RESTful interface patterns, and related implementation caveats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[webx32](https://clawhub.ai/user/webx32)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when building or reviewing magic-api integrations, especially Spring Boot configuration, dynamic HTTP interface generation, database access, CRUD examples, authentication examples, and magic-script usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security-sensitive examples may be unsafe if copied directly, including MD5 or plain password handling, weak token handling, and returning raw user objects.

Mitigation: Treat the examples as reference patterns only; replace them with modern password hashing, random session tokens, least-privilege response payloads, and project-specific authentication and authorization checks.

Risk: Generated or adapted endpoints for upload, export, delete, cleanup, or outbound HTTP calls can expose data or write unsafe files without additional controls.

Mitigation: Add authorization, input validation, upload hardening, destination allowlists, and review of all outbound data before using these patterns in deployed services.

## Reference(s):

- [Magic API Documentation](https://www.ssssssss.org/magic-api/)
- [Magic API GitHub Repository](https://github.com/ssssssss-team/magic-api)
- [Magic API Gitee Repository](https://gitee.com/ssssssss-team/magic-api)
- [Magic API Online Demo](https://magic-api.ssssssss.org.cn)
- [magic-script syntax reference](references/syntax.md)
- [Database operation reference](references/database.md)
- [Business scenario examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline XML, YAML, JavaScript, SQL, and shell-style snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require review before production use because the release security guidance identifies unsafe security-sensitive patterns.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
