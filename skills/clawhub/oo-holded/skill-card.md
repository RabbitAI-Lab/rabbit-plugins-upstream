## Description:

Holded (holded.com) enables agents to read contacts and products and create basic contacts through the OOMOL-connected Holded connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Holded through an OOMOL-connected account, including reading contacts and products and creating basic contacts after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review setup commands before installing; prefer a verified release or documented package source, and do not let an agent automatically run remote installer pipelines unless the source has been independently reviewed and trusted.

Risk: Write actions can create or change Holded business data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Holded homepage](https://www.holded.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-holded)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
