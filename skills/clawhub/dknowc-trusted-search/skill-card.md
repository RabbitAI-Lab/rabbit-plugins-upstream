## Description:

dknowc trusted search helps agents retrieve and verify authoritative sources for policies, regulations, standards, compliance, subsidies, tax benefits, and related policy research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search trusted Chinese legal, policy, standards, government-service, subsidy, tax, and compliance materials, then produce answers with source-backed traces. It is intended for tasks where cited authority, clickable provenance, clean Markdown, and optional policy visualization are useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to dknowc services, and onboarding may require a phone number and SMS verification code when no API key is configured.

Mitigation: Use the skill only with user consent for that sharing, and pause rather than proceed if the user declines phone verification or service access.

Risk: API keys could be exposed in chat, logs, or persistent environment configuration.

Mitigation: Do not reveal full API keys, avoid logging secrets, and persist DKNOWC_API_KEY only after explicit user consent.

Risk: Endpoint overrides can redirect trusted-search traffic away from the expected dknowc service endpoints.

Mitigation: Avoid endpoint overrides unless the user has explicitly approved the destination and understands the data-sharing impact.

Risk: The server security verdict is suspicious because the skill handles phone verification and API keys with misleading privacy and disclosure language.

Mitigation: Review the onboarding and privacy statements before installation, and require clear disclosure for phone verification, query sharing, and key storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-search)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [README](artifact/README.md)
- [Search introduction and onboarding reference](artifact/reference/search_intro.md)
- [Sample trusted-search result](artifact/reference/sample_search_result.md)
- [Sample trace report](artifact/reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, JSON, shell commands, configuration, guidance]

**Output Format:** [Direct answers, Markdown, clickable provenance HTML, JSON search results, optional visualization files, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DKNOWC_API_KEY for service access and writes generated search, trace, clean Markdown, and optional visualization artifacts under the skill workspace.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
