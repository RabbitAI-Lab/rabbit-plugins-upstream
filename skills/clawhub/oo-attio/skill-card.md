## Description:

Enables agents to inspect Attio action schemas and read, create, update, upsert, or delete Attio records through the OOMOL oo CLI and Attio connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Attio workspaces, objects, attributes, records, and access-token details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer scripts for the oo CLI.

Mitigation: Prefer a separately verified, version-pinned oo CLI installation path before installing or running commands.

Risk: Attio write, upsert, update, and delete actions can change or remove workspace data.

Mitigation: Review requested Attio scopes and require explicit approval for the exact payload and target before state-changing actions.

## Reference(s):

- [ClawHub Attio skill page](https://clawhub.ai/oomol/skills/oo-attio)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Attio homepage](https://attio.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
