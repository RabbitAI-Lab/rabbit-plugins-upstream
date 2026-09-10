## Description:

Pipedrive API integration with managed OAuth for managing deals, persons, organizations, activities, and pipelines through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect and manage Pipedrive CRM records through Maton OAuth, starting with read and list operations and requiring confirmation before new connections or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted Maton installation sources or overly broad Pipedrive scopes can expose CRM data.

Mitigation: Confirm Maton and its package distribution channels before installing, prefer OAuth, and grant the narrowest Pipedrive scopes available.

Risk: Create, update, or delete requests can change Pipedrive CRM records.

Mitigation: Default to read and list calls, then review the target resource, payload, and intended effect before approving any write operation.

Risk: Long-lived API keys or surfaced tokens can leak credentials.

Mitigation: Prefer OAuth-backed credential storage and avoid printing, logging, persisting, or passing credentials on command lines.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
- [Pipedrive Deals API](https://developers.pipedrive.com/docs/api/v1/Deals)
- [Pipedrive Persons API](https://developers.pipedrive.com/docs/api/v1/Persons)
- [Pipedrive Organizations API](https://developers.pipedrive.com/docs/api/v1/Organizations)
- [Pipedrive Activities API](https://developers.pipedrive.com/docs/api/v1/Activities)
- [Pipedrive Pipelines API](https://developers.pipedrive.com/docs/api/v1/Pipelines)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance defaults to read and list calls; new connections and write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
