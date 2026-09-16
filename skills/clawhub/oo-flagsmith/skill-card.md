## Description:

Flagsmith skill for reading feature flags, evaluating identity flags, and operating selected Flagsmith actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Flagsmith feature flags and evaluated identity flags through an OOMOL-connected Flagsmith account. It can also identify a Flagsmith identity and optionally update traits when the user explicitly intends that state change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer one-liners can execute installer code before the user has reviewed the source.

Mitigation: Verify the oo CLI source and installation path independently before running installer commands.

Risk: The identify_identity action can update Flagsmith identity traits.

Mitigation: Confirm the exact payload and intended state change with the user before invoking identify_identity with traits.

Risk: Flagsmith data is routed through an OOMOL-connected account.

Mitigation: Confirm that OOMOL handling is acceptable for the account's data-handling requirements.

## Reference(s):

- [ClawHub Flagsmith Skill Page](https://clawhub.ai/oomol/skills/oo-flagsmith)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Flagsmith Homepage](https://www.flagsmith.com)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
