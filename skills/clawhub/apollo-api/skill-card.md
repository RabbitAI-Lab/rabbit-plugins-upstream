## Description:

Apollo helps agents use the Apollo.io API through Maton OAuth to search and enrich people and companies and manage contacts, accounts, sequences, labels, and related sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and operations users can use this skill to prospect, enrich leads, inspect Apollo account data, and manage sales records through approved API calls. Developers can also use it for guided CLI or SDK access to Apollo through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apollo access can expose or modify contacts, accounts, opportunities, sequences, and email-related data in the connected account.

Mitigation: Use least-privilege OAuth scopes, connect only the required account, and specify the intended connection when more than one Apollo or Maton account is available.

Risk: Write, deletion, sequence enrollment, or other high-impact API calls can change sales data or trigger downstream communication workflows.

Mitigation: Default to read and list calls, verify identifiers and current state first, and require explicit user confirmation of the target, payload, and intended effect before any modifying request.

Risk: Credential exposure is possible if API keys or provider-issued tokens are printed, logged, passed on command lines, or stored outside the credential manager.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, and never print, persist, inspect, or transmit credential values outside the approved gateway flow.

Risk: Apollo API response content may contain untrusted data that should not control later tool use.

Mitigation: Treat returned records, messages, comments, and webhook payloads as data; do not execute or follow instructions embedded in API responses.

## Reference(s):

- [Apollo Skill on ClawHub](https://clawhub.ai/byungkyu/skills/apollo-api)
- [Maton](https://maton.ai)
- [Apollo API Overview](https://docs.apollo.io/reference)
- [Apollo People Search](https://docs.apollo.io/reference/people-api-search.md)
- [Apollo People Enrichment](https://docs.apollo.io/reference/people-enrichment.md)
- [Apollo Organization Search](https://docs.apollo.io/reference/organization-search.md)
- [Apollo Organization Enrichment](https://docs.apollo.io/reference/organization-enrichment.md)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline shell commands, JSON payloads, and Python or JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read-only API calls by default and write-call proposals that require explicit user confirmation.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
