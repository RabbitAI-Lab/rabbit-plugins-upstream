## Description:

AI Code Review Expert helps agents review code snippets and diffs for bugs, security issues, performance concerns, style violations, refactoring opportunities, and PR-ready feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, tech leads, security engineers, and maintainers use this skill to get structured code review findings, concrete fixes, quality scoring, and PR summary comments before merging changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share more source code, secrets, customer data, or production samples than the review requires.

Mitigation: Submit only the smallest relevant snippet, file, or diff and redact tokens, credentials, customer identifiers, and production data before review.

Risk: Broad trigger phrases such as 'check this code' may start a review workflow before the user intends to share sensitive material.

Mitigation: Confirm the review intent and scope before providing sensitive source code or repository context.

Risk: Suggested fixes, PR comments, and shell commands may be context-dependent or require validation before use.

Mitigation: Review proposed changes locally, run project tests or security checks, and have a human reviewer approve changes before applying them.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown review comments with severity labels, explanations, code blocks, scoring tables, and PR summary text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested fixes, local verification commands, security review notes, and license compliance prompts.]

## Skill Version(s):

3.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
