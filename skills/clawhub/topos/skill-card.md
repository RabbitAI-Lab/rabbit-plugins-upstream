## Description:

Evaluate and improve code with Topos for complexity reduction, structural security checks, and refactor verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Topos to assess local code quality, identify structural issues, and check whether refactors improve code without sacrificing correctness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation instructions pipe an unpinned remote script directly to bash.

Mitigation: Review the installer before running it and prefer a pinned release or package-manager installation when available.

Risk: Installing across all supported agent harnesses may change more configurations than intended.

Mitigation: Avoid `topos install --all` unless registration across all supported harnesses is desired.

Risk: Structural security scores may be mistaken for a full security audit.

Mitigation: Treat scores as advisory and use dedicated security review for high-stakes code.

Risk: Suggested structural refactors may change program behavior.

Mitigation: Review changes and run relevant project tests or linters after each edit.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent guidance](https://docs.krv.ai/topos/agents.html)
- [ClawHub skill listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown guidance with suggested commands and summarized assessment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structural scores and refactor suggestions are advisory; verify behavior with project tests.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release; skill frontmatter says 0.9.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
