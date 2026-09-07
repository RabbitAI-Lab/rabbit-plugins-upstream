## Description:

Write, review, or debug Dataify SERP, Web Unlocker, Builder, MCP, or SDK integration code using correct authentication, task lifecycle, retry, error, and output patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, review, and debug Dataify API integrations. It focuses on environment-based authentication, bounded retries, asynchronous task handling, error categorization, output validation, and production readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the package may perform live external API calls and local report generation beyond static integration review.

Mitigation: Install and run it only where live Dataify API usage is intended, and review workflow scope, cost, and generated outputs before execution.

Risk: The security evidence flags under-disclosed live scraping and business-intelligence workflows.

Mitigation: Review or remove the business_workflow scripts before installation when those workflows are not needed.

Risk: The security evidence flags insecure token handling and possible query-string polling exposure.

Mitigation: Keep DATAIFY_API_TOKEN environment-scoped, avoid running generated curl previews with untrusted input, and rotate or restrict any token that may have been used with query-string polling.

## Reference(s):

- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-api-best-practices)
- [Integration contract](references/integration-contract.md)
- [Authentication](references/authentication.md)
- [SERP API](references/serp-api.md)
- [Web Unlocker](references/web-unlocker.md)
- [Builder API](references/builder-api.md)
- [Task lifecycle](references/task-lifecycle.md)
- [Python production pattern](references/python.md)
- [JavaScript and TypeScript production pattern](references/javascript-typescript.md)
- [Error catalog](references/error-catalog.md)
- [Production checklist](references/production-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code snippets, shell commands, and structured integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audit findings, retry and recovery patterns, API-call examples, and token setup guidance without exposing API token values.]

## Skill Version(s):

1.1.1 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
