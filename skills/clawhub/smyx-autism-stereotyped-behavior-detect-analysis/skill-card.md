## Description:

This skill analyzes fixed-camera child behavior videos using pose estimation and temporal action detection to identify and report repetitive behaviors such as spinning, hand flapping, and body rocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External rehabilitation teams, caregivers, and developers use this skill to submit fixed-camera child behavior videos or URLs for cloud analysis and receive event-level behavior statistics, summaries, and report links for professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends sensitive child behavior videos or video URLs to external cloud services.

Mitigation: Use only with explicit guardian or operator consent, confirm the account and data-retention model, and minimize or secure video data before analysis.

Risk: The workflow can silently create or reuse identity data and store authentication tokens locally.

Mitigation: Run only in a trusted workspace, review local identity and token storage before installation, and remove stored tokens when access is no longer needed.

Risk: Historical report queries may expose prior child behavior reports through cloud APIs.

Mitigation: Limit use to authorized operators, verify report ownership before sharing links or exports, and avoid using local memory as a source for historical reports.

Risk: Behavior recognition can be incorrect or misused as clinical decision support.

Mitigation: Treat outputs as visual behavior statistics for professional review only; do not use them for diagnosis, scale scoring, or rehabilitation prescriptions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON report text with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a cloud report link; results are descriptive behavior statistics, not diagnosis or treatment advice.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
