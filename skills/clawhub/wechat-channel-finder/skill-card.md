## Description:

Searches WeChat Channel accounts and posts by keyword, returning account names, post titles, and IDs for competitor, peer, or creator-partner discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to find WeChat Channel accounts or related posts by keyword, then export lookup results for review or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup queries and returned data are sent through api.we-media.cn.

Mitigation: Use only data approved for that third-party service, and avoid sensitive queries or returned records unless policy permits.

Risk: The artifact exposes local-file upload behavior through --file, videoUrl, audioUrl, or local filesystem paths even though uploads are not needed for the lookup purpose.

Mitigation: Do not pass local files or local media paths unless the upload behavior has been removed or explicitly confirmed.

Risk: config.json and cached or output files may contain an API key or paid API results.

Mitigation: Treat configuration, cache, and output files as sensitive; restrict sharing and clean them up according to local data-handling policy.

Risk: Multi-page paid runs may cost more than the displayed estimate.

Mitigation: Review cost estimates before confirmation, require explicit user approval for paid calls, and keep --pages conservative.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-channel-finder)
- [We-Media API](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers and optional report Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a WM_API_KEY; paid calls require confirmation and may cache paid POST responses for 24 hours.]

## Skill Version(s):

1.0.1 (source: server release; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
