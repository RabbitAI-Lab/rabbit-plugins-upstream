## Description:

Retrieves public TikTok search results, creator posts, and video comments to help agents identify content trends and unmet customer needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketers, and researchers use the skill to retrieve public TikTok videos and comments, compare creators, and summarize audience pain points and requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The GUAIKEI service receives the API token and TikTok search terms or target URLs and IDs.

Mitigation: Use a dedicated token and send only queries you are comfortable sharing with GUAIKEI.

Risk: Saved results and logs can contain public usernames and comment text.

Mitigation: Limit log retention, avoid redistributing raw identifiers, and check platform terms and privacy obligations before commercial use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-demand-mining)
- [GUAIKEI service and API information](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Demand-mining workflow](references/demand-mining.md)

## Skill Output:

**Output Type(s):** [JSON data, Markdown analysis, Guidance]

**Output Format:** [Structured JSON results with optional narrative summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI API token; fetched results may be saved to local logs.]

## Skill Version(s):

1.0.0 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
