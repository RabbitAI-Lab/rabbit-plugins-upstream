## Description:

当用户问"抖音搜一下""这个博主最近发了什么""这条视频评论怎么看""今天抖音热搜是什么"时，使用本技能，分别对应搜索、博主作品、评论、热榜四项能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content researchers, and marketing teams use this skill to collect structured public Douyin search results, creator posts, comments, and trending-list data for content research, competitor analysis, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk public-data collection and automatic local result retention can preserve sensitive research topics, search terms, posts, or comment datasets longer than intended.

Mitigation: Use the skill only for lawful public Douyin research and periodically delete generated logs when retained datasets are no longer needed.

Risk: Broad activation wording can cause the skill to run for ambiguous non-Douyin research prompts.

Mitigation: Confirm that the user wants Douyin data before running commands when the prompt does not explicitly mention Douyin.

Risk: Authentication failures may show vendor contact information even though the skill text says runtime auth errors should remain neutral.

Mitigation: Review auth-failure output before deployment and avoid exposing promotional contact text in automated user-facing flows.

Risk: The skill depends on a private API token for an external service.

Mitigation: Keep GUAIKEI_API_TOKEN private, provide it only through the environment, and do not copy it into prompts, logs, or source files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-posts-for-content-research)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; executed commands produce structured JSON and local JSON logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js >= 16.14. Output schemas are provided under assets/.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
