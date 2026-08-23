## Description:

用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research Kuaishou/Kwai short-video content, creator profiles, creator works, video details, comments, and comment replies through the SocialDataX CLI or matching MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime calls require SOCIALDATAX_API_KEY and may send requested Kuaishou/Kwai research parameters to SocialDataX.

Mitigation: Use an intended SocialDataX account key, store it in the environment only, and avoid embedding credentials in prompts, files, or command history.

Risk: API usage may consume SocialDataX account credits, especially when commands request multiple pages, all comments, replies, or creator work lists.

Mitigation: Confirm scope before broad collection, monitor account balance, and follow the skill guidance to avoid repeated retries on insufficient-balance responses.

Risk: The preferred CLI examples use npm package execution at runtime.

Mitigation: Run only in environments where Node.js/npm execution is approved and review or pin the package according to local dependency controls.

## Reference(s):

- [SocialDataX API Access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou)
- [ClawHub Publisher Profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and SocialDataX CLI or MCP usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, npx package execution, and SOCIALDATAX_API_KEY for runtime data calls.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
