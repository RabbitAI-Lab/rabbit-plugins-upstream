## Description:

Compile MQL4 (.mq4) and MQL5 (.mq5) sources to .ex4/.ex5 on Linux with the mql-compiler command, and read its compile errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to compile MetaTrader MQL4 and MQL5 sources on Linux and diagnose compiler errors and warnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation instructions run a mutable remote shell script, optionally with sudo.

Mitigation: Inspect a version-pinned installer before running it; avoid sudo unless system-wide installation is necessary.

Risk: Compiling uses an external Docker image and leaves persistent images, toolchain volumes, and outputs next to sources; existing compiled outputs may be replaced.

Mitigation: Review the external image before use, compile only trusted source folders, and back up existing outputs when needed.

## Reference(s):

- [Installation and troubleshooting](references/installation.md)
- [mql-compiler project documentation](https://github.com/psyb0t/docker-mql-compiler)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and compile diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-file errors and warnings; compiled .ex4/.ex5 files are written beside source files.]

## Skill Version(s):

0.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
