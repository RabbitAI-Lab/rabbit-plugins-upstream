## Description:

Run code snippets in 30+ programming languages including JavaScript, Python, TypeScript, Java, C, C++, Go, Rust, Ruby, PHP, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[formulahendry](https://clawhub.ai/user/formulahendry)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to execute snippets, test algorithms, verify output, run quick scripts, and inspect syntax or runtime behavior across interpreted and compiled languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes supplied snippets on the host without enforced isolation.

Mitigation: Use it only in a disposable sandbox, container, or VM with no sensitive files, credentials, or network access unless those capabilities are explicitly required.

Risk: Unsafe shell interpolation patterns can mishandle or execute unintended content.

Mitigation: Feed code through a quoted heredoc or an argument-array API instead of interpolating user code into an echo command.

Risk: Global language tool installations can introduce version drift or unexpected behavior.

Mitigation: Prefer pinned local or container-local language runtimes and compilers.

## Reference(s):

- [Supported Languages Reference](references/LANGUAGES.md)
- [Code Runner on ClawHub](https://clawhub.ai/formulahendry/skills/code-runner)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with command examples, stdout, stderr, and concise troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution depends on locally installed language runtimes and compilers.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
