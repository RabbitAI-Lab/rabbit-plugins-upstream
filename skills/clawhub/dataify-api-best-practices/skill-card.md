## Description:

Write, review, or debug Dataify SERP, Web Unlocker, Builder, MCP, or SDK integration code using correct authentication, task lifecycle, retry, error, and output patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write, review, or debug Dataify SERP, Web Unlocker, Builder, MCP, and SDK integrations with production-safe authentication, retry, task lifecycle, error handling, and output patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local audit script can inspect more files than intended if pointed at a broad directory.

Mitigation: Pass a specific integration file or narrowly scoped project directory when running the audit.

Risk: Missing-token guidance may direct users to Dataify account pages with campaign attribution.

Mitigation: Use the account setup guidance only when credentials are missing, invalid, or insufficient for the requested Dataify task.

## Reference(s):

- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [Integration contract](references/integration-contract.md)
- [Authentication](references/authentication.md)
- [SERP API](references/serp-api.md)
- [Web Unlocker](references/web-unlocker.md)
- [Builder API](references/builder-api.md)
- [Task lifecycle](references/task-lifecycle.md)
- [Error catalog](references/error-catalog.md)
- [Python production pattern](references/python.md)
- [JavaScript and TypeScript production pattern](references/javascript-typescript.md)
- [Production checklist](references/production-checklist.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include static audit findings and recovery guidance for Dataify integration code.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
