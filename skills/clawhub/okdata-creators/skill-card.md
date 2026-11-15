## Description:

Find and vet creators and KOLs for a niche on Douyin, Xiaohongshu (RedNote), TikTok, X (Twitter) and Weibo with the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users can find creators in a niche across supported social platforms, then review public profile details, recent posts, engagement, and links to build a shortlist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes external API requests that require an okdata API key.

Mitigation: Use the API only if you trust the provider, supply the key through the configured environment, and never expose it in chat or logs.

Risk: Creator searches and profile checks can incur API charges.

Mitigation: Estimate the calls and cost before running them, and ask before exceeding the documented $1 threshold unless the user has set a budget.

Risk: The security review is benign with medium confidence but incomplete because referenced local paths were unavailable during scanning.

Mitigation: Review the missing referenced paths and confirm the API behavior fits the intended use before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-creators)
- [okdata API documentation](https://okdata.online/apis/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown shortlist with creator links, profile and engagement details, fit notes, and source information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The number of candidates and platforms depend on the user's request.]

## Skill Version(s):

0.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
