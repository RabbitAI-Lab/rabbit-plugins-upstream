## Description:

Captures robotics autonomy failures, operational incidents, and engineering learnings to enable continuous improvement across perception, localization, planning, control, simulation, safety, and hardware integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to capture autonomy failures, operational incidents, and reusable engineering learnings in local markdown logs. It supports incident triage and promotion of recurring patterns into safety checklists, calibration playbooks, tuning runbooks, agent guidance, or reusable skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks can persist across sessions or trigger too broadly if configured outside the intended robotics workspace.

Mitigation: Use project-scoped hooks only, keep matchers narrow to robotics terms, and start with the minimal reminder hook before enabling command-output detection.

Risk: Command-output detection may encounter sensitive logs, telemetry, or secrets when PostToolUse is enabled.

Mitigation: Avoid PostToolUse when command output may contain secrets, do not log raw command output, and prefer redacted summaries in learning entries.

Risk: Promoted learnings or extracted skills can introduce incorrect or unsafe operational guidance if accepted without review.

Mitigation: Review diffs before promotion, require explicit user approval, and validate robotics mitigations with simulation, HIL, controlled field checks, and safety review where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jose-compu/skills/self-improving-robotics)
- [Entry examples](references/examples.md)
- [Hook setup guide](references/hooks-setup.md)
- [OpenClaw integration](references/openclaw-integration.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JSON, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local learning entries, issue records, feature requests, hook setup guidance, and optional skill scaffolds for human review.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
