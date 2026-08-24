## Description:

Monitor influencer campaigns across TikTok, Instagram, and YouTube by creating and managing monitor tasks, pulling metrics, downloading tracked assets, and producing post-campaign review insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, campaign managers, and agents use this skill to create or inspect influencer monitoring tasks, fetch platform metrics and tracked assets, and summarize trends, anomalies, and campaign recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-bearing campaign requests and metrics are sent to the configured Scrumball/scdata gateway.

Mitigation: Use only trusted SCRUMBALL_BASE_URL values, protect SCRUMBALL_API_KEY, and avoid sending sensitive campaign identifiers unless this third-party processing is acceptable.

Risk: A persistent installation identifier may be retained for quota or tracking behavior.

Mitigation: Disclose this behavior before installation and remove ~/.scrumball_install_id when persistent identification is not desired.

## Reference(s):

- [API Index](artifact/references/api-index.md)
- [Request and Response Guide](artifact/references/request-response.md)
- [Operations Manifest](artifact/references/operations.json)
- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-campaign-monitoring)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown summaries with optional shell commands and JSON API results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected summaries include task status, performance trend, anomalies, and a recommendation.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact/config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
