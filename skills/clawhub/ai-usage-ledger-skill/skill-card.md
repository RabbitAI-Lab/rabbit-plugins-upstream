## Description:

Compiles locally recorded AI coding-agent usage into an append-only ledger with pricing, account attribution, validation, dashboards, study packages and exportable ledger documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[completetech](https://clawhub.ai/user/completetech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers and operations teams use this skill to audit local AI coding-agent activity, estimate API-equivalent costs, attribute usage by account or project, and produce internal evidence packages or anonymized publication copies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive AI-agent logs, prompt text, account labels and generated usage records may be written to local ledger or work directories with ambient filesystem permissions.

Mitigation: Install only when local read access is acceptable, keep the ledger home and work directory private, avoid shared folders, and leave prompt capture, credential-derived account labels, raw-log archiving, WSL or other-profile scans, SSH hosts and schedules disabled unless needed.

Risk: Optional SSH scans may stage usage data on remote hosts before local collection.

Mitigation: Use only named hosts that the operator is authorized to audit, and manually clean remote staging directories after SSH scans until private staging and cleanup are enforced.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/completetech/skills/ai-usage-ledger-skill)
- [Project Homepage](https://github.com/CompleteTech-LLC/ai-usage-ledger-skill)
- [Project README](https://github.com/CompleteTech-LLC/ai-usage-ledger-skill#readme)
- [Harness Catalog](references/harness-catalog.md)
- [Log Formats](references/log-formats.md)
- [Discovery Guide](references/discovery.md)
- [Ledger Document Catalog](references/ledger-document-catalog.md)
- [Pitfalls](references/pitfalls.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands; generated ledger data, dashboards, reports and documents in SQLite, JSON, CSV, Markdown, HTML, PDF and DOCX.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only by default; prompt text, credential-derived account labels, raw-log archives, WSL or other-profile scans, SSH hosts and scheduled refreshes require opt-in.]

## Skill Version(s):

1.5.11 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
