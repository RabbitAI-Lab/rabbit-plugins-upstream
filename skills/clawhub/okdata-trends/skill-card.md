## Description:

See what is trending right now on Douyin, Weibo, Bilibili, Xiaohongshu (RedNote), X (Twitter) and TikTok with the okdata API: hot search boards with rank and heat, then the posts behind a topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to compare current hot topics across social platforms and inspect representative posts behind selected topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes external API requests to api.okdata.online using OKDATA_API_KEY; the security review was partial and its evidence is incomplete.

Mitigation: Confirm that you trust the API host before installation, keep the key in the environment, and never show, log, or echo it.

## Reference(s):

- [okdata hot search service](https://okdata.online/tools/hot-search/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-trends)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text]

**Output Format:** [Markdown with ranked topic lists and linked post summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Snapshot data changes quickly; platform heat scores are not directly comparable, and a single read cannot establish a trend.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
