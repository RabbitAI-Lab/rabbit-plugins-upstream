## Description:

Yuanqing yotta-intel extracts and normalizes threat-intelligence IOCs from existing text, logs, reports, and emails, handles defanged indicators, deduplicates results, and outputs text, CSV, JSON, or STIX-lite without network lookups or scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts and developers use this skill to extract, normalize, deduplicate, defang, refang, and convert candidate IOCs from reports, phishing emails, logs, or other existing text for authorized threat-intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer modes can copy the skill into multiple agent skill directories when run globally or without a narrow target.

Mitigation: Install with an explicit --agent or --dir target after checking the destination path, and avoid global or no-argument installer modes unless broad installation is intended.

Risk: Extracted IOCs are candidate indicators and may be incorrect or not malicious.

Mitigation: Have an analyst review the extracted indicators and confirm maliciousness with trusted sources before operational blocking, alerting, or production threat-intelligence import.

## Reference(s):

- [IOC Type and Normalization Rules](references/ioc-spec.md)
- [Defang and Refang Rules](references/defang-rules.md)
- [STIX-lite Output Specification](references/stix-lite-spec.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-intel)

## Skill Output:

**Output Type(s):** [text, JSON, CSV, STIX-lite, shell commands, guidance]

**Output Format:** [Plain text reports, JSON objects, CSV tables, and STIX 2.1 Bundle JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on file or stdin input with optional IOC type filters, minimum-count filtering, and output-file selection.]

## Skill Version(s):

0.1.1 (source: SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
