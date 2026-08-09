## Description:

Retrieves public Xiaohongshu note comments, keyword search results, note details, and profile post data, then returns structured JSON for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, and analysts use this skill to collect public Xiaohongshu search results, note details, comments, and profile posts for trend research, competitor monitoring, content planning, and comment summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is broader than a comment-only fetcher and can perform keyword searches, note detail and comment retrieval, and blogger profile post listing.

Mitigation: Install it only when those broader Xiaohongshu public-data collection capabilities are intended.

Risk: Inputs and task parameters are transmitted to a third-party API service using GUAIKEI_API_TOKEN.

Mitigation: Confirm data-sharing authorization and token handling requirements before use.

Risk: Successful runs can save structured result data to local JSON files under logs/.

Mitigation: Review log retention and cleanup practices for collected Xiaohongshu data.

## Reference(s):

- [Options and usage guide](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei service website](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [Structured JSON printed to stdout, with matching JSON result files under logs/ when successful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: server release metadata, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
