## Description:

Evaluate and improve code with Topos. Use for complexity reduction, security checks, refactor verification, and PLATINUM/GOLD goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding agents use this skill to assess local repositories, identify structural code quality issues, verify refactors, and work toward Topos PLATINUM or GOLD quality goals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow asks users to execute a remote installer and install global npm tooling.

Mitigation: Review the installer source and provenance before running it, and prefer a pinned, checksum-verified Topos release when available.

Risk: The optional MCP setup can register Topos broadly across supported agent harnesses.

Mitigation: Register the MCP server only in the specific agent harness where it is needed instead of using broad registration.

Risk: Topos structural scores can guide refactors that still change application behavior.

Mitigation: Run the project's tests or linters after edits and treat Topos results as structural guidance rather than functional proof.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos)
- [Publisher profile](https://clawhub.ai/user/krv-labs)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [CLI tables, ranked file lists, MCP structured payloads, markdown reports, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write .gitnexus graph artifacts when dependency graph generation is used; the skill itself does not modify source files unless an agent acts on its guidance.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact frontmatter reports 0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
