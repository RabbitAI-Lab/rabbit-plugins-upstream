## Description:

Retrieves public Kuaishou videos, creator posts, and comments to support content-performance reviews and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use the skill to find public Kuaishou videos, review creator posts and video comments, and develop evidence-based content recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Kuaishou links or IDs, request parameters, and the API token are sent to a third-party service.

Mitigation: Use only if that transfer is acceptable; protect the GUAIKEI_API_TOKEN and avoid sensitive inputs.

Risk: Saved search, post, and comment results may remain in the local logs directory.

Mitigation: Review and delete local logs when retention is not appropriate.

Risk: Public social-media data may still be subject to platform, privacy, and organizational rules.

Mitigation: Use collected data only within applicable platform, privacy, and organizational requirements.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/kuaishou-performance-review)
- [GUAIKEI service and token information](https://www.guaikei.com)
- [Options and usage](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured JSON results with optional written summary or content review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include success, empty, or error status; successful queries may save results in local logs.]

## Skill Version(s):

1.0.0 (source: skill frontmatter, package.json, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
