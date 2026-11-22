## Description:

Searches TikTok’s public videos by keyword, retrieves a creator’s public posts, and collects comments into structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Creators, marketers, and researchers use this skill to discover TikTok trends, review public creator posts, monitor competitors, plan content, and summarize video comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the release benign but noted that 12 of 32 components were only partially assessed.

Mitigation: Review the packaged components before deployment, especially if adapting the scripts or running them in a sensitive environment.

Risk: Search terms or TikTok links and the API token are sent to the Guaikei data service to retrieve results.

Mitigation: Use the service only for data you are comfortable sharing with it, and keep GUAIKEI_API_TOKEN private.

Risk: Results may contain public usernames and comment text that can identify people.

Mitigation: Check permissions before external or commercial publication and anonymize personal details where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-video-search)
- [Service and token information](https://www.guaikei.com)
- [Options and parameters](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [Structured JSON response envelope containing search results, creator posts, or video comments.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include public video, creator, engagement, and comment fields; an empty result is returned as a normal response.]

## Skill Version(s):

1.1.2 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
