## Description:

Celigo enables agents to read, create, and update Celigo data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Celigo action schemas, run Celigo connector actions, and retrieve connection, export, flow, import, and token metadata from an authenticated OOMOL-connected Celigo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run a remote installer directly from the internet.

Mitigation: Review the oo CLI installation path first, prefer a signed or package-manager installation, verify the installer source, and avoid running pipe-to-shell or Invoke-Expression commands from an elevated terminal.

Risk: Some connector actions can change Celigo state.

Mitigation: Inspect the live action schema before constructing payloads and confirm the exact payload and expected effect with the user before running any state-changing action.

## Reference(s):

- [Celigo homepage](https://www.celigo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Celigo skill page](https://clawhub.ai/oomol/skills/oo-celigo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions should inspect the live schema before constructing payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
