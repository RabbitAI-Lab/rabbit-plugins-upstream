## Description:

Installs and audits a repository documentation governance system that checks source-of-truth layering, decision records, planning state, references, links, tables, and documented contracts against code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to diagnose documentation drift in a repository and install optional local checks that keep plans, decisions, links, tables, and documented contracts aligned with code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: init can install persistent repository-local hooks that block commits or new plan files.

Mitigation: Run init without --yes first, review the planned changes, and use --yes only after the team accepts the hook behavior.

Risk: Installed enforcement can become unwanted after project workflow changes.

Mitigation: Remove the generated .githooks and Claude Code hook registrations from .claude/settings.json when persistent documentation gates are no longer needed.

Risk: Pattern-based documentation checks can miss unusual phrasing or report findings that need interpretation.

Mitigation: Treat a clean run as no detected drift, and review red findings against the documented incident context before changing code or docs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/doc-governance)
- [Documentation governance framework](framework.md)
- [Incident traceability reference](incidents.md)
- [Decision record template README](templates/adr-README.md)
- [Plan template README](templates/plan-README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, audit findings, check results, and repository-local file changes when init is approved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [audit and check are read-only; init writes configuration, a governance script copy, hooks, and templates only when approved with --yes.]

## Skill Version(s):

2.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
