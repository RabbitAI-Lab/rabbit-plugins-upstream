## Description:

将用户自备的群聊/私聊导出分析为单页抖音/群聊会话价值报告（硬事实、矛盾、需求原话、动作）。零 IM 登录，不强制云端 Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tars1230](https://clawhub.ai/user/tars1230)

### License/Terms of Use:

MIT

## Use Case:

External users, community operators, researchers, consultants, and agent developers use this skill to inspect chat exports they already possess, inventory available conversations, and generate evidence-linked conversation insight reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat exports and generated reports can contain message excerpts, participant names, and other sensitive personal data.

Mitigation: Run the skill only on local exports you intentionally provide, keep reports private by default, and redact sensitive details before sharing.

Risk: The analysis is heuristic and can produce incomplete or misleading conclusions if treated as final evidence.

Mitigation: Use the report as a review draft and manually verify hard facts, contradictions, demand quotes, and recommended actions before external use.

Risk: Optional cloud ASR configuration can expose the presence of local API-key environment variables or incur external processing if the user chooses that path.

Mitigation: Keep text-chat analysis on the default local path unless link transcription is explicitly needed, and review optional ASR configuration before enabling it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tars1230/skills/douyin-chat-insight)
- [Input formats](references/input-formats.md)
- [Report format](references/report-4block.md)
- [Routing boundaries](references/routing-boundaries.md)
- [How to get exports](references/how-to-get-exports.md)
- [Optional Douyin link ASR](references/optional-douyin-link-asr.md)
- [Security policy](SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Local HTML, Markdown, and JSON reports, plus terminal guidance and optional JSON status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include hard facts, open contradictions, demand quotes, action items, optional enhancement status, and a note that heuristic drafts require human review.]

## Skill Version(s):

0.2.1 (source: frontmatter, release evidence, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
