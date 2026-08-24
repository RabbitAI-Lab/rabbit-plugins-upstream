## Description:

Fetch fresh, on-demand creator data across TikTok, Instagram, Facebook, and YouTube, including page/profile information, latest videos, posts, and media details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creator-research teams, and agent operators use this skill to fetch current creator and content data, compare it with prior assumptions, and summarize decision-relevant deltas for campaign or monitoring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator handles, post URLs, video IDs, and similar lookup data are sent to the configured Scrumball/SCData gateway.

Mitigation: Use the skill only for targets appropriate to share with that gateway, avoid sensitive or non-public targets, and use a dedicated API key.

Risk: A persistent install identifier may be reused across requests.

Mitigation: Delete ~/.scrumball_install_id if stable identifier reuse is not acceptable for the deployment.

Risk: Local .env files can contain API credentials used by the operation runner.

Mitigation: Keep .env files out of version control and rotate the API key if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-realtime-enrichment)
- [API Index](artifact/references/api-index.md)
- [Request and Response Guide](artifact/references/request-response.md)
- [Operation Manifest](artifact/references/operations.json)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown, Shell commands]

**Output Format:** [Markdown summaries with optional JSON API responses from executed operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes freshness, key deltas, impact, and recommended next step when realtime retrieval succeeds.]

## Skill Version(s):

1.0.5 (source: server release metadata and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
