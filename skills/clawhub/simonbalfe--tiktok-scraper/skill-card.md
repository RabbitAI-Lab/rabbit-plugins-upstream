## Description:

Access live TikTok data via the CreatorCrawl API. Look up creator profiles, search videos, pull comments and transcripts, track trending hashtags, discover popular songs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simonbalfe](https://clawhub.ai/user/simonbalfe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social media researchers use this skill to retrieve TikTok profiles, videos, comments, transcripts, search results, trends, hashtags, and songs through CreatorCrawl API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok handles, URLs, search terms, and requested lookup parameters are sent to CreatorCrawl.

Mitigation: Use the skill only for TikTok-specific research where sending those inputs to CreatorCrawl is acceptable.

Risk: The skill can retrieve social-media data such as comments, transcripts, followers, and following lists.

Mitigation: Handle returned social-media data according to applicable privacy, consent, and organizational data-use requirements.

Risk: API access depends on a CreatorCrawl API key and account credits.

Mitigation: Configure CREATORCRAWL_API_KEY deliberately and monitor credit use before large or paginated requests.

## Reference(s):

- [CreatorCrawl](https://creatorcrawl.com)
- [ClawHub tiktok-scraper skill](https://clawhub.ai/simonbalfe/skills/tiktok-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with inline curl commands and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CREATORCRAWL_API_KEY and curl; API responses are JSON.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
