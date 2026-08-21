## Description:

Monitor influencer campaigns across TikTok, Instagram, and YouTube by creating and managing monitor tasks, pulling metrics, downloading tracked assets, and running post-campaign reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, creator managers, and agent developers use this skill to create or inspect cross-platform monitoring tasks, retrieve TikTok, Instagram, and YouTube metrics or tracked assets, and produce campaign reviews with trends, anomalies, and recommended next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send requests through a hosted third-party API gateway or a user-configured base URL.

Mitigation: Review the endpoint before use, avoid setting SCRUMBALL_BASE_URL to untrusted hosts, and keep .env files trusted.

Risk: The operation runner may store a persistent install identifier and send it with API requests.

Mitigation: Delete ~/.scrumball_install_id to reset the local identifier, and review this behavior before installing in environments with strict tracking controls.

Risk: API credentials may be supplied through SCRUMBALL_API_KEY and sent to the configured endpoint.

Mitigation: Use trusted environment files, scope API keys appropriately, and rotate keys if endpoint configuration is changed unexpectedly.

## Reference(s):

- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operations Manifest](references/operations.json)
- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-campaign-monitoring)
- [Publisher Profile](https://clawhub.ai/user/chengyu-xixihaha)
- [API Key and Quota Information](https://data.scdata.cc/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown campaign review text with optional JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected response includes task status, performance trend, anomalies, and a continue, adjust, or stop recommendation.]

## Skill Version(s):

1.0.2 (source: config.yaml and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
