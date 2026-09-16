## Description:

Operates Bazhuayu through OOMOL's oo CLI for reading, creating, and updating Bazhuayu task data without direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Bazhuayu task groups, tasks, statuses, analytics, execution data, exports, and controlled write actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through verified official packages, or download and review or verify the installer before running it.

Risk: Bazhuayu write actions can start, stop, copy, update, or mark task data as exported.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and only mark data exported after the retrieved records have been persisted.

Risk: The skill depends on an OOMOL-connected Bazhuayu account and server-managed credentials.

Mitigation: Install only when the user accepts the OOMOL/Bazhuayu integration model and use the live action schema before sending requests.

## Reference(s):

- [Bazhuayu homepage](https://www.bazhuayu.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bazhuayu)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relies on live oo connector schemas; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
