## Description:

Retrieves Weibo creator posts for recent publishing reviews, content research, style analysis, benchmarking, and account tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve Weibo creator post lists for recent publishing reviews, content research, style analysis, benchmarking, and account tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider credentials could be exposed through local configuration or version control.

Mitigation: Store the API key in the client's secret storage and keep local credential settings out of version control.

Risk: Unbounded page or item retrieval can use more API credits than intended.

Mitigation: Set page or item limits to control credit usage.

Risk: The external npm CLI implementation is outside the scope of the skill instruction review.

Mitigation: Prefer a reviewed, pinned CLI version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)
- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON creator post data with an agent-written summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; pagination is supported, with optional page and item limits.]

## Skill Version(s):

0.1.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
