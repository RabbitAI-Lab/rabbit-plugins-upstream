## Description:

Lead Enrichment helps an agent build lead dossiers from a name, company, email, or LinkedIn URL, with profile details, company context, contact guesses, recent activity, and personalized talking points.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[audsmith28](https://clawhub.ai/user/audsmith28)

### License/Terms of Use:


## Use Case:

Sales, recruiting, partnerships, and investor users can ask an agent to research prospects or candidates and produce structured profiles for outreach preparation. The included scripts currently demonstrate the workflow with mock enrichment output and should be reviewed before operational use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shipped enrichment script produces mock dossier data that can be mistaken for real research.

Mitigation: Treat generated dossiers as demonstration output until the enrichment implementation is replaced or independently verified against source URLs.

Risk: Batch processing can handle untrusted CSV input through shell scripts.

Mitigation: Review and harden the scripts before installation, and only process trusted input files.

Risk: Lead and candidate data may include personal information and CRM-bound exports.

Mitigation: Apply privacy, retention, consent, and CRM-transfer controls before using the skill with prospect or candidate data.

Risk: Setup checks for shared secrets files and optional premium-source API keys.

Mitigation: Avoid broad shared secrets-file probing and scope any required credentials to the minimum needed data source.

## Reference(s):

- [Lead Enrichment ClawHub Page](https://clawhub.ai/audsmith28/skills/lead-enrichment)
- [Skill Documentation](artifact/SKILL.md)
- [Example Configuration](artifact/config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON lead dossiers, Markdown reports, CSV exports, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-lead enrichment, batch processing, configurable data sources, local storage, and export conversion.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
