## Description:

Claudify helps agents create, improve, and preserve Claude Code automations such as agents, skills, rules, commands, hooks, background polling workflows, and persistence routines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to turn recurring work into Claude Code automations, review and improve those automations, manage long-running background work, and preserve useful project knowledge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist session and project knowledge to an unspecified memory or RAG store without asking first.

Mitigation: Enable persistence only with a trusted receiver, review the exact content before storage, and disable or gate the persist and Ralph flows when that receiver is not trusted.

Risk: Hook examples include patterns such as auto-stage, npx execution, forced extension installation, logging, and shared /tmp state.

Mitigation: Require confirmation, use allowlists and pinned local tools, and replace shared /tmp paths with private per-session state paths before adopting those examples.

## Reference(s):

- [Claudify skill page](https://clawhub.ai/drumrobot/skills/claudify)
- [CHANGELOG.md](CHANGELOG.md)
- [background-polling.md](background-polling.md)
- [improve.md](improve.md)
- [persist.md](persist.md)
- [Automation Decision Guide](resources/automation-decision-guide.md)
- [Agent Templates](resources/agent-templates.md)
- [Hook Examples](resources/hook-examples.md)
- [Plugin Creation Guide](resources/plugin-creation.md)
- [Rules Guide](resources/rules-guide.md)
- [Slash Command Syntax Reference](resources/slash-command-syntax.md)
- [AskUserQuestion Usage Patterns](resources/askuserquestion-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include proposed automation files, workflow steps, review notes, and persistence guidance depending on the selected topic.]

## Skill Version(s):

0.9.0 (source: ClawHub release metadata and CHANGELOG, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
