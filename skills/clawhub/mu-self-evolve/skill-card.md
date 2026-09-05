## Description:

AI Agent continuous self-evolution system for daily experience logging, weekly error reflection, VFM verification, score-based memory eviction, WHERE x WHY pathology archiving, and draft skill synthesis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to help an LLM agent keep local learning logs, extract corrections and errors from daily work, verify recurring patterns before promotion, and summarize ongoing self-improvement activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can set up recurring agent runs that rewrite local memory files and retain conversation or error details.

Mitigation: Review or disable the cron/crontab setup, keep learning logs out of sensitive projects where possible, and avoid recording secrets or detailed token state.

Risk: Self-reflection output can promote incorrect or misleading rules into long-term memory or new skill drafts.

Mitigation: Inspect proposed memory updates, archive decisions, and generated skill drafts before promoting them or installing derivative skills.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/muippt/skills/mu-self-evolve)
- [File structure and taxonomy](references/file-structure.md)
- [Record templates](references/record-templates.md)
- [Weekly reflection workflow](references/weekly-reflection.md)
- [Claude Code compatibility](references/claude-code-compat.md)
- [Project landing page](https://muippt.github.io/mu-self-evolve/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local-memory workflows, verification commands, cron setup guidance, and draft skill scaffolding suggestions for human review.]

## Skill Version(s):

3.0.1 (source: server release metadata; artifact frontmatter 3.0 and changelog 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
