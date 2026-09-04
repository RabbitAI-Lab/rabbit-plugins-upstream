## Description:

Claude Skill Doctor checks Claude/Agent Skill directories for SKILL.md quality, trigger clarity, progressive disclosure, portability, security hygiene, host compatibility, and produces a scorecard with prioritized fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill maintainers use this skill to audit Agent Skill packages, run local SKILL.md quality checks, review JSON or text reports, and receive concrete remediation guidance before release or CI adoption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional trigger evaluation calls the Claude CLI and can incur user-side cost.

Mitigation: Run trigger evaluation only when needed, start with a small eval set, and review expected cost before increasing samples or runs.

Risk: The suite wrapper expects related doctor skills in the local skills directory and runs checks across selected project paths.

Mitigation: Confirm HEKOUWANG_SKILLS_DIR and target paths before running the suite on broad directories or CI jobs.

Risk: Reports and remediation guidance can influence future skill behavior if applied without review.

Mitigation: Review suggested edits, re-run the checker, and scan the updated skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill)
- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill)
- [Doctor suite reference](references/doctor-suite.md)
- [Trigger evaluation reference](references/trigger-eval.md)
- [Skill writing vocabulary reference](references/skill-writing-vocab.md)
- [SkillSpector](https://github.com/NVIDIA/skillspector)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text reports, optional JSON reports, shell commands, and prioritized remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scores, grades, gate status, PASS/WARN/FAIL/INFO counts, references, and suggested edits; optional trigger evaluation invokes the Claude CLI and can incur user-side cost.]

## Skill Version(s):

1.8.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
