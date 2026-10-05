## Description:

Researches public Instagram profiles, posts, and Reels through the Crawlora API and returns structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can inspect public Instagram profiles, review Reels feeds, and check individual posts for influencer vetting or social-media audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and requested Instagram identifiers are sent to a third-party service.

Mitigation: Use an environment variable for the key and make requests only when disclosure to Crawlora is acceptable.

Risk: Sensitive investigative targets or private content may create inappropriate disclosure or access expectations.

Mitigation: Limit use to public content and avoid submitting sensitive targets or login and session data.

## Reference(s):

- [Instagram endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Instagram Research on ClawHub](https://clawhub.ai/crawlora-org/skills/instagram-research)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [JSON results with optional natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public profile, post, and Reels data; Reels results support cursor-based pagination.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
