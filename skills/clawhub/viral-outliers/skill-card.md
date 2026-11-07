## Description:

Find viral outlier posts on TikTok, Instagram and YouTube, pull creator stats, transcribe and analyse videos, build competitor watchlists, and crawl profiles on demand using prepaid credits, MCP or REST.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketers, and creators can find unusually high-performing TikTok, Instagram, and YouTube posts, compare creators, and review transcripts, comments, and video analyses. They can also monitor profiles and turn examples into niche-adapted content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup example runs an unpinned package and supplies it with a service credential; a changed package could expose credentials or local data.

Mitigation: Pin and review the package version before use, and provide the API key only to a version you trust.

Risk: The security scan is incomplete: it inspected two of three components and its tool-misuse analysis was degraded.

Mitigation: Treat the scan as limited evidence and review the package and its requested access before installing or supplying credentials.

## Reference(s):

- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Getting started](https://viraloutliers.com/docs/getting-started)
- [REST API specification](https://viraloutliers.com/openapi.json)
- [Agent API and MCP server reference](references/skills.md)
- [ClawHub release page](https://clawhub.ai/matsclaes2/skills/viral-outliers)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis, Guidance]

**Output Format:** [Structured API data and natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post metrics, transcripts, visual analyses, comments, creator comparisons, watchlists, and remix ideas. Billable actions use prepaid credits.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
