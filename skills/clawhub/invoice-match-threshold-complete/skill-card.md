## Description:

Computes an invoice-matching threshold and reconciliation summary, saves a local record, and optionally delivers the result to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance teams and developers can calculate an invoice-matching threshold and reconciliation summary, keep a local record, and optionally submit the result to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery may automatically send reconciliation results to an external destination, including through generic environment-variable fallbacks.

Mitigation: Before running, review or unset delivery endpoint, API key and SMTP environment variables; use a dedicated output directory and avoid unrelated delivery credentials.

## Reference(s):

- [Reconciliation Threshold Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-complete)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON result and local JSON record, with optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only without delivery configuration; configured delivery can contact an external endpoint.]

## Skill Version(s):

1.2.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
