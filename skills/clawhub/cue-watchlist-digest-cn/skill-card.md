## Description:

根据用户维护的自选清单和转写事件生成带官方出处与时点的每日增量摘要。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向希望逐日核对自选公司的公告和公司行动的用户。用户提供公司清单及事件数据后，可生成今日新增、近端变化和需人工核对的日报，并保留来源索引与运行记录。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuring CUE_API_KEY can expose the credential to an unintended destination during connection setup.

Mitigation: Leave the key unset and use local event files until authenticated setup enforces HTTPS, approved destinations, and safe redirect handling in both connection methods.

Risk: External installation sources may introduce unreviewed code.

Mitigation: Review and pin external installation sources before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-watchlist-digest-cn)
- [Cue data channel configuration](https://cuecue.cn/hub/mcp)
- [Cue document parsing configuration](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL]

**Output Format:** [Markdown daily digest with JSON run records and a JSONL source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-watchlist daily increment with source links and as-of times; explicitly reports when a search window returns no new items.]

## Skill Version(s):

0.2.24 (source: SKILL.md frontmatter, CHANGELOG released 2026-10-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
