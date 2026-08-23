## Description:

Skill Forge is a meta-skill for creating, upgrading, reviewing, consolidating, and clarifying WorkBuddy or AI agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and agent operators use this skill to turn methods, tools, and existing skill folders into reusable skills, then review, refine, package, publish, or consolidate them with explicit quality and safety gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default local telemetry and session hooks can create persistent method-level usage records.

Mitigation: Install only if this local recordkeeping is acceptable; use the provided controls to view, turn off, or delete local signals.

Risk: Optional cloud sync can send anonymous method-level signals to configured cloud endpoints after opt-in.

Mitigation: Keep cloud sync disabled unless desired, review endpoint configuration before enabling it, and use the stop-control described by the skill to turn cloud sync off.

Risk: Publishing, test, proposal, and telemetry-injection workflows can affect target skill directories or depend on local creator tokens.

Mitigation: Review the target skill directory, endpoint configuration, and local creator tokens before running those scripts, and scan the skill before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Skill definition](artifact/SKILL.md)
- [Intro](artifact/references/intro.md)
- [Discovery](artifact/references/discovery.md)
- [Forge modes](artifact/references/forge-modes.md)
- [Skill review rubric](artifact/references/skill-review-rubric.md)
- [Skill consolidation](artifact/references/skill-consolidation.md)
- [Signals](artifact/references/signals.md)
- [Security audit](artifact/references/security-audit.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code blocks, JSON or YAML-style schemas, shell commands, and file edits when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify skill files, run local validation or publishing scripts, and produce review reports or consolidation plans during requested workflows.]

## Skill Version(s):

3.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
