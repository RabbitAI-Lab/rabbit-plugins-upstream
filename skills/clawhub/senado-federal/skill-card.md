## Description:

Research Brazil's Federal Senate using its official legislative and administrative open-data APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[olegantonov](https://clawhub.ai/user/olegantonov)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, journalists, civic-tech developers, and agents use this skill to retrieve and summarize official Brazilian Senate legislative records and administrative transparency data with auditable API URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative transparency records can include personal or financial fields from official Senate datasets.

Mitigation: Summarize only the fields needed for the task, avoid republishing unnecessary personal details, and state the year, filters, currency treatment, and source URL used.

Risk: Official APIs can time out, fail, or return response-shape variations that could be mistaken for no records.

Mitigation: Use bounded retries, validate expected response shapes, treat upstream failures differently from empty results, and preserve the exact API URL and retrieval date.

Risk: Dependency ranges may change future installs.

Mitigation: Pin and review dependencies when reproducible or controlled deployments are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/olegantonov/skills/senado-federal)
- [Senate legislative open-data API](https://legis.senado.leg.br/dadosabertos)
- [Senate legislative API Swagger](https://legis.senado.leg.br/dadosabertos/api-docs/swagger-ui/index.html)
- [Senate administrative open-data API](https://adm.senado.gov.br/adm-dadosabertos)
- [Senate administrative API Swagger](https://adm.senado.gov.br/adm-dadosabertos/swagger-ui/index.html)
- [Senate legislative API endpoint reference](references/api-endpoints.md)
- [Senate response shapes, identifiers, and dates](references/response-shapes.md)
- [Senate administrative and transparency API](references/administrative-api.md)
- [Tracking a process across the Senate and Chamber](references/cross-house.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown prose with official API URLs, JSON snippets, Python code, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish official Senate data from interpretation and include retrieval dates, identifiers, filters, and source API URLs when freshness or auditability matters.]

## Skill Version(s):

1.1.0 (source: frontmatter, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
