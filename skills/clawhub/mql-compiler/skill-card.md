## Description:

Compile MQL4 (.mq4) and MQL5 (.mq5) sources to .ex4/.ex5 on Linux with the mql-compiler command, and read its compile errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to compile MQL4 and MQL5 source files on Linux and interpret compiler errors and warnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation guidance executes a changeable internet installer, and its downloaded wrapper has not been fixed to a revision.

Mitigation: Review and verify a fixed revision of both installer and wrapper before installation; prefer a per-user installation.

Risk: The system-wide installation option runs with full system privileges.

Mitigation: Use the per-user installation unless a system-wide installation is needed.

Risk: External executable dependencies are not fully audited.

Mitigation: Review dependencies before use and limit compilation to intended project folders.

Risk: Deleting the shared compiler cache affects every user's toolchain on the machine.

Mitigation: Delete the shared cache only deliberately; use a pinned image and a read-only cache mount when inspecting logs.

## Reference(s):

- [Project homepage](https://github.com/psyb0t/docker-mql-compiler)
- [Installing mql-compiler](references/installation.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, JSON, Text]

**Output Format:** [Shell commands, .ex4/.ex5 compiled files, and JSON Lines compiler diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compiled files are written beside their source files; diagnostics report compile status, errors, and warnings.]

## Skill Version(s):

0.5.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
