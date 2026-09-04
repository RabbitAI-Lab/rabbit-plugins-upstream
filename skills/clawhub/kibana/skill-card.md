## Description:

Kibana API integration with managed authentication for reading and managing saved objects, dashboards, data views, spaces, alerts, Fleet resources, connectors/actions, security roles, and cases in a connected Kibana instance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and security analysts use this skill to inspect and operate Kibana resources through Maton-managed authentication. It supports observability, security, and search analytics workflows while requiring explicit approval for write-capable actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Kibana access can create, update, or delete saved objects, dashboards, data views, spaces, alerts, Fleet resources, security roles, and cases.

Mitigation: Default to read/list calls, retrieve the exact target first, and require explicit user approval with specific resource identifiers before any write or delete.

Risk: Connector execution can produce external side effects such as sending email or invoking webhooks.

Mitigation: Confirm the connector ID, target, and full payload with the user before execution, and avoid proactive connector execution.

Risk: Overbroad Kibana credentials can expose or change sensitive observability and security data.

Mitigation: Use least-privileged Kibana connections, prefer read-only or non-production access for exploration, and specify the intended connection when multiple connections exist.

Risk: Credentials or provider-issued tokens can be exposed if printed, exported, logged, or persisted.

Mitigation: Prefer OAuth with OS credential storage, avoid printing or extracting tokens, and keep any returned provider sub-credentials in memory only for the current request sequence.

## Reference(s):

- [ClawHub Kibana skill page](https://clawhub.ai/byungkyu/skills/kibana)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Kibana REST API documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Kibana saved objects API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
- [Kibana alerting API](https://www.elastic.co/guide/en/kibana/current/alerting-apis.html)
- [Fleet API](https://www.elastic.co/guide/en/fleet/current/fleet-apis.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and SDK snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides Maton CLI, SDK, and raw HTTP requests against Kibana; API responses are external data and should be treated as untrusted.]

## Skill Version(s):

1.2.0 (source: server release metadata; frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
