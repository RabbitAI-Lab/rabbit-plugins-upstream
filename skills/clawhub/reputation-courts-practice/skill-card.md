## Description:

Russian court practice via reputation.ru for finding cases, generating synthesized analysis reports, and fetching document full text across arbitration, general jurisdiction, and Supreme Court sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[reputationru](https://clawhub.ai/user/reputationru)

### License/Terms of Use:

MIT-0

## Use Case:

External users and legal research agents use this skill to search Russian court practice, retrieve source documents, and produce synthesized court-practice analysis through the paid reputation.ru service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends court queries, case identifiers, document requests, and API credentials or OAuth authorization to the paid reputation.ru service.

Mitigation: Install only when use of that service is intended; prefer OAuth or a scoped, revocable API key and monitor account access.

Risk: Search, document retrieval, and analysis calls may incur paid service charges.

Mitigation: Monitor billing and avoid repeated near-duplicate searches or unnecessary deep analysis requests.

Risk: Changing the reputation.ru base URL could send legal queries and credentials to an untrusted endpoint.

Mitigation: Use the default reputation.ru API endpoint unless a trusted endpoint has been explicitly approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/reputationru/skills/reputation-courts-practice)
- [reputation.ru API account](https://reputation.ru/account/api)
- [reputation.ru API base URL](https://api.reputation.ru)
- [reputation.ru MCP endpoint](https://api.reputation.ru/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON, Python, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include court case links, document identifiers, synthesized reports, setup guidance, and API or MCP request examples.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
