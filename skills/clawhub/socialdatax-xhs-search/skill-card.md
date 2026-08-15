## Description:

用于小红书数据分析、小红书笔记搜索、关键词检索、内容调研、竞品分析和趋势研究，覆盖 Xiaohongshu / XHS / RedNote note search，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Xiaohongshu / XHS / RedNote notes for keyword research, content planning, competitor research, market observation, and trend scanning through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key and executes the SocialDataX npm package through npx or npm.

Mitigation: Install and run it only in environments where providing SOCIALDATAX_API_KEY and executing the package are acceptable.

Risk: Returned Xiaohongshu note URLs may include xsec_token query parameters that can be sensitive when stored or forwarded.

Mitigation: Treat returned note URLs as sensitive output and share or persist them only where those query tokens are appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search)
- [SocialDataX API Access](https://socialdatax.com/ai?from=clawhub)
- [Publisher Profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and summarized search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm or compatible MCP tool access; returned note URLs may include xsec_token query parameters.]

## Skill Version(s):

0.1.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
