## Description:

Build a stakeholder configuration report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and release operations stakeholders use this skill to turn a supplied configuration entry into a concise stakeholder report entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated stakeholder report can expose configuration details supplied in the request.

Mitigation: Provide only configuration details intended for stakeholder reporting and review the markdown before sharing it.

Risk: Incorrect or unclear configuration entries can produce misleading report text.

Mitigation: Check config_key, config_value, and config_label for accuracy before publishing the report entry.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-report-label-workbench)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Object containing report_id, title, and markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The output is returned in the report_entry field.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
