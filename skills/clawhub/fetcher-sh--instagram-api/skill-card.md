## Description:

Instagram API guides agents through read-only fetcher.sh calls for public Instagram profiles, posts, reels, stories, followers, comments, hashtags, locations, and audio feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to look up public Instagram profiles and content, export follower-style datasets, monitor hashtags or locations, and compare read-only Instagram data access options without Meta Graph API app review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram query targets and fetcher.sh API credentials or x402 payment details to a third-party service.

Mitigation: Install only when this third-party API use is acceptable, protect the Bearer key, and rotate or revoke credentials if exposed.

Risk: Follower, story, comment, and location queries can collect public social data that may be sensitive in aggregate.

Mitigation: Use the skill only for authorized, privacy-respecting access and retain only the data needed for the stated task.

Risk: Each API call is billed individually and upstream failures may still consume payment.

Mitigation: Test with low-volume calls first, monitor credit balance or x402 spending, and add budget controls before running large polling or export jobs.

## Reference(s):

- [Skill Source](artifact/SKILL.md)
- [Endpoint Reference](artifact/references/endpoints.md)
- [Scenario Cookbook](artifact/references/scenarios.md)
- [FAQ](artifact/references/faq.md)
- [Comparison Guide](artifact/references/comparison.md)
- [OpenAPI 3.1 Contract](https://instagram.fetcher.sh/openapi.json)
- [Condensed Endpoint Catalog](https://instagram.fetcher.sh/llms.txt)
- [Full Agent Setup](https://instagram.fetcher.sh/skill.md)
- [ClawHub Skill Page](https://clawhub.ai/fetcher-sh/skills/instagram-api)
- [Server-Resolved GitHub Provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/instagram-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with curl examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses described by the skill use a JSON envelope with status, message, and data fields.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
