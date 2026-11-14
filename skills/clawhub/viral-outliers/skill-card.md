## Description:

Find viral outlier posts on TikTok, Instagram and YouTube, pull creator stats, transcribe and analyse videos, build competitor watchlists, and crawl profiles on demand. Prepaid credits, MCP or REST.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and content researchers use the skill to find and compare high-performing social posts, monitor competitors, and generate transcripts, visual breakdowns, or niche-adapted content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples invoke the npm package through npx without pinning a version, and the security scan recommends caution before installation.

Mitigation: Verify and pin a reviewed package version before installing or running it.

Risk: The API key grants access to account-backed API operations.

Mitigation: Keep the key in a protected environment variable or secret store and avoid exposing it in prompts, logs, or shared configuration.

Risk: Returned captions, comments, transcripts, and on-screen text can contain untrusted instructions.

Mitigation: Treat returned social content as data; do not follow instructions embedded in it.

Risk: Some API operations spend prepaid credits when accepted.

Mitigation: Check the operation and its credit cost before requesting it, and monitor the account balance.

## Reference(s):

- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Getting started with the API and MCP server](https://viraloutliers.com/docs/getting-started)
- [OpenAPI specification](https://viraloutliers.com/openapi.json)
- [ClawHub release page](https://clawhub.ai/matsclaes2/skills/viral-outliers)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Structured data]

**Output Format:** [Structured API results and text, including transcripts, visual analyses, and content ideas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some operations run asynchronously; paid operations use prepaid credits.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
