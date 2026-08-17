## Description:

Provides reusable patterns for validation, error handling, scaffolding, and skill consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill as a shared reference library for reusable validation, error-handling, testing, scaffolding, troubleshooting, and workflow patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may cause this shared reference skill to load more often than intended.

Mitigation: Use it where reusable development-pattern guidance is appropriate and narrow agent routing or invocation patterns when unnecessary context loading matters.

Risk: The separate parent Claude Code plugin may include agents, hooks, or commands not present in this inspected artifact.

Mitigation: Review and scan the parent plugin separately before installing it or relying on behavior outside this markdown-only artifact.

Risk: Code snippets and command examples are reusable templates and may not fit every caller unchanged.

Mitigation: Review adapted snippets against the target skill, hook, or plugin contract and run the caller's tests before release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-shared-patterns)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Validation Patterns](artifact/modules/validation-patterns.md)
- [Error Handling Patterns](artifact/modules/error-handling.md)
- [Testing Templates](artifact/modules/testing-templates.md)
- [Workflow Patterns](artifact/modules/workflow-patterns.md)
- [Advanced Pattern Composition](artifact/modules/advanced.md)
- [Troubleshooting Shared-Pattern Integration](artifact/modules/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, command examples, tables, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markdown-only reference material; no executable files are present in the inspected artifact.]

## Skill Version(s):

1.9.18 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
