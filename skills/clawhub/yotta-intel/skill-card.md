## Description:

Extracts, normalizes, and deduplicates threat indicators from supplied reports, messages, and logs locally, with text, CSV, JSON, and STIX-lite output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and developers use this skill to extract and safely share candidate IP addresses, domains, URLs, email addresses, hashes, and CVE identifiers from existing threat reports, phishing messages, and logs. Results are not a determination that an indicator is malicious.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad or global installation makes the skill available to more agents than intended.

Mitigation: Install only to intended agent directories, pin the package version, and use --dry-run before broad installations.

Risk: Indicators from hostile reports may become active spreadsheet formulas when CSV output is opened.

Mitigation: Prefer JSON or STIX output for untrusted content, or neutralize formula cells before opening CSV in a spreadsheet.

Risk: Extracted indicators may be mistaken for confirmed malicious threats.

Mitigation: Verify candidate indicators independently before taking action and share defanged forms to reduce accidental activation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-intel)
- [Project homepage listed in metadata](https://github.com/YottaMeta/yotta-intel)
- [IOC specification](references/ioc-spec.md)
- [Defanging rules](references/defang-rules.md)
- [STIX-lite specification](references/stix-lite-spec.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Plain text, CSV, JSON, or STIX-lite JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deduplicated candidate indicators include occurrence counts, first-seen lines, and defanged forms; the skill does not verify maliciousness.]

## Skill Version(s):

0.2.2 (source: server release, frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
