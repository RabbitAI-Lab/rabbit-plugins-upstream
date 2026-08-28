## Description:

This skill supports pre-campaign audience quality and follower-authenticity analysis across TikTok, Instagram, and YouTube, including geography, language, age, gender, interests, and creator comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, creator partnerships, and analyst teams use this skill to evaluate whether an influencer's audience matches campaign targeting before committing spend. It produces fit scores, confidence, dimension-by-dimension breakdowns, and go/test/no-go recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator identifiers, campaign-fit queries, optional custom headers, and a stable install identifier may be sent to the configured Scrumball gateway.

Mitigation: Use a trusted gateway, avoid unnecessary custom headers, and only submit creator or campaign data that is appropriate to share with that service.

Risk: Audience-demographic and follower-authenticity outputs are inferred analytics that may be sensitive or incomplete.

Mitigation: Treat results as decision support, review the confidence score and missing dimensions, and validate important campaign decisions with additional evidence.

Risk: A local .env file may contain an API key for expanded quota.

Mitigation: Use a dedicated API key and keep .env files out of source control.

Risk: Overriding SCRUMBALL_BASE_URL can redirect requests to another endpoint.

Mitigation: Only override SCRUMBALL_BASE_URL when the endpoint is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-audience-fit-scoring)
- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with scores, confidence notes, recommendations, and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a configurable remote Scrumball gateway and may require creator identifiers such as TikTok unique_id, Instagram username, or YouTube channel_id.]

## Skill Version(s):

1.0.3 (source: server release evidence and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
