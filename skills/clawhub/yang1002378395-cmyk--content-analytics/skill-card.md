## Description:

Analyzes creator content performance across Juejin, Xiaohongshu, and Zhihu and provides cross-platform summaries and AI-assisted optimization recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yang1002378395-cmyk](https://clawhub.ai/user/yang1002378395-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to compare recent performance across Juejin, Xiaohongshu, and Zhihu and turn analytics into publishing recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator-platform cookies may act like account sessions and the artifact does not explain credential handling safeguards.

Mitigation: Use scoped tokens or official APIs when available, avoid cookies for high-impact accounts, and confirm how credentials are stored before use.

Risk: Analytics data and cookies may be processed by GLM-5 or another external model.

Mitigation: Confirm where analytics data is sent and remove sensitive account, customer, or business data before analysis.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown report with platform metrics, cross-platform comparisons, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require creator-platform cookies and may rely on an external AI model for analysis.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
