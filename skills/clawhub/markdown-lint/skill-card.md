## Description:

Check markdown files for common issues including heading structure, link validity, list formatting, trailing whitespace, and code block language tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to review README files, documentation directories, and CI documentation quality gates for common Markdown structure and formatting issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation advertises automatic fixes and custom rules, but the inspected release evidence says the current script reports lint results and does not implement those advertised features.

Mitigation: Use the skill as a local reporting checker, review proposed documentation changes manually, and verify any claimed fix or custom-rule behavior before relying on it in CI.

Risk: Lint findings can be incomplete or noisy for project-specific Markdown conventions.

Mitigation: Treat output as review guidance and keep maintainers responsible for accepting, rejecting, or adapting findings to the repository's documentation standards.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON lint results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports file paths, line and column positions, rule identifiers, severity, messages, and summary counts.]

## Skill Version(s):

0.1.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
