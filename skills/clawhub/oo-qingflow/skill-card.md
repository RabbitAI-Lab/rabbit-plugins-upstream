## Description:

Qingflow (qingflow.com). Use this skill for ANY Qingflow request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Qingflow through an OOMOL-connected account, including reading business data, managing records, inspecting forms, and running workflow actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer path before installation and prefer a trusted, versioned, verifiable source for the oo CLI.

Risk: The skill can create, update, reassign, approve, roll back, or otherwise change Qingflow business data.

Mitigation: Use a Qingflow account with only the needed permissions and require explicit confirmation for any state-changing or destructive workflow operation.

## Reference(s):

- [Qingflow homepage](https://qingflow.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qingflow)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides the agent to inspect live connector schemas before constructing Qingflow action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
