## Description:

Researches public social profiles, posts, trends, Facebook Marketplace listings, and explicitly requested Reddit buying-intent leads through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to research public social activity, compare profiles and engagement, monitor trends, and perform clearly requested public listing or Reddit lead searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and requested search terms, handles, URLs, locations, or listing targets are sent to Crawlora.

Mitigation: Use a dedicated API key and send only public, nonsensitive research targets; avoid confidential investigations and sensitive personal data.

Risk: Public social data or Reddit lead scores could be misused for sensitive targeting or high-impact decisions.

Mitigation: Run lead discovery only when explicitly requested, disclose post-level scoring, and do not infer sensitive traits or make high-impact targeting decisions from results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/social-media-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with optional shell examples and JSON excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research is based on public data returned by Crawlora; list results may require pagination and coverage varies by platform.]

## Skill Version(s):

1.0.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
