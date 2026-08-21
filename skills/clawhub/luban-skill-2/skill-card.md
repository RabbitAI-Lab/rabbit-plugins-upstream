## Description:

Luban Skill helps agents evaluate, optimize, harden, and regression-check AI agent skills using a ten-dimension rubric and adaptive Quick or Full workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to review, score, harden, and iteratively improve agent skill files while preserving auditability and rollback paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated optimization may edit and persist changes across skill repositories beyond a simple review workflow.

Mitigation: Use review-only or dry-run mode for assessment, limit target repositories, and require human approval before broad optimization commands.

Risk: Backup files, git operations, and persistent optimization history can change workspace state.

Mitigation: Run the skill only in repositories where those state changes are acceptable, then inspect diffs, diagnostics, and rollback points before deployment.

Risk: Live URL checking and scheduled or event-driven maintenance can interact with external resources or alter reference material in sensitive workspaces.

Mitigation: Disable or gate live URL checks and scheduled maintenance unless the workspace policy explicitly allows them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ebandao777-oss/skills/luban-skill-2)
- [Server-resolved GitHub provenance](https://github.com/ebandao777-oss/luban-skill)
- [Scenario-Adaptive Dual-Mode Architecture reference](references/SA-DM.md)
- [Module and scheduler reference](references/modules.md)
- [FAQ and anti-patterns](references/faq.md)
- [EvoSkill paper](https://arxiv.org/abs/2603.02766)
- [SkillOps paper](https://arxiv.org/abs/2605.13716)
- [Skill Distill paper](https://arxiv.org/abs/2604.01608)
- [HASP paper](https://arxiv.org/abs/2605.17734)
- [MUSE-Autoskill paper](https://arxiv.org/abs/2605.27366)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON diagnostics, patch guidance, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply skill edits, diagnostics, test cases, backup files, and optimization history depending on mode and user approval.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
