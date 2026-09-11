## Description:

Coda API integration with managed OAuth for managing docs, pages, tables, rows, formulas, controls, permissions, and analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Coda through managed OAuth, list and inspect Coda resources, and perform user-approved changes to docs, pages, tables, rows, formulas, controls, and permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Coda account authority can expose or modify more workspace data than the current task requires.

Mitigation: Choose the narrowest available scopes, specify the intended connection when multiple accounts exist, start with read/list calls, and require explicit approval before writes, deletes, sharing, or permission changes.

Risk: Unpinned or unofficial Maton installation sources can introduce supply-chain risk.

Mitigation: Install Maton only from official package sources and avoid elevated privileges during installation.

Risk: Long-lived API keys can be exposed through environment variables, logs, files, or command lines.

Mitigation: Prefer OAuth-backed CLI profiles, keep credentials in the operating system credential store, and avoid printing, exporting, or persisting tokens.

## Reference(s):

- [Coda Skill on ClawHub](https://clawhub.ai/byungkyu/skills/coda-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Coda API Documentation](https://coda.io/developers/apis/v1)
- [Coda API Postman Collection](https://www.postman.com/codaio/coda-workspace/collection/0vy7uxn/coda-api)
- [Coda API Python Library](https://codaio.readthedocs.io/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request paths, JSON payload examples, and user-supplied connection identifiers.]

## Skill Version(s):

1.2.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
