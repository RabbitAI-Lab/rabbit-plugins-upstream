## Description:

Extracts and normalizes candidate threat indicators from supplied text, logs, and reports for local, offline analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and developers use this skill to extract, deduplicate, and safely share candidate IP addresses, domains, URLs, email addresses, hashes, and CVE identifiers from authorized threat reports, phishing emails, and logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can write the skill into multiple agent environments.

Mitigation: Install only into the intended agent directory, preferably using --agent or --dir instead of a global installation.

Risk: CSV output may preserve spreadsheet formulas from untrusted reports or emails.

Mitigation: Prefer JSON or STIX output, or sanitize CSV before opening it in a spreadsheet.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-intel)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-intel)
- [IOC extraction specification](artifact/references/ioc-spec.md)
- [Defang and refang rules](artifact/references/defang-rules.md)
- [STIX-lite output specification](artifact/references/stix-lite-spec.md)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, STIX-lite, Guidance]

**Output Format:** [Plain text, JSON, CSV, or STIX 2.1 Bundle with Indicator objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs candidate indicators only; no reputation checks or maliciousness determination.]

## Skill Version(s):

0.2.1 (source: server release, frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
