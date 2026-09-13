## Description:

Opinionated best practices for building Agent Skills - SKILL.md structure, frontmatter, description writing, progressive disclosure, testing, distribution. Use when creating or reviewing a skill, or debugging why one will not trigger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to create, review, validate, and publish Agent Skills with clear frontmatter, concise instructions, useful references, and practical testing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell command examples may be copied into a sensitive project without review.

Mitigation: Review commands before running them and use a restricted environment for sensitive projects.

Risk: The validator example can resolve the latest skills-ref package at runtime.

Mitigation: Pin the validator version when reproducibility or supply-chain control matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/skills-best-practices)
- [Source Homepage](https://github.com/tenequm/skills/tree/main/skills/skills-best-practices)
- [ClawHub publishing](references/clawhub-publishing.md)
- [Agent Skills Spec](https://agentskills.io/specification)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [API Skills Guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; the skill itself does not generate files.]

## Skill Version(s):

0.8.2 (source: frontmatter, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
