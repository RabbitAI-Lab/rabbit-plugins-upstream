## Description:

Evaluate and improve code with Topos for complexity reduction, structural security checks, and refactor verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Topos to assess code structure, prioritize refactors, and check whether changes improve code-quality scores. Project tests and security review remain necessary before accepting changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation instructions pipe an unpinned remote script into a shell.

Mitigation: Review the installer before execution, prefer a pinned or signed release if available, and do not let an agent run it unattended.

Risk: Registering Topos across agent harnesses can modify configuration, and dependency-graph generation can write .gitnexus files into a repository.

Mitigation: Review configuration changes before using install --all and check generated repository files before committing.

Risk: Structural quality or security scores do not establish functional correctness or complete security coverage.

Mitigation: Run project tests after refactors and use dedicated security tools for security-sensitive code.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub skill listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Code-quality assessments, ranked refactor targets, and suggested changes or commands]

**Output Parameters:** [Medal verdict, pillar scores, refactor targets, and change-assessment status]

**Other Properties Related to Output:** [Dependency-graph generation can write .gitnexus files; source changes require an agent's separate edits.]

## Skill Version(s):

1.0.20 (ClawHub release; artifact frontmatter: 0.11.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
