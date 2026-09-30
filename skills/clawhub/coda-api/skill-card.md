## Description:

Connects an agent to the Coda API through Maton to read and manage docs, pages, tables, rows, formulas, and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Coda can ask an agent to find, read, create, or update documents and structured content through their authorized connection. Optional hosted functions and triggers support approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad account access or unintended document changes through a Coda connection.

Mitigation: Review OAuth scopes, use only the access needed, and confirm each connection and write before proceeding.

Risk: Sharing or permission changes can expose Coda content beyond the intended audience.

Mitigation: Confirm the exact document, recipient, and resulting access before changing permissions.

Risk: Hosted functions, triggers, or destination URLs can create recurring actions or forward event data.

Mitigation: Approve automations and destinations separately; check what data flows, where it goes, and how long it remains active.

Risk: Long-lived API keys or third-party destinations may disclose connected account data.

Mitigation: Prefer managed OAuth, avoid embedding credentials in destinations, and use external forwarding only when explicitly understood and approved.

## Reference(s):

- [Coda skill release on ClawHub](https://clawhub.ai/byungkyu/skills/coda-api)
- [Maton homepage](https://maton.ai)
- [Coda API documentation](https://coda.io/developers/apis/v1)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses depend on the authorized connection and requested operation.]

## Skill Version(s):

1.2.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
