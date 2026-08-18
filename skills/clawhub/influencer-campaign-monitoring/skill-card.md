## Description:

Campaign monitoring operations for TikTok, Instagram, and YouTube, including cross-platform monitor task lifecycle APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, analysts, and agent users use this skill to create or inspect influencer campaign monitoring tasks, retrieve platform metrics, download tracked assets, and summarize campaign status, trends, anomalies, and recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call a hosted API gateway or a user-configured SCRUMBALL_BASE_URL.

Mitigation: Confirm the gateway is trusted before use and avoid directing requests to untrusted endpoints.

Risk: API credentials may be loaded from environment variables or a local .env file.

Mitigation: Use a dedicated SCRUMBALL_API_KEY and keep unrelated secrets out of the skill and working-directory .env files.

Risk: Monitor task operations can create, refresh, or stop campaign monitoring tasks.

Mitigation: Review the requested platform, video identifier, and monitor_id before running state-changing operations.

## Reference(s):

- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operations Manifest](references/operations.json)
- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-campaign-monitoring)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include task status, performance trend, anomalies, and a recommendation when reviewing campaign monitoring data.]

## Skill Version(s):

1.0.0 (source: config.yaml and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
