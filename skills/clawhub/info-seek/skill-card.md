## Description:

Infoseek helps agents run end-to-end research workflows by discovering sources, scoring and fetching content, detecting contradictions and entities, and producing structured Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gyint](https://clawhub.ai/user/gyint)

### License/Terms of Use:

MIT

## Use Case:

Developers and research analysts use this skill to automate industry, market, technical, competitor, and entity research, including source discovery, content collection, cross-source synthesis, and report generation. Use OSINT and account-forensics capabilities only for authorized subjects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The HTTP/MCP server includes hardcoded admin authentication and can expose OAuth token behavior when run for shared or remote access.

Mitigation: Prefer stdio or local-only use, avoid exposing /oauth/token, set a unique INFOSEEK_JWT_SECRET, and restrict which users or systems can call the server.

Risk: Exposed tools can read local files and may persist research data under user home directories.

Mitigation: Avoid file:// inputs for sensitive paths and review or delete ~/.infoseek and ~/infoseek-archives when the stored data is no longer needed.

Risk: OSINT and account-forensics capabilities can create privacy or authorization concerns.

Mitigation: Enable those features only for subjects the operator is authorized to investigate and keep consent-gated capabilities disabled otherwise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gyint/skills/info-seek)
- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [Release notes](artifact/RELEASE_NOTES.md)
- [Configuration reference](artifact/references/configuration.md)
- [API keys reference](artifact/references/api-keys.md)
- [External dependencies](artifact/references/external-deps.md)
- [Network boundary report](artifact/references/network-boundary-report.md)
- [Risk register](artifact/references/risk-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown reports with supporting JSON, text, shell commands, and local archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit structured research reports, fetched-content summaries, entity or contradiction analysis, key-management guidance, and optional local archives.]

## Skill Version(s):

2.0.0 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
