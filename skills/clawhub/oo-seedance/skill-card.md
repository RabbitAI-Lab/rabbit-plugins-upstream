## Description:

This skill lets agents submit, list, retrieve, cancel, or delete Seedance video generation tasks through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Seedance video generation tasks from an agent session, including submitting jobs and retrieving task status or results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Inspect and verify the installer first, or use a verified, versioned installation method before running setup commands.

Risk: Submit, cancel, and delete actions can change Seedance task state or remove task records.

Mitigation: Confirm the exact payload and expected effect before submit actions, and require explicit approval before cancel or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-seedance)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Seedance Homepage](https://www.volcengine.com/product/ark)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
