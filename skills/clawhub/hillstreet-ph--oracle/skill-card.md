## Description:

Oracle CLI second-model review/debug/refactor/design with selected files, dry-run token checks, API or browser engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Oracle to send a focused prompt and selected project files to a second model for review, debugging, refactoring, or design feedback. They can preview the payload and token usage, choose an API or browser engine, and should verify suggestions against the code and tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI downloads and executes an unpinned package, and the security review does not cover an unresolved local path-like reference.

Mitigation: Review and pin the package version before installation, and resolve the missing reference as part of the review.

Risk: Second-model suggestions could introduce incorrect or misleading changes.

Mitigation: Treat responses as advisory and verify proposed changes against the project code and tests.

## Reference(s):

- [Oracle project website](https://askoracle.dev)
- [Oracle on ClawHub](https://clawhub.ai/hillstreet-ph/skills/oracle)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown prompts and second-model responses, with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are advisory; verify suggestions against project code and tests.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
