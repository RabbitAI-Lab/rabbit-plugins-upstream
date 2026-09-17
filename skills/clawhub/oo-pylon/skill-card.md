## Description:

Pylon (usepylon.com). Use this skill for Pylon requests that read, create, or update Pylon data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support operators, and other external users use this skill to inspect Pylon schemas and run Pylon connector actions for accounts, contacts, issues, internal notes, organization details, searches, and time-bounded issue lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of a downloaded installer script.

Mitigation: Review the CLI installation path before installing and prefer a signed package manager or installer with checksum or signature verification.

Risk: Write actions can create or update Pylon records.

Mitigation: Confirm exact payloads and expected effects with the user before running connector actions that change Pylon state.

## Reference(s):

- [Pylon homepage](https://www.usepylon.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Pylon skill page](https://clawhub.ai/oomol/skills/oo-pylon)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
