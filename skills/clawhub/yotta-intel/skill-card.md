## Description:

Extracts and normalizes IPs, domains, URLs, email addresses, hashes, and CVE identifiers from existing threat text, including common defanged forms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and developers use this skill to extract, deduplicate, normalize, and export candidate indicators of compromise from existing threat reports, phishing emails, and logs. It is intended for authorized, own-asset, or educational analysis, and findings require verification before being treated as malicious.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refang or safe-sharing output may restore active links that can be clicked or trigger link previews.

Mitigation: Inspect defanged output before sharing and verify that links remain defanged; prefer sharing the defanged form.

Risk: CSV exports can preserve formulas that spreadsheet software may interpret as active formulas.

Mitigation: Use JSON, or import CSV strictly as text with formula interpretation disabled.

## Reference(s):

- [IOC types and normalization rules](artifact/references/ioc-spec.md)
- [Defang and refang rules](artifact/references/defang-rules.md)
- [STIX-lite output specification](artifact/references/stix-lite-spec.md)
- [FAQ](artifact/references/faq.md)
- [GitHub repository](https://github.com/YottaMeta/yotta-intel)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-intel)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-intel)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, STIX 2.1 Bundle]

**Output Format:** [Plain text, JSON, CSV, or STIX-lite JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deduplicated canonical indicators with occurrence counts, first-seen line numbers, context snippets, and defanged values.]

## Skill Version(s):

0.2.3 (source: SKILL.md frontmatter, CHANGELOG.md, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
