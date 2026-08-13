## Description:

Assists development-branch finishing workflows with code generation, programming support, debugging, testing, deployment tasks, and structured output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to finish development branches by requesting code, debugging, testing, deployment, workflow, and structured-output assistance. It is best suited to a clearly scoped repository and branch-finishing task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad file, command, credential, and network capabilities that are poorly scoped for a branch-finishing helper.

Mitigation: Use only in a specific repository with a clearly defined branch-finishing workflow, and limit file, shell, network, and credential access to what that workflow requires.

Risk: The skill may propose code, command, configuration, or deployment changes that affect the target project.

Mitigation: Review generated changes before applying them, run the relevant tests or checks, and avoid providing API keys or broad shell access unless the publisher documents the required services, commands, and files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/finishing-a-development-branch)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code blocks, shell commands, configuration details, and JSON-style structured examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require repository file access, API credentials, network access, and shell execution depending on the branch-finishing task.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
