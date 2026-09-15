## Description:

Altoviz (altoviz.com) lets an agent read, create, and update Altoviz data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Altoviz customer workflows through an OOMOL-connected account, including creating customers and finding, retrieving, or listing customer records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell and PowerShell installer commands that can execute code on the user's machine.

Mitigation: Review the oo CLI installation path first, prefer a trusted package manager or versioned verifiable release, and run the remote installer only after accepting that execution risk.

Risk: The skill can create or change Altoviz customer data through write actions.

Mitigation: Confirm the exact write payload and expected effect with the user before creating or changing customer records.

## Reference(s):

- [Altoviz homepage](https://altoviz.com/en/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-altoviz)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
