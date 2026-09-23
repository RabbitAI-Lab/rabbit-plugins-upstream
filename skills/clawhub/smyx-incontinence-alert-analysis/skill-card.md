## Description:

Uses visual AI to analyze caregiving images, videos, or media URLs for damp clothing or abnormal excretion and return caregiver alerts, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and care operations teams use this skill to analyze uploaded care images, videos, or URLs for incontinence-related conditions in disabled seniors, bedridden patients, infants, or other people receiving care. The skill produces structured monitoring results, alert levels, warnings, suggestions, and links to generated reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive caregiving images or videos may be sent to the publisher's cloud service.

Mitigation: Use only with explicit consent from the person or guardian, upload the minimum necessary media, and restrict report access to authorized caregivers.

Risk: Insecure or non-production networking configuration could expose care media or report data.

Mitigation: Verify the installed package is configured for HTTPS production endpoints before use.

Risk: Silent identity handling and persistent token storage can leave reusable credentials or care-history links in the local workspace.

Mitigation: Limit workspace access, treat local databases as sensitive, and rotate or clear stored credentials when access changes.

Risk: Visual analysis may be wrong or incomplete and is not a substitute for professional care judgment.

Mitigation: Require human confirmation before taking care actions, especially for urgent alerts or unclear images.

## Reference(s):

- [Incontinence Alert Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown or JSON text with optional saved JSON output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include structured alert levels, care warnings, care suggestions, report links, and Markdown tables for historical report lists.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
