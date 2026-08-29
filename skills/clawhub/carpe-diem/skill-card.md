## Description:

Helps developers and creators who have access to a coding agent but no clear project direction discover, validate, plan, and later track a worthwhile open source project; it is for project guidance, not feature implementation or business-code writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wanghaonan3333-web](https://clawhub.ai/user/wanghaonan3333-web)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill when they want an agent to help turn vague interests, available skills, and real-world evidence into a concrete open source project plan. It guides discovery, validation, planning, and progress tracking while keeping implementation work outside the skill's scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local profile and project-planning state can contain sensitive personal or project context.

Mitigation: Review proposed summaries or diffs before approving writes, and avoid saving secrets, tokens, passwords, full private materials, or unauthorized source copies.

Risk: Installation and state commands write files to local skill, profile, or project-state locations.

Mitigation: Review generated install plans before applying them, confirm source and target paths, and approve only local reads and writes you understand.

Risk: Project validation and tracking guidance may be incomplete when evidence is unavailable or weak.

Mitigation: Keep evidence, agent inference, and unknowns separate; mark validation incomplete when sources are insufficient; use read-only evidence collection unless the user explicitly approves a state update.

## Reference(s):

- [Carpe Diem Skill Page](https://clawhub.ai/wanghaonan3333-web/skills/carpe-diem)
- [Methodology](references/methodology.md)
- [Safety Boundaries](references/safety-boundaries.md)
- [State Schema](references/state-schema.md)
- [Discover Stage](references/stages/discover.md)
- [Validate Stage](references/stages/validate.md)
- [Plan Stage](references/stages/plan.md)
- [Track Stage](references/stages/track.md)
- [OpenAI Agent Skills](https://github.com/openai/skills)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/slash-commands)
- [Cursor Agent Skills Documentation](https://cursor.com/docs/skills)
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with optional shell commands and generated planning documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project-plan, project-handoff, and progress-summary Markdown drafts after user confirmation.]

## Skill Version(s):

0.1.0 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
