## Description:

Build release configuration entries and publish stakeholder reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams use this skill to prepare concise configuration entries from supplied release notes and turn those entries into stakeholder-facing configuration report entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release configuration or stakeholder report text may be incomplete or misleading if the provided release note is incomplete.

Mitigation: Provide only the release data needed for the requested output and review the generated configuration entry or report before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-configuration-report-desk)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, configuration]

**Output Format:** [Structured objects containing concise text fields and Markdown report content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces either a configuration_entry object with config_key, config_value, and config_label, or a report_entry object with report_id, title, and markdown.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
