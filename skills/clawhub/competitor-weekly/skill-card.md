## Description:

Generates an evidence-based weekly comparison report for a primary Amazon ASIN and authorized competitors after quote review and explicit user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to guide an agent through ARI account checks, product readiness checks, quote review, and confirmed generation of a weekly competitor evidence report. The fixed workflow is weekly/competitor with the ops_weekly output template.

### Deployment Geography for Use:

Global; supported Amazon marketplace sites are controlled by the ARI service and command parameters.

## Known Risks and Mitigations:

Risk: The server security summary says the skill exposes monitoring, account-state changes, paid workflows, and data export features beyond a weekly competitor report.

Mitigation: Install only when broad ARI review-operations access is intended, and verify each --confirm action, watch or schedule change, competitor binding, workbench status update, alert mark-read action, and export destination before use.

Risk: Paid collection or AI analysis workflows can consume ARI credits, and an interrupted stream may already have charged and archived a report.

Mitigation: Use quote commands before paid runs, require explicit user confirmation, and check reports or operation status with the original ASIN or requestId before retrying interrupted paid actions.

Risk: The skill requires an ARI API key that can access account state and ARI operations.

Mitigation: Use the documented setup or ARI_API_KEY configuration path, keep the key out of reports and prompts, and review account permissions before deployment.

## Reference(s):

- [Amazon 竞品周报 workflow reference](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-weekly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report content and concise command guidance, with JSON returned by ARI CLI commands when compact output is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection or AI analysis actions require a quote and explicit user confirmation before --confirm is used.]

## Skill Version(s):

1.4.3 (source: artifact frontmatter, _meta.json, script VERSION, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
