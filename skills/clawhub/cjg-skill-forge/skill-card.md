## Description:

Skill Forge is a meta-skill for creating, upgrading, reviewing, consolidating, and clarifying WorkBuddy and AI agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this meta-skill to build, improve, audit, merge, and organize agent skills. It supports skill creation workflows, review rubrics, release-readiness checks, consolidation planning, and feedback-loop guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default local usage logging may create privacy concerns for users who do not want local signal records.

Mitigation: Set .optin=off before use if local signal logging is not wanted, and review the skill's signal controls before installation.

Risk: Cloud synchronization can transmit or restore anonymous usage signals when explicitly enabled.

Mitigation: Keep .cloud_optin=off unless network sync is desired, and inspect cloud_config.json endpoints before enabling sync.

Risk: Publishing workflows may leak credentials if a skill package contains secrets in configuration files.

Mitigation: Scan skill packages for secrets before publishing and avoid placing API keys or tokens in config.json or other packaged files.

Risk: As a meta-skill, it can guide edits and publishing actions for other skills.

Mitigation: Review generated changes, run validation and security checks, and require explicit approval before applying or publishing skill changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Publisher profile](https://clawhub.ai/user/j-levee)
- [Forge modes](references/forge-modes.md)
- [Skill review rubric](references/skill-review-rubric.md)
- [Skill consolidation](references/skill-consolidation.md)
- [Clarity coverage](references/clarity-coverage.md)
- [Signals](references/signals.md)
- [Security audit](references/security-audit.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce file-edit plans, review findings, checklists, command sequences, and configuration guidance for skill creation, auditing, publishing, and consolidation workflows.]

## Skill Version(s):

3.0.4 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
