## Description:

用于小红书数据助手、小红书搜索热榜、小红书数据分析、小红书笔记搜索、笔记详情、评论分析、博主数据和博主笔记。覆盖 Xiaohongshu / XHS / RedNote，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Xiaohongshu / XHS / RedNote hot searches, notes, comments, creator profiles, and creator note lists through SocialDataX. It supports content research, note discovery, detail lookup, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Returned note URLs can include xsec_token query parameters that may be sensitive when stored, displayed, or forwarded.

Mitigation: Limit use of full returned note URLs to cases where the user needs to open the note, and treat xsec_token-bearing URLs as sensitive.

Risk: The skill depends on a runtime API key and Node.js/npm tooling for data access.

Mitigation: Keep SOCIALDATAX_API_KEY in the runtime environment, use the official SocialDataX access page, and verify local Node.js/npm availability before running commands.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and returned Xiaohongshu data references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus Node.js/npm; returned note URLs may include xsec_token query parameters and should be treated as sensitive.]

## Skill Version(s):

0.1.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
