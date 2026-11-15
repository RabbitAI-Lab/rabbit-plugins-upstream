## Description:

Oracle CLI second-model review/debug/refactor/design with selected files, dry-run token checks, API or browser engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to ask the Oracle CLI for a one-shot second-model pass on selected project files for code review, debugging, refactoring, design feedback, or prompt restoration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and can run an unpinned third-party npm CLI that may change after review.

Mitigation: Install only from a trusted @steipete/oracle package path, prefer a pinned reviewed version, and preview runs with dry-run and file reports before sending prompts.

Risk: Prompts and file attachments can expose secrets, private tokens, or unnecessary project data to a second-model run.

Mitigation: Attach only the files needed for the task, avoid secrets and key files, and redact sensitive values before use.

Risk: Second-model output can be incorrect or misleading if used without verification.

Mitigation: Treat results as advisory and validate recommendations against the codebase, tests, and project constraints.

## Reference(s):

- [Oracle homepage](https://askoracle.dev)
- [ClawHub oracle skill page](https://clawhub.ai/azizbrownint/skills/oracle)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and prose guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output is advisory and should be checked against code and tests before use.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
