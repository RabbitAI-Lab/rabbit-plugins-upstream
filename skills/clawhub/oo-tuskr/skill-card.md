## Description:

Tuskr enables agents to read, create, and update Tuskr projects, test cases, test runs, and test run results through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

QA, engineering, and release teams use this skill to manage Tuskr projects, test cases, and test runs from an agent workflow while confirming write payloads before state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code on a user's machine.

Mitigation: Review the oo CLI installation path, prefer an official package manager or pinned release with checksum or signature verification when available, and avoid running installers from an elevated shell.

Risk: Write actions can change Tuskr projects, test cases, test runs, or test run results.

Mitigation: Approve Tuskr write actions only after checking the exact payload and intended effect.

## Reference(s):

- [ClawHub Tuskr skill page](https://clawhub.ai/oomol/skills/oo-tuskr)
- [Tuskr homepage](https://tuskr.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions may run directly; write and destructive actions require user confirmation before changing Tuskr state.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
