## Description:

Route requests to user-connected third-party apps through Maton and manage approved hosted automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use it to read or update data in apps a user has connected, and to administer Maton functions and event triggers after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests pass through Maton and the connected service, so connected account data is handled by both providers.

Mitigation: Connect only the accounts and permissions needed for the task.

Risk: Writes, uploads, and ongoing automations can affect external systems or forward event data.

Mitigation: Confirm the exact connection, target, recipients, and file before approval; approve ongoing automation deliberately and remove it when finished.

Risk: Some SharePoint downloads use a provider pre-signed URL outside the gateway.

Mitigation: Use only the requested file's HTTPS download URL and do not forward gateway authorization.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API responses, JSON, Shell commands, Code, Guidance]

**Output Format:** [JSON responses, shell command examples, code, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
