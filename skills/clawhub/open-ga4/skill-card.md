## Description:

Open GA4 lets an agent answer website traffic questions from Google Analytics 4 by running read-only reports, comparisons, live queries, property discovery, and setup diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anatoli-iliev](https://clawhub.ai/user/anatoli-iliev)

### License/Terms of Use:

MIT-0

## Use Case:

Website owners, operators, analysts, and developers use this skill to ask natural-language questions about Google Analytics 4 traffic and receive read-only reports or setup guidance without opening the GA4 dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GA4 credentials and returned analytics data are sensitive.

Mitigation: Install only for properties suitable for the configured model provider, grant Viewer access only to needed properties, and prefer storing the service-account key as a private file path rather than pasting JSON into configuration.

Risk: The skill can enumerate every GA4 property visible to the configured credential unless restricted.

Mitigation: Set GA4_PROPERTY_ALLOWLIST when only specific numeric property ids should be available.

Risk: Visitor-authored GA4 dimension values can appear in report rows and may contain misleading or adversarial text.

Mitigation: Treat report strings as untrusted data, keep human review in workflows that act on analytics results, and keep redaction enabled unless there is a deliberate need to disable it.

Risk: Optional audit logging writes local query-history metadata.

Mitigation: Enable GA4_AUDIT_LOG only when local query history is desired and protect the chosen log path appropriately.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/anatoli-iliev/skills/open-ga4)
- [Project Homepage](https://github.com/anatoli-iliev/open-ga4)
- [README](README.md)
- [Setup Guide](SETUP.md)
- [Privacy Behaviour](PRIVACY.md)
- [Security Policy](SECURITY.md)
- [Design Notes](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON diagnostics, and concise setup or command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GA4 API results are returned into the agent conversation; optional audit logging records what was asked, not report rows.]

## Skill Version(s):

0.2.1 (source: frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
