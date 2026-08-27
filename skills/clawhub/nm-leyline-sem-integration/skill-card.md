## Description:

Provides sem semantic-diff detection, install-on-first-use, and fallback patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when building or modifying skills that consume git diff output and need sem semantic diffs, install-on-first-use guidance, or file-level fallback patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may appear in broad git-related workflows and suggest optional sem installation.

Mitigation: Only accept the optional sem installation when semantic diff support is needed and the installation source is acceptable for the environment.

## Reference(s):

- [sem CLI](https://github.com/Ataraxy-Labs/sem)
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-sem-integration)
- [Publisher profile](https://clawhub.ai/user/athola)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sem CLI detection, optional install commands, normalized diff-output schema, and fallback impact-analysis patterns.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
