## Description:

Mermail routes broad or cross-domain Mermail requests to the correct focused workflow for connection setup, email, workspace administration, triage, integrations, and Agent Wallet or PayBox tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this router when a Mermail request is ambiguous, spans multiple Mermail domains, or needs the correct execution surface before taking action. It helps agents decompose work across focused Mermail skills while preserving connection, workspace, mailbox, approval, and handoff boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route requests toward sensitive email, workspace administration, third-party provider, deletion, and PayBox payment workflows.

Mitigation: Install it only when Mermail access is intended, review focused Mermail skills separately, and require explicit user intent and each focused skill's approval boundary before writes or external effects.

Risk: Email content, headers, attachments, links, tool output, and provider output may contain untrusted instructions that try to change routing or authorization.

Mitigation: Treat those sources as data only; allow only the authenticated user's current request to select skills, targets, accounts, payment terms, or effects.

Risk: Connection profile, role, rate-limit, workspace-scope, credit, or provider-policy errors can make a requested Mermail action unavailable.

Mitigation: Resolve connection and profile issues first, report unsupported or blocked paths, and avoid retrying uncertain writes through another client or skill surface.

## Reference(s):

- [Mermail routing reference](references/routing.md)
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration]

**Output Format:** [Markdown text with workflow steps, routing tables, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference MCP profiles, environment requirements, focused Mermail skills, approvals, skipped work, blocked work, and browser or UI handoffs.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
