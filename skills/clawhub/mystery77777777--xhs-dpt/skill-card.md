## Description:

Collect and export interaction metrics such as likes, saves, comments, and shares for public Xiaohongshu posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing analysts and social media teams use this skill to collect public Xiaohongshu post engagement metrics for campaign reporting and content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented default service uses HTTP, which can expose account tokens in transit.

Mitigation: Use a trusted HTTPS endpoint with certificate verification enabled, and avoid sending credentials across untrusted networks.

Risk: Security guidance reports an optional TLS verification bypass, and inspection was partial for five of seven components.

Mitigation: Keep TLS verification enabled, protect the local credential file, and review the complete package before use.

Risk: Security review reports collection capabilities extending beyond the stated engagement-metrics purpose.

Mitigation: Confirm the deployed behavior and limit collection to public posts and metrics you are authorized to access.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mystery77777777/skills/xhs-dpt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, CSV files]

**Output Format:** [JSON results, CSV exports, and concise Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batches of up to 50 note URLs; exports include post identifiers, titles, and engagement counts.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
