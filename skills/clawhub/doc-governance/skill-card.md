## Description:

Installs and runs documentation governance checks that audit source-of-truth layers, decision records, plans, links, tables, and doc/code contract drift in a repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to diagnose documentation governance gaps, install repository-local checks, and keep project documentation aligned with code and decisions. It is most relevant for repositories that maintain ADRs, plans, source-of-truth documents, and API or contract documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: init --yes installs persistent project-local hooks that can block commits or Claude Code file writes when documentation checks fail.

Mitigation: Run init without --yes to preview changes, review and commit hook files intentionally, and remove the hook files plus settings entries if enforcement is no longer wanted.

Risk: Pattern-based documentation checks can miss unusual phrasing or produce findings that require judgment.

Mitigation: Treat a clean run as no issue detected, review findings against the repository context, and configure contract checks and exclusions deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/doc-governance)
- [Documentation governance framework](artifact/framework.md)
- [Incident list](artifact/incidents.md)
- [ADR template guidance](artifact/templates/adr-README.md)
- [Plan template guidance](artifact/templates/plan-README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, terminal-oriented findings, shell commands, and repository files/configuration when init is confirmed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [audit and check are read-only; init --yes can write project-local configuration, scripts, git hooks, Claude Code hooks, and documentation templates.]

## Skill Version(s):

2.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
