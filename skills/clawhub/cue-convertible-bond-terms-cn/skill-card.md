## Description:

将一份 A 股可转债募集说明书或发行公告整理为八项逐字条款卡，附原文锚点并标出缺失项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要核对 A 股可转债文件的外部用户，整理募集说明书或发行公告中的八项条款及其原句和来源锚点。收益、赎回结果、评级和交易决策留给人工核验。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security evidence flags remote-service checks and credential handling, including validation of the bearer-key destination.

Mitigation: Review the remote-service behavior and validate the key destination before providing CUE_API_KEY.

Risk: The security evidence flags document handling when content may be sent for external parsing.

Mitigation: Confirm what document content is sent to the parsing service before using that path.

Risk: The security evidence reports an unpinned installation method and a partial scan with an unresolved local path-like reference.

Mitigation: Use a reviewed, pinned installer and repository revision; the partial scan does not establish that the artifact is safe.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-convertible-bond-terms-cn)
- [Convertible bond clause reference](artifact/references/cb-clauses.md)
- [Cue MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown clause card with source quotations and anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight clause entries; missing information is marked 未检索到, and investment judgments are reserved for human review.]

## Skill Version(s):

0.1.3 (source: release evidence, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
