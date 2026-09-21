## Description:

Yunbiao lets an agent read, create, update, upload, download, and delete Yunbiao business data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Yunbiao connector schemas and run read, write, upload, download, user, role, and form actions against an OOMOL-connected Yunbiao account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or overwrite Yunbiao business data through write and destructive actions.

Mitigation: Require a clear payload preview and explicit approval before write, upload, user, role, form, or destructive interface actions.

Risk: The agent could operate the wrong OOMOL or Yunbiao account if the connected account is not checked.

Mitigation: Confirm the intended OOMOL/Yunbiao connection before approving state-changing actions.

Risk: Setup commands install the oo CLI or start account connection flows.

Mitigation: Review installer commands before execution and run first-time setup only after an authentication or connection failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-iyunbiao)
- [Yunbiao homepage](https://www.iyunbiao.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
