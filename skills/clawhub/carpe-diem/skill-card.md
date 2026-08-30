## Description:

Carpe Diem helps developers and creators with a coding agent discover, validate, plan, and read-only track worthwhile open-source project directions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wanghaonan3333-web](https://clawhub.ai/user/wanghaonan3333-web)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill when they need help choosing a project direction, validating an idea against real-world signals, turning a validated direction into an implementation plan, or tracking progress without shifting the agent into implementation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can download code from GitHub and modify local agent skill folders.

Mitigation: Review the install plan with the dry-run flow first, inspect the source and target paths, and install from a trusted local checkout when possible.

Risk: The skill may store confirmed profile facts and project summaries locally.

Mitigation: Grant only narrow read-only access to specific repos, folders, notes, issues, or CI data, and confirm profile or project-state changes before applying them.

## Reference(s):

- [Carpe Diem skill page](https://clawhub.ai/wanghaonan3333-web/skills/carpe-diem)
- [Methodology](references/methodology.md)
- [Safety boundaries](references/safety-boundaries.md)
- [Stage transition graph](references/stage-transition-graph.md)
- [State schema](references/state-schema.md)
- [Claude Code Skills documentation](https://code.claude.com/docs/en/slash-commands)
- [Cursor Skills documentation](https://cursor.com/docs/skills)
- [OpenClaw Skills documentation](https://docs.openclaw.ai/skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Conversational guidance, markdown planning artifacts, and optional shell commands for deterministic state or installation workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is designed to keep project implementation out of scope and to require user confirmation before writing long-term profile or project-plan state.]

## Skill Version(s):

0.2.0 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
