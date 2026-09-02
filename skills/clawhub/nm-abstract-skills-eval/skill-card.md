## Description:

Evaluate Claude skill quality through auditing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to audit Claude skills for structure, quality, token efficiency, activation reliability, tool integration, and concrete improvement opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to run integration tests, benchmarks, scan-all workflows, auto-fix commands, chmod, or pip install steps against skills or repositories under evaluation.

Mitigation: Use it only in a trusted local workspace, review paths and commands before execution, and prefer a sandbox for untrusted skills or repositories.

Risk: Under-scoped evaluation instructions can cause an agent to execute tools from the skill being evaluated.

Mitigation: Treat evaluated artifact files as evidence, review proposed tool execution separately, and avoid executing bundled tools until they have been inspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skills-eval)
- [ClawDis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and evaluation criteria]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces audit workflows, scoring guidance, improvement checklists, benchmarking guidance, and troubleshooting guidance for skill evaluation.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
