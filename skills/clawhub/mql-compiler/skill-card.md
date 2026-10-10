## Description:

Compile MQL4 (.mq4) and MQL5 (.mq5) sources to .ex4/.ex5 on Linux with the mql-compiler command, and read its compile errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to compile MQL4 and MQL5 sources on x86-64 Linux and troubleshoot compiler errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation instructions execute a mutable remote script, including an optional sudo path, without verification.

Mitigation: Download and inspect the installer first; verify it against a trusted release or checksum, and avoid sudo unless system-wide installation is necessary and the upstream is trusted.

Risk: Docker downloads images and MetaTrader installers, retains a toolchain volume and last-run logs, and writes compiled files beside source files.

Mitigation: Review download and storage requirements before running; inspect the Docker image and choose source locations where compiled outputs and cached logs are acceptable.

## Reference(s):

- [Installation and troubleshooting](references/installation.md)
- [mql-compiler project](https://github.com/psyb0t/docker-mql-compiler)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with shell commands and compiler diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compile results identify files and errors; successful runs write .ex4 or .ex5 files beside their sources.]

## Skill Version(s):

0.2.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
