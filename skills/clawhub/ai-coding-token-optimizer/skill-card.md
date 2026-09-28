## Description:

Measures and slims always-loaded agent instructions, then builds task-focused project maps so coding agents can find relevant documentation without repeatedly exploring the repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asif2bd](https://clawhub.ai/user/asif2bd)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use this skill with a repository-capable coding agent to reduce always-loaded instruction context and create maintained, task-specific documentation routes without changing application behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rewriting AGENTS.md or CLAUDE.md can weaken project rules or change future agent behavior.

Mitigation: Review the diff and confirm existing instructions, release gates, and required rules are preserved.

Risk: Project maps could disclose secrets or private paths.

Mitigation: Inspect new documentation for sensitive details before use; keep secrets and private paths out of maps.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/asif2bd/skills/ai-coding-token-optimizer)
- [Skill homepage](https://proskills.md/skills/coding/ai-coding-token-optimizer)
- [Adoption guide](artifact/references/adoption.md)
- [Map templates](artifact/references/templates.md)
- [Verification guide](artifact/references/verification.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown project maps and agent instructions, with a text summary of changes and measured instruction-file sizes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only changes; later savings from reduced rediscovery are not measured.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, CHANGELOG.md, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
