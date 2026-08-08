## Description:

Connect to external services through Maton-managed API routes for user-specified apps, accounts, and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and operate user-authorized third-party services through Maton-managed API routes. It is intended for tasks where the user has named the target app, account, and action, with read-only checks before any state-changing request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized connections can expose business data across many third-party services.

Mitigation: Install only when the publisher and Maton account are trusted, and use least-privilege OAuth scopes for each connected service.

Risk: Write, automation, or trigger actions can change external systems or send data continuously.

Mitigation: Confirm every non-GET request or automation step with the exact connection, endpoint, request body, destination URL, and expected outcome before execution.

Risk: API keys, provider tokens, and webhook destinations can leak credentials or data if copied into logs, prompts, or untrusted endpoints.

Mitigation: Keep credentials secret, send them only to trusted Maton API routes, avoid broad trigger rules, and approve only destination URLs controlled by the user.

## Reference(s):

- [API Gateway ClawHub skill page](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, API paths, request examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton account setup, and user-controlled credentials for authorized services.]

## Skill Version(s):

1.0.141 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
