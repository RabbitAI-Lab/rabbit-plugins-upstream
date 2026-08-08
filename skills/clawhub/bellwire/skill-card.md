## Description:

Bellwire helps agents add, update, test, diagnose, and maintain private-first live cards, inbox events, and iPhone notifications in application backends, automation, and CI/CD workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xwchris](https://clawhub.ai/user/xwchris)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Bellwire notifications and live cards into applications, including Private mode signed Direct v2 endpoints, opaque outboxes, provider webhooks, conformance tests, and production verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to modify application code, automation, or deployment workflows to send Bellwire notifications and cards.

Mitigation: Install and use it only when those integration changes are intended, and review generated diffs and project identifiers before applying them.

Risk: Bellwire management, wake, and ingest tokens could be exposed if printed, committed, or stored outside an approved secret store.

Mitigation: Keep tokens in platform secrets or an approved password manager, avoid logging token values or payloads, and remove temporary secret files after import.

Risk: Hosted mode can store event, inbox, and surface content in Bellwire Cloud.

Mitigation: Use Private mode by default and switch to Hosted mode only after explicit user approval.

Risk: Destructive project operations can permanently remove project-scoped Bellwire data.

Mitigation: Resolve the exact project ID and require explicit user intent before running delete or revocation commands.

## Reference(s):

- [Bellwire ClawHub Skill Page](https://clawhub.ai/xwchris/skills/bellwire)
- [Integration Adapters](references/adapters.md)
- [Bellwire API](references/api.md)
- [Direct Connections](references/direct-connections.md)
- [Event Spec](references/event-spec.md)
- [Production Verification](references/production-verification.md)
- [Security](references/security.md)
- [Surfaces](references/surfaces.md)
- [Troubleshooting](references/troubleshooting.md)
- [Webhooks](references/webhooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, JSON, YAML, SQL, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
