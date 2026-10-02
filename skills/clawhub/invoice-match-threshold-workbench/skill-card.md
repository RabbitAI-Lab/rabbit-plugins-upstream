## Description:

Build an invoice reconciliation summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations teams use this skill to match bundled invoice candidates against a chosen threshold and produce a local reconciliation summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill creates a receipt directory and reconciliation-summary.json in the selected output directory.

Mitigation: Use a dedicated, writable --output-dir and review the generated files before relying on them.

Risk: Matching is based on bundled local invoice candidates, not a live invoice system.

Mitigation: Check the matched invoice IDs against the records relevant to the actual reconciliation.

## Reference(s):

- [Invoice Matching Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON reconciliation summary and local summary file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a summary identifier, threshold, matched count, invoice IDs and a local effect receipt.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
