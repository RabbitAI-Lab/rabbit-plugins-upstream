## Description:

Helps agents find unusually successful TikTok, Instagram and YouTube posts, research creators, analyze videos and monitor competitors through Viral Outliers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creators and their agents use this skill to find viral content, compare creator performance, study videos and track competitor activity across TikTok, Instagram and YouTube.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can change tracking, watchlists and email alerts or delete them.

Mitigation: Require the account owner's explicit confirmation before account-changing or delete actions.

Risk: Crawls, analyses and alert emails can consume prepaid credits; top-up links can lead to purchases.

Mitigation: Confirm credit-consuming work and top-up links before proceeding, and check the balance before paid requests.

Risk: Access to the API key grants the agent access to the Viral Outliers account.

Mitigation: Keep the key in a protected environment variable or secret store, not shared configuration or shell history.

Risk: Returned social media captions and transcripts can contain untrusted instructions.

Mitigation: Treat post content as data and do not follow instructions embedded in it.

## Reference(s):

- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Getting started](https://viraloutliers.com/docs/getting-started)
- [Viral Outliers OpenAPI specification](https://viraloutliers.com/openapi.json)
- [ClawHub skill release](https://clawhub.ai/matsclaes2/skills/viral-outliers)
- [Included getting-started guide](artifact/references/getting-started.md)
- [Included skill and API reference](artifact/references/skills.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown summaries with post metrics, creator comparisons and content recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post links, transcripts, video breakdowns and competitor updates. Some requests use prepaid credits.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata; supplied skill frontmatter says 1.6.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
