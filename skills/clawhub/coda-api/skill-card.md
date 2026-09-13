## Description:

Coda API integration with managed OAuth for managing docs, pages, tables, rows, and formulas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Coda through Maton-managed OAuth, list or inspect Coda resources, and perform user-approved create, update, or delete operations on docs, pages, tables, rows, formulas, and controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access data in the authorized Coda account.

Mitigation: Install only when the user is comfortable authorizing Maton for the intended Coda account, select the least necessary scopes when available, and revoke unused connections.

Risk: Write operations, permission changes, hosted functions, triggers, and destinations can change user data or automate future actions.

Mitigation: Treat each write, permission change, function deployment, trigger, and destination as a separate explicit approval.

Risk: External trigger destinations or local event handlers can expose data or execute reviewed events in unintended environments.

Mitigation: Keep destinations on Maton-hosted URLs unless the user explicitly trusts an external host, avoid watch --exec unless the handler script has been reviewed, and delete automations when finished.

## Reference(s):

- [Coda skill release page](https://clawhub.ai/byungkyu/skills/coda-api)
- [Maton homepage](https://maton.ai)
- [Coda API Documentation](https://coda.io/developers/apis/v1)
- [Coda API Postman Collection](https://www.postman.com/codaio/coda-workspace/collection/0vy7uxn/coda-api)
- [Coda API Python Library](https://codaio.readthedocs.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands, code snippets, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated Coda operations require a user-approved Maton connection; writes, permission changes, hosted functions, triggers, and destinations require separate approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
