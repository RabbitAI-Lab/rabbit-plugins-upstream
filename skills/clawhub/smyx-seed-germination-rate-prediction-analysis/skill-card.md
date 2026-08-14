## Description:

Analyzes seedling tray images or videos to identify emerged seedlings, count germinated seeds, estimate germination rate, and return a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze seedling tray or planting-pot media, estimate germinated seed counts and germination rate, and retrieve prior germination analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads seed tray media or media URLs to the Life Emergence backend for analysis.

Mitigation: Use only media that is appropriate for third-party processing, and review retention, deletion, and account controls before using sensitive or production data.

Risk: The skill can create or reuse a backend-linked identity automatically and store tokens or profile data in a local workspace database.

Mitigation: Run the skill in a controlled workspace, restrict access to local state files, and clear local credentials or profile data when the workflow is no longer needed.

Risk: The skill can retrieve cloud report history without a separate confirmation step.

Mitigation: Limit use to users authorized to view the associated reports, and review report-history access behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API error documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured report text or JSON, with Markdown tables for history listings and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs visual counting estimates, germination-rate calculations, status messages, and cloud report links when available.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter: 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
