## Description:

Lists accessible WeChat Channels live replays and retrieves replay details and engagement metrics for live-stream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to review accessible WeChat Channels live-stream replays, examine engagement, and export findings for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid data service can incur charges for confirmed queries and additional pages.

Mitigation: Estimate current costs, set an explicit page limit, and obtain approval before paid requests.

Risk: A locally stored API key or exported results could be disclosed unintentionally.

Mitigation: Keep the key in local configuration, never paste it into chat or reports, and choose output paths deliberately.

Risk: Pagination failures or temporary replay links can make results incomplete or time-limited.

Mitigation: Label partial results and failed items, and do not present temporary links as permanent.

## Reference(s):

- [Skill listing](https://clawhub.ai/dunkong/skills/wechat-channel-live-replay)
- [曼格云 API guide](https://api.we-media.cn/client/ai-guide)
- [曼格云 product documentation](https://api.we-media.cn/client/products)

## Skill Output:

**Output Type(s):** [Text, Markdown, Data files]

**Output Format:** [Markdown summary with JSON, Markdown, or Excel exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full JSON accompanies exported previews; partial results and actual charges are reported.]

## Skill Version(s):

1.4.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
