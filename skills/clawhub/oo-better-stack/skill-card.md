## Description:

This skill enables an agent to read and manage Better Stack incident data through OOMOL's Better Stack connector and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Better Stack incident schemas, list and retrieve incident information, and perform incident actions such as create, acknowledge, or escalate with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Better Stack actions can create, acknowledge, or escalate incidents.

Mitigation: Review the exact incident target, payload, and expected effect with the user before approving write or destructive actions.

Risk: First-time setup may require installing the oo CLI from a remote installer.

Mitigation: Confirm the user trusts OOMOL and the oo CLI installation source before running installation commands.

## Reference(s):

- [ClawHub Better Stack Skill](https://clawhub.ai/oomol/skills/oo-better-stack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Better Stack Homepage](https://betterstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before building payloads and should request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
