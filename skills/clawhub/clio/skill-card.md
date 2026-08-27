## Description:

Clio API integration with managed OAuth for reading and modifying Clio Manage legal practice data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Clio Manage matters, contacts, activities, tasks, documents, calendar entries, users, and bills while keeping authentication in the Maton gateway. It supports read/list workflows by default and write workflows only after explicit user approval with specific resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change sensitive legal practice data, including matters, contacts, activities, tasks, documents, calendar entries, time entries, and billing.

Mitigation: Default to read/list calls, verify resource identifiers, describe the intended effect, and require explicit user confirmation before any create, update, or delete operation.

Risk: Clio credentials and provider-issued tokens could expose privileged client data if printed, logged, exported, or persisted outside the gateway flow.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the gateway or operating system credential store, never display or persist tokens, and revoke unused connections promptly.

Risk: The generic API transport can forward Clio paths beyond the endpoints reviewed by the skill.

Mitigation: Use only the documented Clio endpoints and methods unless the user asks for a specific additional endpoint and explicitly approves the exact call.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/clio)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Clio API documentation](https://docs.developers.clio.com/api-reference/)
- [Clio fields guide](https://docs.developers.clio.com/api-docs/clio-manage/fields/)
- [Clio rate limits](https://docs.developers.clio.com/api-docs/clio-manage/rate-limits/)
- [Clio permissions](https://docs.developers.clio.com/api-docs/permissions/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and API-call guidance; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
