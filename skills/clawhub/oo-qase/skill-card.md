## Description:

Qase connector for reading, creating, updating, and deleting Qase data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test managers use this skill to inspect Qase projects, cases, and runs, and to create or complete Qase test assets through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include executing an unverified remote installer.

Mitigation: Review or replace the remote installer path with a package-managed or verified installation method before use.

Risk: Write and destructive Qase actions can change or complete test assets.

Mitigation: Confirm exact payloads for write actions and require explicit approval before destructive actions.

Risk: The skill uses an OOMOL-connected Qase account with server-side credentials.

Mitigation: Use only OOMOL and Qase accounts the agent is intended to access, and limit connected account permissions where practical.

## Reference(s):

- [Qase homepage](https://qase.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qase)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema inspection before constructing Qase action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
