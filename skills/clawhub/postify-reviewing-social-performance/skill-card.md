## Description:

Reviews Postify delivery analytics, failed posts, per-channel performance, and suggested posting times in a concise report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and workspace owners use this skill to review Postify delivery rates, failed posts, channel performance, and suggested posting times for a chosen period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Postify connection may grant access beyond the analytics and post-listing data needed for this report.

Mitigation: Confirm the OAuth connection grants the expected read-only analytics and post-listing access before use, including when using Code Mode.

Risk: Incomplete or missing analytics could make a performance report misleading.

Mitigation: Report only returned metrics and identify unavailable data instead of estimating it or using external benchmarks.

## Reference(s):

- [Postify: Reviewing Social Performance on ClawHub](https://clawhub.ai/bsalaeddin/skills/postify-reviewing-social-performance)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Short report with a per-channel table and actionable next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only available Postify workspace metrics; does not publish or modify posts.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
