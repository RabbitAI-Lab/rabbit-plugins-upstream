## Description:

Token Optimizer helps agents audit local OpenClaw token usage, identify high-context sessions, excessive calls, main-session cron jobs, and oversized workspace Markdown, and propose optimization steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lilozhao](https://clawhub.ai/user/lilozhao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to diagnose OpenClaw token consumption from local usage logs and workspace file sizes. It supports review of findings and cautious optimization steps such as session archiving, cron isolation, and Markdown slimming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagnostic reads local OpenClaw session usage logs and workspace context file metadata.

Mitigation: Run the read-only audit commands first and review outputs manually before taking action.

Risk: A Markdown slimming helper can modify files outside the intended workspace when used with unsafe paths.

Mitigation: Do not run md-slim.js --apply with absolute paths or paths containing .. until path containment is fixed.

Risk: The documentation discusses high-risk cross-agent write and shell delegation patterns.

Mitigation: Avoid cross-agent write or shell delegation unless the receiving owner explicitly approves the action.

## Reference(s):

- [Token Optimizer ClawHub Page](https://clawhub.ai/lilozhao/skills/token-optimizer)
- [Token Optimization Methodology](artifact/docs/methodology.md)
- [Self-Serve Playbook](artifact/docs/self-serve-playbook.md)
- [Cross-Agent Token Optimization Case Study](artifact/docs/case-cross-agent.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON diagnostic reports with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools are read-only by default; write-capable flows require explicit apply flags and user review.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
