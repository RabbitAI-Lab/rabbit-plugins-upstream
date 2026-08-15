## Description:

ChatCut 口播与录屏视频的一句话编排和安全默认层，负责意图路由、四套默认方案、风险分级、代表样片、审批绑定、中断恢复、证据分级与可编辑时间线交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Creators and editing agents use this skill to orchestrate conservative ChatCut talking-head and screen-recording edits from a one-sentence request. It routes stable, fast, professional, review, and resume workflows while preserving approvals, evidence state, recovery checkpoints, and an editable ChatCut timeline handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the active ChatCut project and keeps local run state for recovery.

Mitigation: Use it only when that project access is acceptable; keep run records local, and exclude project details, private terms, and identifiers from public reports.

Risk: Whole-video edits can remove or alter meaning if approval gates are bypassed.

Mitigation: Review the representative sample before expansion and require explicit approval for high-risk edits such as sentence deletion, reordering, privacy changes, generation, export, or publishing.

Risk: The current release does not claim real ChatCut end-to-end production validation.

Mitigation: Treat real writes, rendered pixels, human listening, and production samples as unverified until live canary evidence passes; verify final timelines before export.

Risk: Repository-maintenance commands can modify or publish skill source when used outside normal editing workflows.

Mitigation: Run development or release commands only when intentionally maintaining the skill, and separate that activity from normal ChatCut project execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maojiebc/skills/majia-chatcut-koubo)
- [README.en.md](README.en.md)
- [Official ChatCut Skill Map](workflows/official-skill-map.md)
- [Live Canary Report v1.6.0](reports/live-canary-v1.6.0.json)
- [CHANGELOG](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON-backed workflow artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces editable timeline handoff guidance and local run-state artifacts; it does not export or publish by default.]

## Skill Version(s):

1.6.0 (source: SKILL.md metadata, package.json, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
