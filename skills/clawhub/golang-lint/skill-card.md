## Description:

Provides Go linting guidance for golangci-lint configuration, running linters, interpreting warnings, suppressing warnings with justified nolint directives, and selecting linters for Go projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure and run golangci-lint, adopt linting in existing Go codebases, interpret linter output, and apply or avoid suppressions with documented justification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-fix lint workflows can change Go code behavior or formatting unexpectedly.

Mitigation: Review diffs and run project tests before committing generated changes.

Risk: Parallel legacy cleanup can produce overlapping edits across linter categories.

Mitigation: Merge cleanup in small batches and rerun golangci-lint after resolving conflicts.

Risk: Suppressing lint warnings can hide correctness or security issues.

Mitigation: Require named //nolint directives with justification and avoid suppressing security or resource-leak linters unless strongly justified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-lint)
- [Project Homepage](https://github.com/samber/cc-skills-golang)
- [Linter Reference](references/linter-reference.md)
- [Nolint Directives](references/nolint-directives.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline Go, YAML, Bash, and Makefile snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits, lint commands, configuration changes, and cleanup workflows for Go projects.]

## Skill Version(s):

1.4.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
