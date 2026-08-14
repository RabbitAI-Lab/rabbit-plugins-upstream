## Description:

The ClickHelp skill lets an agent read, create, and update ClickHelp data through the OOMOL `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected ClickHelp account from an agent, including listing, retrieving, searching, creating, and updating ClickHelp projects and topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update ClickHelp content through a connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: First-time setup may require installing the oo CLI or completing authentication and connection steps.

Mitigation: Inspect the installer and authentication flow before installation or sign-in if the CLI is not already installed.

## Reference(s):

- [ClickHelp homepage](https://clickhelp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector data and an execution id under meta.executionId.]

## Skill Version(s):

1.0.0 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
