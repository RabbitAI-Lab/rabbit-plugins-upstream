## Description:

Infoseek helps agents run end-to-end research workflows that discover sources, score and fetch content, detect cross-source conflicts, identify entities, synthesize findings, and optionally archive structured Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gyint](https://clawhub.ai/user/gyint)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and agent builders use Infoseek to automate industry research, trend analysis, competitor intelligence, market research, technical research, content collection, report generation, and long-term local knowledge-base building.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist local knowledge state and archived research outputs.

Mitigation: Review the local data directory and archive retention policy before deployment, and delete retained local state when it is no longer needed.

Risk: The skill can manage API keys and call external search, LLM, and QVeris services.

Mitigation: Restrict access to key-management tools, keep credentials in approved stores, and review which external services are enabled for the deployment.

Risk: Optional identity-attribution OSINT capabilities can affect individuals if used without authorization.

Mitigation: Keep OSINT disabled unless there is a lawful, authorized use and require explicit consent before enabling identity-attribution workflows.

Risk: Remote SSE hosting with weak default authentication could expose tools to unintended callers.

Mitigation: Avoid exposing the SSE server beyond localhost unless default OAuth credentials and secrets are replaced and access is restricted.

## Reference(s):

- [README](README.md)
- [Skill Definition](SKILL.md)
- [Privacy Policy](PRIVACY.md)
- [Release Notes](RELEASE_NOTES.md)
- [External Dependencies](references/external-deps.md)
- [API Keys](references/api-keys.md)
- [Credential Tools](references/credential-tools.md)
- [Configuration](references/configuration.md)
- [Risk Register](references/risk-register.md)
- [Trusted Sources](references/trusted-sources.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON tool results, Python examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can persist local research state and optional archives when configured by the user.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
