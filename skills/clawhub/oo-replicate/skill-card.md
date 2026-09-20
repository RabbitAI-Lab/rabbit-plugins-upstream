## Description:

Replicate (replicate.com) lets agents handle Replicate requests through the OOMOL oo CLI connector, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Replicate through an OOMOL-connected account, including creating or canceling predictions and reading accounts, collections, models, versions, and prediction history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded code immediately.

Mitigation: Review the oo CLI installation path first, and prefer a verified package, pinned release, or manually inspected installer before running installation commands.

Risk: Create and cancel prediction actions can change state in the connected OOMOL and Replicate account.

Mitigation: Confirm the exact action, target, and payload with the user before running write or destructive actions.

## Reference(s):

- [Replicate homepage](https://replicate.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-replicate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI connector and may return JSON containing data plus meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
