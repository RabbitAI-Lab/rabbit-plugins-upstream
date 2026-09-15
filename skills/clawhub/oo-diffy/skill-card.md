## Description:

Diffy helps agents inspect and retrieve Diffy visual testing projects, screenshots, comparison statuses, and result details through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to query Diffy visual testing projects, screenshots, and comparison results from an already connected OOMOL account. It is intended for read-oriented Diffy workflows and schema-guided CLI execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Prefer a verified package-manager or manually reviewed oo CLI installation path before using the skill.

Risk: The skill depends on OOMOL as an intermediary for the connected Diffy account.

Mitigation: Install only when that account connection model is acceptable for the intended environment.

Risk: Future or schema-discovered actions may change Diffy state if tagged as write or destructive.

Mitigation: Inspect the live action schema and confirm exact payloads and effects with the user before approving state-changing commands.

## Reference(s):

- [Diffy homepage](https://diffy.website/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-diffy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
