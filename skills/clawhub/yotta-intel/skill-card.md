## Description:

元情 yotta-intel helps agents locally extract, normalize, deduplicate, defang/refang, and export IOCs from threat reports, phishing emails, logs, and other existing security text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, incident responders, and developers use this skill to turn existing threat-intelligence text into normalized IOC records for review, sharing, or import into downstream workflows. It is suited to authorized security analysis where the agent should process local text without reputation lookups, sample downloads, or proactive scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can target multiple local agent environments, which may make the skill available more broadly than intended.

Mitigation: Install only where needed; prefer --agent or --dir for a single target and use -g only for an intentional multi-agent deployment.

Risk: Extracted IOCs are candidate indicators and are not a verdict that an item is malicious.

Mitigation: Review results before enforcement or sharing, and confirm maliciousness with authorized human review or separate intelligence sources.

Risk: Threat reports may contain clickable or otherwise active URLs, domains, IPs, or email addresses.

Mitigation: Use the defanged output for sharing and keep processing local and offline unless a separate authorized workflow requires enrichment.

## Reference(s):

- [IOC type and normalization rules](references/ioc-spec.md)
- [Defang and refang rules](references/defang-rules.md)
- [STIX-lite output specification](references/stix-lite-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated text, JSON, CSV, or STIX-lite output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs candidate indicators with normalized values, defanged forms, counts, first-line references, and context snippets when available.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
