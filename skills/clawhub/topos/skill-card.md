## Description:

Evaluate and improve code with Topos through complexity reduction, structural security checks, and refactor verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Topos to assess local code quality, prioritize structural refactors, and check whether changes improve measured results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install command runs an unpinned remote shell script.

Mitigation: Prefer a versioned or package-manager installation; otherwise inspect the downloaded script, verify its provenance where possible, and avoid elevated privileges.

Risk: Structural scores may not reveal incorrect behavior or all security issues after a refactor.

Mitigation: Treat findings as advisory and run the project's usual tests and security checks after proposed changes.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub skill listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, JSON, Shell commands, Guidance]

**Output Format:** [CLI tables and ranked file lists, or structured MCP results]

**Output Parameters:** [Medal verdict, pillar scores, ranked refactor targets, and change assessment status]

**Other Properties Related to Output:** [Results are advisory; dependency graph artifacts may be generated during analysis.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; skill documentation states 0.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
