## Description:

Kuaishou Hot Trend collects public Kuaishou video, creator post, and comment data through keyword search, profile lookup, and video comment commands, returning structured JSON for trend research, competitor monitoring, KOL discovery, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, MCN teams, and analysts use this skill to collect public Kuaishou data for content ideation, competitor monitoring, KOL screening, and comment or trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends query terms, Kuaishou URLs, and request metadata to the GUAIKEI third-party API.

Mitigation: Use it only for public Kuaishou data and only when the user or organization accepts the GUAIKEI API relationship and token requirement.

Risk: Fetched public Kuaishou results are saved locally as JSON logs and may contain business-sensitive research or user-generated content.

Mitigation: Protect the logs directory, limit sharing of exported results, and delete saved outputs when they are no longer needed.

Risk: The skill is scoped to public Kuaishou data and does not support private, hidden, login-required, or non-Kuaishou platform data.

Mitigation: Clarify unsupported requests before execution and avoid using the commands for private content or other platforms.

## Reference(s):

- [Kuaishou Hot Trend on ClawHub](https://clawhub.ai/engheng-art/skills/kuaishou-hot-trend)
- [GUAIKEI API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON from command-line tools, with brief text guidance when parameters, tokens, or platform scope need clarification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful outputs include status, request metadata, runtime metadata, and results; failed or empty outputs include status, error_code, message, and null results.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, and changelog; artifact frontmatter metadata states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
