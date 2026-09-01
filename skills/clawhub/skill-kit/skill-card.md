## Description:

skill-kit helps Claude Code users create, validate, merge, upgrade, route, publish, and maintain multi-topic skills, including trigger hooks, dependency graphs, language checks, and portability review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use skill-kit to author and maintain Claude Code skills, validate frontmatter, organize multi-topic skill content, inspect dependencies, and prepare public releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can register persistent Claude hook behavior and update local Claude settings.

Mitigation: Use dry-run or list modes before compiling triggers, inspect generated hook scripts, and register hooks only after reviewing their matchers and actions.

Risk: Maintenance workflows such as dedup, convert, merge, and upgrade can modify installed skills, backups, and git state.

Mitigation: Review proposed commands and affected paths before execution, prefer single-skill scopes, and keep backup moves explicit and reversible.

Risk: Generated hook behavior may include environment-specific patterns that are wider than expected for a general user.

Mitigation: Inspect trigger resources and generated dispatchers after compilation, remove private or irrelevant matchers, and keep public skills free of environment-specific references.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [Skills CLI ecosystem](https://skills.sh/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration examples, and generated files where the selected workflow calls for them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or generate edits to skill files, hook scripts, settings, dependency graphs, and validation reports depending on the invoked topic.]

## Skill Version(s):

0.8.0 (source: server release metadata; changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
