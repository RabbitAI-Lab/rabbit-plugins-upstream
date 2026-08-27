## Description:

Go naming guidance for packages, identifiers, functions, methods, types, constants, errors, booleans, tests, and related refactoring decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, or refactoring Go code to choose idiomatic names and avoid common naming mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed Go identifier renames can affect public APIs, references across the repository, and downstream callers.

Mitigation: Review proposed renames before applying them and prefer Go-aware rename tooling for changes that cross file or package boundaries.

Risk: Naming guidance may be too broad for a repository with intentional local conventions or generated interoperability code.

Mitigation: Check repository conventions and exempt generated, OS-specific, cgo, or otherwise intentional naming exceptions before changing code.

## Reference(s):

- [ClawHub metadata homepage](https://github.com/samber/cc-skills-golang)
- [Packages, Files & Import Aliasing](artifact/references/packages-files.md)
- [Variables, Booleans, Receivers & Acronyms](artifact/references/identifiers.md)
- [Functions, Methods & Options](artifact/references/functions-methods.md)
- [Types, Constants & Errors](artifact/references/types-errors.md)
- [Test Naming](artifact/references/testing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with code examples and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Go identifier renames or edits that should be reviewed before application.]

## Skill Version(s):

1.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
