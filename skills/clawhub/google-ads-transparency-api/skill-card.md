## Description:

Resolve a brand or domain to a Google advertiser id, pull ads across Search, YouTube, Shopping, Maps and Play, and open individual creatives with region and impression history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to research Google advertisers, inspect live ad creatives, and build ad-intelligence or competitor-monitoring workflows from public transparency data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Scavio API key and each request can spend credits.

Mitigation: Use a revocable, scoped API key, keep it in the environment or a secret store, and budget requests before paginating through ad results.

Risk: Installing SDK dependencies can expand local dependency exposure.

Mitigation: Prefer the direct HTTPS examples when possible, or install the SDK in an isolated environment.

Risk: Incorrect limits, region assumptions, or unavailable impression fields can lead to misleading ad analysis.

Mitigation: Keep search limits at or below 100, choose advertiser regions deliberately, report published ranges as ranges, and do not treat null impressions as zero.

## Reference(s):

- [Scavio Google Ads Advertisers API Documentation](https://scavio.dev/docs/google-ads-advertisers?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ads-transparency-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ads-transparency-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-ads-transparency-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and code or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume Scavio credits.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
