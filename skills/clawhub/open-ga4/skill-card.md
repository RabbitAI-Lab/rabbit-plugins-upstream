## Description:

Answers website-traffic questions from Google Analytics 4 through read-only local commands for reports, comparisons, live activity, property discovery, and setup diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anatoli-iliev](https://clawhub.ai/user/anatoli-iliev)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners, marketers, and developers use this skill through an OpenClaw agent to answer GA4 traffic, acquisition, ecommerce, realtime, and setup questions without opening the GA4 UI. It is intended for read-only analytics reporting and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically use existing local Google credentials and read every GA4 property those credentials can access.

Mitigation: Use a dedicated GA4 service account with Viewer access only and set GA4_PROPERTY_ALLOWLIST to the exact properties intended for agent access.

Risk: A pasted service-account key may be stored in local OpenClaw configuration and backups.

Mitigation: Store the key as a private file path with restrictive permissions instead of pasting key contents into configuration.

Risk: Returned GA4 report data enters the agent or model context and may include visitor-supplied strings.

Mitigation: Keep redaction enabled, treat dimension values as untrusted report data, and require human review before acting on analytics-derived strings.

Risk: The optional audit log writes local request metadata.

Mitigation: Enable GA4_AUDIT_LOG only when local request logging is desired and protect the log like other analytics metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anatoli-iliev/skills/open-ga4)
- [Open GA4 homepage](https://github.com/anatoli-iliev/open-ga4)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and tables, JSON diagnostics, and concise setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GA4 outputs may include visitor-supplied dimension values that should be treated as untrusted report data.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
