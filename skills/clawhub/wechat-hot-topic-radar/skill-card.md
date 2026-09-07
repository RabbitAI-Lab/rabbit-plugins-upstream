## Description:

选题灵感雷达（部分免费）：全网热搜榜（微博/抖音/知乎/头条/百度）、低粉爆文榜单、搜一搜联想推荐词，帮助内容运营快速找到可写、可拍的热点选题方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content operators use this skill to query current hot-search lists, low-follower viral content, and WeChat search suggestion terms for topic planning. It helps identify timely writing or short-video angles and can export the returned results for review or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or reads a We-Media API key from local config.json or WM_API_KEY and sends queries and returned data to api.we-media.cn.

Mitigation: Install only when that data flow is acceptable; use a scoped API key where possible and remove the local key when the skill is no longer needed.

Risk: The security evidence flags an under-disclosed local-file upload path.

Mitigation: Do not use --file with this skill unless the publisher clearly documents and fixes the upload flow.

Risk: The security evidence notes a broader shared API surface than the visible topic-radar workflow.

Mitigation: Review the bundled scripts and endpoint catalog before installation; publishers should remove or isolate unused upload and media endpoints.

Risk: Bundled Python bytecode is present in the artifact.

Mitigation: Prefer source-only releases and remove bundled __pycache__ files before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-hot-topic-radar)
- [We-Media API site](https://api.we-media.cn)
- [We-Media API key registration](https://api.we-media.cn?source=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a We-Media API key in local config or WM_API_KEY; Excel export requires openpyxl.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
