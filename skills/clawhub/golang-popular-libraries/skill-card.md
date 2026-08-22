## Description:

Recommends production-ready Golang libraries and frameworks when developers ask for library suggestions, compare alternatives, choose a library for a task, or add a new dependency to a Go project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose Go standard library features, third-party packages, and development tools with attention to maturity, maintenance, performance, dependency footprint, and project fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend new Go dependencies that later prove unsuitable, unmaintained, vulnerable, or unnecessarily broad for the project.

Mitigation: Review each recommendation before adoption, verify package maintenance and vulnerability status, and prefer standard library options when they satisfy the requirement.

Risk: The skill can suggest Go tooling commands and code or configuration changes in projects where those tools are available.

Mitigation: Run suggested commands only in expected Go workspaces and review generated code, dependency, and configuration changes before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-popular-libraries)
- [Declared homepage](https://github.com/samber/cc-skills-golang)
- [Standard Library - New & Experimental](references/stdlib.md)
- [Top Go Libraries by Category](references/libraries.md)
- [Go Development Tools](references/tools.md)
- [Awesome Go](https://github.com/avelino/awesome-go)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with package recommendations, tradeoff analysis, code examples, and Go tooling commands when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should prefer the Go standard library when sufficient and should ask the developer before recommending abandoned or unmaintained libraries.]

## Skill Version(s):

1.2.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
