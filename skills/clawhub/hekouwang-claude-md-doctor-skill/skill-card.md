## Description:

Audits AGENTS.md or CLAUDE.md runtime configuration files, returns a scorecard with prioritized fixes, and can apply user-approved repairs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to audit project agent runtime configuration files for context cost, actionable guidance, routing, and safety guardrails. It produces a report and prioritized repair plan, with file edits only after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional suite script runs broader sibling skill and local environment checks beyond the core AGENTS.md/CLAUDE.md audit.

Mitigation: Use the core checker for standard audits; run scripts/run-all-doctors.sh only when broader local checks are intentional.

Risk: The skill can propose or apply changes to project runtime configuration files.

Mitigation: Review the generated scorecard and proposed edits before approving file changes.

## Reference(s):

- [Repository homepage](https://github.com/huiyonghkw/hekouwang-claude-md-doctor-skill)
- [Doctor Suite reference](references/doctor-suite.md)
- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-md-doctor-skill)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with optional JSON CLI output and proposed file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run the local checker; proposed file edits require user approval.]

## Skill Version(s):

1.3.1 (source: frontmatter and changelog, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
