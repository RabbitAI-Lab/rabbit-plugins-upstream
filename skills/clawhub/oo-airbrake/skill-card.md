## Description:

Airbrake enables agents to read, create, and update Airbrake projects, error groups, notices, deploys, and notice status through an OOMOL-connected Airbrake account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to inspect Airbrake projects, deploys, error groups, notices, and notice status, and to perform supported Airbrake updates through the OOMOL oo CLI when the user confirms state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to execute a remote oo CLI installer directly in a shell.

Mitigation: Review the installation path first; prefer a verified or package-manager installation, or inspect the installer and validate checksum or signature before running it.

Risk: Some Airbrake connector actions may change Airbrake state.

Mitigation: Confirm any action tagged write or destructive, including the exact payload and target, before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-airbrake)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Airbrake homepage](https://airbrake.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before constructing action payloads; command results are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
