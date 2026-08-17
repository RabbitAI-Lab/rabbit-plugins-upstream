## Description:

Finds expiring contract renewal opportunities by scanning upcoming contract-end windows, incumbent suppliers, urgency, buyer type, proposed projects, and procurement-intent signals for a requested industry or region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to identify public-procurement renewal and replacement opportunities by industry, product, geography, buyer type, budget threshold, and contract-expiry window. The skill returns prioritized opportunity lists and can generate a shareable HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and opportunity criteria are sent to the ZLBX service and API credits may be consumed.

Mitigation: Tell users the scan scope and expected credit use before starting; use only a user-provided or explicitly approved ZLBX_API_KEY.

Risk: The skill stores a ZLBX API key and generated reports in the user's home directory.

Mitigation: Prefer preconfigured environment credentials, protect local configuration and report directories, and avoid committing generated files.

Risk: Generated HTML reports may contain signed login-bypass links returned by the service.

Mitigation: Share generated reports only with trusted recipients and avoid publishing report files outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/expiring-contract-renewal-finder)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists, HTML report files, JSON report inputs, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY for ZLBX service calls; generated reports are written locally and may include signed source links returned by the service.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
