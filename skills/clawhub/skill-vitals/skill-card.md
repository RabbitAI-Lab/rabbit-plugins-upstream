## Description:

Audits installed Agent Skills across Claude Code, Codex, OpenClaw, Hermes, and Tencent WorkBuddy for runtime visibility, context cost, conflicts, trigger failures, cleanup opportunities, and security risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gold3bear](https://clawhub.ai/user/gold3bear)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to audit local Agent Skill installations, understand which skills are active, diagnose why a skill did not trigger, and identify cleanup, conflict, cost, and security review actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scan reports can expose absolute paths, skill names, usernames, and full skill descriptions that reveal private project or business context.

Mitigation: Use the documented redaction options before sharing output externally, especially name redaction for public issue reports or chat transcripts.

Risk: Security findings are heuristic and cannot prove that an installed skill is safe.

Mitigation: Review flagged file paths, line numbers, and snippets before acting on findings or deploying a skill.

## Reference(s):

- [Skill Vitals on ClawHub](https://clawhub.ai/gold3bear/skills/skill-vitals)
- [README](README.md)
- [Chinese Guide](references/guide.zh-CN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports with inline shell commands; scanner output can also be written as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports separate measured facts, host evidence, estimates, and model judgment; redaction options are available before sharing scan output.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
