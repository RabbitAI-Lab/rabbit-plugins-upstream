## Description:

Researches public Instagram profiles, posts, and Reels through the Crawlora API and returns structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this skill to review public Instagram profile statistics, Reels, and individual post details for influencer vetting and social audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public Instagram identifiers and the Crawlora API key are sent to Crawlora when making requests.

Mitigation: Use only the documented public-profile, Reels, and post-detail endpoints; keep CRAWLORA_API_KEY in the environment and do not commit it.

## Reference(s):

- [Instagram endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/instagram-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text summaries and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public profiles, Reels feeds, and individual post details only; Reels support cursor pagination.]

## Skill Version(s):

1.0.19 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
