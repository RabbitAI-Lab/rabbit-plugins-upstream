## Description:

Research Brazil's Chamber of Deputies using its official open-data API. Use for federal deputies, Chamber bills, votes, events, committees, parliamentary fronts, and CEAP expenses; use senado-federal for Senate-only records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[olegantonov](https://clawhub.ai/user/olegantonov)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and researchers use this skill to answer factual questions about Brazil's Chamber of Deputies and to build reproducible API queries for deputies, propositions, votes, events, committees, parliamentary fronts, and CEAP expenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency versions may drift when the skill is installed in locked-down or production environments.

Mitigation: Pin dependencies or install from a reviewed lockfile before deployment.

Risk: Legislative data, reference codes, and current-day results can change, making cached or uncited answers misleading.

Mitigation: Resolve reference endpoints at query time, include the retrieval date when freshness matters, and cite the exact API URL used.

Risk: Upstream API errors, empty results, or pagination mistakes can be confused with a valid absence of records.

Mitigation: Distinguish empty successful responses from HTTP or parsing errors and follow the API-provided next links during pagination.

## Reference(s):

- [Câmara dos Deputados Skill Page](https://clawhub.ai/olegantonov/skills/camara-deputados)
- [Official Chamber Open Data API](https://dadosabertos.camara.leg.br/api/v2)
- [Official Chamber API Swagger](https://dadosabertos.camara.leg.br/swagger/api.html)
- [Portal de Dados Abertos](https://www2.camara.leg.br/transparencia/dados-abertos)
- [Câmara API endpoint reference](references/api-endpoints.md)
- [Tracking a proposition across both houses](references/cross-house.md)
- [Chamber response, pagination, and time rules](references/response-shapes.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance, API calls]

**Output Format:** [Markdown, Python snippets, shell commands, JSON-compatible API responses, and cited API URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve official field names, separate Chamber data from interpretation, include retrieval dates when freshness matters, and cite exact API URLs for auditable answers.]

## Skill Version(s):

1.1.1 (source: SKILL.md metadata, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
