## Description:

Comprehensive documentation guide for Golang projects, covering godoc comments, README, CONTRIBUTING, CHANGELOG, Go Playground, Example tests, API docs, and llms.txt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write or review documentation for Go libraries, applications, and CLIs, including doc comments, README files, contribution guides, changelogs, examples, API documentation, and AI-facing documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation edits may introduce incorrect or misleading guidance in README files, generated llms.txt files, Go Playground links, examples, or code comments.

Mitigation: Review proposed edits before applying them and verify examples, links, and generated documentation against the target Go project.

Risk: Optional sub-agent use on large private codebases can make merged documentation changes harder to audit.

Mitigation: Limit sub-agent scope to independent packages or documentation layers and review the merged output before committing changes.

Risk: The skill can run Go, golangci-lint, and git commands as part of documentation work.

Mitigation: Inspect suggested shell commands before execution and run them in the intended repository context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-documentation)
- [Project homepage from ClawHub metadata](https://github.com/samber/cc-skills-golang)
- [Code Comments](artifact/references/code-comments.md)
- [Project Documentation](artifact/references/project-docs.md)
- [Library Documentation](artifact/references/library.md)
- [Application Documentation](artifact/references/application.md)
- [README Template](artifact/assets/templates/README.md)
- [CONTRIBUTING Template](artifact/assets/templates/CONTRIBUTING.md)
- [CHANGELOG Template](artifact/assets/templates/CHANGELOG.md)
- [llms.txt Template](artifact/assets/templates/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with Go code examples, shell command blocks, and documentation file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or edit README, CONTRIBUTING, CHANGELOG, llms.txt, Go doc comments, examples, and project documentation.]

## Skill Version(s):

1.2.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
