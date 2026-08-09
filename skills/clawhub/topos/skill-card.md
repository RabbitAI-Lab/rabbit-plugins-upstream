## Description:

Evaluate and improve code with Topos. Use for complexity reduction, security checks, refactor verification, and PLATINUM/GOLD goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding agents use Topos to evaluate local repositories, identify structural code-quality issues, verify refactors, and optimize toward PLATINUM or GOLD goals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topos analyzes local repository code and can create .gitnexus artifacts during dependency graph generation.

Mitigation: Run it only in repositories where local analysis and generated graph artifacts are acceptable; review generated artifacts before committing them.

Risk: The optional MCP installation can modify agent harness configuration.

Mitigation: Use the MCP install command only after reviewing the installation path and verify the resulting harness configuration with `topos status`.

Risk: Topos security and refactor scores are advisory structural signals, not proof of functional correctness or complete security coverage.

Mitigation: Run project tests, linters, and appropriate security tools before accepting or shipping code changes based on Topos guidance.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [CLI tables, ranked file lists, Markdown guidance, MCP structured payloads, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .gitnexus graph artifacts when dependency graph generation is used; does not modify source files unless the agent chooses to edit based on the guidance.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 0.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
