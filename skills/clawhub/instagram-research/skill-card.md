## Description:

Researches Instagram profiles, posts, and Reels via the Crawlora API, returning clean JSON for public Instagram profile, post, and Reels lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and social media analysts use this skill to retrieve public Instagram profile statistics, Reels feeds, and single-post media or engagement details through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted Instagram handle or path could cause the helper to send multiple authenticated Crawlora requests, consuming credits or billing resources.

Mitigation: Reject curl URL-globbing metacharacters and other unsafe path characters before calling the helper, or patch the helper to disable curl globbing.

Risk: The skill depends on a Crawlora API key and public Instagram endpoints.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, avoid hardcoding or committing it, and scope usage to public profiles, posts, and Reels.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns normalized JSON from public Instagram endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
