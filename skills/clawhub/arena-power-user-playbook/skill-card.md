## Description:

Executable power-user playbook for arena.ai that helps agents choose modes, check leaderboard rotation, screen weak-response flags, carry SESSION-STATE.md across long work, and use cloud-only fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agents, and arena.ai power users use this skill to select the right arena.ai mode, compare a fresh leaderboard dump with a dated snapshot, screen response-quality warning signs, preserve state across long Agent tasks, and choose cloud-only fallback paths when arena.ai is degraded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The README install command executes the latest ClawHub installer from npm.

Mitigation: Use a pinned or verified installer when available, and review the resolved package before installing in sensitive environments.

Risk: The CLI reads and writes local files supplied by the user, including state files, leaderboard dumps, snapshots, and feedback logs.

Mitigation: Pass only files that are appropriate for local processing, use explicit paths, and review generated state or log files before sharing or committing them.

Risk: arena.ai processes prompts server-side when users follow the playbook's product workflow.

Mitigation: Share only data appropriate for arena.ai, and avoid sending confidential or regulated content unless the user's organization permits it.

Risk: The bundled model snapshot is dated and model names or tiers can rotate.

Mitigation: Use the live arena.ai picker or Agent leaderboard before acting on a model choice, and run model-check against a fresh dump.

Risk: The weak-response command reports heuristic screening flags and can produce false positives for legitimate short answers.

Mitigation: Treat flags as review cues rather than quality judgments, use --expect-short for intentionally brief responses, and inspect the flagged response before escalating.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-power-user-playbook)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [arena.ai modes reference](references/modes.md)
- [Agent Arena leaderboard reference](references/leaderboard.md)
- [Fallback and weak-response playbook](references/fallback.md)
- [Dated Agent Arena model snapshot](data/model_snapshot_2026-09-05.json)
- [arena.ai Agent leaderboard](https://arena.ai/leaderboard/agent)
- [Agent Arena methodology](https://arena.ai/blog/agent-arena-methodology)
- [arena.ai Agent Mode](https://arena.ai/blog/agent-mode)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands print one summary line and can write full JSON with --out; state, snapshot, and feedback-log files are created only when explicitly requested.]

## Skill Version(s):

2.0.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
