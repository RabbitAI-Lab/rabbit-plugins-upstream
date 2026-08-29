## Description:

Python package creation and PyPI distribution via pyproject.toml and entry points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for guidance on creating distributable Python libraries and CLI tools, configuring pyproject.toml, managing uv workflows, entry points, and publishing pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing examples can publish packages publicly if copied and run against the production PyPI registry.

Mitigation: Confirm the target registry, inspect package contents, publish to TestPyPI first, and require protected environments or manual approval for production PyPI tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-parseltongue-python-packaging)
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/parseltongue)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline TOML, YAML, Python, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; examples may require user review before execution.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
