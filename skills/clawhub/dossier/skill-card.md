## Description:

Готовит русскоязычное досье на живого человека перед встречей с проверкой фактов и ссылками на источники.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sergeypetrakov](https://clawhub.ai/user/sergeypetrakov)

### License/Terms of Use:

MIT-0

## Use Case:

Руководители и другие участники деловых встреч используют навык, чтобы получить краткую справку о собеседнике, подтверждённые факты и темы для разговора.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profiling living people can expose sensitive personal information or unsupported claims.

Mitigation: Limit dossiers to relevant public information, exclude private contact and health details, and review claims and citations before sharing.

Risk: Names, search queries, and fact-check claims are sent to Perplexity/Sonar; generated dossiers and logs may be sensitive.

Mitigation: Use only with appropriate authorization, minimize submitted information, and restrict access to generated files and logs.

Risk: Relative-path lookup may cross task boundaries, and cited-source fetching may reach unintended internal URLs.

Mitigation: Review or fix path and network access before broad deployment; isolate task files and restrict source fetches to approved public destinations.

## Reference(s):

- [Поисковый справочник навыка](references/search-playbook.md)
- [Страница навыка на ClawHub](https://clawhub.ai/sergeypetrakov/skills/dossier)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Russian-language Word document (.docx) and matching chat text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cited sources and fact-check status; requires PERPLEXITY_API_KEY for search and verification.]

## Skill Version(s):

1.1.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
