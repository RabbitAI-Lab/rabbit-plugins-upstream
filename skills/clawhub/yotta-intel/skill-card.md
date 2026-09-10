## Description:

元情 yotta-intel extracts, normalizes, deduplicates, defangs, refangs, and converts threat-intelligence indicators from local text, logs, phishing emails, and reports into text, CSV, JSON, or STIX-lite outputs without performing reputation lookups, sample downloads, or proactive scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, developers, and incident-response teams use this skill to extract candidate IOCs from existing threat-intelligence text, normalize and deduplicate them, safely share them in defanged form, or convert them for downstream tooling. It is intended for authorized security analysis of owned assets, approved engagements, CTFs, or educational environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can modify agent skill directories broadly, including global locations when selected.

Mitigation: Install to one explicit destination with --agent or --dir, avoid --global unless broad installation is intended, and review installer behavior before execution.

Risk: Installer overwrite and symlink handling was flagged by security evidence as unsafe.

Mitigation: Run the installer only from trusted project directories and inspect the destination path before allowing it to copy files.

Risk: CSV output from hostile reports can carry spreadsheet formula content.

Mitigation: Treat CSV output as data for security tools or neutralize formula-like cells before opening it in spreadsheet software.

Risk: Extracted indicators are candidates, not confirmed malicious infrastructure.

Mitigation: Have an analyst or trusted intelligence source verify context and maliciousness before blocking, enriching, or publishing the indicators.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-intel)
- [IOC type and normalization rules](references/ioc-spec.md)
- [Defang and refang rules](references/defang-rules.md)
- [STIX-lite output specification](references/stix-lite-spec.md)
- [FAQ and troubleshooting](references/faq.md)
- [GitHub repository](https://github.com/YottaMeta/yotta-intel)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-intel)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and shell commands for running a local Python IOC tool; generated tool outputs may be text, CSV, JSON, or STIX-lite JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local and deterministic for a given input except generated timestamps and STIX bundle identifiers; extracted indicators remain candidate IOCs that require analyst review before maliciousness is asserted.]

## Skill Version(s):

0.2.0 (source: frontmatter, CHANGELOG, package.json, CLI)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
