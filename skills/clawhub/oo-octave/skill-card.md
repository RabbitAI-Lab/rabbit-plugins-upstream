## Description:

This skill enables an agent to operate Octave through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Octave connector schemas, list workspace Octave agents and supported languages, validate workspace metadata, and run synchronous Octave enrichment, qualification, context, and call preparation agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may execute downloaded scripts without independent package verification.

Mitigation: Prefer a verified or package-manager installation of the oo CLI, and review installer source before executing downloaded scripts.

Risk: Octave agent actions may send sensitive workspace data or incur account costs.

Mitigation: Require explicit user approval before running Octave agent actions, especially enrichment, qualification, context, and call preparation runs.

Risk: Incorrect action payloads could cause failed or unintended Octave requests.

Mitigation: Fetch the live connector schema before constructing each payload and confirm the action target and data before execution.

## Reference(s):

- [ClawHub Octave skill page](https://clawhub.ai/oomol/skills/oo-octave)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Octave homepage](https://www.octavehq.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; requires an installed oo CLI and an OOMOL-connected Octave account.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
