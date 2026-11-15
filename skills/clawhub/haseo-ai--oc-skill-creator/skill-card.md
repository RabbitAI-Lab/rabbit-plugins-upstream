## Description:

Create, edit, improve, tidy, review, audit, or restructure OpenClaw AgentSkills and SKILL.md files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haseo-ai](https://clawhub.ai/user/haseo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, review, audit, and restructure OpenClaw skills. It guides skill design from pattern analysis through SKILL.md authoring, testing, and iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workspace skills can persist and auto-load in later agent sessions, which may change future agent behavior.

Mitigation: Review generated SKILL.md files before use, especially the trigger description, language policy, and scope of future agent instructions.

Risk: A generated or revised skill may encode incomplete style, validation, or sub-agent context guidance.

Mitigation: Validate the skill against the documented 5-step process and run a skill audit or security scan before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haseo-ai/skills/oc-skill-creator)
- [OpenClaw vs Codex Skill Creator](references/openclaw-vs-codex.md)
- [Validation example: summarize](examples/summarize.md)
- [Validation example: changelog](examples/changelog.md)
- [Validation example: scaffold](examples/scaffold.md)
- [Validation example: screenshot-capture](examples/screenshot-capture.md)
- [Validation example: unit-converter](examples/unit-converter.md)
- [Validation example: skill-audit](examples/skill-audit.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, checklists, and file specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or revise SKILL.md files, references, examples, and review guidance for OpenClaw skills.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
