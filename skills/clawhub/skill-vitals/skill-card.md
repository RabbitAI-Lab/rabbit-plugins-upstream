## Description:

Audit installed Agent Skills across Claude Code, Codex, OpenClaw, Hermes, and Tencent WorkBuddy to identify inventory, runtime visibility, context cost, trigger failures, cleanup opportunities, conflicts, and security risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gold3bear](https://clawhub.ai/user/gold3bear)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent administrators use this skill to audit installed Agent Skills for visibility, context budget, semantic overlap, copy precedence, trigger evidence, structure, and security posture. It helps decide which skills to revise, merge, keep, or remove after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects local skill directories and host state, and scan output may include absolute paths, usernames, skill names, descriptions, and usage evidence.

Mitigation: Use the documented redaction options before sharing reports and treat unredacted scan output as private.

Risk: Security findings are heuristic and can include false positives or false negatives.

Mitigation: Review flagged lines manually and treat scanner output as triage rather than a complete security audit.

## Reference(s):

- [Chinese workflow guide](references/guide.zh-CN.md)
- [Skill Vitals ClawHub page](https://clawhub.ai/gold3bear/skills/skill-vitals)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report with shell command examples and optional JSON scan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates measured facts, host evidence, estimates, and model judgment; supports redacted reports before sharing.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
