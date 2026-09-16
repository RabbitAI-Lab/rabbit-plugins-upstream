## Description:

This skill helps an agent operate Altiria through OOMOL's oo CLI, including inspecting action schemas, managing contacts and groups, sending SMS messages, and retrieving SMS details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Altiria from an agent through an OOMOL-connected account. It supports contact and group lookup, contact changes, SMS sending, and SMS retrieval after the agent checks the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct remote script execution for installing the oo CLI.

Mitigation: Install the oo CLI from trusted documentation using a versioned or verifiable method, and do not let an agent run curl-to-bash or PowerShell download-and-execute commands automatically.

Risk: Write, SMS-send, and delete actions can modify Altiria state or send external messages.

Mitigation: Review the live action schema and confirm the exact payload, recipient, target, and expected effect with the user before running write or destructive actions.

Risk: The security summary flags routing language that is broader than necessary.

Mitigation: Use this skill only for concrete Altiria tasks, and prefer read-only get or list actions unless the user explicitly requests a state-changing operation.

## Reference(s):

- [Altiria homepage](https://www.altiria.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-altiria)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report JSON responses returned by the oo CLI, including data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
